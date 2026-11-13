# KodeWorks – kunnskapsgrunnlag og leveranser

Prosjektrepo for kunnskapsgrunnlag og leveranser om **KodeWorks**-selskapene (KodeWorks AS, KodeWorks Trondheim AS, KodeWorks Eiendom AS, KodeWorks Oslo AS). Se `CLAUDE.md` for prosjektkontekst, konsern-fakta og arbeidsregler.

Prosjektet er primært **Python**-basert (`uv run python`). Scripts ligger i `src/`.

## Mappestruktur

```
<prosjektrot>/
├── CLAUDE.md        – prosjektkontekst og arbeidsregler for AI-assistent
├── README.md        – dette dokumentet
├── background/      – kildedokumenter, analyser og notater (datoprefiks YYYY-MM-DD_)
│   ├── new/         – innboks for nye originaler; tømmes når de er konvertert
│   └── visualprofile/Fonts/ – profilfonten Non Natural Grotesk (lisensiert, med lisensene); brukes av alle byggene
├── cvs/             – de ansattes CV-er i Markdown, én mappe per person (<navn>.md, images/foto.jpg); oppdateres med commits.
│                      logos/: felles logobibliotek, én fil per kunde.
│                      CV-PDF og visittkort bygges ved siden av og er utenfor git. AVVIK.md: hva konsulentene bør rette
├── deliverable/     – ferdige dokumenter (rapporter, notater, presentasjoner)
│   ├── itko/        – månedlige ITKO Temp-rapporter (rapport_YYYY-MM.md)
│   └── visualprofile/ – revidert visuell profil (profile/) og maler bygget på den (cv/, presentation/, document/, business-card/)
├── src/             – Python-scripts og kjørbare hjelpeverktøy
│   ├── profile_manual/ – layoutsystem (LaTeX-mal, sidetyper, komponenter, palett, kerningrettinger) for profilmanualen
│   ├── cv_pdf/         – LaTeX-stil for CV-malen versjon 3 (src/build_cv_pdf.py)
│   ├── presentation/   – beamer-tema og Lua-filter for presentasjonsmalen (src/build_presentation.py)
│   ├── document/       – LaTeX-stil, pandoc-mal og Lua-filter for dokumentmalen (A4, brev; src/build_document.py)
│   ├── business_card/  – LaTeX-mal for visittkortet (src/build_business_card.py)
│   ├── build_all.py    – bygger alle PDF-er og PNG-er fra kildene (se «Bygge alt»)
│   └── project_tmp.py  – arbeidsmapper for scriptene i tmp/ (se «Konvensjoner»)
├── tests/           – pytest-tester for scriptene i src/ (fixtures/documents/: testkorpus for dokumentmalen)
├── data/            – lokale arbeidsdata, git-ignorert (drive/: hentet fra Google Drive; cv_sources.csv: lenker til CV-dokumentene)
├── secrets/         – Google OAuth-klient og token (git-ignorert, legges inn per maskin)
├── tmp/             – midlertidige filer og arbeidsmapper for scriptene (git-ignorert, kan slettes når ingenting kjører)
├── .claude/skills/  – prosjekt-skills for Claude Code (oversikt i .claude/skills/README.md)
└── pyproject.toml   – prosjektmiljø (uv), med uv.lock og .python-version
```

## Konvensjoner

- **Språk:** Dokumenter og rapporter skrives på norsk (bokmål). Kode, variabelnavn og CLI-flagg skrives på engelsk.
- **Filnavn i `background/`:** Bruk dato-prefix `YYYY-MM-DD_beskrivelse.ext` (f.eks. `2026-09-22_konsernstruktur.md`). Dato er dokumentets egen dato, ikke arkiveringsdato.
- **Nye filer:** Legg innkommende, uklassifiserte filer i `background/new/`. Konverter til Markdown, dato-prefix, og flytt ut til `background/` når de er lest og klassifisert.
- **Scripts:** Alle scripts ligger i `src/` og kjøres fra prosjektroten (`uv run python src/navn.py`).
- **Midlertidige filer:** Scripts og kommandoer vi styrer selv, skriver ikke utenfor prosjektet. Arbeidsmapper og mellomfiler legges i `tmp/` i prosjektroten (git-ignorert) med `src/project_tmp.py`: `work_dir(prefix)` lager en mappe som slettes når blokken avsluttes, også ved feil, og `mkdtemp(prefix)` lager en mappe som scriptet selv sletter (beholdes med `--keep-build`). Testen `tests/test_project_tmp.py` feiler hvis et script i `src/` bruker systemets midlertidige mappe. Installerte programmer (uv, LuaLaTeX, pytest, pandoc) beholder sine egne hurtigbuffere og midlertidige mapper.
- **Docx/PDF-generering:** Markdown er kilden. Konvertering til `.docx`/`.pdf` skjer med Pandoc, kun når det bestilles eksplisitt.

---

## Python-oppsett

**`uv`** brukes til å styre Python-versjoner og virtuelle miljøer.

**Windows (PowerShell):**

```powershell
winget install --id=astral-sh.uv
```

**Linux / WSL2 (Ubuntu):**

```bash
sudo apt install pipx
pipx install uv
pipx ensurepath              # legger ~/.local/bin på PATH
```

Restart shellet etter `pipx ensurepath` første gang.

**Oppgradering:**

```bash
uv self update
```

### To måter å deklarere avhengigheter på

1. **Prosjektmiljø (`pyproject.toml` + `uv.lock`).** Felles avhengigheter (Google API for `src/fetch_from_drive.py`) og utviklingsverktøy (`pytest`, `pytest-timeout`) ligger i `pyproject.toml`; `uv.lock` låser versjonene og sjekkes inn. Python-versjonen står i `.python-version` (3.11). Prosjektet er ikke en installerbar pakke (`package = false`).
2. **Inline per script (PEP 723).** Scripts med egne, tunge avhengigheter (visuell profil, CV-generering) deklarerer dem øverst i fila og kjøres i et eget, midlertidig miljø — uavhengig av prosjektmiljøet:

   ```python
   # /// script
   # dependencies = ["openpyxl", "python-docx", "pypdf", "Pillow"]
   # ///
   ```

| Script-type | Kjør med |
|---|---|
| Uten inline-blokk (bruker prosjektmiljøet) | `uv run python src/navn.py` |
| Med PEP 723-blokk | `uv run src/navn.py` (`uv run python …` ignorerer inline-blokken) |

### Venv per operativsystem

