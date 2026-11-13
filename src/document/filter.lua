-- KodeWorks document filter: pandoc Markdown -> raw LaTeX macros defined in kwdocument.sty.
-- Reads the YAML contract (variant, title, subtitle, company, date, recipient, refs, sender, contact) and turns
-- the body into \kw... macros. Problems are reported on stderr as lines starting with KWWARN: (the build
-- script prints them as VARSEL).
local utils = pandoc.utils
local stringify = utils.stringify

local function warn(msg) io.stderr:write("KWWARN: " .. msg .. "\n") end
local function info(msg) io.stderr:write("KWINFO: " .. msg .. "\n") end
local function trim(s) return (s:gsub("^%s+", ""):gsub("%s+$", "")) end

local COMPANIES = {
  ["KodeWorks AS"] = { org = "820 478 452", addr = "Fjordgata 30, 7010 Trondheim" },
  ["KodeWorks Trondheim AS"] = { org = "920 478 492", addr = "Fjordgata 30, 7010 Trondheim" },
  ["KodeWorks Eiendom AS"] = { org = "920 478 506", addr = "Fjordgata 30, 7010 Trondheim" },
  ["KodeWorks Oslo AS"] = { org = "922 070 709", addr = "Grønnegata 10, 0350 Oslo" },
}
local MONTHS = { "januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september",
  "oktober", "november", "desember" }

-- ---------------------------------------------------------------- inline helpers
local function nbsp_numbers(inl)
  local out = pandoc.List()
  for i, x in ipairs(inl) do
    local prev, nxt = inl[i - 1], inl[i + 1]
    if x.t == "Space" and prev and nxt and prev.t == "Str" and nxt.t == "Str" and
        ((prev.text:match("%d$") and nxt.text:match("^%d%d%d%f[%D]")) or
         (prev.text:match("%d$") and nxt.text:match("^%%")) or
         (prev.text:match("%d$") and (nxt.text == "kr" or nxt.text == "kr." or nxt.text == "timer" or nxt.text == "år"))) then
      out:insert(pandoc.Str("\u{00A0}"))
    else
      out:insert(x)
    end
  end
  return out
end

-- long unbreakable words (not links/URLs) get discretionary hyphens so they never exceed the margin
local function break_long(inl)
  local out = pandoc.List()
  for _, x in ipairs(inl) do
    if x.t == "Str" and utf8.len(x.text) and utf8.len(x.text) > 26 and not x.text:find("[/@]") then
      local chars, n = {}, 0
      for _, c in utf8.codes(x.text) do n = n + 1; chars[n] = utf8.char(c) end
      local i = 1
      while i <= n do
        local j = math.min(i + 17, n)
        out:insert(pandoc.Str(table.concat(chars, "", i, j)))
        if j < n then out:insert(pandoc.RawInline("latex", "\\discretionary{-}{}{}")) end
        i = j + 1
      end
    else
      out:insert(x)
    end
  end
  return out
end

-- bind the last two words so a paragraph never ends on a single short word
local function bind_tail(inl)
  local n = #inl
  if n < 7 then return inl end
  local last = inl[n]
  if last.t == "Str" and inl[n - 1].t == "Space" and utf8.len(last.text) <= 12 and inl[n - 2].t == "Str"
      and not inl[n - 2].text:match("[%-–]$") then
    local words = 0
    for _, x in ipairs(inl) do if x.t == "Space" then words = words + 1 end end
    if words >= 4 then
      local copy = pandoc.List(inl)
      copy[n - 1] = pandoc.Str("\u{00A0}")
      return copy
    end
  end
  return inl
end

local function fix_quotes(inl)
  local out = pandoc.List()
  for _, x in ipairs(inl) do
    if x.t == "Quoted" then
      local o, c = "«", "»"
      if x.quotetype == "SingleQuote" then o, c = "‹", "›" end
      out:insert(pandoc.Str(o))
      out:extend(x.content)
      out:insert(pandoc.Str(c))
    else
      out:insert(x)
    end
  end
  return out
end

