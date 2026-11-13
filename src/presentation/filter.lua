-- KodeWorks presentation filter: pandoc Markdown -> beamer macros defined in beamerthemekodeworks.sty.
-- Use with: pandoc deck.md -t beamer --slide-level=2 --lua-filter=filter.lua --template=template.tex
-- Metadata switch: -M shownotes=true adds a notes page after every slide.
local utils = pandoc.utils

local function trim(s) return (s:gsub("^%s+", ""):gsub("%s+$", "")) end

-- Norwegian guillemets instead of English quotes
local function nbsp_numbers(el)
  return el:walk {
    Inlines = function(inl)
      local out = pandoc.List()
      for i, x in ipairs(inl) do
        local prev, nxt = inl[i - 1], inl[i + 1]
        if x.t == "Space" and prev and nxt and prev.t == "Str" and nxt.t == "Str"
            and prev.text:match("%d$") and nxt.text:match("^%d%d%d%f[%D]") then
          out:insert(pandoc.Str("\u{00A0}"))
        else
          out:insert(x)
        end
      end
      return out
    end
  }
end

local function fix_quotes(el)
  return el:walk {
    Quoted = function(q)
      local open, close = "«", "»"
      if q.quotetype == "SingleQuote" then open, close = "‹", "›" end
      local out = pandoc.List({ pandoc.Str(open) })
      out:extend(q.content)
      out:insert(pandoc.Str(close))
      return out
    end
  }
end

local function blocks_tex(blocks)
  if #blocks == 0 then return "" end
  local doc = nbsp_numbers(fix_quotes(pandoc.Pandoc(blocks)))
  return trim(pandoc.write(doc, "latex"))
end

local function inlines_tex(inlines)
  if inlines == nil or #inlines == 0 then return "" end
  return blocks_tex({ pandoc.Plain(inlines) })
end

local function meta_inlines(v)
  if v == nil then return nil end
  local ty = utils.type(v)
  if ty == "Inlines" then return v end
  if ty == "Blocks" then return pandoc.List(utils.blocks_to_inlines(v)) end
  if ty == "string" then return pandoc.List({ pandoc.Str(v) }) end
  if ty == "List" then
    local out = pandoc.List()
    for i, item in ipairs(v) do
      if i > 1 then out:insert(pandoc.Str(", ")) end
      out:extend(meta_inlines(item) or {})
    end
    return out
  end
  return pandoc.List({ pandoc.Str(utils.stringify(v)) })
end
local function meta_tex(v) return inlines_tex(meta_inlines(v)) end

local function nbsp_phone(s) return (s:gsub(" ", "\u{00A0}")) end

local function has_class(el, cls)
  for _, c in ipairs(el.classes) do if c == cls then return true end end
  return false
end

-- find (and optionally remove) the first image in a list of blocks
local function extract_image(blocks)
  local found
  local new = {}
  for _, b in ipairs(blocks) do
    local before = found
    local nb = b:walk {
      Image = function(img)
        if not found then found = img.src; return {} end
      end
    }
    if found and not before then
      -- the block held the image: drop it if nothing but the image (and spaces) was in it
      if b.t == "Figure" or utils.stringify(nb):match("^%s*$") then nb = nil end
    end
    if nb then table.insert(new, nb) end
  end
  return found, new
end

local function item_image(item)
  local src
  for _, b in ipairs(item) do
    b:walk { Image = function(img) src = src or img.src end }
  end
  return src
end

local function notes_tex(blocks, title)
  if #blocks == 0 then return "" end
  local t = blocks_tex(blocks)
  if title ~= "" then t = "{\\kwmedium\\kwsize{14}{18}\\color{kwdarkgreen}" .. title .. "}\\par\\vskip 4mm " .. t end
  return t
end

-- ---------- slide builders ----------
local function slide_title(h) return inlines_tex(h.content) end

local function split_lead(blocks, is_lead)
  if is_lead and #blocks > 0 and (blocks[1].t == "Para" or blocks[1].t == "Plain") then
    local lead = inlines_tex(blocks[1].content)
    local rest = {}
    for i = 2, #blocks do table.insert(rest, blocks[i]) end
    return lead, rest
  end
  return "", blocks
end

local function build_columns(div)
  -- returns a list of {heading=, blocks=}
  local cols = {}
  for _, c in ipairs(div.content) do
    if c.t == "Div" and has_class(c, "column") then
      local heading, body = "", {}
      for i, b in ipairs(c.content) do
        if b.t == "Header" and heading == "" and #body == 0 then
          heading = inlines_tex(b.content)
        else
          table.insert(body, b)
        end
      end
      table.insert(cols, { heading = heading, blocks = body })
    end
  end
  return cols