En venv er ikke portabel mellom Windows og Linux. Når samme checkout brukes fra både Windows og WSL2 (`/mnt/c/dev/...`), må hvert OS ha sin egen venv-mappe:

| Miljø | Venv-mappe | Oppsett |
|---|---|---|
| Windows (Git Bash, PowerShell) | `.venv` (uv-standard) | ingenting ekstra |
| WSL2 / native Linux | `.venv-linux` | `export UV_PROJECT_ENVIRONMENT=.venv-linux` i `~/.bashrc` |

Begge er git-ignorert. Verdien er relativ til prosjektroten, så den samme linjen i `~/.bashrc` fungerer for alle prosjekter som følger konvensjonen. Native Linux uten delt Windows-checkout kan like gjerne bruke `.venv`.

**Førstegangsoppsett per maskin** (fra prosjektroten, vilkårlig skall):

```bash
uv sync                 # oppretter venv og installerer avhengigheter fra uv.lock
```

**Aktivering per terminalvindu:** ikke nødvendig — `uv run …` finner og synkroniserer riktig venv selv. Vil du likevel aktivere (f.eks. for IDE eller REPL):

```bash
source .venv/Scripts/activate      # Git Bash (Windows)
.\.venv\Scripts\Activate.ps1       # PowerShell (Windows)
source .venv-linux/bin/activate    # WSL2 / Linux
```

**Ny avhengighet:** `uv add <pakke>` (eller `uv add --dev <pakke>` for utviklingsverktøy). Oppdaterer `pyproject.toml` og `uv.lock`.

### Tester

Tester ligger i `tests/` og kjøres fra prosjektroten:

```bash
uv run pytest --timeout=3
```

Aldri `pytest` uten `--timeout` (standard 3 sek er også satt i `pyproject.toml`). `tests/` importerer moduler direkte fra `src/` (`pythonpath = ["src"]`). Se CLAUDE.md for regler om test-timeout, skippede tester og bakgrunnsprosesser.

`tests/test_english_names.py` håndhever språkregelen: hjelpetekster til flagg, meldinger fra skriptene og mappenavn skal være på engelsk, mens PDF-er, kildene deres og dokumentasjon er på norsk. Tekst i «…» i en melding regnes som innhold.

---

## Dokumentkonvertering

### PDF → tekst

Bruk `pdftotext` (fra Poppler) — aldri Read-verktøyet side for side på PDF.

**Windows (Chocolatey):**

```powershell
choco install poppler
```

**Linux:**

```bash
sudo apt install poppler-utils
```

**Bruk:**

```bash
pdftotext -layout "background/foo.pdf" background/foo.txt
```

`-layout` bevarer kolonner og tabeller. Drop det hvis det gir artefakter.

### DOCX / PPTX / ODT / RTF / HTML → Markdown

Bruk Pandoc.

**Windows (Chocolatey, PowerShell som administrator):**

```powershell
choco install pandoc
```

**Linux:**

```bash
sudo apt install pandoc
```

**Bruk:**

```bash
pandoc "background/new/foo.docx" -o background/new/foo.md --wrap=none
```

Med bilder ekstrahert til en dedikert mappe:

```bash
pandoc "background/new/foo.docx" -o background/new/foo.md \
  --wrap=none --extract-media="background/new/foo_media"
```

### XLSX → data

Bruk `openpyxl` fra Python. Pandoc støtter `.xlsx` som input, men resultatet er ofte rotete for komplekse ark — foretrekk `openpyxl` + manuell strukturering.

```python
# /// script
# dependencies = ["openpyxl"]
# ///
from openpyxl import load_workbook

wb = load_workbook("background/foo.xlsx", data_only=False)  # False = les formler, True = les cached verdier
for sheet in wb.sheetnames:
    ws = wb[sheet]
    for row in ws.iter_rows(values_only=True):
        print(row)
```

### PDF med innebygde bilder → tekst + bilder

Hvis en PDF har figurer som `pdftotext` mister:

```python
# /// script
# dependencies = ["pypdf", "Pillow"]
# ///
```

Se mønsteret i `../sure-d61/scripts/extract_pdf_images.py` — pakker ut hver embedded raster-image til `<output-dir>/<pdf-stem>/img-<page>-<idx>.<ext>`, bevarer originalformat (PNG/JPEG/JP2). JP2 må konverteres videre til PNG med `convert file.jp2 file.png` (ImageMagick) for at Markdown-viewere skal rendre dem.

Alternativ for slide-decks: `pdftoppm -png -r 150 file.pdf out_prefix` rendrer hver side som en PNG.

### PDF / DOCX / PPTX → Markdown med separate bilder (`src/extract_visualprofile.py`)

Konverterer ett dokument til `.md` der teksten er ekstrahert og bildene ligger i en egen mappe ved siden av:

```bash
uv run src/extract_visualprofile.py "background/new/Rapport.pdf"
# → background/new/<dato>_rapport.md
# → background/new/<dato>_rapport_media/
```

- **PDF:** tekst per side med `pdftotext` (`## Side N`), bilder per side med `pdfimages`. Hvert bilde lagres én gang (dedup på PDF-objekt-ID) og refereres på alle sider det brukes. Soft masks hoppes over.
- **Vektorgrafikk (PDF):** PyMuPDF `get_drawings()` → én frittstående SVG per figur (`vec_<hash>.svg`, dedup på innhold), uten tekst og raster. Tegninger som overlapper eller ligger tett grupperes til én figur; bakgrunner og store rektangel-paneler holdes utenfor grupperingen. Terskler ligger som konstanter øverst i scriptet (`BACKGROUND_SHARE`, `PANEL_SHARE`, `GROUP_*`). Gradienter og klippebaner kommer ikke med.
- **DOCX/PPTX:** `pandoc --extract-media`. Tabeller med sammenslåtte celler skrives som HTML, så bilder i dem refereres med `<img src>` i stedet for `![]()`. Pandoc tar ikke med topp- og bunntekst; for DOCX henter scriptet tekst og bilder derfra selv og legger dem under `## Topp- og bunntekst` sist i `.md`-en (tomme og like topp-/bunntekster hoppes over).
- **Linjeskift:** alle `.md`- og SVG-filer skrives med LF, uavhengig av plattform.
- **Tekst i bilder:** finnes en søskenfil `<stem>_image_text.md`, flettes innholdet inn som sitatblokk «Tekst i bildet» etter første referanse til hvert bilde. Fila har én `## <bildefilnavn>`-seksjon per bilde, skrives for hånd (avskrift fra originalbildet i full oppløsning), og overskrives aldri av scriptet. Brukes for skjermbilder der teksten blir uleselig etter nedskalering.
- **Bilder** nedskaleres til 25 % av bredde/høyde (`--scale 0.25`, beholdes uendret om lengste side da blir under `--min-side 200`) og lagres som JPEG q85 (PDF) eller i originalformat (DOCX/PPTX). Formålet er fargeuttrekk og sammenligning, ikke gjenbruk i full oppløsning.
- **Dato-prefix** hentes fra metadata (PDF `CreationDate`, OOXML `dcterms:created`); seks-sifrede datoprefikser i originalnavnet (`030521_`) fjernes. Mangler metadata, brukes dagens dato og usikkerheten noteres i filen.
- Kjøring på nytt overskriver `.md` og mediemappen. En PDF på 79 sider og 348 MB tok ~55 sek.
- Resultatet havner ved siden av originalen. For en fil i innboksen flyttes `.md` og mediemappen deretter til `background/` etter innboksprosedyren.
- Avhengigheter (`Pillow`, `pymupdf`) er deklarert inline (PEP 723); poppler (`pdftotext`, `pdfimages`, `pdfinfo`) og `pandoc` må finnes på PATH.