-- titles and subjects: the last word never stands alone (bind it to the word before; also a third one if short)
local function bind_title(inl)
  local l = pandoc.List(inl)
  local n = #l
  local spaces = 0
  for _, x in ipairs(l) do if x.t == "Space" then spaces = spaces + 1 end end
  if spaces < 2 or l[n].t ~= "Str" or l[n - 1].t ~= "Space" then return l end
  l[n - 1] = pandoc.Str("\u{00A0}")
  if utf8.len(l[n].text) <= 5 and n >= 4 and l[n - 2].t == "Str" and l[n - 3].t == "Space" and spaces >= 3 then
    l[n - 3] = pandoc.Str("\u{00A0}")
  end
  return l
end

local function prep(inl, bind)
  local doc = pandoc.Pandoc({ pandoc.Plain(inl) })
  doc = doc:walk({ Inlines = function(l) return break_long(nbsp_numbers(fix_quotes(l))) end })
  local blk = doc.blocks[1]
  local l = blk.content
  if bind == "title" then l = bind_title(l)
  elseif bind then l = bind_tail(l) end
  return l
end

local function tex(inl, bind)
  if inl == nil or #inl == 0 then return "" end
  local l = prep(inl, bind)
  local s = trim(pandoc.write(pandoc.Pandoc({ pandoc.Plain(l) }), "latex"))
  s = s:gsub("\\ldots{}", "\\kwellip{}"):gsub("…", "\\kwellip{}")
  return s
end

local function esc(s)
  return trim(pandoc.write(pandoc.Pandoc({ pandoc.Plain({ pandoc.Str(s) }) }), "latex"))
end

local function meta_inlines(v)
  if v == nil then return nil end
  local ty = utils.type(v)
  if ty == "Inlines" then return v end
  if ty == "Blocks" then return pandoc.List(utils.blocks_to_inlines(v)) end
  if ty == "string" then return pandoc.List({ pandoc.Str(v) }) end
  return pandoc.List({ pandoc.Str(stringify(v)) })
end

-- lines of a metadata value (soft/hard breaks split lines)
local function meta_lines(v)
  local inl = meta_inlines(v)
  if not inl then return {} end
  local lines, cur = {}, pandoc.List()
  for _, x in ipairs(inl) do
    if x.t == "SoftBreak" or x.t == "LineBreak" then
      if #cur > 0 then lines[#lines + 1] = cur end
      cur = pandoc.List()
    else
      cur:insert(x)
    end
  end
  if #cur > 0 then lines[#lines + 1] = cur end
  return lines
end

