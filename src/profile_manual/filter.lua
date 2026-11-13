-- Pandoc Lua filter: turns fenced divs into layout macros (see NOTES.md).
local function esc(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([&%%#_{}$])", "\\%1")
  s = s:gsub("%s*|%s*", "\\\\")
  return s
end
local function attr(el, k, d) return el.attributes[k] or d end
local defbg = {white="kwwhite", grey="kwgrey", green="kwgreen", black="kwblack",
  darkgreen="kwdarkgreen", deepgreen="kwdeepgreen", pink="kwpink"}
local darkbg = {black=true, darkgreen=true, deepgreen=true}
local deffooter = {white="grey", grey="white", green="none", black="black",
  darkgreen="none", deepgreen="none", pink="none"}

function Div(el)
  local c = el.classes[1]
  if c == "cover" then
    return pandoc.RawBlock("latex", string.format("\\kwcover{%s}{%s}{%s}",
      esc(attr(el,"title","")), esc(attr(el,"subtitle","")), esc(attr(el,"meta",""))))
  elseif c == "divider" then
    return pandoc.RawBlock("latex", string.format("\\kwdivider{%s}{%s}{%s}",
      esc(attr(el,"number","")), esc(attr(el,"title","")), esc(attr(el,"text",""))))
  elseif c == "page" then
    local bg = attr(el, "bg", "white")
    local fg = attr(el, "fg", darkbg[bg] and "kwwhite" or "kwblack")
    local footer = attr(el, "footer", deffooter[bg] or "grey")
    local out = {pandoc.RawBlock("latex", string.format("\\kwbegin{%s}{%s}{%s}{%s}",
      esc(attr(el,"section","")), defbg[bg] or bg, fg, footer))}
    local title = attr(el, "title", nil)
    if title then
      out[#out+1] = pandoc.RawBlock("latex", string.format("\\kwpagehead{%s}{%s}",
        esc(title), esc(attr(el,"lead",""))))
    end
    for _, b in ipairs(el.content) do out[#out+1] = b end
    return out
  elseif c == "cols" then
    local n = attr(el, "n", "2")
    local out = {pandoc.RawBlock("latex", "\\begin{multicols}{" .. n .. "}")}
    for _, b in ipairs(el.content) do out[#out+1] = b end
    out[#out+1] = pandoc.RawBlock("latex", "\\end{multicols}")
    return out
  elseif c == "colbreak" then
    return pandoc.RawBlock("latex", "\\columnbreak")
  end
end

function Header(el)
  local macro = ({"\\kwhone","\\kwhtwo","\\kwhthree"})[math.min(el.level,3)]
  local inl = pandoc.List({pandoc.RawInline("latex", macro .. "{")})
  inl:extend(el.content)
  inl:insert(pandoc.RawInline("latex", "}"))
  return pandoc.Para(inl)
end

-- Pandoc pipe/grid tables -> kwtable (profile style). Column widths from the
-- relative dash widths of the pipe table separator, equal widths when unspecified.
local function cell_tex(cell)
  local s = pandoc.write(pandoc.Pandoc(cell.contents), "latex")
  s = s:gsub("%s+$", ""):gsub("\n\n", "\\par ")
  return s
end

function Table(el)
  local n = #el.colspecs
  local total, haswidth = 0, false
  for _, cs in ipairs(el.colspecs) do
    local w = cs[2]
    if type(w) == "number" then total = total + w; haswidth = true end
  end
  local spec = {"@{}"}
  for i, cs in ipairs(el.colspecs) do
    local frac = (haswidth and total > 0) and cs[2] / total or 1 / n
    spec[#spec+1] = string.format("p{\\dimexpr(\\linewidth-%d\\dimexpr4mm\\relax)*%d/1000\\relax}", n - 1, math.floor(frac * 1000 + 0.5))
    spec[#spec+1] = (i < n) and "@{\\hspace{4mm}}" or "@{}"
  end
  local out = {"\\begin{kwtable}{" .. table.concat(spec) .. "}"}
  local function row_tex(row, head)
    local cells = {}
    for _, c in ipairs(row.cells) do
      local t = cell_tex(c)
      cells[#cells+1] = head and ("\\kwth{" .. t .. "}") or t
    end
    return table.concat(cells, " & ") .. " \\\\ \\hline"
  end
  for _, r in ipairs(el.head.rows) do out[#out+1] = row_tex(r, true) end
  for _, b in ipairs(el.bodies) do
    for _, r in ipairs(b.body) do out[#out+1] = row_tex(r, false) end
  end
  out[#out+1] = "\\end{kwtable}"
  return pandoc.RawBlock("latex", table.concat(out, "\n"))
end