### Kontroll: Markdown → PDF og sammenligning med original (`src/build_md_pdf.py`, `src/compare_md_pdf.py`)

```bash
uv run src/build_md_pdf.py "background/<dato>_rapport.md"
# → background/<dato>_rapport.pdf (ved siden av .md-en)
uv run python src/compare_md_pdf.py "background/new/Rapport.pdf" "background/<dato>_rapport.pdf"
# → f.eks. text 605/607 words (99.7 %), raster images original=13 generated=13
```

- **`build_md_pdf.py`** bygger PDF med lualatex uten å endre `.md` eller mediemappe. Den bruker TeX Gyre Heros fra TeX Live, med samme tegnbredder som Arial (profilens reserveskrift), DejaVu Sans Mono til kode, norsk orddeling og fontkontrollen. SVG-er konverteres til PDF med PyMuPDF i en arbeidsmappe under `tmp/`, så `rsvg-convert` ikke trengs. Bygget går Markdown → HTML → PDF, slik at HTML-tabeller fra DOCX-kilder blir med; overskrifter inne i tabellceller gjøres om til fet tekst (LaTeX skriver ellers ikke ut `\paragraph` uten etterfølgende tekst), og nakne URL-er blir lenker (ellers deler LaTeX dem ved bindestrek).
- **`compare_md_pdf.py`** henter originalens tekst uavhengig av pandoc (`pdftotext` for PDF, `<w:t>`/`<a:t>` direkte fra XML for DOCX/PPTX, inkl. topp-/bunntekst) og rapporterer andel av originalens ord som finnes i den genererte PDF-en, manglende ord, og antall rasterbilder i original mot generert. Bindestreker fjernes på begge sider før sammenligning, så LaTeX-orddeling ikke gir falske avvik.

---

## Dokumentgenerering

### Markdown → DOCX

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.docx
```

**Tabell-rammer og kolonnebredder** er dårlig som default fra Pandoc. Et post-prosesseringsscript i `src/format_docx.py` (mønster fra `../sure-d61/scripts/format_docx.py`) legger til 0.5 pt grå rammer på alle celler og setter kolonnebredder per fil via en `TABLE_WIDTHS_BY_STEM`-dict:

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.docx
uv run src/format_docx.py deliverable/rapport.docx
```

### Markdown → PDF

Krever TeX Live med `lualatex`. Fontene lastes som filer fra TeX Live, ikke fra operativsystemet, så resultatet er det samme på Windows, WSL2 og Linux.

**Windows:** Installer TeX Live 2026 fra <https://tug.org/texlive/>.

**Linux:**

```bash
sudo apt install texlive-luatex texlive-lang-european texlive-fonts-recommended texlive-fonts-extra
```

**Bruk:**

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.pdf   --pdf-engine=lualatex   -V documentclass=scrartcl   -V geometry:margin=1in   -V lang=nb   -V mainfont=texgyretermes-regular.otf   -V mainfontoptions="BoldFont=texgyretermes-bold.otf, ItalicFont=texgyretermes-italic.otf, BoldItalicFont=texgyretermes-bolditalic.otf"   -V monofont=DejaVuSansMono.ttf   --number-sections=false
```

| Flagg | Effekt |
|---|---|
| `--pdf-engine=lualatex` | Unicode-tegn (`≥`, `–`, `€`), OpenType-fonter, og norske orddelingsmønstre lastet ved kjøring. xelatex-formatet har ingen bokmålsmønstre og deler stille med engelske. |
| `-V documentclass=scrartcl` | KOMA-Script article-klasse — renere typografi enn default `article`. |
| `-V geometry:margin=1in` | 1 tomme marg. |
| `-V lang=nb` | Norsk bokmål: orddeling og typografiske konvensjoner. |
| `-V mainfont=texgyretermes-…` | Brødtekst i TeX Gyre Termes (Times-klone fra TeX Live), med fet og kursiv som filer. |
| `-V monofont=DejaVuSansMono.ttf` | Mono-font for kodeblokker fra TeX Live. Default (`Latin Modern Mono`) mangler box-drawing-tegn (├, ─, └, │). |
| `--number-sections=false` | Ikke auto-nummerer overskrifter — rapporten bruker allerede eksplisitt nummerering. |

### Mermaid-diagrammer i rapporter

Hvis rapporten har `` ```mermaid ``-blokker: bruk **`mermaid-filter`** (Node-basert Pandoc-filter som rendrer hvert diagram til PNG ved konverteringstid).

**Installasjon (én gang per maskin):**

Node installeres via `nvm`, ikke systempakkemanager.

**Windows (Chocolatey, PowerShell som administrator):**

```powershell
choco install nvm
# Åpne nytt PowerShell/CMD for at nvm skal dukke opp på PATH:
nvm install lts
nvm use lts
npm install -g mermaid-filter
```

**Linux:**

Installer nvm ved å følge kommandoen fra <https://github.com/nvm-sh/nvm>. Deretter:

```bash
# Etter nvm-installasjon, start nytt shell eller: source ~/.bashrc
nvm install --lts
nvm use --lts
npm install -g mermaid-filter    # ikke sudo — nvm er brukerlokal
```

