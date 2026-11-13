# TASKS

Åpne og in-progress oppgaver for prosjektet. Se `ARCHIVE.md` for løste oppgaver.

Format: `### T<n> [<status>] <tittel>` — status er `[ ]` (åpen), `[~]` (in-progress) eller `[x]` (løst). Ved løsning: skriv løsningen under tasken før den flagges `[x]` og eventuelt arkiveres.

## Nye oppgaver

Uprosesserte bullet-punkter listes her — spør brukeren om de skal konverteres til T-tasks.

## Tasks

### T21 [x] English documentation with a quick start for new developers

A developer who checks out the project on Windows or Linux should understand within a few minutes what the project can be used for, what to install and how to check that the setup works. Today the README is a reference manual: the use cases are spread over 600 lines, the getting-started section is last, vague and partly wrong, and the docs are in Norwegian. The user has decided (2026-11-13) that the documentation is written in English. Deliverables (CVs, letters, presentations, background notes) keep Norwegian content.

Findings (2026-11-13):

- The opening describes the repo as a knowledge base and sends readers to the AI instruction file. The main use cases (own CV with PDF and business card, presentations/letters/documents in the visual profile, the monthly ITKO report, fetching from Google Drive) are not listed up front. The CV workflow starts around line 500.
- The getting-started section calls TeX Live optional, although every build needs it. It does not mention Pandoc, `uv sync` or the venv setting for WSL2, and its third step is about the document inbox, which is not a developer task.
- Prerequisites are spread over four sections with three Windows installers. Nothing says which tool is needed for what: uv + TeX Live (lualatex) + Pandoc for all builds; Poppler for document conversion; Node + mermaid-filter for diagrams; OAuth files in `secrets/` for Google Drive.
- The CV guide says a CV build needs only uv and TeX Live. `build_employee_cvs.py` also builds the business card, which runs Pandoc (`src/build_business_card.py`), so a developer without Pandoc gets a failure.
- There is no step that verifies the setup.
- The README contains rules meant for the AI assistant (never read PDFs with the Read tool, inbox procedure, batch transformations, test-timeout rules).

**Changes:**