local function split_lines(inl)
  local lines, cur = {}, pandoc.List()
  for _, x in ipairs(inl) do
    if x.t == "SoftBreak" or x.t == "LineBreak" then
      lines[#lines + 1] = cur
      cur = pandoc.List()
    else
      cur:insert(x)
    end
  end
  lines[#lines + 1] = cur
  return lines
end

local function trim_inlines(inl)
  local l = pandoc.List(inl)
  while #l > 0 and (l[1].t == "Space" or l[1].t == "SoftBreak") do l:remove(1) end
  while #l > 0 and (l[#l].t == "Space" or l[#l].t == "SoftBreak") do l:remove(#l) end
  return l
end

local function format_date(s)
  local y, m, d = s:match("^(%d%d%d%d)%-(%d%d)%-(%d%d)$")
  if y then
    local mi = tonumber(m)
    if mi >= 1 and mi <= 12 and tonumber(d) >= 1 and tonumber(d) <= 31 then
      return string.format("%d. %s %s", tonumber(d), MONTHS[mi], y)
    end
  end
  return nil
end

-- ---------------------------------------------------------------- facts
-- a line is `**Label:** value` (colon inside or right after the strong label)
local function parse_fact_line(line)
  local l = trim_inlines(line)
  if #l < 2 or l[1].t ~= "Strong" then return nil end
  local label = stringify(l[1])
  local rest = pandoc.List()
  for i = 2, #l do rest:insert(l[i]) end
  if label:sub(-1) == ":" then
    label = label:sub(1, -2)
  elseif #rest > 0 and rest[1].t == "Str" and rest[1].text:sub(1, 1) == ":" then
    local t = rest[1].text:sub(2)
    if t == "" then rest:remove(1) else rest[1] = pandoc.Str(t) end
  else
    return nil
  end
  rest = trim_inlines(rest)
  label = trim(label)
  if #rest == 0 or label == "" or utf8.len(label) > 25 or label:find("%.") then return nil end
  return { label = label, value = rest }
end

-- all lines of the paragraphs must be fact lines; returns list of facts or nil
local function facts_from_blocks(blocks)
  local facts = {}
  for _, b in ipairs(blocks) do
    if b.t ~= "Para" and b.t ~= "Plain" then return nil end
    for _, line in ipairs(split_lines(b.content)) do
      local f = parse_fact_line(line)
      if not f then return nil end
      facts[#facts + 1] = f
    end
  end
  if #facts == 0 then return nil end
  return facts
end

local function render_facts(facts)
  local out = { "\\begin{kwfacts}" }
  for _, f in ipairs(facts) do
    out[#out + 1] = "\\kwfact{" .. tex(f.label and pandoc.List({ pandoc.Str(f.label) })) .. "}{" .. tex(f.value, true) .. "}"
  end
  out[#out + 1] = "\\end{kwfacts}"
  return table.concat(out, "\n")
end

-- ---------------------------------------------------------------- tables
local function cell_text(cell)
  local parts = {}
  for _, b in ipairs(cell.contents) do
    if b.content and type(b.content) == "table" and (b.t == "Plain" or b.t == "Para") then
      parts[#parts + 1] = tex(b.content)
    end
  end
  return table.concat(parts, "\\par ")
end

local function render_table(tbl)
  local ncol = #tbl.colspecs
  if ncol == 0 then return "" end
  local rows_head, rows_body = {}, {}
  for _, r in ipairs(tbl.head.rows) do rows_head[#rows_head + 1] = r end
  for _, body in ipairs(tbl.bodies) do
    for _, r in ipairs(body.body) do rows_body[#rows_body + 1] = r end
  end
  local weight = {}
  for c = 1, ncol do weight[c] = 8 end
  local function measure(rows)
    for _, r in ipairs(rows) do
      for c, cell in ipairs(r.cells) do
        local n = utf8.len(stringify(cell.contents)) or 0
        local longest = 0
        for w in stringify(cell.contents):gmatch("%S+") do longest = math.max(longest, utf8.len(w) or 0) end
        weight[c] = math.max(weight[c] or 8, math.min(n, 38), longest)
      end
    end
  end
  measure(rows_head); measure(rows_body)
  local total = 0
  for c = 1, ncol do total = total + weight[c] end
  local gap = 4 -- mm padding per column side-by-side
  local avail = 145 - (ncol - 1) * gap
  local spec = {}
  for c = 1, ncol do
    local w = avail * weight[c] / total
    local al = tbl.colspecs[c][1]
    local fmt = "\\RaggedRight"
    if al == "AlignRight" then fmt = "\\RaggedLeft" elseif al == "AlignCenter" then fmt = "\\Centering" end
    spec[#spec + 1] = string.format(">{%s\\arraybackslash}p{%.1fmm}", fmt, w)
  end
  local out = { "\\par\\vspace{6pt}{\\parskip=0pt\\kwnh\\kwragged\\setlength{\\tabcolsep}{0pt}\\setlength{\\extrarowheight}{2.6mm}",
    "\\begin{tabular}{@{}" .. table.concat(spec, "@{\\hspace{" .. gap .. "mm}}") .. "@{}}" }
  local function row_tex(r, head)
    local cells = {}
    for c, cell in ipairs(r.cells) do
      local t = cell_text(cell)
      if head then t = "\\kwth{" .. t .. "}" end
      cells[#cells + 1] = t
    end
    return table.concat(cells, " & ") .. " \\\\"
  end
  out[#out + 1] = "\\kwtablerule"
  if #rows_head > 0 then
    for _, r in ipairs(rows_head) do out[#out + 1] = row_tex(r, true) .. "[1.4mm]" end
    out[#out + 1] = "\\kwtablerule"
  end
  for _, r in ipairs(rows_body) do
    out[#out + 1] = row_tex(r, false) .. "[1.8mm]"
    out[#out + 1] = "\\kwtablerule"
  end
  out[#out + 1] = "\\end{tabular}}\\par\\vspace{4pt}"
  return table.concat(out, "\n")
end

-- ---------------------------------------------------------------- contacts
local function person_tex(p)
  -- p: {name=inl, title=inl, email=inl, phone=inl} (each optional, already LaTeX strings)
  return "\\kwpers{" .. (p.name or "") .. "}{" .. (p.title or "") .. "}{" .. (p.email or "") .. "}{" .. (p.phone or "") .. "}"
end

local function mail_tex(s)
  local addr = trim(s)
  local shown = esc(addr):gsub("%.", ".\\allowbreak{}")
  return "\\href{mailto:" .. addr .. "}{" .. shown .. "}"
end

local function people_from_meta(v)
  local list = {}
  if v == nil then return list end
  local ty = utils.type(v)
  local items = {}
  if ty == "List" then
    for _, x in ipairs(v) do items[#items + 1] = x end
  else
    items[1] = v
  end
  for _, m in ipairs(items) do
    if utils.type(m) == "table" then
      local p = {}
      if m.name then p.name = tex(meta_inlines(m.name)) end
      if m.title then p.title = tex(meta_inlines(m.title)) end
      if m.email then p.email = mail_tex(stringify(m.email)) end
      if m.phone then p.phone = esc(stringify(m.phone):gsub("^(%+%d%d)%s", "%1\u{00A0}")) end
      if p.name or p.email or p.phone then list[#list + 1] = p end
    end
  end
  return list
end

local function people_row(people, per_row, textw_mm, box)
  local out = {}
  local n = #people
  local i = 1
  while i <= n do
    local cnt = math.min(per_row, n - i + 1)
    local gap = 8
    local avail = textw_mm - (box and 6 or 0)
    local w = (avail - gap * (per_row - 1)) / per_row
    local cells = {}
    for k = i, i + cnt - 1 do
      cells[#cells + 1] = string.format("\\begin{minipage}[t]{%.1fmm}%s\\end{minipage}", w, person_tex(people[k]))
    end
    local row = table.concat(cells, "\\hspace{" .. gap .. "mm}")
    if box then
      out[#out + 1] = "\\begin{kwcontactbox}" .. row .. "\\end{kwcontactbox}"
    else
      out[#out + 1] = row .. "\\par"
    end
    i = i + cnt
  end
  return table.concat(out, "\n")
end

-- a contact Div (.contact): first line is the name
local function contact_from_lines(lines)
  local p = {}
  local extra = {}
  for i, line in ipairs(lines) do
    local l = trim_inlines(line)
    if #l > 0 then
      if i == 1 then
        p.name = tex(l)
      else
        extra[#extra + 1] = tex(l)
      end
    end
  end
  -- a second line without e-mail, phone digits or a label colon is a title (shown muted, like the YAML title)
  local second = lines[2] and stringify(trim_inlines(lines[2])) or ""
  if #extra >= 1 and second ~= "" and not second:find("@") and not second:find("%d%d") and not second:find(":") then
    p.title = table.remove(extra, 1)
  end
  p.email = table.concat(extra, "\\par ")
  return p
end

-- ---------------------------------------------------------------- blocks
local render_blocks

local function only_strong_label(b)
  -- paragraph that consists only of a bold label (e.g. **Må ha:**), no value
  if b.t ~= "Para" and b.t ~= "Plain" then return false end
  local l = trim_inlines(b.content)
  if #l == 0 or l[1].t ~= "Strong" then return false end
  if #l == 1 then return true end
  return #l == 2 and l[2].t == "Str" and l[2].text == ":"
end

local function render_list(list, depth, out)
  local ordered = list.t == "OrderedList"
  local num = ordered and (list.start or 1) or 0
  local nitems = #list.content
  for idx, item in ipairs(list.content) do
    if depth == 1 and nitems >= 4 and (idx == 2 or idx == nitems) then out[#out + 1] = "\\nobreak" end
    local marker
    if ordered then
      if depth == 1 then
        marker = "\\kwnum{" .. num .. ".}"
      else
        marker = "\\kwnum{" .. string.char(96 + ((num - 1) % 26) + 1) .. ".}"
      end
      num = num + 1
    else
      marker = (depth == 1) and "\\kwdot" or "\\kwdottwo"
    end
    local first = true
    for _, b in ipairs(item) do
      if (b.t == "Plain" or b.t == "Para") then
        out[#out + 1] = "\\kwitem{" .. depth .. "}{" .. (first and marker or "") .. "}{" .. tex(b.content, true) .. "}"
        first = false
      elseif b.t == "BulletList" or b.t == "OrderedList" then
        if first then
          out[#out + 1] = "\\kwitem{" .. depth .. "}{" .. marker .. "}{}"
          first = false
        end
        render_list(b, math.min(depth + 1, 2), out)
      else
        out[#out + 1] = "\\kwitem{" .. depth .. "}{}{" .. render_blocks({ b }, {}) .. "}"
      end
    end
  end
end

local contact_seen = false

local function render_block(b, ctx, nextb)
  if b.t == "Header" then
    local s = tex(b.content)
    if b.level >= 3 then return "\\kwsubhead{" .. s .. "}" end
    return "\\kwhead{" .. s .. "}"
  elseif b.t == "Para" or b.t == "Plain" then
    if #b.content == 1 and b.content[1].t == "Image" then
      return "\\par\\vspace{4pt}\\noindent{" ..
          trim(pandoc.write(pandoc.Pandoc({ b }), "latex")) .. "}\\par"
    end
    if only_strong_label(b) then
      local l = trim_inlines(b.content)
      local s = tex(pandoc.List({ l[1] }))
      return "\\kwlead{" .. s .. "}"
    end
    return "\\par " .. tex(b.content, true) .. "\\par"
  elseif b.t == "BulletList" or b.t == "OrderedList" then
    local out = { "\\par" .. (ctx.listgap or "") }
    render_list(b, 1, out)
    out[#out + 1] = "\\kwlistend"
    return table.concat(out, "\n")
  elseif b.t == "BlockQuote" then
    return "\\par\\vspace{6pt}\\begin{kwquote}\\kwquotetext\\kwragged\n" .. render_blocks(b.content, { quote = true }) .. "\n\\end{kwquote}"
  elseif b.t == "Table" then
    return render_table(b)
  elseif b.t == "HorizontalRule" then
    return "\\kwrule"
  elseif b.t == "CodeBlock" then
    return "\\begin{verbatim}\n" .. b.text .. "\n\\end{verbatim}"
  elseif b.t == "LineBlock" then
    local parts = {}
    for _, l in ipairs(b.content) do parts[#parts + 1] = tex(l) end
    return "\\par " .. table.concat(parts, "\\\\\n") .. "\\par"
  elseif b.t == "Div" then
    local cls = b.classes
    if cls:includes("facts") then
      local facts = facts_from_blocks(b.content)
      if facts then return render_facts(facts) end
      warn("A facts box (::: {.facts}) has lines that are not of the form «**Label:** value»; the content is shown as plain text.")
      return render_blocks(b.content, ctx)
    elseif cls:includes("columns") then
      local cols = {}
      for _, c in ipairs(b.content) do
        if c.t == "Div" and c.classes:includes("column") then cols[#cols + 1] = c end
      end
      if #cols == 0 then return render_blocks(b.content, ctx) end
      local n = #cols
      local gap = 9
      local w = (ctx.textw - gap * (n - 1)) / n
      local parts = {}
      for _, c in ipairs(cols) do
        parts[#parts + 1] = string.format("\\begin{minipage}[t]{%.2fmm}\\kwragged\\kwhyph\\vspace{-7.5pt}\n%s\n\\end{minipage}", w,
          render_blocks(c.content, { textw = w }))
      end
      return "\\par\\kwneed{8\\baselineskip}\\vspace{4pt}\\noindent" .. table.concat(parts, "\\hspace{" .. gap .. "mm}") .. "\\par\\vspace{6pt}"
    elseif cls:includes("contact") then
      local lines = {}
      for _, c in ipairs(b.content) do
        if c.t == "Para" or c.t == "Plain" then
          for _, l in ipairs(split_lines(c.content)) do lines[#lines + 1] = l end
        end
      end
      contact_seen = true
      local p = contact_from_lines(lines)
      return people_row({ p }, 1, ctx.textw, true)
    elseif cls:includes("column") then
      return render_blocks(b.content, ctx)
    else
      return render_blocks(b.content, ctx)
    end
  elseif b.t == "RawBlock" then
    if b.format == "latex" or b.format == "tex" then return b.text end
    return ""
  end
  warn("Unknown Markdown element (" .. b.t .. ") was skipped.")
  return ""
end

render_blocks = function(blocks, ctx)
  ctx = ctx or {}
  ctx.textw = ctx.textw or 135
  local out = {}
  for i, b in ipairs(blocks) do
    local prev = blocks[i - 1]
    ctx.listgap = ""
    if prev and (b.t == "BulletList" or b.t == "OrderedList") then
      if prev.t == "BulletList" or prev.t == "OrderedList" then
        ctx.listgap = "\\vspace{4pt}"
      elseif (prev.t == "Para" or prev.t == "Plain") and not only_strong_label(prev)
          and stringify(prev):sub(-1) ~= ":" then
        ctx.listgap = "\\vspace{3pt}"
      end
    end
    out[#out + 1] = render_block(b, ctx, blocks[i + 1])
  end
  return table.concat(out, "\n")
end

-- ---------------------------------------------------------------- main
function Pandoc(doc)
  local meta = doc.meta
  local variant = meta.variant and stringify(meta.variant) or "document"
  -- the Norwegian values from the first version are still accepted
  local legacy = { brev = "letter", dokument = "document" }
  if legacy[variant] then
    warn("variant: " .. variant .. " is the old Norwegian value; use variant: " .. legacy[variant] .. ".")
    variant = legacy[variant]
  end
  if variant ~= "letter" and variant ~= "document" then
    warn("Unknown variant «" .. variant .. "» (valid: letter, document); using document.")
    variant = "document"
  end
  local letter = variant == "letter"
  local textw = 145

  -- company
  local company = meta.company and stringify(meta.company) or nil
  if not company then
    info("The field company is missing; using KodeWorks AS in the footer.")
    company = "KodeWorks AS"
  elseif not COMPANIES[company] then
    warn("Unknown company «" .. company .. "» in company (valid: KodeWorks AS, KodeWorks Trondheim AS, KodeWorks Eiendom AS, KodeWorks Oslo AS); using KodeWorks AS.")
    company = "KodeWorks AS"
  end

  -- title
  local blocks = pandoc.List(doc.blocks)
  local title_inl = meta_inlines(meta.title)
  local h1_warned = false
  if not title_inl then
    for i, b in ipairs(blocks) do
      if b.t == "Header" and b.level == 1 then
        title_inl = b.content
        blocks:remove(i)
        break
      elseif b.t ~= "RawBlock" then
        break
      end
    end
  else
    for _, b in ipairs(blocks) do
      if b.t == "Header" and b.level == 1 then
        warn("Both the YAML field title and a # heading («" .. stringify(b.content) .. "») exist; the YAML title is used, and the # heading is shown as a section heading.")
        break
      end
    end
  end
  if not title_inl then
    warn(letter and "The letter has no subject (title in the YAML header); the subject line is left out." or
      "The document has no title (title in the YAML header or a first # heading); the title is left out.")
  end
  local subtitle = meta_inlines(meta.subtitle)

  -- date
  local date_s = nil
  if meta.date then
    local raw = trim(stringify(meta.date))
    date_s = format_date(raw)
    if not date_s then
      warn("The date «" .. raw .. "» is not of the form YYYY-MM-DD; it is shown as written.")
      date_s = esc(raw)
    end
  elseif letter then
    local t = os.date("*t")
    date_s = string.format("%d. %s %d", t.day, MONTHS[t.month], t.year)
  end

  -- facts directly after the title (only if every line is a fact line)
  local body = pandoc.List()
  local facts = nil
  do
    local lead = {}
    local j = 1
    while j <= #blocks and (blocks[j].t == "Para" or blocks[j].t == "Plain") do
      lead[#lead + 1] = blocks[j]
      j = j + 1
    end
    -- take the longest prefix of paragraphs that are all fact lines
    local k = #lead
    while k >= 1 do
      local f = facts_from_blocks({ table.unpack(lead, 1, k) })
      if f then
        facts = f
        break
      end
      k = k - 1
    end
    if facts and #facts == 1 then
      local v = stringify(facts[1].value)
      if utf8.len(v) > 160 then facts = nil; k = 0 end
    end
    if facts then
      for i = k + 1, #blocks do body:insert(blocks[i]) end
    else
      body = blocks
    end
  end

  -- trailing contact paragraph (name in bold, lines, an e-mail address) becomes a contact block
  local trailing_contact = nil
  if not meta.contact and #body > 0 then
    local last = body[#body]
    if (last.t == "Para" or last.t == "Plain") and #last.content > 2 and last.content[1].t == "Strong" then
      local lines = split_lines(last.content)
      local txt = stringify(last.content)
      if #lines >= 2 and txt:find("@") then
        trailing_contact = lines
        body:remove(#body)
      end
    end
  end

  local out = {}
  local running_src = nil
  -- title block
  if letter then
    if title_inl then
      out[#out + 1] = "\\kwsubject{" .. (meta.recipient and "81mm" or "49mm") .. "}{" .. tex(title_inl, "title") .. "}"
    else
      out[#out + 1] = "\\kwnosubject{" .. (meta.recipient and "67mm" or "43mm") .. "}"
    end
  else
    if title_inl then
      local kicker, main = "", title_inl
      for i = 1, math.min(#title_inl, 7) do
        local x = title_inl[i]
        if x.t == "Str" and x.text:sub(-1) == ":" and i < #title_inl - 2 then
          local kl = {}
          for q = 1, i do kl[#kl + 1] = title_inl[q] end
          local ktxt = stringify(pandoc.List(kl))
          if utf8.len(ktxt) <= 28 and i <= 4 then
            kl[#kl] = pandoc.Str(x.text:sub(1, -2))
            local rest = pandoc.List()
            for q = i + 2, #title_inl do rest:insert(title_inl[q]) end
            kicker = tex(pandoc.List(kl)); main = rest
          end
          break
        end
      end
      if kicker ~= "" then running_src = stringify(main) end
      local n = utf8.len(stringify(main)) or 0
      local size, lead
      if n <= 30 then size, lead = 30, 34 elseif n <= 56 then size, lead = 25, 29.5 else size, lead = 21, 26.5 end
      out[#out + 1] = string.format("\\kwdoctitle{%s}{%s}{%s}{%d}{%s}", kicker, tex(main, "title"), subtitle and tex(subtitle, "title") or "", size, tostring(lead))
    else
      out[#out + 1] = "\\par\\vspace*{14mm}"
    end
  end
  if facts then out[#out + 1] = render_facts(facts) end

  local ctx = { textw = textw }
  -- letter: keep the last paragraph together with the closing and signature, so the sign-off
  -- never stands alone at the top of a page (about 88 characters per line in the 145 mm column)
  if letter and #body > 0 and body[#body].t == "Para" then
    local lines = math.ceil((utf8.len(stringify(body[#body])) or 0) / 88)
    local at = #body
    if at > 1 and body[at - 1].t == "Header" then at, lines = at - 1, lines + 3 end  -- take the heading along
    body:insert(at, pandoc.RawBlock("latex", string.format("\\kwneed{%d\\baselineskip}", lines + 9)))
  end
  out[#out + 1] = render_blocks(body, ctx)

  -- contact block (document) / signature (letter)
  local sender_people = people_from_meta(meta.sender)
  local contact_people = people_from_meta(meta.contact)
  if trailing_contact then
    local p = contact_from_lines(trailing_contact)
    out[#out + 1] = people_row({ p }, 1, textw, true)
  end
  if #contact_people > 0 then
    out[#out + 1] = people_row(contact_people, 2, textw, true)
  end
  if letter then
    local closing = meta.closing and tex(meta_inlines(meta.closing)) or "Vennlig hilsen"
    if #sender_people == 0 then
      warn("The letter has no sender (sender in the YAML header); the signature is left out.")
      out[#out + 1] = "\\par\\kwneed{5\\baselineskip}\\vspace{14pt}{\\parskip=0pt\\noindent " .. closing .. "\\par}"
    else
      out[#out + 1] = "\\kwsignoff{" .. closing .. "}{" .. people_row(sender_people, 2, textw, false) .. "}"
    end
    if not meta.recipient then
      warn("The letter has no recipient (recipient in the YAML header); the recipient block is left out.")
    end
  end

  -- preamble macros
  local pre = {}
  pre[#pre + 1] = "\\def\\kwcompany{" .. esc(company) .. "}"
  pre[#pre + 1] = "\\def\\kworgnr{" .. COMPANIES[company].org:gsub(" ", "\\,") .. "}"
  pre[#pre] = "\\def\\kworgnr{" .. COMPANIES[company].org:gsub(" ", "~") .. "}"
  if date_s then pre[#pre + 1] = "\\def\\kwdate{" .. date_s:gsub(" ", "~", 1) .. "}" end
  local full_title = title_inl and stringify(title_inl) or ""
  local running = running_src or full_title
  if utf8.len(running) > 66 then
    -- cut at a word boundary, never leave trailing punctuation or an open parenthesis
    local words, cut = {}, ""
    for w in running:gmatch("%S+") do words[#words + 1] = w end
    for _, w in ipairs(words) do
      local try = (cut == "") and w or (cut .. " " .. w)
      if utf8.len(try) > 64 then break end
      cut = try
    end
    local changed = true
    while changed do
      changed = false
      for _, tail in ipairs({ " –", " —", " -", ",", ";", ":", ".", " (", "(", " og", " med", " i", " på", " for", " av", " til" }) do
        if cut:sub(-#tail) == tail and #cut > #tail then
          cut = cut:sub(1, #cut - #tail)
          changed = true
        end
      end
    end
    local open = select(2, cut:gsub("%(", "")) - select(2, cut:gsub("%)", ""))
    if open > 0 then cut = cut:gsub("%s*%([^()]*$", "") end
    running = cut .. "…"
  end
  local ellipsis = running:sub(-3) == "…"
  if ellipsis then running = running:sub(1, -4) end
  pre[#pre + 1] = "\\def\\kwrunning{" .. esc(running) .. (ellipsis and "\\kwellip{}" or "") .. "}"
  pre[#pre + 1] = "\\hypersetup{pdftitle={" .. (full_title:gsub("[{}\\#%%&_^~$]", "")) .. "},pdfauthor={" .. company .. "},pdfcreator={KodeWorks}}"
  if letter then
    local lines = meta_lines(meta.recipient)
    local parts = {}
    for i, l in ipairs(lines) do
      local s = tex(l)
      if i == 1 then s = "{\\kwmedium " .. s .. "}" end
      parts[#parts + 1] = s
    end
    if #parts > 0 then
      pre[#pre + 1] = "\\def\\kwrecipient{" .. table.concat(parts, "\\par ") .. "}"
      pre[#pre + 1] = "\\def\\kwretline{" .. esc(company .. " · " .. COMPANIES[company].addr) .. "}"
    end
    local meta_rows = {}
    local function row(label, v)
      meta_rows[#meta_rows + 1] = "{\\kwlabel{" .. label .. "}\\par\\vspace{0.8mm}\\kwsize{9.5}{13}\\kwregular " .. v .. "\\par}"
    end
    if date_s then row("Dato", date_s:gsub(" ", "\u{00A0}", 1)) end
    if meta["their-ref"] then row("Deres ref.", tex(meta_inlines(meta["their-ref"]))) end
    if meta["our-ref"] then row("Vår ref.", tex(meta_inlines(meta["our-ref"]))) end
    pre[#pre + 1] = "\\def\\kwmeta{\\parskip=0pt\\kwragged\\kwnh " .. table.concat(meta_rows, "\\vspace{3mm}") .. "}"
  end
  local early = "\\newif\\ifkwletter" .. (letter and "\\kwlettertrue\n" or "\n") .. "\\def\\kwtextwmm{" .. textw .. "}"

  doc.meta = pandoc.Meta({
    kwearly = pandoc.MetaBlocks({ pandoc.RawBlock("latex", early) }),
    kwpreamble = pandoc.MetaBlocks({ pandoc.RawBlock("latex", table.concat(pre, "\n")) }),
  })
  doc.blocks = { pandoc.RawBlock("latex", table.concat(out, "\n")) }
  return doc
end