**Manuell Chromium-nedlasting (kritisk på Node 24+):** `mermaid-filter` bruker puppeteer 19, og install-hooken som skal laste ned Chromium hopper stille på moderne Node (24+). Uten Chromium feiler filteret med `spawn ... chrome.exe ENOENT`. Kjør nedlastingen manuelt:

```bash
# Windows (Git Bash) — juster Node-versjonen i stien:
cd /c/ProgramData/nvm/v<version>/node_modules/mermaid-filter/node_modules/puppeteer
node install.js

# Linux (nvm):
cd ~/.nvm/versions/node/v<version>/lib/node_modules/mermaid-filter/node_modules/puppeteer
node install.js
```

**Fallback — peke på allerede installert Chrome/Edge:**

```bash
# Windows – Chrome:
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files/Google/Chrome/Application/chrome.exe"
# Windows – Edge:
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# Linux:
export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome
```

**Bruk:**

```bash
# Fra Git Bash på Windows — .cmd-suffiks påkrevd (Pandoc gjør eksakt filnavn-oppslag)
pandoc deliverable/rapport.md -o deliverable/rapport.docx -F mermaid-filter.cmd

# Fra PowerShell/CMD, eller Linux/macOS — uten .cmd
pandoc deliverable/rapport.md -o deliverable/rapport.docx -F mermaid-filter
```

---

## Hente filer fra Google Drive (`src/fetch_from_drive.py`)

Verktøyet henter enkeltfiler eller hele mapper fra Google Drive, for eksempel originaler som skal inn i innboksen `background/new/`. Det brukes ved behov. De ansattes CV-er hentes ikke herfra lenger: de vedlikeholdes i Markdown i `cvs/`, og utviklerne oppdaterer dem med commits.

```bash
uv run python src/fetch_from_drive.py <lenke eller ID> --dry-run          # vis hva som hentes, og hvor
uv run python src/fetch_from_drive.py <lenke eller ID> [...]              # -> data/drive/
uv run python src/fetch_from_drive.py <mappelenke> --recursive --out data/drive/neue
uv run python src/fetch_from_drive.py <lenke> --format md --out background/new
uv run python src/fetch_from_drive.py --list data/cv_sources.csv --out data/drive/cv
```

| Flagg | Effekt |
|---|---|
| (argumenter) | Drive-lenker eller fil- og mappe-ID-er: Docs, Sheets, Slides, `drive/folders/…`, `file/d/…` og `open?id=…` |
| `--list` | CSV-fil med kolonnen `Link` (skilletegn `;` eller `,`). Lenkene hentes i tillegg til argumentene. |
| `--out` | Målmappe, standard `data/drive/` (utenfor git) |
| `--format` | Eksportformat for Google-dokumenter: `docx` (standard), `pdf`, `md`, `txt`, `odt`. Regneark blir `xlsx` og presentasjoner `pptx`, eller `pdf` med `--format pdf`. Opplastede filer lastes ned uendret. |
| `--recursive` | Hent også undermappene til en mappe. De speiles som undermapper lokalt. Uten flagget nevnes de hoppet over. |
| `--force` | Hent på nytt selv om den lokale fila er à jour med Drive |
| `--dry-run` | Vis filene og målstiene uten å hente (leser fortsatt fra Drive) |
| `--credentials`, `--token` | OAuth-filer, standard `secrets/credentials.json` og `secrets/token.json` |

- **Mapper:** en mappe havner i en undermappe med samme navn i målmappen, for eksempel `data/drive/Master CV/`.
- **Filnavn** er navnet på Drive, med tegn som er ugyldige i Windows-filnavn byttet til `_`.
- **Fildato er lik «sist endret» på Drive.** Scriptet setter filens endringstidspunkt (mtime) lik `modifiedTime` på Drive, så fildatoen viser når fila sist ble endret, og ikke når den ble hentet. En fil hentes bare på nytt når den mangler eller tidspunktet avviker fra Drive (ellers `SKIP … up to date`). Ikke kopier filene på en måte som nullstiller tidspunktet (bruk `cp -p`).
- **Innlogging:** OAuth-klient av typen «Desktop app» i `secrets/credentials.json`. Første kjøring uten `secrets/token.json` åpner nettleseren for godkjenning (scope `drive.readonly`) og lagrer tokenet. Et eksisterende token med bredere Drive-tilgang brukes som det er. `secrets/` er git-ignorert og må legges inn på hver maskin.
- **Lenkelisten over de ansattes CV-dokumenter** ligger lokalt i `data/cv_sources.csv` (`Name;Link;Intern`), utenfor git.
- Prosedyren for Claude Code står i skillen `fetch-from-drive`.

---

## Innboks-arbeidsflyt (`background/new/`)

Standard prosessering av nye filer:

1. **Konverter** til Markdown per pipelinen over (PDF → `pdftotext`, DOCX/PPTX → `pandoc`, XLSX → `openpyxl`, bilder beholdes som-er).
2. **Preamble** — legg til en kort blokk øverst i `.md`-en med kildefilnavn og dokumentdato (om kjent).
3. **Rename** til `YYYY-MM-DD_beskrivelse.md` (dato = dokumentets egen dato, ikke arkiveringsdato).
4. **Flytt** til `background/` (eller passende undermappe).
5. **Rydd opp** — fjern midlertidig `.txt` fra `pdftotext`. Behold original binær kun hvis den er autoritativ (signerte PDF-er, signerte kontrakter). Ellers erstatter `.md` originalen.

Ved sesjonsstart: sjekk om `background/new/` inneholder ubehandlete filer. Hvis ja: list dem og spør brukeren før prosessering.

---

## ITKO Temp-rapportering (`deliverable/itko/`)

KodeWorks rapporterer månedlig til ITKO via boten @itko-temp i ITKO-slacken (eller ITKO sitt nettskjema). Frist er den 10. hver måned, og rapporten gjelder forrige måned.

- **Filnavn:** `deliverable/itko/rapport_YYYY-MM.md`, der `YYYY-MM` er måneden rapporten gjelder (ikke innsendingsmåneden).
- **Innhold:** Én kodeblokk som limes rett inn i Slack, med `Måned`, `Inn`, `Ut`, `Timeprisendring` (endring i kroner, ikke nivå), `Markedsfølelse` og `Forventning` (1–5), `Nysalg` (én linje per salg: rolle, teknologi, sektor, bransje, eller `ingen`) og `Ansatte` (hele ansattlista, én linje per ansatt).
- **Ansattlista:** Ta utgangspunkt i forrige måneds rapport og endre det som har endret seg. Formatet er beskrevet i `deliverable/ansattliste_itko.md`. Ingen navn på personer eller kunder.
- **Vurderingene:** Markedsfølelse og forventning skal settes av samme person hver måned.