1. **README in English**, opening with a quick start: what the project is for (one line and one command per use case), a table of tools per use, setup for Windows and for Linux/WSL2 (about five lines each, including `uv sync` and `UV_PROJECT_ENVIRONMENT=.venv-linux`), and a verification step (`uv run pytest --timeout=3` and building one CV). The reference sections follow, translated.
2. **The template guides** in `deliverable/visualprofile/{cv,presentation,document,business-card}/README.md` and `.claude/skills/README.md` in English. The CV guide is named as the starting point for consultants, and its list of required tools includes Pandoc.
3. **Language rule:** the README convention says documentation is English and document content (PDFs and their sources) Norwegian. The docstring in `tests/test_english_names.py` says the same.
4. **AI-specific rules** move out of the README. They already exist in CLAUDE.md; anything missing there is moved only with the user's yes for CLAUDE.md.
5. **CLAUDE.md** (only with the user's own yes): the rule «Dokumentasjon og rapporter til brukere/interessenter skrives på norsk» is changed so documentation is English and deliverables Norwegian.

**Verification:**

1. A reader without context can, from the first screen of the README, name the use cases, the tools to install and the command that verifies the setup.
2. Every command in the quick start runs as written on Windows (Git Bash). The Linux package list is compared with what the WSL2 machine needed.
3. No Norwegian prose is left in the README, the template guides or the skills overview, apart from quoted Norwegian content (CV labels, slide titles, file names of the nine background documents).
4. `pytest --timeout=5` passes.

**Estimert innsats:** 34 min

**Solution (2026-11-13):**

- **README** rewritten in English. It opens with «Quick start»: what the project is for (a table with one command and one guide per use case), «What to install» (a table of tools per use with Windows and Linux commands; Pandoc is listed as needed for every PDF build), «Set up» (`uv sync`, and `UV_PROJECT_ENVIRONMENT=.venv-linux` for WSL2), «Check that it works» (tests and one CV build, with the expected output) and the other files at the root. The reference sections follow, translated. On Windows, Pandoc is installed with winget like uv, so only the optional Poppler and nvm use Chocolatey.
- **Removed from the README:** the rule against reading PDFs with the Read tool, the step-by-step inbox procedure, the section on batch transformations, the pointers to sibling projects, and the helper scripts `src/format_docx.py` and `src/nbsp_numbers.py`, which do not exist. The inbox now has a short section «Document conversion» with a table of tools and a pointer to CLAUDE.md. CLAUDE.md already had the removed rules; the pointer to the image extraction pattern in a sibling project was moved there.
- **Stale facts corrected:** the warnings from the document build, the presentation theme («Too much text on slide …») and the business card build (`WARNING:`) are in English, not Norwegian as the guides said.
- **The template guides** (CV, presentation, document, business card) and the skills overview are in English. The CV guide says «Start here if you are a consultant», has its own «What you need» section that includes Pandoc, and a step to commit the Markdown file and the photo. The business card guide says that employees with a CV get their card from the CV build. The Markdown examples keep their Norwegian CV labels and sample text, because they are document content.
- **Language rule:** the README convention and the docstring of `tests/test_english_names.py` say documentation is English and documents Norwegian. In CLAUDE.md (with the user's yes) the rule under «Kode og parametere på engelsk» and the first line of «Tone og format» say the same, and the references to README sections use the new names («Python setup», «Visual profile»).
- **Not changed:** CLAUDE.md is otherwise still Norwegian, and so are `cvs/DEVIATIONS.md` and the skill `fetch-from-drive/SKILL.md`. `src/build_presentation.py` names the notes version `<deck>-notater.pdf`, a Norwegian file name; the docs describe it as it is.

**Verification:**

1. The first screen of the README names the use cases, the tools and the verification commands.
2. The quick start commands were run as written in Git Bash on Windows: `uv sync`, `uv run pytest --timeout=3` (386 passed) and `uv run python src/build_employee_cvs.py paal-noedseth` (ends with `CV check: 1 files, 0 with deviations`). The winget IDs `astral-sh.uv` and `JohnMacFarlane.Pandoc` exist. All file links and heading links in the README resolve. **Not verified:** the Linux package list. A lookup of which TeX Live collection each LaTeX package belongs to was too slow with `tlmgr` (it went past the two-minute limit and was stopped). Packages such as `tcolorbox`, `needspace` and `lastpage` may be in Ubuntu's `texlive-latex-extra`, which the list does not name. It should be confirmed on the WSL2 machine (`dpkg -l texlive-latex-extra`).
3. A search for common Norwegian words in the prose of the README, the guides and the skills overview (outside code and «…») finds none.
4. `pytest --timeout=5`: 386 passed.

**Faktisk innsats:** 7m 29s (veggklokke)

**Berørte filer:** `README.md`, `deliverable/visualprofile/cv/README.md`, `deliverable/visualprofile/presentation/README.md`, `deliverable/visualprofile/document/README.md`, `deliverable/visualprofile/business-card/README.md`, `.claude/skills/README.md`, `tests/test_english_names.py` (docstring), `TASKS.md`, and `CLAUDE.md` (only with the user's own yes)

### T22 [x] Purge TASKS.md and ARCHIVE.md, and remove references to task IDs

The task history in `TASKS.md` and `ARCHIVE.md` is to be purged, and no document may point to a task ID.

Finding (2026-11-13): a search for task IDs (`T<n>`, `T<n>.<m>`) in Markdown, Python, LaTeX, Lua, `pyproject.toml` and `.gitignore` outside the two task files only finds the made-up examples with real-looking numbers in the rule about task IDs in CLAUDE.md.

**Changes:**

1. Purge `TASKS.md` and `ARCHIVE.md` to the extent the user decides (open question: delete all tasks including solution notes, or keep the files with only the format header and open tasks).
2. Search all files in the repo (except `.venv*`, `tmp/`, `data/`) for task IDs and remove or rephrase any that point to a task.
3. CLAUDE.md treats the solution notes as the chronological backbone of the project, and refers to `TASKS.md`/`ARCHIVE.md` in several rules. Any change there needs the user's own yes.

**Verification:**

1. The search for task IDs finds nothing outside the task files (and outside the examples in CLAUDE.md, if they are kept).
2. `pytest --timeout=5` passes.

**Estimert innsats:** 8 min

**Solution (2026-11-13):** The user chose to keep the files with only the format header and the open tasks.

- **`TASKS.md`** keeps its header, «Nye oppgaver» and the two tasks from the same session (the English documentation and this one), because a solved task must have its solution note written. All earlier tasks with their solution notes are deleted.
- **`ARCHIVE.md`** keeps only its header and an empty «Tasks» section.
- **Task IDs:** a search of every text file in the repo (except `.venv*`, `tmp/`, `data/`, `secrets/` and the caches) found only the made-up examples in CLAUDE.md. They are replaced by placeholders (`T<n>`, `T<n>.<m>`), and this task's own description no longer quotes them.
- **CLAUDE.md** (with the user's yes): the rule «Ingen historikk-fil brukes» says the tasks and solution notes from before 2026-11-13 were deleted from both files and exist only in the git history, and that what still applies is in the README, CLAUDE.md and the code. The numbering rule says a number is never reused, also when older tasks have been deleted.

**Verification:**

1. The search for task IDs outside the two task files finds nothing (a binary PDF matches by chance and is not a reference). Inside `TASKS.md` the only IDs are the two task headings.
2. `pytest --timeout=5`: 386 passed.

**Faktisk innsats:** 0m 44s (veggklokke, from the purge to the solution note; the search when the task was filed came before)

**Berørte filer:** `TASKS.md`, `ARCHIVE.md`, files with task IDs found by the search, and `CLAUDE.md` (only with the user's own yes)