end

local function slide_tex(h, blocks, notes)
  local classes = h.classes
  local title = slide_title(h)
  local ntex = notes_tex(notes, title)
  local lead, rest
  local function is(c) return has_class(h, c) end

  if is("quote") then
    local quote, source = {}, ""
    for _, b in ipairs(blocks) do
      if b.t == "BlockQuote" then
        for _, q in ipairs(b.content) do table.insert(quote, q) end
      elseif (b.t == "Para" or b.t == "Plain") and b.content[1] and b.content[1].t == "Str"
          and b.content[1].text:match("^Kilde:") then
        local inl = pandoc.List(b.content)
        local first = inl[1].text:gsub("^Kilde:", "")
        inl:remove(1)
        if first ~= "" then inl:insert(1, pandoc.Str(first)) end
        if inl[1] and inl[1].t == "Space" then inl:remove(1) end
        source = inlines_tex(inl)
      elseif source == "" and #quote == 0 then
        table.insert(quote, b)
      end
    end
    local qtex = blocks_tex(quote):gsub("\n\n", "\\par\\vskip 6mm ")
    return string.format("\\kwquoteslide{%s}{%s}{%s}", qtex, source, ntex)
  end

  if is("figures") then
    lead, rest = split_lead(blocks, true)
    -- a leading paragraph is only a lead if it is not the definition list
    local items = {}
    for _, b in ipairs(rest) do
      if b.t == "DefinitionList" then
        for _, it in ipairs(b.content) do table.insert(items, it) end
      end
    end
    if #items == 0 and lead == "" then lead = "" end
    local n = math.min(#items, 4)
    local out = {}
    local y = (lead == "") and 62 or 88
    for i = 1, n do
      local term = inlines_tex(items[i][1])
      local def = ""
      if items[i][2][1] then def = blocks_tex(items[i][2][1]) end
      table.insert(out, string.format("\\kwfig{%d}{%d}{%d}{%s}{%s}", i, n, y, term, def))
    end
    return string.format("\\kwfigures{%s}{%s}{%s}{%s}", title, lead, table.concat(out, "\n"), ntex)
  end

  if is("logos") then
    lead, rest = split_lead(blocks, true)
    local items = {}
    for _, b in ipairs(rest) do
      if b.t == "BulletList" then
        for _, it in ipairs(b.content) do table.insert(items, it) end
      end
    end
    local y = (lead == "") and 62 or 80
    local out = {}
    for i = 1, math.min(#items, 8) do
      local src = item_image(items[i])
      if src then
        table.insert(out, string.format("\\kwlogoimg{%d}{%d}{%s}", i, y, src))
      else
        -- longest unbreakable piece (split at spaces and hyphens): the theme checks that it fits the tile
        local plain, longest = utils.stringify(pandoc.Div(items[i])), ""
        for piece in plain:gmatch("[^%s%-]+") do
          if utf8.len(piece) and utf8.len(piece) > (utf8.len(longest) or 0) then longest = piece end
        end
        longest = longest:gsub("[\\{}%%#&_$^~]", "")
        table.insert(out, string.format("\\kwlogo{%d}{%d}{%s}{%s}", i, y, blocks_tex(items[i]), longest))
      end
    end
    return string.format("\\kwlogos{%s}{%s}{%s}{%s}", title, lead, table.concat(out, "\n"), ntex)
  end

  if is("closing") then
    local contacts = pandoc.List()
    local cm = doc_meta and doc_meta.contacts
    local out = {}
    local body = {}
    for _, b in ipairs(blocks) do table.insert(body, b) end
    if #body > 0 then
      table.insert(out, string.format("\\kwclosingtext{%s}", blocks_tex(body)))
    elseif cm then
      for i, c in ipairs(cm) do
        local function f(k) return c[k] and utils.stringify(c[k]) or "" end
        local name = f("name")
        if name ~= "" then
          local phone = nbsp_phone(f("phone"))
          table.insert(out, string.format("\\kwcontact{%d}{%s}{%s}{%s}{%s}", i,
            inlines_tex(meta_inlines(c.name)), inlines_tex(meta_inlines(c.role)),
            f("email"):gsub("_", "\\_"), inlines_tex(pandoc.List({ pandoc.Str(phone) }))))
        end
      end
    end
    if #out == 0 then
      -- no contacts and no text: a tidy default block so the closing slide is never nearly empty
      table.insert(out, "\\kwcontact{1}{KodeWorks}{}{post@kodeworks.no}{kodeworks.no}")
    end
    return string.format("\\kwclosing{%s}{%s}{%s}", title, table.concat(out, "\n"), ntex)
  end

  -- columns / comparison
  for _, b in ipairs(blocks) do
    if b.t == "Div" and has_class(b, "columns") then
      local before = {}
      for _, bb in ipairs(blocks) do
        if bb == b then break end
        table.insert(before, bb)
      end
      lead, _ = split_lead(before, true)
      if lead == "" and #before > 0 then lead = blocks_tex(before) end
      local cols = build_columns(b)
      local n = #cols
      local out = {}
      for i, c in ipairs(cols) do
        table.insert(out, string.format("\\kwcol{%d}{%d}{\\kwcy}{%s}{%s}", i, n, c.heading, blocks_tex(c.blocks)))
      end
      return string.format("\\kwcolumns{%s}{%s}{%s}{%s}", title, lead, table.concat(out, "\n"), ntex)
    end
  end

  -- image slide
  if is("image") then
    local src, others = extract_image(blocks)
    if src then
      lead, rest = split_lead(others, is("lead"))
      return string.format("\\kwimageslide{%s}{%s}{%s}{%s}{%s}", title, lead, blocks_tex(rest), src, ntex)
    end
    blocks = others
  end

  -- plain content (with optional lead)
  lead, rest = split_lead(blocks, is("lead"))
  return string.format("\\kwcontent{%s}{%s}{%s}{%s}", title, lead, blocks_tex(rest), ntex)
end

function Pandoc(doc)
  doc_meta = doc.meta
  local meta = doc.meta
  local out = {}
  local function raw(s) table.insert(out, pandoc.RawBlock("latex", s)) end
  -- every slide is a level-2 header with an empty title; pandoc opens the frame, the theme macros fill it
  local function slide(s)
    table.insert(out, pandoc.Header(2, {}, pandoc.Attr("", { "t" })))
    raw(s)
  end

  -- title slide from YAML
  local title = meta_tex(meta.title)
  if title ~= "" then
    local date = meta_tex(meta.date)
    slide(string.format("\\kwtitleslide{%s}{%s}{%s}{%s}{}", title, meta_tex(meta.subtitle), meta_tex(meta.author), date))
  end

  local blocks = doc.blocks
  local i, section_no = 1, 0
  local n = #blocks
  local function collect_until(maxlevel)
    local body = {}
    while i <= n do
      local b = blocks[i]
      if b.t == "Header" and b.level <= maxlevel then break end
      table.insert(body, b)
      i = i + 1
    end
    return body
  end
  local function split_notes(body)
    local content, notes = {}, {}
    for _, b in ipairs(body) do
      if b.t == "Div" and has_class(b, "notes") then
        for _, nb in ipairs(b.content) do table.insert(notes, nb) end
      else
        table.insert(content, b)
      end
    end
    return content, notes
  end

  while i <= n do
    local b = blocks[i]
    if b.t == "Header" and b.level == 1 then
      i = i + 1
      section_no = section_no + 1
      local number = b.attributes["number"] or string.format("%02d", section_no)
      local body = collect_until(2)
      local content, notes = split_notes(body)
      local text = ""
      for _, c in ipairs(content) do
        if (c.t == "Para" or c.t == "Plain") and text == "" then text = inlines_tex(c.content) end
      end
      slide(string.format("\\kwdivider{%s}{%s}{%s}{%s}", number, inlines_tex(b.content), text, notes_tex(notes, inlines_tex(b.content))))
    elseif b.t == "Header" and b.level == 2 then
      i = i + 1
      local body = collect_until(2)
      local content, notes = split_notes(body)
      slide(slide_tex(b, content, notes))
    else
      i = i + 1 -- stray content before the first heading is ignored
    end
  end

  -- the title is consumed here, so the pandoc template must not emit its own title page
  meta.title, meta.subtitle, meta.author, meta.date, meta.contacts = nil, nil, nil, nil, nil
  meta.theme = pandoc.MetaString("kodeworks")
  meta.aspectratio = pandoc.MetaString("169")
  if not meta.lang then meta.lang = pandoc.MetaString("nb") end
  return pandoc.Pandoc(out, meta)
end