---

## Bygge alt (`src/build_all.py`)

PDF-er og PNG-er som lages fra Markdown-kilder, ligger ikke i git. De bygges ved siden av kildene sine, og `.gitignore` holder dem utenfor. Etter en ny checkout, eller når noe er endret, bygger én kommando alt som er utdatert:

```bash
uv run python src/build_all.py                      # alt som er utdatert, til slutt de ansattes CV-er
uv run python src/build_all.py --list               # alle mål, og om de er oppdatert
uv run python src/build_all.py --dry-run            # hva som ville blitt bygget, og hvorfor
uv run python src/build_all.py --only cv,document   # bare noen grupper
uv run python src/build_all.py --force              # bygg alt på nytt
uv run python src/build_all.py --no-check           # hopp over kontrollene etter hvert bygg
```

Et mål bygges bare når en utfil mangler, eller når en av innfilene er nyere enn utfilene. Innfilene er kilden, bildene, stil- og malfilene, byggeskriptet og fontarkivet. Et mål som bruker resultatet av et annet mål (for eksempel oversiktsarket, som viser alle de andre PDF-ene), bygges også på nytt når det andre målet bygges i samme kjøring. Kommandoen avslutter med kode 1 hvis et bygg eller en kontroll feiler.

Gruppene, i byggerekkefølge:

| Gruppe | Hva | Script |
|---|---|---|
| `assets` | Logoer og grafikk fra SVG til PDF og PNG (`profile/assets/pdf/`, `png/`) | `src/export_profile_assets.py` |
| `profile` | Profilmanualen (`profile/profilmanual.pdf`) | `src/build_profile_manual.py` |
| `cv` | CV-malen og CV-eksempelet | `src/build_cv_pdf.py`, kontroll med `src/check_cv_md.py` |
| `presentation` | Presentasjonsmalen og eksempelet | `src/build_presentation.py`, kontroll med `src/check_presentation_pdf.py` |
| `document` | Brevmal, dokumentmal og to eksempler | `src/build_document.py`, kontroll med `src/check_document_pdf.py` |
| `business-card` | Visittkortmalen og eksempelkortet (trykkontrollene ligger i bygget) | `src/build_business_card.py` |
| `overview` | Oversiktsarket over alle leveransene (`oversikt.pdf`) | `src/build_visualprofile_overview.py` |
| `employee-cvs` | CV-PDF og visittkort for hver ansatt i `cvs/` | `src/build_employee_cvs.py` |

De ansattes CV-er har en egen kommando med samme endringssjekk, som `build_all.py` kjører til slutt. Den kontrollerer alle CV-ene med `src/check_cv_md.py` etter byggene:

```bash
uv run python src/build_employee_cvs.py                    # alle CV-er som er utdatert
uv run python src/build_employee_cvs.py paal-noedseth      # én person (mappenavnet i cvs/)
uv run python src/build_employee_cvs.py --list | --dry-run | --force
```

Et fullt bygg fra en tom checkout tar flere minutter, mest for de ansattes CV-er (10–45 sekunder hver). Listen over mål og endringssjekken ligger i `src/build_targets.py`. Testen `tests/test_build_all.py` sjekker at hver Markdown-kilde i malmappene står i byggelista, og at alle utfilene er dekket av `.gitignore` mens kildene ikke er det. En ny mal eller et nytt eksempel må derfor legges inn i `src/build_all.py`.

## Visuell profil (`deliverable/visualprofile/`)

Revidert visuell profil for KodeWorks (2026), bygget på designmanualen fra 2021 (Neue) og designet på kodeworks.no (kartlagt i `background/2026-11-11_kodeworks_no_design.md`). Profilen står nå på egne ben: logoer og grafikk ligger som rensede SVG-er i `profile/assets/`, og originalene fra 2021 er ikke i repoet (de ligger på Google Drive). Fra den gamle leveransen er bare profilfonten igjen, i `background/visualprofile/Fonts/`. Malene (CV, visittkort, presentasjon, salgsbrev) bygger på profilen og legges i egne undermapper.

```
deliverable/visualprofile/profile/
├── profilmanual.md    – kilde: én Markdown-fil med sidetyper (::: {.cover} / {.divider} / {.page}) og rå LaTeX-komponenter
├── profilmanual.pdf   – 40 sider 16:9 (297 × 167 mm), Non Natural Grotesk innebygd
├── farger.md / .json  – palett med roller, HEX/RGB/CMYK/PMS (forslag merket) og beregnet kontrastmatrise
├── assets/            – rensede SVG-er (navnetrekk, symbol, femte element; presentation/ for slidebakgrunner)
│   ├── pdf/           – vektor-PDF av hver SVG (generert)
│   └── png/           – transparent PNG, 2000 px lengste side (generert)
└── images/            – KodeWorks' egne foto (fra kodeworks.no) brukt i manualen
```

**Bygg manualen:**

```bash
uv run src/build_profile_manual.py          # → deliverable/visualprofile/profile/profilmanual.pdf (~20 sek)
```

Skriptet bygger i en arbeidsmappe under `tmp/` og skriver bare PDF-en. Motoren er **lualatex**, fordi den laster de norske bokmålsmønstrene for orddeling ved kjøring. xelatex-formatet har dem ikke og deler stille med engelske mønstre. `src/profile_manual/kernfix.json` legger til kerningpar som fonten mangler: rundt j (sj, kj …) og r–f. Rettingene slås på i `fonts.tex` og deles med CV-malen. Det pakker ut Non Natural Grotesk fra den lisensierte font-zip-en i `background/visualprofile/Fonts/` og laster fontene med fontspec `Path=` (ingen installasjon; lisensen tillater innbygging i PDF, ikke i `.docx`/`.pptx`). SVG-er konverteres til PDF med PyMuPDF (`rsvg-convert` trengs ikke). Layoutsystemet ligger i `src/profile_manual/`: `colors.tex` er eneste sted paletten defineres, `layout.tex` har sidetyper og komponenter (`\kwtile`, `\kwswatch`, `\kwmark`, `\kwtable` …), `filter.lua` gjør `:::`-blokker om til makroer. Hver `.page` er én fysisk side uten automatisk sideskift — sjekk PDF-en etter endringer. Eksemplene på reserveskriften Arial vises med TeX Gyre Heros fra TeX Live, som har samme tegnbredder. Bygget kopierer den inn i byggemappen.

