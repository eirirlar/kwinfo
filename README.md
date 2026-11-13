# KodeWorks – knowledge base and deliverables

This repository holds two things for the KodeWorks companies (KodeWorks AS, KodeWorks Trondheim AS, KodeWorks Eiendom AS and KodeWorks Oslo AS):

- **Tools and templates in the KodeWorks visual profile.** Every employee's CV is kept here in Markdown and built into a PDF and a business card. There are also templates for presentations, letters, documents and business cards, and the profile manual.
- **A knowledge base** about the companies (structure, background, key figures, governing documents) in `background/`, and finished deliverables in `deliverable/`.

Everything is built with Python scripts in `src/` and gives the same result on Windows, WSL2 and Linux.

## Quick start

### What you can use it for

| I want to … | Command (from the project root) | Guide |
|---|---|---|
| Update my CV and get a PDF and business card | `uv run python src/build_employee_cvs.py <my-folder>` | [CV guide](deliverable/visualprofile/cv/README.md) |
| Make a presentation | `uv run src/build_presentation.py <deck>.md` | [Presentation guide](deliverable/visualprofile/presentation/README.md) |
| Write a letter or an A4 document | `uv run src/build_document.py <file>.md` | [Document guide](deliverable/visualprofile/document/README.md) |
| Make a business card on its own | `uv run src/build_business_card.py <card>.md` | [Business card guide](deliverable/visualprofile/business-card/README.md) |
| Build every PDF in the repo | `uv run python src/build_all.py` | [Building everything](#building-everything-srcbuild_allpy) |
| Write the monthly ITKO report | Copy last month's file in `deliverable/itko/` | [ITKO reporting](#itko-reporting-deliverableitko) |
| Fetch files from Google Drive | `uv run python src/fetch_from_drive.py <link>` | [Fetching from Google Drive](#fetching-from-google-drive-srcfetch_from_drivepy) |

Your CV is `cvs/<my-folder>/<my-folder>.md`, where the folder is your name in lower case with hyphens (æ → ae, ø → oe, å → aa). The documents themselves (CVs, letters, presentations) are written in Norwegian or English. The documentation, the code and the file names are in English.

### What to install

| Tool | Needed for | Windows | Linux / WSL2 (Ubuntu) |
|---|---|---|---|
| [uv](https://docs.astral.sh/uv/) | everything | `winget install --id=astral-sh.uv` | `sudo apt install pipx && pipx install uv && pipx ensurepath` |
| TeX Live with `lualatex` | every PDF build | installer from <https://tug.org/texlive/> | `sudo apt install texlive-luatex texlive-lang-european texlive-fonts-recommended texlive-fonts-extra` |
| Pandoc | every PDF build (the CV command also builds the business card, which uses Pandoc) | `winget install --id=JohnMacFarlane.Pandoc` | `sudo apt install pandoc` |
| Poppler (`pdftotext`, `pdfimages`) | only the document conversion tools | `choco install poppler` | `sudo apt install poppler-utils` |
| Node + `mermaid-filter` | only Mermaid diagrams in reports | see [Mermaid diagrams](#mermaid-diagrams-in-reports) | see [Mermaid diagrams](#mermaid-diagrams-in-reports) |
| OAuth files in `secrets/` | only fetching from Google Drive | see [Fetching from Google Drive](#fetching-from-google-drive-srcfetch_from_drivepy) | same |

No fonts need to be installed. The profile font is unpacked from the licensed font file in the repo, and all other fonts come from TeX Live. Restart the terminal after installing, so the tools are on `PATH`.

### Set up (once per machine)

**Windows (Git Bash or PowerShell), from the project root:**

```bash
uv sync                  # creates .venv and installs the dependencies from uv.lock
```

**Linux / WSL2, from the project root:**

```bash
echo 'export UV_PROJECT_ENVIRONMENT=.venv-linux' >> ~/.bashrc   # only when the checkout is shared with Windows (/mnt/c/...)
source ~/.bashrc
uv sync                  # creates .venv-linux and installs the dependencies from uv.lock
```

A virtual environment cannot be shared between Windows and Linux. The setting keeps the Linux one in its own folder (see [Python setup](#python-setup)).

### Check that it works

```bash
uv run pytest --timeout=3                                    # all tests pass, in a few seconds
uv run python src/build_employee_cvs.py paal-noedseth        # builds one CV and business card, about 10 seconds
```

The second command ends with `CV check: 1 files, 0 with deviations` and writes `cvs/paal-noedseth/paal-noedseth.pdf` (on a second run it reports the CV as unchanged instead). If it stops with a message about `lualatex` or `pandoc`, that tool is missing from `PATH`.

### Other files at the root

- `CLAUDE.md` – project context and working rules for the AI assistant (Claude Code).
- `TASKS.md` and `ARCHIVE.md` – open and solved tasks.

---

## Folder structure

```
<project root>/
├── CLAUDE.md        – project context and working rules for the AI assistant
├── README.md        – this document
├── TASKS.md         – open tasks; ARCHIVE.md: solved tasks
├── background/      – source documents, analyses and notes (date prefix YYYY-MM-DD_)
│   ├── new/         – inbox for new originals; emptied once they are converted
│   └── visualprofile/Fonts/ – the profile font Non Natural Grotesk (licensed, with the licences); used by every build
├── cvs/             – the employees' CVs in Markdown, one folder per person (<name>.md, images/photo.jpg); updated with commits.
│                      logos/: shared logo library, one file per customer.
│                      The CV PDF and business card are built next to the CV and kept out of git. DEVIATIONS.md: what the consultants should fix
├── deliverable/     – finished documents (reports, notes, presentations)
│   ├── itko/        – monthly ITKO Temp reports (report_YYYY-MM.md)
│   └── visualprofile/ – the revised visual profile (profile/) and templates built on it (cv/, presentation/, document/, business-card/)
├── src/             – Python scripts and helper tools
│   ├── profile_manual/ – layout system (LaTeX template, page types, components, palette, kerning fixes) for the profile manual
│   ├── cv_pdf/         – LaTeX style for the CV template (src/build_cv_pdf.py)
│   ├── presentation/   – beamer theme and Lua filter for the presentation template (src/build_presentation.py)
│   ├── document/       – LaTeX style, pandoc template and Lua filter for the document template (A4, letter; src/build_document.py)
│   ├── business_card/  – LaTeX template for the business card (src/build_business_card.py)
│   ├── build_all.py    – builds every PDF and PNG from the sources (see «Building everything»)
│   └── project_tmp.py  – working folders for the scripts in tmp/ (see «Conventions»)
├── tests/           – pytest tests for the scripts in src/ (fixtures/documents/: test corpus for the document template)
├── data/            – local working data, ignored by git (drive/: fetched from Google Drive; cv_sources.csv: links to the CV documents)
├── secrets/         – Google OAuth client and token (ignored by git, added per machine)
├── tmp/             – temporary files and working folders for the scripts (ignored by git, can be deleted when nothing is running)
├── .claude/skills/  – project skills for Claude Code (overview in .claude/skills/README.md)
└── pyproject.toml   – project environment (uv), with uv.lock and .python-version
```

## Conventions

- **Language:** documentation (this README, the template guides), code, variable names, command-line flags, messages from the scripts, folder names and file names are in English. Documents and reports for readers (CVs, letters, presentations, the profile manual, the notes in `background/`) are written in Norwegian (bokmål), or in English where the document is meant for English readers. Nine older background documents keep Norwegian file names (the list is in `tests/test_english_names.py`).
- **File names in `background/`:** use the date prefix `YYYY-MM-DD_description.ext` (e.g. `2026-09-22_company_structure.md`). The date is the document's own date, not the date it was filed.
- **New files:** put incoming, unclassified files in `background/new/`. They are converted to Markdown, given a date prefix and moved out to `background/`.
- **Scripts:** all scripts are in `src/` and are run from the project root (`uv run python src/name.py`).
- **Temporary files:** the scripts do not write outside the project. Working folders and intermediate files go in `tmp/` at the project root (ignored by git), via `src/project_tmp.py`: `work_dir(prefix)` creates a folder that is deleted when the block ends, also on errors, and `mkdtemp(prefix)` creates a folder the script deletes itself (kept with `--keep-build`). The test `tests/test_project_tmp.py` fails if a script in `src/` uses the system's temporary folder. Installed programs (uv, LuaLaTeX, pytest, pandoc) keep their own caches and temporary folders.
- **Docx/PDF of reports:** Markdown is the source. Conversion to `.docx`/`.pdf` is done with Pandoc, only when it is ordered explicitly.
- **Line endings and file permissions:** every text file has LF line endings in the repo and in every checkout, also on Windows. This is set by `.gitattributes`, independent of each person's git settings. No file in the repo is executable: scripts are started with `uv run`, not directly, so they do not need the executable bit.

---

## Python setup

**`uv`** manages Python versions and virtual environments. Installation is shown under [What to install](#what-to-install). Upgrade with `uv self update`.

### Two ways to declare dependencies

1. **Project environment (`pyproject.toml` + `uv.lock`).** Shared dependencies (the Google API for `src/fetch_from_drive.py`) and development tools (`pytest`, `pytest-timeout`) are in `pyproject.toml`; `uv.lock` pins the versions and is checked in. The Python version is in `.python-version` (3.11). The project is not an installable package (`package = false`).
2. **Inline per script (PEP 723).** Scripts with their own, heavier dependencies (visual profile, CV generation) declare them at the top of the file and run in their own temporary environment, independent of the project environment:

   ```python
   # /// script
   # dependencies = ["openpyxl", "python-docx", "pypdf", "Pillow"]
   # ///
   ```

| Script type | Run with |
|---|---|
| Without an inline block (uses the project environment) | `uv run python src/name.py` |
| With a PEP 723 block | `uv run src/name.py` (`uv run python …` ignores the inline block) |

### Venv per operating system

A venv is not portable between Windows and Linux. When the same checkout is used from both Windows and WSL2 (`/mnt/c/dev/...`), each OS needs its own venv folder:

| Environment | Venv folder | Setup |
|---|---|---|
| Windows (Git Bash, PowerShell) | `.venv` (uv default) | nothing extra |
| WSL2 / native Linux | `.venv-linux` | `export UV_PROJECT_ENVIRONMENT=.venv-linux` in `~/.bashrc` |

Both are ignored by git. The value is relative to the project root, so the same line in `~/.bashrc` works for every project that follows the convention. Native Linux without a shared Windows checkout can just as well use `.venv`.

**Activation per terminal window** is not needed: `uv run …` finds and syncs the right venv itself. To activate anyway (e.g. for an IDE or a REPL):

```bash
source .venv/Scripts/activate      # Git Bash (Windows)
.\.venv\Scripts\Activate.ps1       # PowerShell (Windows)
source .venv-linux/bin/activate    # WSL2 / Linux
```

**New dependency:** `uv add <package>` (or `uv add --dev <package>` for development tools). This updates `pyproject.toml` and `uv.lock`.

### Tests

Tests are in `tests/` and are run from the project root:

```bash
uv run pytest --timeout=3
```

Always pass `--timeout` (the default of 3 seconds is also set in `pyproject.toml`), so a hanging test cannot lock the terminal. `tests/` imports modules directly from `src/` (`pythonpath = ["src"]`).

`tests/test_english_names.py` enforces the language rule: help texts for flags, messages from the scripts, folder names and file names must be in English. File names are checked against a list of Norwegian words, so person and customer names in `cvs/` do not trigger it. Nine background documents are exempt, and the test checks that they still exist. Text in «…» in a message counts as content.

---

## Building everything (`src/build_all.py`)

PDFs and PNGs made from Markdown sources are not in git. They are built next to their sources, and `.gitignore` keeps them out. After a new checkout, or when something has changed, one command builds everything that is out of date:

```bash
uv run python src/build_all.py                      # everything out of date, the employees' CVs last
uv run python src/build_all.py --list               # every target, and whether it is up to date
uv run python src/build_all.py --dry-run            # what would be built, and why
uv run python src/build_all.py --only cv,document   # only some groups
uv run python src/build_all.py --force              # rebuild everything
uv run python src/build_all.py --no-check           # skip the checks after each build
```

A target is built only when an output file is missing, or when one of its input files is newer than the output files. The input files are the source, the images, the style and template files, the build script and the font archive. A target that uses the result of another target (for example the overview sheet, which shows all the other PDFs) is also rebuilt when the other target is built in the same run. The command exits with code 1 if a build or a check fails.

The groups, in build order:

| Group | What | Script |
|---|---|---|
| `assets` | Logos and graphics from SVG to PDF and PNG (`profile/assets/pdf/`, `png/`) | `src/export_profile_assets.py` |
| `profile` | The profile manual (`profile/profile-manual.pdf`) | `src/build_profile_manual.py` |
| `cv` | The CV template and the CV example | `src/build_cv_pdf.py`, checked with `src/check_cv_md.py` |
| `presentation` | The presentation template and the example | `src/build_presentation.py`, checked with `src/check_presentation_pdf.py` |
| `document` | Letter template, document template and two examples | `src/build_document.py`, checked with `src/check_document_pdf.py` |
| `business-card` | The business card template and the example card (the print checks are part of the build) | `src/build_business_card.py` |
| `overview` | The overview sheet of all the deliverables (`overview.pdf`) | `src/build_visualprofile_overview.py` |
| `employee-cvs` | CV PDF and business card for each employee in `cvs/` | `src/build_employee_cvs.py` |

The employees' CVs have their own command with the same change check, which `build_all.py` runs last. It checks all the CVs with `src/check_cv_md.py` after the builds:

```bash
uv run python src/build_employee_cvs.py                    # every CV that is out of date
uv run python src/build_employee_cvs.py paal-noedseth      # one person (the folder name in cvs/)
uv run python src/build_employee_cvs.py --list | --dry-run | --force
```

A full build from an empty checkout takes several minutes, mostly for the employees' CVs (10–45 seconds each). The list of targets and the change check are in `src/build_targets.py`. The test `tests/test_build_all.py` checks that every Markdown source in the template folders is in the build list, and that all output files are covered by `.gitignore` while the sources are not. A new template or example must therefore be added to `src/build_all.py`.

---

## Visual profile (`deliverable/visualprofile/`)

The revised visual profile for KodeWorks (2026), based on the design manual from 2021 (by the agency Neue) and the design of kodeworks.no (mapped in `background/2026-11-11_kodeworks_no_design.md`). The profile stands on its own: logos and graphics are cleaned SVGs in `profile/assets/`, and the 2021 originals are not in the repo (they are on Google Drive). Only the profile font is left from the old delivery, in `background/visualprofile/Fonts/`. The templates (CV, business card, presentation, letter and document) build on the profile and have their own subfolders.

```
deliverable/visualprofile/profile/
├── profile-manual.md    – source: one Markdown file with page types (::: {.cover} / {.divider} / {.page}) and raw LaTeX components
├── profile-manual.pdf   – 40 pages 16:9 (297 × 167 mm), Non Natural Grotesk embedded
├── colors.md / .json  – palette with roles, HEX/RGB/CMYK/PMS (proposals marked) and a computed contrast matrix
├── assets/            – cleaned SVGs (wordmark, symbol, fifth element; presentation/ for slide backgrounds)
│   ├── pdf/           – vector PDF of each SVG (generated)
│   └── png/           – transparent PNG, 2000 px longest side (generated)
└── images/            – KodeWorks' own photos (from kodeworks.no) used in the manual
```

**Build the manual:**

```bash
uv run src/build_profile_manual.py          # → deliverable/visualprofile/profile/profile-manual.pdf (~20 s)
```

The script builds in a working folder under `tmp/` and writes only the PDF. The engine is **lualatex**, because it loads the Norwegian bokmål hyphenation patterns at run time. The xelatex format does not have them and silently hyphenates with English patterns. `src/profile_manual/kernfix.json` adds kerning pairs the font lacks: around j (sj, kj …) and r–f. The fixes are switched on in `fonts.tex` and shared with the CV template. The script unpacks Non Natural Grotesk from the licensed font zip in `background/visualprofile/Fonts/` and loads the fonts with fontspec `Path=` (no installation; the licence allows embedding in PDF, not in `.docx`/`.pptx`). SVGs are converted to PDF with PyMuPDF (`rsvg-convert` is not needed). The layout system is in `src/profile_manual/`: `colors.tex` is the only place the palette is defined, `layout.tex` has page types and components (`\kwtile`, `\kwswatch`, `\kwmark`, `\kwtable` …), and `filter.lua` turns `:::` blocks into macros. Each `.page` is one physical page with no automatic page break, so check the PDF after changes. The examples of the fallback font Arial are shown with TeX Gyre Heros from TeX Live, which has the same character widths. The build copies it into the build folder.

**Platform independence (`src/font_guard.py`).** Every document build must give the same result on Windows, WSL2 and Linux, whatever fonts are installed on the machine. Fonts are therefore loaded only as files: the profile font from the font zip in the repo, and everything else from TeX Live (TeX Gyre, DejaVu, Latin Modern). The profile manual, the CV template and the control PDFs of Markdown have a font check. LuaTeX writes the file name of every font it loaded, and the build stops with an error if a font is outside the build folder or the TeX trees. `tests/test_platform_independence.py` also checks that no build source refers to the system's font folders or to fonts that exist only as installed fonts.

**Export assets** (after changing an SVG):

```bash
uv run src/export_profile_assets.py         # → assets/pdf/*.pdf and assets/png/*.png
```

**Contrast matrix:**

```bash
uv run src/wcag_contrast.py deliverable/visualprofile/profile/colors.json
```

Writes WCAG 2.x contrast ratios for every colour pair (AA normal 4.5:1, AA large text 3:1, AAA 7:1) as Markdown. Reads `colors` and, if present, `technical` from the JSON file.

### CV template, version 3 (`deliverable/visualprofile/cv/`)

The CV is written in **Markdown** and typeset directly to PDF with lualatex. There is no Word file, no LibreOffice and no raster graphics apart from the photo and customer logos. The folder contains:
- `cv-template.md` and `.pdf`: an empty template, with guidance in HTML comments;
- `cv-example.md` and `.pdf`: Pål Nødseth's CV with 8 projects, his own portrait and customer logos, in `images/`;
- `README.md`: the guide for consultants, with the format, photo and logo, writing advice and a checklist.

```bash
uv run src/build_cv_pdf.py deliverable/visualprofile/cv/cv-template.md deliverable/visualprofile/cv/cv-template.pdf        # 5–40 s
uv run src/build_cv_pdf.py deliverable/visualprofile/cv/cv-example.md deliverable/visualprofile/cv/cv-example.pdf
uv run src/build_cv_pdf.py <cv.md> <out.pdf> --keep <folder>    # keeps the whole build folder (cv.tex, cv.log) for debugging
uv run python src/cv_markdown.py <cv.md>                         # shows the data model as JSON
uv run python src/check_cv_md.py <cv.md> [...]                   # checks the conventions, exit 1 on deviations
```

- **`cv_markdown.py`** reads the CV from Markdown and gives the build script's data model. It can also go the other way.
  - `#` is the name, the paragraph below is the title, and the list of «Label: value» is the contact information.
  - `## Om …`, `## Teknisk kompetanse` (with `###` per group) and `## Erfaring` (with `###` per project: metadata list, description and a line «Nøkkelord:»).
  - `## Arbeidserfaring`, `## Utdanning` and `## Sertifiseringer` have rows of the form `period | name | place`. Every other `##` becomes its own list.
  - English labels and headings give an English CV.
  - The format is described in the module docstring and in the CV guide, and tested in `tests/test_cv_markdown.py`.
- **`check_cv_md.py`** checks that every CV follows the same conventions:
  - section order and fixed titles for the extra lists;
  - contact list in a fixed order and form;
  - projects newest first and fields in a fixed order;
  - periods as `MM.YYYY – nå`;
  - skill groups in sentence case without duplicates;
  - bullet points as Markdown lists;
  - images in `images/photo.*` and `images/logo-<customer>.*`; for the employees' CVs in `cvs/` the logos come from `../logos/<customer>.*`, the photo is a JPG without metadata with at most 1200 pixels across the crop, and PNG logos are at most 700 × 260 pixels (the image headers are read without Pillow);
  - round trip parse → render → parse.

  Tested in `tests/test_check_cv_md.py` and `tests/test_cv_images.py`.
- **The employees' CVs** are in Markdown in `cvs/<name>/`, one folder per person: `<name>.md` and `images/photo.jpg`. The customer logos are in the shared logo library `cvs/logos/<customer>.<ext>`, one file per customer. The developers update their own CV with commits in git. The CV PDF and business card are built next to it and kept out of git. `cvs/DEVIATIONS.md` lists what the consultants should fix. The files were converted once from the Word originals and are now maintained in Markdown in git.
- **`normalize_cv_images.py`** (Pillow, numpy) gives the photos and logos in `cvs/` the same format: photos as JPG with quality 85 (lower, down to 70, if the file would otherwise grow), sRGB, without metadata, transparency flattened onto white, and scaled down so the crop with the frame's aspect ratio (60:74) is 1200 pixels wide. Logos have their edges trimmed and are scaled down to at most 700 × 260 pixels, and PNGs are saved with a palette. Images are never scaled up, and the photo is not cropped in the file. The default is a dry run that shows the change per file and flags files that shrink below 30 %. `--apply` changes the files and fixes the reference when a photo goes from `.png` to `.jpg`. The script is idempotent. `--self-test` checks the rules on synthetic images and is used by the tests.

  ```bash
  uv run src/normalize_cv_images.py            # dry run for every photo and logo in cvs/
  uv run src/normalize_cv_images.py --apply
  ```
- **`build_cv_pdf.py`** (PyMuPDF, PyYAML, fontTools, Pillow, numpy) builds the CV.
  - YAML with the same data model is still read, for tests.
  - All text is escaped for LaTeX. Glyphs the font lacks are removed with a warning.
  - Logos are trimmed, scaled by optical area and hidden when the customer is KodeWorks.
  - The photo is cropped to fill the frame. `Fotofokus` overrides the focus point.
  - The font is unpacked from the licensed zip, and the font check runs in every build.
- **Automatic fitting:** the build tries density 1 and 2, whether «Erfaring» starts on the front page, and a page break before «Generelt», and picks the fewest pages.
  - The requirements are a good front page (two columns first), no middle page under 40 % full and a last page down to 30 %.
  - The body text is always 9.5 pt.
  - Skills are never split inside a group, and short lists in «Generelt» are never split.
  - Projects have at least two lines on each side of a page break.
- **Style:** `src/cv_pdf/cv-style.tex` holds the geometry, fonts with kerning fixes (`src/profile_manual/kernfix.json`), palette, seismograph band, project blocks and hyphenation exceptions.

Versions 1 and 2 of the CV template (Word files via python-docx) are replaced by version 3. Both the deliverables and the generators are deleted.

- **`seismograph.py`** (PyMuPDF/Pillow): a general, deterministic generator for seismograph stripes in the profile's stroke (thick:thin 13:3), with the variants `band`, `band-up`, `closing`, `corner`, `vleft` and `vright`, as PNG and SVG: `uv run src/seismograph.py --width-mm 170 --height-mm 6 --variant band --colour B6FF9E --out band.png [--svg band.svg] [--thin-colour 000000] [--seed N]`. Made for reuse in the business card and the letter template.

### Presentation template (`deliverable/visualprofile/presentation/`)

Presentations are written in pandoc Markdown and typeset directly to PDF (16:9, 338.67 × 190.5 mm) with pandoc → beamer → lualatex. There is no PowerPoint file and no LibreOffice. The folder contains `presentation-template.md` and `.pdf` (a template that explains every slide type), `example.md` and `.pdf` (14 slides), `images/` and `README.md` (the guide, with the Markdown syntax for each slide type).

```bash
uv run src/build_presentation.py deliverable/visualprofile/presentation/example.md     # → example.pdf next to it (~6 s)
uv run src/build_presentation.py <deck.md> --notes            # → <deck>-notater.pdf with speaker notes
uv run src/build_presentation.py <deck.md> -o <out.pdf> [--theme-dir DIR] [--keep-build]
uv run src/check_presentation_pdf.py <deck.pdf>              # PASS/WARN/FAIL, exit 1 on FAIL
```

- **`build_presentation.py`** (PyMuPDF): unpacks the font from the licensed zip and exports the profile's SVGs to vector PDF in a working folder under `tmp/`, runs pandoc with the theme's Lua filter and lualatex twice, and deletes the build folder (`--keep-build` keeps it, with the font files; delete it afterwards). Image paths are relative to the Markdown file; missing images are reported with line numbers. Overfull/Underfull boxes and the theme's own warning «Too much text on slide …» are printed with the slide title. `max_print_line` is set high so the warnings are not cut off in the log.
- **Theme (`src/presentation/`):** `beamerthemekodeworks.sty` (absolute positioning in mm, surfaces, footer with the vector wordmark, seismograph on the opening and section dividers, content measuring: 20 pt → 18 pt → wider → scaling with a warning), `filter.lua` (the classes `.lead`, `.image`, `.quote`, `.figures`, `.logos`, `.closing`, section dividers from `#` with `number`, colour highlighting of `*word*` in titles, non-breaking spaces in numbers, «»), `template.tex`, and `kernfix.json` (the profile manual's kerning fixes plus pairs before a colon; the table is also embedded in the `.sty`, so changes must be made in both places). The font families are set with `Ligatures=TeX`; without it `--` and `'` do not become an en dash and a typographic apostrophe.
- **`check_presentation_pdf.py`** (PyMuPDF): page size, only NON Natural Grotesk and embedded, no raster images apart from photos (photos under 150 dpi effective give WARN), text outside the page, in the margin or in the footer area, text under 12 pt, colours outside `colors.json`, and nearly empty pages.

### Document template for A4, with a letter variant (`deliverable/visualprofile/document/`)

One shared template for A4 documents: the variant `letter` (sales letters, enquiries) and the variant `document` (consultant assignment postings, notes, offers). The source is pandoc Markdown with a YAML header, and the PDF is typeset with pandoc → LaTeX → lualatex. There is no Word file and no LibreOffice. New needs are added as elements in the shared template, not as local solutions in single documents. The folder contains `document-template.md`/`.pdf` and `letter-template.md`/`.pdf` (empty templates with instructions), `example-letter.md`/`.pdf` (a sales letter, two pages), `example-job-posting.md`/`.pdf` (the posting of the Android assignment) and `README.md` (YAML fields, syntax for each element, checklist).

```bash
uv run src/build_document.py deliverable/visualprofile/document/example-letter.md   # → example-letter.pdf next to it
uv run src/build_document.py <file.md> -o <out.pdf> [--style-dir DIR] [--keep-build]
uv run src/check_document_pdf.py <file.pdf> [--company "KodeWorks Oslo AS"]      # OK/WARN/FAIL, exit 1 on FAIL
uv run src/check_document_pdf.py --self-test                                      # a deliberately bad PDF; every check must fire
```

- **`build_document.py`** (PyMuPDF): imports `extract_fonts`, `write_kernfix`, `build_assets`, `find_root` and more from `build_presentation.py`, unpacks the font from the licensed zip in a working folder under `tmp/`, exports the profile's SVGs to vector PDF, enforces `font_guard.py`, runs pandoc with the style's template and Lua filter and lualatex twice, and deletes the build folder also on errors (`--keep-build` keeps it, with the font files, and warns about it). The kerning fixes come from `src/presentation/kernfix.json`. It warns about a missing subject/recipient/sender, an unknown company or variant, a date that is not ISO, a title both in YAML and as `#`, overfull lines, characters missing from the font, text outside the margin and single words alone on the last line.
- **Style (`src/document/`):** `kwdocument.sty` (A4, left margin 20 mm and text column 145 mm, Light titles and headings, Regular body text 10/14.4 pt, Medium emphasis and labels, green bullets, facts box on a grey surface with a green edge, quote and contact block with a green edge, tables with hairlines, letterhead with the wordmark, return address and recipient field fitted to a window envelope, date/references at the top right, the subject line moved down below long recipient and reference blocks, header from page 2, footer with company, organisation number, both office addresses and page number, green L frame with a seismograph stroke on the first and last page), `filter.lua` (variants, automatic facts box from `**Label:** value` lines right after the title, `.facts`, `.columns`, `.contact`, automatic contact block, a label above the title from the part before a colon, no single word alone on the last title line, the last paragraph of a letter kept together with the closing and signature, company data for the four companies) and `template.tex`.
- **`check_document_pdf.py`** (PyMuPDF): A4, only NON Natural Grotesk and embedded, no raster images, text outside the page or near the edge, a footer with the right company name, organisation number and both addresses on every page, Markdown leftovers, straight apostrophes and `--`, page numbers from page 2, and nearly empty pages.

### Business card (`deliverable/visualprofile/business-card/`)

A two-sided business card following the business card page in the profile manual: a grey front with the black wordmark (40 mm) and a contact block (name in Medium 9 pt, the rest in Regular 8 pt), and a green back with the black symbol (28 mm). Each card is a Markdown file where only the YAML header is used: `name` (required), `title`, `phone`, `email` and `web`. Fields that are left out disappear without the rest moving. The folder contains `business-card-template.md`/`.pdf`/`.png`, `business-card-example.md`/`.pdf`/`.png` (Eirik Larsen) and `README.md` (new card, print specification, colour table, ordering).

```bash
uv run src/build_business_card.py deliverable/visualprofile/business-card/business-card-example.md   # → .pdf and .png next to it (~10 s)
uv run src/build_business_card.py <card.md> [-o <out.pdf>] [--png <out.png>] [--keep-build]
```

- **`build_business_card.py`** (PyMuPDF): fills the template `src/business_card/card.tex` with pandoc and typesets it with lualatex. The font is unpacked from the licensed zip, and `font_guard.py` is enforced; the functions for this are imported from `build_presentation.py`. The build runs twice:
  - **Print PDF (CMYK):** sheet 105 × 75 mm, trim 85 × 55 mm, 3 mm bleed with TrimBox/BleedBox set, and crop marks in registration colour outside the bleed. The profile colours are written as CMYK from `colors.json`, and the wordmark and symbol are rewritten from RGB black to 100 % K.
  - **Screen version (PNG):** the profile's RGB colours, front and back side by side, cropped to the trim. It is built separately because the neon green cannot be shown correctly via CMYK.
- **Checks in the build** (exit 1 on a warning): sheet size, trim box and bleed, all text at least 3 mm inside the cut edge and at least 5 mm below the wordmark, only NON Natural Grotesk and embedded, no raster images, no drawing or text in RGB or greyscale (also inside the logos), and characters missing from the font.
- **Business cards from the CVs (`build_cv_business_cards.py`):** reads name, title, phone and email from the CVs in Markdown (`src/cv_markdown.py`), with `kodeworks.no` as the web address, and builds each card with `build_business_card.py`. The cards end up as `business-card-<name>.pdf` and `.png` next to each CV, or in `--out`. Fields missing in the CV are left out. A card that fails the print check is reported, and the run ends with exit 1:

  ```bash
  uv run src/build_cv_business_cards.py --dry-run                 # shows the fields for every CV in cvs/
  uv run src/build_cv_business_cards.py                           # builds cards for everyone (about 6 s per card)
  uv run src/build_cv_business_cards.py cvs/<name>/<name>.md [--out <folder>]
  ```

### Overview sheet (`deliverable/visualprofile/overview.pdf`)

`src/build_visualprofile_overview.py` makes one landscape A4 sheet per deliverable: the profile manual, the CV, the business card, the presentation and the document template. The pages are inserted as vectors from the finished PDFs, with headings in the profile font from the licensed zip. Build the deliverables first:

```bash
uv run src/build_visualprofile_overview.py        # → deliverable/visualprofile/overview.pdf (5 pages, ~3 s)
```

---

## ITKO reporting (`deliverable/itko/`)

KodeWorks reports monthly to ITKO through the bot @itko-temp in the ITKO Slack (or ITKO's web form). The deadline is the 10th of each month, and the report covers the previous month.

- **File name:** `deliverable/itko/report_YYYY-MM.md`, where `YYYY-MM` is the month the report covers (not the month it is sent).
- **Content:** one code block that is pasted straight into Slack, with `Måned`, `Inn`, `Ut`, `Timeprisendring` (change in kroner, not the level), `Markedsfølelse` and `Forventning` (1–5), `Nysalg` (one line per sale: role, technology, sector, industry, or `ingen`) and `Ansatte` (the whole employee list, one line per employee). The field names are ITKO's and stay in Norwegian.
- **The employee list:** start from the previous month's report and change what has changed. The format is described in `deliverable/employee_list_itko.md`. No names of people or customers.
- **The ratings:** market sentiment and expectation are set by the same person every month.

---

## Fetching from Google Drive (`src/fetch_from_drive.py`)

The tool fetches single files or whole folders from Google Drive, for example originals that go into the inbox `background/new/`. It is used when needed. The employees' CVs are no longer fetched from here: they are maintained in Markdown in `cvs/`, and the developers update them with commits.

```bash
uv run python src/fetch_from_drive.py <link or ID> --dry-run          # show what would be fetched, and where
uv run python src/fetch_from_drive.py <link or ID> [...]              # -> data/drive/
uv run python src/fetch_from_drive.py <folder link> --recursive --out data/drive/neue
uv run python src/fetch_from_drive.py <link> --format md --out background/new
uv run python src/fetch_from_drive.py --list data/cv_sources.csv --out data/drive/cv
```

| Flag | Effect |
|---|---|
| (arguments) | Drive links or file and folder IDs: Docs, Sheets, Slides, `drive/folders/…`, `file/d/…` and `open?id=…` |
| `--list` | CSV file with the column `Link` (separator `;` or `,`). The links are fetched in addition to the arguments. |
| `--out` | Target folder, default `data/drive/` (outside git) |
| `--format` | Export format for Google documents: `docx` (default), `pdf`, `md`, `txt`, `odt`. Spreadsheets become `xlsx` and presentations `pptx`, or `pdf` with `--format pdf`. Uploaded files are downloaded unchanged. |
| `--recursive` | Also fetch the subfolders of a folder. They are mirrored as local subfolders. Without the flag they are reported as skipped. |
| `--force` | Fetch again even if the local file is up to date with Drive |
| `--dry-run` | Show the files and target paths without fetching (still reads from Drive) |
| `--credentials`, `--token` | OAuth files, default `secrets/credentials.json` and `secrets/token.json` |

- **Folders:** a folder ends up in a subfolder with the same name in the target folder, for example `data/drive/Master CV/`.
- **File names** are the names on Drive, with characters that are invalid in Windows file names replaced by `_`.
- **The file date equals «last modified» on Drive.** The script sets the file's modification time (mtime) to `modifiedTime` on Drive, so the file date shows when the file was last changed, not when it was fetched. A file is fetched again only when it is missing or the time differs from Drive (otherwise `SKIP … up to date`). Do not copy the files in a way that resets the time (use `cp -p`).
- **Sign-in:** an OAuth client of the type «Desktop app» in `secrets/credentials.json`. The first run without `secrets/token.json` opens the browser for approval (scope `drive.readonly`) and saves the token. An existing token with wider Drive access is used as it is. `secrets/` is ignored by git and must be added on each machine.
- **The link list for the employees' CV documents** is kept locally in `data/cv_sources.csv` (`Name;Link;Intern`), outside git.
- The procedure for Claude Code is in the skill `fetch-from-drive`.

---

## Document conversion

Incoming originals (`.docx`, `.pdf`, `.pptx`, `.xlsx`, images) are put in the inbox `background/new/`, converted to Markdown with a date prefix and moved to `background/`. The detailed procedure is in `CLAUDE.md`. These tools are used for it:

| From | To | Tool |
|---|---|---|
| PDF | text | `pdftotext -layout "background/new/foo.pdf" foo.txt` (Poppler) |
| DOCX / PPTX / ODT / RTF / HTML | Markdown | `pandoc "background/new/foo.docx" -o foo.md --wrap=none` (add `--extract-media=<folder>` for the images) |
| XLSX | data | `openpyxl` from Python (Pandoc reads `.xlsx`, but complex sheets come out messy) |
| PDF / DOCX / PPTX | Markdown with separate images | `src/extract_visualprofile.py` (below) |
| PDF slide deck | one PNG per page | `pdftoppm -png -r 150 file.pdf out_prefix` |

### PDF / DOCX / PPTX → Markdown with separate images (`src/extract_visualprofile.py`)

Converts one document to `.md` with the text extracted and the images in their own folder next to it:

```bash
uv run src/extract_visualprofile.py "background/new/Report.pdf"
# → background/new/<date>_report.md
# → background/new/<date>_report_media/
```

- **PDF:** text per page with `pdftotext` (`## Side N`), images per page with `pdfimages`. Each image is saved once (deduplicated on the PDF object ID) and referenced on every page that uses it. Soft masks are skipped.
- **Vector graphics (PDF):** PyMuPDF `get_drawings()` → one stand-alone SVG per figure (`vec_<hash>.svg`, deduplicated on content), without text and raster. Drawings that overlap or lie close together are grouped into one figure; backgrounds and large rectangular panels are kept out of the grouping. The thresholds are constants at the top of the script (`BACKGROUND_SHARE`, `PANEL_SHARE`, `GROUP_*`). Gradients and clipping paths are not included.
- **DOCX/PPTX:** `pandoc --extract-media`. Tables with merged cells are written as HTML, so images in them are referenced with `<img src>` instead of `![]()`. Pandoc leaves out headers and footers; for DOCX the script fetches text and images from them itself and puts them under `## Topp- og bunntekst` at the end of the `.md` (empty and identical headers/footers are skipped).
- **Line endings:** every `.md` and SVG file is written with LF, whatever the platform.
- **Text in images:** if there is a sibling file `<stem>_image_text.md`, its content is merged in as a quote block «Tekst i bildet» after the first reference to each image. The file has one `## <image file name>` section per image, is written by hand (transcribed from the original image at full resolution), and is never overwritten by the script. Used for screenshots where the text becomes unreadable after downscaling.
- **Images** are downscaled to 25 % of width/height (`--scale 0.25`, kept unchanged if the longest side would then be under `--min-side 200`) and saved as JPEG q85 (PDF) or in the original format (DOCX/PPTX). The purpose is colour extraction and comparison, not reuse at full resolution.
- **The date prefix** comes from the metadata (PDF `CreationDate`, OOXML `dcterms:created`); six-digit date prefixes in the original name (`030521_`) are removed. Without metadata, today's date is used and the uncertainty is noted in the file.
- Running again overwrites the `.md` and the media folder. For example, a PDF of 79 pages and 348 MB took about 55 s.
- The result ends up next to the original. For a file in the inbox, the `.md` and the media folder are then moved to `background/`.
- Dependencies (`Pillow`, `pymupdf`) are declared inline (PEP 723); Poppler (`pdftotext`, `pdfimages`, `pdfinfo`) and `pandoc` must be on `PATH`.

### Control: Markdown → PDF and comparison with the original (`src/build_md_pdf.py`, `src/compare_md_pdf.py`)

```bash
uv run src/build_md_pdf.py "background/<date>_report.md"
# → background/<date>_report.pdf (next to the .md)
uv run python src/compare_md_pdf.py "background/new/Report.pdf" "background/<date>_report.pdf"
# → e.g. text 605/607 words (99.7 %), raster images original=13 generated=13
```

- **`build_md_pdf.py`** builds a PDF with lualatex without changing the `.md` or the media folder. It uses TeX Gyre Heros from TeX Live, with the same character widths as Arial (the profile's fallback font), DejaVu Sans Mono for code, Norwegian hyphenation and the font check. SVGs are converted to PDF with PyMuPDF in a working folder under `tmp/`, so `rsvg-convert` is not needed. The build goes Markdown → HTML → PDF, so HTML tables from DOCX sources are included; headings inside table cells are turned into bold text (LaTeX otherwise does not print a `\paragraph` without following text), and bare URLs become links (otherwise LaTeX breaks them at hyphens).
- **`compare_md_pdf.py`** extracts the original's text independently of pandoc (`pdftotext` for PDF, `<w:t>`/`<a:t>` directly from the XML for DOCX/PPTX, including headers/footers) and reports the share of the original's words found in the generated PDF, the missing words, and the number of raster images in the original against the generated PDF. Hyphens are removed on both sides before the comparison, so LaTeX hyphenation does not give false differences.

---

## Reports: Markdown → DOCX and PDF

Reports in `deliverable/` are written in Markdown and converted with Pandoc when they are ordered.

```bash
pandoc deliverable/report.md -o deliverable/report.docx
```

PDF needs TeX Live with `lualatex`. The fonts are loaded as files from TeX Live, not from the operating system, so the result is the same on Windows, WSL2 and Linux:

```bash
pandoc deliverable/report.md -o deliverable/report.pdf \
  --pdf-engine=lualatex \
  -V documentclass=scrartcl \
  -V geometry:margin=1in \
  -V lang=nb \
  -V mainfont=texgyretermes-regular.otf \
  -V mainfontoptions="BoldFont=texgyretermes-bold.otf, ItalicFont=texgyretermes-italic.otf, BoldItalicFont=texgyretermes-bolditalic.otf" \
  -V monofont=DejaVuSansMono.ttf \
  --number-sections=false
```

| Flag | Effect |
|---|---|
| `--pdf-engine=lualatex` | Unicode characters (`≥`, `–`, `€`), OpenType fonts, and Norwegian hyphenation patterns loaded at run time. The xelatex format has no bokmål patterns and silently hyphenates with English ones. |
| `-V documentclass=scrartcl` | The KOMA-Script article class, with cleaner typography than the default `article`. |
| `-V geometry:margin=1in` | 1 inch margin. |
| `-V lang=nb` | Norwegian bokmål: hyphenation and typographic conventions. |
| `-V mainfont=texgyretermes-…` | Body text in TeX Gyre Termes (a Times clone from TeX Live), with bold and italic as files. |
| `-V monofont=DejaVuSansMono.ttf` | Monospace font for code blocks from TeX Live. The default (`Latin Modern Mono`) lacks box-drawing characters (├, ─, └, │). |
| `--number-sections=false` | No automatic heading numbers; the reports already number their headings. |

### Mermaid diagrams in reports

If a report has `` ```mermaid `` blocks, use **`mermaid-filter`** (a Node-based Pandoc filter that renders each diagram to PNG during conversion).

**Installation (once per machine).** Node is installed with `nvm`, not the system package manager.

**Windows (Chocolatey, PowerShell as administrator):**

```powershell
choco install nvm
# Open a new PowerShell/CMD so nvm is on PATH:
nvm install lts
nvm use lts
npm install -g mermaid-filter
```

**Linux:** install nvm with the command from <https://github.com/nvm-sh/nvm>. Then:

```bash
# After installing nvm, start a new shell or: source ~/.bashrc
nvm install --lts
nvm use --lts
npm install -g mermaid-filter    # no sudo: nvm is per user
```

**Download Chromium manually (needed on Node 24+):** `mermaid-filter` uses puppeteer 19, and the install hook that should download Chromium silently does nothing on modern Node (24+). Without Chromium the filter fails with `spawn ... chrome.exe ENOENT`. Run the download manually:

```bash
# Windows (Git Bash) — adjust the Node version in the path:
cd /c/ProgramData/nvm/v<version>/node_modules/mermaid-filter/node_modules/puppeteer
node install.js

# Linux (nvm):
cd ~/.nvm/versions/node/v<version>/lib/node_modules/mermaid-filter/node_modules/puppeteer
node install.js
```

**Fallback: point to an installed Chrome/Edge:**

```bash
# Windows – Chrome:
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files/Google/Chrome/Application/chrome.exe"
# Windows – Edge:
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# Linux:
export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome
```

**Use:**

```bash
# From Git Bash on Windows — the .cmd suffix is required (Pandoc looks up the exact file name)
pandoc deliverable/report.md -o deliverable/report.docx -F mermaid-filter.cmd

# From PowerShell/CMD, or Linux/macOS — without .cmd
pandoc deliverable/report.md -o deliverable/report.docx -F mermaid-filter
```