**Plattformuavhengighet (`src/font_guard.py`).** Alle dokumentbygg skal gi samme resultat på Windows, WSL2 og Linux, uansett hvilke fonter som er installert på maskinen. Fonter lastes derfor bare som filer: profilfonten fra font-zip-en i repoet, og alt annet fra TeX Live (TeX Gyre, DejaVu, Latin Modern). Profilmanualen, CV-malen og kontroll-PDF-ene av Markdown har en fontkontroll. LuaTeX skriver filnavnet til hver font den lastet, og bygget stopper med en feilmelding hvis en font ligger utenfor byggemappen eller TeX-trærne. `tests/test_platform_independence.py` sjekker i tillegg at ingen byggekilde viser til systemets fontmapper eller til fonter som bare finnes installert.

**Eksporter assets** (etter endring i en SVG):

```bash
uv run src/export_profile_assets.py         # → assets/pdf/*.pdf og assets/png/*.png
```

**Kontrastmatrise:**

```bash
uv run src/wcag_contrast.py deliverable/visualprofile/profile/colors.json
```

Skriver WCAG 2.x-forholdstall for alle fargepar (AA normal 4,5:1, AA stor tekst 3:1, AAA 7:1) som Markdown. Leser `colors` og eventuelt `technical` fra JSON-fila.

### CV-mal versjon 3 — gjeldende (`deliverable/visualprofile/cv/`)

CV-en skrives som **Markdown** og settes direkte til PDF med lualatex. Det er ingen Word-fil, ingen LibreOffice og ingen rastergrafikk utenom foto og kundelogoer. Mappen inneholder:
- `cv-mal.md` og `.pdf`: tom mal, med veiledning i HTML-kommentarer;
- `cv-eksempel.md` og `.pdf`: Pål Nødseths CV med 8 prosjekter, eget portrett og kundelogoer fra hans CV på Drive, i `images/`;
- `README.md`: veiledning for konsulenter, med formatet, foto og logo, skriveråd og sjekkliste.

```bash
uv run src/build_cv_pdf.py deliverable/visualprofile/cv/cv-mal.md deliverable/visualprofile/cv/cv-mal.pdf        # 5–40 sek
uv run src/build_cv_pdf.py deliverable/visualprofile/cv/cv-eksempel.md deliverable/visualprofile/cv/cv-eksempel.pdf
uv run src/build_cv_pdf.py <cv.md> <ut.pdf> --keep <mappe>      # beholder hele byggemappen (cv.tex, cv.log) for feilsøking
uv run python src/cv_markdown.py <cv.md>                         # viser datamodellen som JSON
uv run python src/check_cv_md.py <cv.md> [...]                   # kontrollerer konvensjonene, exit 1 ved avvik
```

- **`cv_markdown.py`** leser CV-en fra Markdown og gir byggescriptets datamodell. Den kan også gjøre motsatt vei.
  - `#` er navnet, avsnittet under er tittelen, og lista med «Etikett: verdi» er kontaktinformasjonen.
  - `## Om …`, `## Teknisk kompetanse` (med `###` per gruppe) og `## Erfaring` (med `###` per prosjekt: metadataliste, beskrivelse og en linje «Nøkkelord:»).
  - `## Arbeidserfaring`, `## Utdanning` og `## Sertifiseringer` har rader på formen `periode | navn | sted`. Alle andre `##` blir egne lister.
  - Engelske etiketter og overskrifter gir engelsk CV.
  - Formatet er beskrevet i modulens docstring og i `README.md`, og testet i `tests/test_cv_markdown.py`.
- **`check_cv_md.py`** kontrollerer at alle CV-er følger de samme konvensjonene:
  - seksjonsrekkefølge og faste titler på egne lister;
  - kontaktliste i fast rekkefølge og form;
  - prosjekter med nyeste først og felt i fast rekkefølge;
  - perioder som `MM.ÅÅÅÅ – nå`;
  - kompetansegrupper i setningsform uten duplikater;
  - kulepunkter som Markdown-lister;
  - bilder i `images/foto.*` og `images/logo-<kunde>.*`; for de ansattes CV-er i `cvs/` kommer logoene fra `../logos/<kunde>.*`, fotoet er en JPG uten metadata med inntil 1200 piksler i bredden på utsnittet, og PNG-logoer er høyst 700 × 260 piksler (bildehodene leses uten Pillow);
  - rundtur parse → render → parse.

  Testet i `tests/test_check_cv_md.py` og `tests/test_cv_images.py`.
- **De ansattes CV-er** ligger i Markdown i `cvs/<navn>/`, med én mappe per person: `<navn>.md` og `images/foto.jpg`. Kundelogoene ligger i det felles logobiblioteket `cvs/logos/<kunde>.<ext>`, én fil per kunde. Utviklerne oppdaterer sin egen CV med commits i git. CV-PDF og visittkort bygges ved siden av og er utenfor git. `cvs/AVVIK.md` lister det konsulentene bør rette. Filene ble konvertert én gang fra Word-originalene, og vedlikeholdes nå i Markdown i git.
- **`normalize_cv_images.py`** (Pillow, numpy) gir fotoene og logoene i `cvs/` samme format: foto som JPG med kvalitet 85 (lavere, ned til 70, hvis fila ellers ville vokst), sRGB, uten metadata, gjennomsiktighet lagt på hvitt, og skalert ned så utsnittet med rammens forhold (60:74) er 1200 piksler bredt. Logoer får trimmet kanter og skaleres ned til høyst 700 × 260 piksler, og PNG-er lagres med palett. Bilder skaleres aldri opp, og fotoet beskjæres ikke i fila. Standard er tørrkjøring som viser endringen per fil og flagger filer som krymper under 30 %. `--apply` endrer filene og retter henvisningen når et foto går fra `.png` til `.jpg`. Skriptet er idempotent. `--self-test` sjekker reglene på syntetiske bilder og brukes av testene.

  ```bash
  uv run src/normalize_cv_images.py            # tørrkjøring for alle foto og logoer i cvs/
  uv run src/normalize_cv_images.py --apply
  ```
- **`build_cv_pdf.py`** (PyMuPDF, PyYAML, fontTools, Pillow, numpy) bygger CV-en.
  - YAML med samme datamodell leses fortsatt, for tester.
  - All tekst escapes for LaTeX. Glyfer som fonten mangler, fjernes med advarsel.
  - Logoer trimmes, skaleres etter optisk areal og skjules når kunden er KodeWorks.
  - Foto beskjæres så det fyller rammen. `Fotofokus` overstyrer fokuspunktet.
  - Fonten pakkes ut fra den lisensierte zip-en, og fontkontrollen kjører i hvert bygg.
- **Autotilpasning:** bygget prøver tetthet 1 og 2, om «Erfaring» starter på forsiden og sideskift før «Generelt», og velger færrest sider.
  - Kravene er god forside (tospaltet først), ingen midtside under 40 % og siste side ned mot 30 %.
  - Brødteksten er alltid 9,5 pt.
  - Kompetanse deles aldri inne i en gruppe, og korte lister i «Generelt» deles aldri.
  - Prosjekter har minst to linjer på hver side av et skift.
- **Stil:** `src/cv_pdf/cv-style.tex` inneholder geometri, fonter med kerningrettinger (`src/profile_manual/kernfix.json`), palett, seismografbånd, prosjektblokker og orddelingsunntak.

Versjon 1 og 2 av CV-malen (Word-filer via python-docx) er erstattet av versjon 3. Både leveransene og generatorene er slettet.

- **`seismograph.py`** (PyMuPDF/Pillow): generell, deterministisk generator for seismografstriper i profilens strek (tykk:tynn 13:3) — varianter `band`, `band-up`, `closing`, `corner`, `vleft`, `vright` — som PNG og SVG: `uv run src/seismograph.py --width-mm 170 --height-mm 6 --variant band --colour B6FF9E --out band.png [--svg band.svg] [--thin-colour 000000] [--seed N]`. Laget for gjenbruk i visittkort og brevmal.

### Presentasjonsmal (`deliverable/visualprofile/presentation/`)

Presentasjoner skrives i pandoc-Markdown og settes direkte til PDF (16:9, 338,67 × 190,5 mm) med pandoc → beamer → lualatex. Det er ingen PowerPoint-fil og ingen LibreOffice. Mappen inneholder `presentasjonsmal.md` og `.pdf` (mal som forklarer alle lysbildetypene), `eksempel.md` og `.pdf` (14 lysbilder), `images/` og `README.md` (veiledning med Markdown-syntaksen for hver lysbildetype).

```bash
uv run src/build_presentation.py deliverable/visualprofile/presentation/eksempel.md     # → eksempel.pdf ved siden av (~6 sek)
uv run src/build_presentation.py <deck.md> --notes            # → <deck>-notater.pdf med talernotater
uv run src/build_presentation.py <deck.md> -o <ut.pdf> [--theme-dir DIR] [--keep-build]
uv run src/check_presentation_pdf.py <deck.pdf>              # PASS/WARN/FAIL, exit 1 ved FAIL
```

- **`build_presentation.py`** (PyMuPDF): pakker ut fonten fra den lisensierte zip-en og eksporterer profilens SVG-er til vektor-PDF i en arbeidsmappe under `tmp/`, kjører pandoc med temaets Lua-filter og lualatex to ganger, og sletter byggemappen (`--keep-build` beholder den, med fontfilene — slett den etterpå). Stier til bilder er relative til Markdown-fila; manglende bilder meldes med linjenummer. Overfull/Underfull-bokser og temaets eget varsel «For mye tekst på lysbildet …» skrives ut med lysbildetittel. `max_print_line` settes høyt så varslene ikke kuttes i loggen.
- **Tema (`src/presentation/`):** `beamerthemekodeworks.sty` (absolutt plassering i mm, flater, footer med vektor-navnetrekk, seismograf på åpning og seksjonsskille, måling av innhold: 20 pt → 18 pt → bredere → skalering med varsel), `filter.lua` (klassene `.lead`, `.image`, `.quote`, `.figures`, `.logos`, `.closing`, seksjonsskille fra `#` med `number`, fargeutheving av `*ord*` i titler, harde mellomrom i tall, «»), `template.tex`, og `kernfix.json` (profilmanualens kerningrettinger pluss par foran kolon; tabellen er også innebygd i `.sty`, så endringer må gjøres begge steder). Fontfamiliene settes med `Ligatures=TeX`; uten det blir `--` og `'` ikke til tankestrek og typografisk apostrof.
- **`check_presentation_pdf.py`** (PyMuPDF): sidestørrelse, bare NON Natural Grotesk og innebygd, ingen rasterbilder utenom foto (foto under 150 dpi effektivt gir WARN), tekst utenfor siden, i margen eller i footer-området, tekst under 12 pt, farger utenfor `colors.json`, og nesten tomme sider.

### Dokumentmal for A4, med brev som variant (`deliverable/visualprofile/document/`)

Én felles mal for A4-dokumenter: varianten `letter` (brev: salgsbrev, henvendelser) og varianten `document` (utlysning av konsulentoppdrag, notat, tilbud). Kilden er pandoc-Markdown med YAML-hode, og PDF-en settes med pandoc → LaTeX → lualatex. Det er ingen Word-fil og ingen LibreOffice. Nye behov legges inn som elementer i den felles malen, ikke som lokale løsninger i enkeltdokumenter. Mappen inneholder `dokumentmal.md`/`.pdf` og `brevmal.md`/`.pdf` (tomme maler med instruks), `eksempel-brev.md`/`.pdf` (salgsbrev, to sider), `eksempel-utlysning.md`/`.pdf` (utlysning av Android-oppdraget) og `README.md` (YAML-felt, syntaks for hvert element, sjekkliste).

```bash
uv run src/build_document.py deliverable/visualprofile/document/eksempel-brev.md   # → eksempel-brev.pdf ved siden av
uv run src/build_document.py <fil.md> -o <ut.pdf> [--style-dir DIR] [--keep-build]
uv run src/check_document_pdf.py <fil.pdf> [--company "KodeWorks Oslo AS"]      # OK/WARN/FAIL, exit 1 ved FAIL
uv run src/check_document_pdf.py --self-test                                      # bevisst dårlig PDF; alle kontroller skal slå ut
```

- **`build_document.py`** (PyMuPDF): importerer `extract_fonts`, `write_kernfix`, `build_assets`, `find_root` m.fl. fra `build_presentation.py`, pakker ut fonten fra den lisensierte zip-en i en midlertidig mappe, eksporterer profilens SVG-er til vektor-PDF, håndhever `font_guard.py`, kjører pandoc med stilens mal og Lua-filter og lualatex to ganger, og sletter byggemappen også ved feil (`--keep-build` beholder den, med fontfilene, og advarer om det). Kerningrettingene hentes fra `src/presentation/kernfix.json`. Varsler på norsk: manglende emne/mottaker/avsender, ukjent selskap eller variant, dato som ikke er ISO, tittel både i YAML og som `#`, overfulle linjer, tegn som mangler i fonten, tekst utenfor margen og enkeltord alene på siste linje.
- **Stil (`src/document/`):** `kwdocument.sty` (A4, venstremarg 20 mm og tekstspalte 145 mm, Light-titler og -overskrifter, Regular brødtekst 10/14,4 pt, Medium utheving og etiketter, grønne punkttegn, faktaboks på grå flate med grønn kant, sitat og kontaktblokk med grønn kant, tabell med hårstreker, brevhode med navnetrekk, returadresse og mottakerfelt tilpasset vinduskonvolutt, dato/referanser øverst til høyre, emnelinjen flyttes ned under lange mottaker- og referanseblokker, topptekst fra side 2, bunntekst med selskap, org.nr., begge kontoradresser og sidetall, grønn L-ramme med seismografstrek på første og siste side), `filter.lua` (varianter, automatisk faktaboks fra `**Etikett:** verdi`-linjer rett etter tittelen, `.facts`, `.columns`, `.contact`, automatisk kontaktblokk, etikett over tittelen fra delen før kolon, ingen enkeltord alene på siste tittellinje, siste avsnitt i brev holdes sammen med hilsen og signatur, selskapsdata for de fire selskapene) og `template.tex`.
- **`check_document_pdf.py`** (PyMuPDF): A4, bare NON Natural Grotesk og innebygd, ingen rasterbilder, tekst utenfor siden eller nær kanten, bunntekst med riktig selskapsnavn, org.nr. og begge adresser på hver side, rester av Markdown, rett apostrof og `--`, sidetall fra side 2, og nesten tomme sider.

### Visittkort (`deliverable/visualprofile/business-card/`)

Tosidig visittkort etter profilmanualens visittkortside: grå forside med svart navnetrekk (40 mm) og kontaktblokk (navn i Medium 9 pt, resten i Regular 8 pt), og grønn bakside med svart symbol (28 mm). Hvert kort er en Markdown-fil der bare YAML-hodet brukes: `name` (påkrevd), `title`, `phone`, `email` og `web`. Felt som utelates, faller bort uten at resten flytter seg. Mappen inneholder `visittkort-mal.md`/`.pdf`/`.png`, `visittkort-eksempel.md`/`.pdf`/`.png` (Eirik Larsen) og `README.md` (nytt kort, trykkspesifikasjon, fargetabell, bestilling).

```bash
uv run src/build_business_card.py deliverable/visualprofile/business-card/visittkort-eksempel.md   # → .pdf og .png ved siden av (~10 sek)
uv run src/build_business_card.py <kort.md> [-o <ut.pdf>] [--png <ut.png>] [--keep-build]
```

- **`build_business_card.py`** (PyMuPDF): fyller malen `src/business_card/card.tex` med pandoc og setter den med lualatex. Fonten pakkes ut fra den lisensierte zip-en, og `font_guard.py` håndheves; funksjonene for dette importeres fra `build_presentation.py`. Bygget kjører to ganger:
  - **Trykk-PDF (CMYK):** ark 105 × 75 mm, trim 85 × 55 mm, 3 mm utfallende kant og TrimBox/BleedBox satt, skjæremerker i registreringsfarge utenfor den utfallende kanten. Profilfargene skrives som CMYK fra `colors.json`, og navnetrekk og symbol skrives om fra RGB-svart til 100 % K.
  - **Skjermversjon (PNG):** RGB-fargene fra profilen, forside og bakside side om side, beskåret til trim. Den bygges separat fordi neongrønnfargen ikke kan vises riktig via CMYK.
- **Kontroller i bygget** (exit 1 ved varsel): arkstørrelse, trimboks og utfallende kant, all tekst minst 3 mm innenfor kuttkanten og minst 5 mm under navnetrekket, bare NON Natural Grotesk og innebygd, ingen rasterbilder, ingen tegning eller tekst i RGB eller gråtone (også inne i logoene), og tegn som mangler i fonten.
- **Visittkort fra CV-ene (`build_cv_business_cards.py`):** leser navn, tittel, telefon og e-post fra CV-ene i Markdown (`src/cv_markdown.py`), med `kodeworks.no` som nettadresse, og bygger hvert kort med `build_business_card.py`. Kortene havner som `visittkort-<navn>.pdf` og `.png` ved siden av hver CV, eller i `--out`. Felt som mangler i CV-en, utelates. Et kort som ikke består trykkontrollen, rapporteres, og kjøringen ender med exit 1:

  ```bash
  uv run src/build_cv_business_cards.py --dry-run                 # viser feltene for alle CV-er i cvs/
  uv run src/build_cv_business_cards.py                           # bygger kort for alle (ca. 6 sek per kort)
  uv run src/build_cv_business_cards.py cvs/<navn>/<navn>.md [--out <mappe>]
  ```

### Oversiktsark (`deliverable/visualprofile/oversikt.pdf`)

`src/build_visualprofile_overview.py` lager ett A4-ark på tvers per leveranse: profilmanualen, CV-en, visittkortet, presentasjonen og dokumentmalen. Sidene settes inn som vektor fra de ferdige PDF-ene, med overskrifter i profilfonten fra den lisensierte zip-en. Bygg leveransene først:

```bash
uv run src/build_visualprofile_overview.py        # → deliverable/visualprofile/oversikt.pdf (5 sider, ~3 sek)
```

---

## Batch-transformasjoner: dry-run + backups

Når et script transformerer mange filer med regex/mønster-erstatning, default må være ikke-destruktiv: skriv til `<navn>.cleaned.<ext>`-søsken-filer eller en separat output-mappe. Overskriv originalene kun etter en dry-run som har printet per-fil word-count / line-count deltas som et menneske har inspisert. Enhver enkeltfil som krymper til under ~70 % av original størrelse er et rødt flagg — en for bred regex kan stille trunkere innhold. Bruk `--promote`/`--in-place`-flagg først etter dry-run.

---

## Kom i gang

1. Installer `uv`, Pandoc, `pdftotext` (og evt. `mermaid-filter` + TeX Live med lualatex hvis du skal generere PDF/DOCX med diagrammer).
2. Les `CLAUDE.md`.
3. Legg nye kildedokumenter i `background/new/` og kjør konverteringspipelinen.
4. Opprett leveranser i `deliverable/`.
