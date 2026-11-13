# TASKS

Åpne og in-progress oppgaver for prosjektet. Se `ARCHIVE.md` for løste oppgaver.

Format: `### T<n> [<status>] <tittel>` — status er `[ ]` (åpen), `[~]` (in-progress) eller `[x]` (løst). Ved løsning: skriv løsningen under tasken før den flagges `[x]` og eventuelt arkiveres.

## Nye oppgaver

Uprosesserte bullet-punkter listes her — spør brukeren om de skal konverteres til T-tasks.

## Tasks

### T14 [x] Generere alle PDF-er med ett byggeskript, og ta dem ut av git

PDF-er og andre genererte filer skal ikke ligge i repoet. De skal genereres fra kildene (Markdown og SVG) med skriptene i `src/`. I dag ligger de sjekket inn ved siden av kildene, og det finnes ingen samlet måte å bygge alt på. Brukerens beslutninger:
- de genererte filene skal fortsatt ligge **ved siden av kilden**, men utenfor git;
- de ansattes CV-er og visittkort skal ha **sin egen byggekommando**, som også kjøres av skriptet som bygger alt;
- kontroll-PDF-ene i `background/` skal **slettes**;
- løsningen skal **dokumenteres**.

Brukeren har slettet Word-originalene i `data/cv/` og gitt `data/cv_md/` nytt navn, `data/cv/`. Mappen har nå én undermappe per person med `<navn>.md`, `images/`, CV-PDF og visittkort, og `AVVIK.md`. Oppryddingen (T16) har siden flyttet mappen til `cvs/`, som git sporer, fordi utviklerne oppdaterer CV-ene med commits. Henvisningene under til `data/cv/` gjelder derfor `cvs/`.

**Endringer:**

1. **Byggeskript for alt:** `src/build_all.py` med en eksplisitt liste over hva som bygges, hvilket skript som bygger det, og i hvilken rekkefølge:
   1. logoer og grafikk (SVG → PDF og PNG, `export_profile_assets.py`);
   2. profilmanualen;
   3. CV-mal og -eksempel;
   4. presentasjonsmal og -eksempel;
   5. brev- og dokumentmal med eksempler;
   6. visittkortmal og -eksempel;
   7. oversiktsarket, som bygger på de ferdige PDF-ene;
   8. de ansattes CV-er og visittkort, via kommandoen i punkt 2.

   Lista inneholder bare dokumenter som skal bli PDF, ikke alle `.md`-filer.

   Skriptet bygger **bare det som er endret**: en fil bygges på nytt når resultatet mangler, eller når kilden, bildene den viser til, stil- og malfilene eller byggeskriptet er nyere. Det har valgene `--only <gruppe>`, `--force`, `--list` og `--dry-run`. Etter byggene kjører det kontrollene (CV-kontrollen, presentasjons- og dokumentkontrollen, trykkontrollen for visittkort) og skriver en kort tabell med resultat per fil. Feiler noe, avslutter det med exit 1.
2. **Egen byggekommando for de ansattes CV-er:** `src/build_employee_cvs.py` (eller et tilsvarende navn) bygger CV-PDF og visittkort for hver person i `cvs/`, med samme endringssjekk, og kjører CV-kontrollen. `src/build_cv_business_cards.py` og `src/check_cv_md.py` peker på `data/cv/` i stedet for `data/cv_md/`.
3. ~~**Nedlastingen kolliderer med den nye mappen.**~~ Løses i T15: nedlastingen blir et generelt verktøy uten en standardmappe som kan treffe CV-ene.
4. **Ut av git:** `.gitignore` utelater alle genererte filer ved siden av kildene: PDF-ene og PNG-ene i leveransemappene, `profile/assets/pdf/` og `profile/assets/png/`, og oversiktsarket. Originalene skal fortsatt følge med, f.eks. Neues `Brand Guidelines.pdf`, `Visittkort.pdf`, lisensfilene for fonten og innboksens filer. En test sjekker mønstrene mot en liste over filer som skal og ikke skal ignoreres. Filene som allerede er sjekket inn, fjernes fra git-indeksen med `git rm --cached`. Det gjør brukeren selv, eller orkestratoren med brukerens uttrykkelige ja, fordi git-kommandoer alltid krever det.
5. **Kontroll-PDF-ene slettes:** de 15 PDF-ene som `src/build_md_pdf.py` laget i `background/visualprofile/` (datoprefiks, ved siden av `.md`-fila). Skriptet beholdes til neste konvertering, men tas ikke med i byggelisten.
6. **Test for byggelisten:** hver `.md` i leveransemappene som ikke er en README, finnes i lista i `build_all.py`, og hvert skript lista nevner, finnes.
7. **Dokumentasjon:**
   - **README** får et eget avsnitt, «Bygge alt»: hvorfor PDF-er ikke ligger i repoet, kommandoene (alt, én gruppe, de ansattes CV-er, `--list`), rekkefølgen og hva som avhenger av hva, endringssjekken, forutsetningene (`uv` og TeX Live med lualatex), omtrent hvor lang tid et fullt bygg tar, og hvor resultatene havner.
   - Avsnittene for hver leveranse viser til `build_all.py` i tillegg til eget skript.
   - Mappeoversikten oppdateres (`cvs/` og `data/` er rettet i T16).
   - Veiledningene for malene (`README.md` i `cv/`, `presentation/`, `document/` og `business-card/`) sier at PDF-en lages av byggekommandoen og ikke ligger i repoet.
   - **CLAUDE.md** får en kort regel om at genererte filer ikke sjekkes inn, men bygges med `build_all.py`, og mappeoversikten for `data/` rettes. Endringer i CLAUDE.md krever brukerens eget ja.

**Verifisering:**

1. `uv run src/build_all.py --list` viser alle mål i riktig rekkefølge. Et fullt bygg, kjørt i grupper så ingen kommando går over 2 minutter, gir ingen feil, og alle kontroller består. En ny kjøring uten endringer bygger ingenting.
2. Endres én kilde (f.eks. `cv-mal.md`), bygges bare den og oversiktsarket på nytt.
3. Byggekommandoen for de ansattes CV-er bygger alle i `cvs/`, og CV-kontrollen gir 0 avvik.
4. Etter at de genererte filene er slettet lokalt, gjenskaper `build_all.py` dem alle.
5. `git status --ignored` (kjøres av brukeren eller med brukerens ja) viser at alle genererte filer er ignorert og ingen originaler.
6. `pytest --timeout=5` består, med de nye testene for byggelisten og `.gitignore`-mønstrene.
7. README er lest gjennom av en leser uten kontekst. Alle kommandoene i «Bygge alt» er kjørt som de står.

**Estimert innsats:** 55 min

**Løsning (2026-11-12):**

- **`src/build_all.py`** bygger alle genererte filer i leveransene i grupper og fast rekkefølge: `assets`, `profile`, `cv`, `presentation`, `document`, `business-card`, `overview`, og til slutt `employee-cvs`. Den har flaggene `--only`, `--force`, `--list`, `--dry-run` og `--no-check`. Kontrollene kjøres etter hvert bygg: CV-kontrollen for CV-eksempelet, `check_presentation_pdf.py` og `check_document_pdf.py`. Visittkortets trykkontroller ligger allerede i byggeskriptet. Kommandoen avslutter med kode 1 ved feil.
- **`src/build_employee_cvs.py`** bygger CV-PDF og visittkort for hver person i `cvs/`, eller for navngitte personer, og kontrollerer CV-ene etterpå.
- **`src/build_targets.py`** (ny, felles) har endringssjekken. Et mål er utdatert når en utfil mangler, eller når en innfil er nyere enn den eldste utfilen. Innfilene er kilden, bilder, stil- og malmapper, byggeskriptet, fontarkivet, fontvakten og kerningrettingene. Et mål som bruker utfilene til et annet mål, bygges også når det andre bygges i samme kjøring. Slik bygges oversiktsarket på nytt når en mal endres. Logoene regnes med som SVG-kilder, ikke som de eksporterte PDF/PNG-filene. Ellers ville eksporten gjort alt utdatert.
- **`.gitignore`**: de bygde filene i `deliverable/visualprofile/` er utenfor git (oversiktsarket, profilmanualen, `profile/assets/pdf/` og `png/`, og PDF-er og PNG-er i malmappene). Det samme gjelder CV-PDF og visittkort i `cvs/*/`. Kildene, bildene og SVG-ene er med. Repoet har ingen commits ennå, så `git rm --cached` trengs ikke.
- **`tests/test_build_all.py`** (257 parametriserte tilfeller): hver Markdown-kilde i malmappene står i byggelista (unntatt `profile/farger.md`, som er referansetekst). Hver utfil er dekket av `.gitignore`, og ingen kilde er det.
- **Kontroll-PDF-ene** (15) i `background/visualprofile/` ble slettet i oppryddingen (T16, punkt 5).
- **Nedlastingen** kolliderer ikke lenger med CV-mappen, fordi CV-ene ligger i `cvs/` (T16). Den generelle nedlastingen er T15.
- **Dokumentasjon:** ny README-seksjon «Bygge alt (`src/build_all.py`)» med kommandoer, grupper og en forklaring av endringssjekken, og `build_all.py` er lagt inn i mappeoversikten. Malveiledningene i `cv/`, `presentation/`, `document/` og `business-card/` sier at PDF/PNG ikke er i git og bygges med `build_all.py`.

**Verifisering:**

1. `--list` viser de 13 målene i riktig rekkefølge. Det som var utdatert, ble bygget gruppe for gruppe uten feil: dokumentmalen, eksempelbrevet, visittkortmal og -eksempel, oversiktsarket, og visittkortene for alle 20 ansatte (endret visittkortskript). Alle kontroller besto. En full `build_all.py` uten endringer etterpå: «0 built, 13 unchanged» for leveransene, «0 built, 40 unchanged» for de ansattes CV-er, og CV-kontrollen ga 20 filer med 0 avvik.
2. Etter `touch cv-mal.md` viste `--dry-run` at bare `cv-mal.pdf` og `oversikt.pdf` ville blitt bygget. Bygget gjorde akkurat det.
3. `build_employee_cvs.py` har bygget alle i `cvs/`, og CV-kontrollen ga 0 avvik.
4. Gjenskaping er sjekket på én leveranse og én ansatt: etter sletting av `document/dokumentmal.pdf` og `cvs/paal-noedseth/visittkort-paal-noedseth.png` bygget kommandoene filene på nytt. Det er ikke kjørt et fullt bygg fra en tom checkout. Det tar flere minutter, mens kommandoene her er holdt under to.
5. `git status --ignored` ble kjørt én gang med brukerens tillatelse (2026-11-13, etter at den gamle profilen var slettet). Alle 100 bygde filer er ignorert: 65 PDF-er og 35 PNG-er i malmappene, i logo-eksporten og i `cvs/*/`. Ingen andre filer enn bygde filer og arbeidsdata er ignorert (de andre er `.venv/`, `tmp/`, `data/`, `secrets/`, `__pycache__/` og `.pytest_cache/`). 276 filer på til sammen 13,5 MB blir med i en commit. Den største er et CV-foto på 1,2 MB, og de eneste PDF-ene er fontlisensene.
6. `pytest --timeout=5`: 364 passed.
7. Kommandoene i «Bygge alt» er kjørt slik de står: `--list`, `--dry-run`, `--only`, `--force --no-check` (på oversiktsarket), og `build_employee_cvs.py` med navn, `--list` og `--dry-run`.

**Ikke gjort:** en egen regel i CLAUDE.md om at genererte filer bygges med `build_all.py` og ikke sjekkes inn. Den krever brukerens ja. Mappeoversikten i CLAUDE.md viser `build_all.py` siden oppryddingen av den gamle profilen.

**Faktisk innsats:** 6m 54s (veggklokke) mot 55 min estimert. Oppryddingen hadde allerede gjort to av punktene (kontroll-PDF-ene og CV-mappen), og byggeskriptene fantes fra før, så oppgaven ble mest en liste med mål.

**Kobling:** bygger på T10 (leveransene og skriptene), T12 (CV-ene i Markdown) og T11 (nedlastingen). Oppfølging, ikke del av denne oppgaven: synk av Markdown-CV-er fra Drive.

**Berørte filer:** `src/build_all.py` (ny), `src/build_employee_cvs.py` (ny), `src/build_targets.py` (ny), `tests/test_build_all.py` (ny), `src/build_cv_business_cards.py`, `src/check_cv_md.py`, `src/download_cvs.py`, `.claude/skills/download-cvs/SKILL.md`, `.gitignore`, `tests/` (nye tester og oppdaterte stier), `background/visualprofile/**/<dato>_*.pdf` (slettes), `deliverable/visualprofile/*/README.md`, `README.md`, `TASKS.md`, og `CLAUDE.md` (bare med eget ja)

### T15 [x] Generell nedlasting fra Google Drive (`fetch_from_drive`)

Utviklerne har bestemt at de oppdaterer CV-ene sine med commits i git. CV-ene skal derfor ikke lenger hentes fra Google Drive som en fast rutine. Koden for Drive skal likevel beholdes, men gjøres generell. I dag er `src/download_cvs.py` bundet til CV-er: en fast liste i `cv_sources.csv`, filtrering på personnavn og standardmappen `data/cv/`, som nå er mappen for CV-ene i Markdown. Skriptet skal skrives om til et generelt verktøy for å hente én fil eller en hel mappe fra Drive.

**Endringer:**

1. `src/download_cvs.py` → `src/fetch_from_drive.py`. Hva som hentes, oppgis som argument: én eller flere Drive-lenker eller fil-ID-er, til en fil eller en mappe. En mappe hentes med innholdet, valgfritt rekursivt (`--recursive`). Eksempel:

   ```bash
   uv run python src/fetch_from_drive.py <lenke eller ID> [...] --out <mappe> [--format docx|pdf|md|txt|odt] [--recursive] [--force] [--dry-run]
   ```
2. Det som fungerer i dag, beholdes:
   - Google-dokumenter eksporteres i valgt format, og opplastede filer lastes ned uendret;
   - fildatoen settes til «sist endret» på Drive, og bare endrede filer hentes på nytt (`--force` henter alt);
   - OAuth med `secrets/credentials.json` og `secrets/token.json`, bare lesetilgang;
   - trygge filnavn.
3. Det er **ingen standardmappe som kan treffe CV-ene i git:** `--out` er påkrevd, eller standarden er en egen, git-ignorert mappe som `data/drive/`. En lenkeliste kan fortsatt brukes (`--list <fil.csv>`, kolonnen `Link`), men `cv_sources.csv` er ikke lenger standard. Den slettes eller flyttes etter avtale med brukeren.
4. Prosjekt-skillen `download-cvs` gjøres om til `fetch-from-drive`, med generelle utløserfraser («hent fra Drive», «last ned fra driven») og prosedyren for engangshenting. Oversikten i `.claude/skills/README.md` oppdateres.
5. Testene for de rene funksjonene (lenke → ID, filnavn, tidsstempel, endringssjekk, lenkeliste) flyttes til `tests/test_fetch_from_drive.py`, og nye tester dekker gjenkjenning av mappe- og fillenker og argumenttolkningen.
6. **Dokumentasjon:** README-avsnittet om CV-er fra Google Drive skrives om til «Hente filer fra Google Drive»: når verktøyet brukes (engangshenting av originaler), og at CV-ene vedlikeholdes i git. Mappeoversikten for `data/` og eventuelle henvisninger i CLAUDE.md oppdateres. Endringer i CLAUDE.md krever brukerens eget ja.

**Verifisering:**

1. `pytest --timeout=5` består.
2. `--dry-run` mot én fil og mot én mappe på Drive viser riktige filer og målstier, uten å laste ned. Kjøres med brukerens tillatelse, fordi det leser fra Drive.
3. Én ekte henting av én fil til en midlertidig mappe gir riktig fil og riktig fildato. Ny kjøring henter ikke fila igjen.
4. Søk etter `download_cvs`, `download-cvs` og `cv_sources.csv` gir bare treff i historiske løsningsnotater.

**Estimert innsats:** 34 min

**Løsning (2026-11-12):**

- **`src/fetch_from_drive.py`** erstatter `src/download_cvs.py`, som er slettet. Hva som hentes, oppgis som Drive-lenker eller ID-er: Docs, Sheets, Slides, `file/d/…`, `open?id=…`, `drive/folders/…`, også med `u/<n>/`, eller en bar ID. Det kan også gis som en CSV med kolonnen `Link` (`--list`, skilletegn `;` eller `,`). En mappe hentes til en undermappe med samme navn. Med `--recursive` speiles også undermappene. Uten flagget nevnes undermappene med `NOTE`.
- **Eksport:** Google-dokumenter hentes som `docx`, `pdf`, `md`, `txt` eller `odt`. `md` er nytt, og Drive eksporterer det direkte. Regneark blir `xlsx` og presentasjoner `pptx`, eller `pdf` med `--format pdf`. Tegninger blir `pdf`. Typer som ikke kan eksporteres (skjemaer o.l.), hoppes over med en melding. Opplastede filer hentes uendret.
- **Beholdt:** fildato lik «sist endret» på Drive, endringssjekk (`--force` henter alt), OAuth med bare lesetilgang og trygge filnavn.
- **Standardmappe** er `data/drive/`, som er utenfor git. Den kan ikke treffe `cvs/`. Brukeren hadde bedt om at spørsmål ble besvart uten å vente, så valget ble tatt slik: `cv_sources.csv` er flyttet fra prosjektroten til `data/cv_sources.csv`. Lenkene til de ansattes CV-dokumenter finnes da fortsatt lokalt og kan brukes med `--list`, men lista ligger ikke i git.
- **Skill:** `download-cvs` er erstattet av `fetch-from-drive`, med generelle utløserfraser, prosedyren for engangshenting og et forbud mot å skrive til `cvs/`. Oversikten i `.claude/skills/README.md` er oppdatert.
- **Tester:** `tests/test_fetch_from_drive.py` erstatter `tests/test_download_cvs.py` (38 tilfeller). Testene dekker gjenkjenning av lenker og ID-er, mappelenker, filnavn per type og format, eksportvalg, lenkelister med begge skilletegn, argumenttolkning og at standardmappen er utenfor git. De dekker også utvidelse av mapper med og uten `--recursive` mot en falsk Drive, tidsstempel og endringssjekk.
- **Dokumentasjon:** README-avsnittet heter nå «Hente filer fra Google Drive (`src/fetch_from_drive.py`)», og forklarer når verktøyet brukes og at CV-ene vedlikeholdes i git. Mappeoversikten for `data/`, kommentaren i `pyproject.toml` og kommentaren i `.gitignore` er rettet.

**Verifisering:**

1. `pytest --timeout=5`: 391 passed.
2. Tørrkjøring mot én CV-fil på Drive viste `data/drive/Master CV - Aleksander Skraastad.docx` (endret 2026-02-09). Tørrkjøring mot mappen fila ligger i, viste 18 filer under `data/drive/Master CV/` og tre undermapper som ble hoppet over uten `--recursive`. Ingenting ble lastet ned. Brukeren var borte og hadde bedt om at spørsmål ble besvart uten å vente. Lesingen fra Drive ble derfor gjort med det eksisterende tokenet, som bare har lesetilgang.
3. Én ekte henting av samme fil med `--format md` til en midlertidig mappe (scratchpad, slettet etterpå) ga en Markdown-fil på 123 KB med fildato 2026-02-09, som på Drive. Ny kjøring: «0 fetched, 1 skipped».
4. `download_cvs` og `download-cvs` finnes bare i historiske løsningsnotater og i oppgaveteksten. `cv_sources.csv` nevnes bevisst i README og i skriptets hjelpetekst, som `data/cv_sources.csv` (den lokale plasseringen).

**Faktisk innsats:** 3m 59s (veggklokke) mot 34 min estimert. Den gamle koden kunne gjenbrukes nesten uendret, så arbeidet var mest å utvide den med mapper og flere eksporttyper.

**Kobling:** erstatter nedlastingen fra T11. Påvirker T14, punkt 3: standardmappen for nedlasting løses her, så T14 trenger ikke `data/cv-download/`.

**Berørte filer:** `src/fetch_from_drive.py` (fra `src/download_cvs.py`), `data/cv_sources.csv` (fra roten), `pyproject.toml`, `.gitignore`, `tests/test_fetch_from_drive.py` (fra `tests/test_download_cvs.py`), `.claude/skills/fetch-from-drive/SKILL.md` (fra `download-cvs/`), `.claude/skills/README.md`, `cv_sources.csv`, `README.md`, `TASKS.md`, og `CLAUDE.md` (bare med eget ja)

### T16 [x] Rydde i repoet

Repoet har samlet opp rester: gamle konverteringer, innboksfiler som er behandlet, dubletter, kontrollfiler, arbeidsmapper og skript uten leveranse, særlig i `background/`. I tillegg er det avklart at utviklerne oppdaterer CV-ene sine med commits i git, så CV-ene i Markdown må ligge i en mappe git sporer.

**Endringer:**

1. **CV-ene inn i git** (krever at brukeren først bekrefter at personopplysningene i CV-ene, som telefonnumre og én privat e-postadresse, kan ligge i repoet): `data/cv/` → `cvs/<navn>/`. Hver mappe har `<navn>.md` og `images/`, og `cvs/AVVIK.md` følger med. Genererte filer i mappene (CV-PDF og visittkort i PDF og PNG) holdes utenfor git i `.gitignore`. Alle henvisninger oppdateres: `src/build_cv_business_cards.py`, `src/check_cv_md.py`, testene, README, CV-veiledningen og T14.
2. **`background/cvs/`** (15 pandoc-utskrifter fra september, med bildelenker til mapper som ikke finnes) slettes. Henvisningene i `background/customers.md`, `background/projects.md` og `background/2026-09-22_startups.md` peker til `cvs/` i stedet.
3. **`background/new/cvs/`** (15 Word-originaler fra september) slettes.
4. **Resten av innboksen `background/new/`:**
   - `README.kw.docx`, `Prosjektoversikt.docx`, `Master KodeWorks Presentasjon.pptx` og `Grunnlag for tekst til webside.docx` er konvertert til `background/`. Det kontrolleres at innholdet finnes i den konverterte fila, og deretter slettes originalen.
   - `Ansatthåndbok - Revisjon.docx` sammenlignes med `background/2026-09-22_ansatthaandbok.md`. Er den nyere, konverteres den etter innboksprosedyren i CLAUDE.md, og den gamle fila oppdateres eller erstattes. Deretter slettes originalen.
   - `ITKO Temp - slik rapporterer du.pdf` konverteres til `background/<dato>_itko_temp_rapportering.md` etter innboksprosedyren (pdftotext, dato fra dokumentet), og originalen slettes.
   - `CV-mal 2023.pdf` flyttes til `background/visualprofile/` ved siden av `CV-mal 2023.docx`, som referanse.
5. **Kontroll-PDF-ene** fra `src/build_md_pdf.py` i `background/visualprofile/` slettes, om de ikke allerede er slettet i T14.
6. **Dubletter i `background/visualprofile/Google slides template/`:** de tre `.emf`-filene og de tre `.emf.jpg`-forhåndsvisningene slettes. SVG-ene av de samme bakgrunnene beholdes.
7. **«Untitled document»** (`neue-delivery/Untitled document.docx` og `2026-11-11_untitled_document.md`): innholdet sjekkes. Er det tomt eller uten verdi, slettes begge. Ellers får fila et beskrivende navn.
8. **Datoprefiks:** `background/customers.md` → `2026-09-22_customers.md` og `background/projects.md` → `2026-09-22_projects.md`, med henvisningene oppdatert.
9. **`temp/`:**
   - `temp/T10.4/` og `temp/T10.5/` (læringslogger og spesifikasjon, der lærdommene står i oppgavefila) slettes.
   - Testkorpuset `temp/T10.5/tester/` flyttes først til `tests/fixtures/documents/` og tas med i byggetestene (T14).
   - `temp/Ansattoversikt_10_26_2026*.xlsx` (tre kopier) slettes bare etter brukerens ja. De er ikke laget av en kjent oppgave.
10. **`notes.txt`** i rotmappen (notater til utlysningen av Android/Kotlin-oppdraget) flyttes til `background/2026-11-11_notat_konsulentoppdrag_android_kotlin.md`, eller slettes, etter brukerens valg.
11. **Gamle CV-skript** for versjon 1 og 2 (`src/build_cv.py`, `src/build_cv_v2.py`, `src/gen_cv_seismograph.py`, `src/check_cv_docx.py`, `src/arial_fallback.py`) slettes, og omtalen i README fjernes. `src/seismograph.py` beholdes.
12. **Arkivering:** de løste oppgavene T1–T13 flyttes fra TASKS.md til ARCHIVE.md, sortert på nummer. TASKS.md beholder de åpne oppgavene.
13. **Dokumentasjon:** README (mappeoversikten, `cvs/`, `data/`, `background/`) og mappeoversikten i CLAUDE.md oppdateres. Endringer i CLAUDE.md krever brukerens eget ja.

**Verifisering:**

1. Søk etter henvisninger til slettede eller flyttede filer (`background/cvs`, `background/new/cvs`, `data/cv`, `customers.md`, `projects.md`, `build_cv.py`, `build_cv_v2.py`, `check_cv_docx.py`, `arial_fallback.py`, `gen_cv_seismograph.py`, `notes.txt`) gir bare treff i historiske løsningsnotater og i ARCHIVE.md.
2. `background/new/` er tom (eller har bare filer brukeren har bestemt skal ligge).
3. `uv run python src/check_cv_md.py cvs/*/*.md` gir 0 avvik, og visittkort og CV for minst én person bygges fra `cvs/`.
4. `pytest --timeout=5` består.
5. TASKS.md har bare åpne oppgaver, og ARCHIVE.md har T1–T13 i stigende rekkefølge.

**Estimert innsats:** 34 min

**Løsning (2026-11-12):** Brukeren var borte og hadde bedt om at spørsmål ble besvart uten å vente. Valgene som ellers krevde brukerens ja, er tatt slik at ingenting går tapt og ingenting blir offentlig:

1. **CV-ene:** `data/cv/` er flyttet til `cvs/` (20 personer og `AVVIK.md`). `.gitignore` holder CV-PDF og visittkort i `cvs/*/` utenfor git. Om personopplysningene skal inn i git, avgjør brukeren først når mappen committes, for repoet har ingen commits ennå. Henvisningene er oppdatert i `src/build_cv_business_cards.py` (standardmønsteret pekte fortsatt på `data/cv_md/`), README, `cvs/AVVIK.md` og T14. `src/check_cv_md.py`, testene og CV-veiledningen hadde ingen gamle stier.
2. **`background/cvs/`** (15 pandoc-utskrifter) er slettet. Henvisningene i kunde- og prosjektoversikten og i startup-notatet peker til `cvs/`.
3. **`background/new/cvs/`** (15 Word-originaler) er slettet.
4. **Innboksen:** de fem Word- og PowerPoint-originalene (README.kw, Prosjektoversikt, Master-presentasjonen, Grunnlag for webside og Ansatthåndbok – Revisjon) ble sammenlignet ord for ord med de konverterte filene i `background/`. Alle ordene på fire tegn eller mer fantes der, for alle fem. Ansatthåndboka var altså ikke nyere enn konverteringen. Alle fem originalene er slettet. ITKO-veiledningen er konvertert til `background/2026-09-24_itko_temp_rapportering.md` (dato fra PDF-en, alle 2 675 ord med), og PDF-en er slettet. `CV-mal 2023.pdf` er flyttet til `background/visualprofile/`. `background/new/` er tom.
5. **Kontroll-PDF-ene:** 15 datoprefiksede PDF-er ved siden av en `.md` i `background/visualprofile/` er slettet.
6. **EMF-dublettene:** de tre `.emf` og tre `.emf.jpg` i `Google slides template/` er slettet. SVG-ene er beholdt.
7. **«Untitled document»** inneholdt notater til nettsiden: gjøremål for menyen, hvem som besøker siden og hva de ser etter. Fila har fått navnet `neue-delivery/2026-11-11_notater_nettside.md` med en beskrivende tittel og innledning. Word-originalen er slettet.
8. **Datoprefiks:** `background/2026-09-22_customers.md` og `background/2026-09-22_projects.md`. Henvisningene i fire bakgrunnsfiler og i T10-teksten er oppdatert.
9. **`temp/`:** testkorpuset (10 filer) er flyttet til `tests/fixtures/documents/`. `temp/T10.4/` og `temp/T10.5/` er slettet. De tre regnearkene `Ansattoversikt_10_26_2026*.xlsx` er **ikke slettet**, men flyttet til `data/ansattoversikt/`, som er utenfor git. Brukeren kan slette dem der. `temp/` er fjernet.
10. **`notes.txt`** er flyttet til `background/2026-11-11_notat_konsulentoppdrag_android_kotlin.md`, med innledning og stikkordene som liste. Flytting ble valgt fordi det ikke mister noe.
11. **De gamle CV-skriptene** (fem filer) er slettet, og README sier at både leveransene og generatorene for versjon 1 og 2 er borte. `src/seismograph.py` er beholdt.
12. **Arkivering:** T1–T13 (943 linjer) er flyttet til ARCHIVE.md i stigende rekkefølge. TASKS.md har bare T14–T16.
13. **README:** mappeoversikten har `cvs/`, `business_card/`, testkorpuset, ny beskrivelse av `data/` og innboksen, og `cv_sources.csv` er fjernet fra roten. **CLAUDE.md er ikke endret** (krever brukerens ja). Mappeoversikten der beskriver fortsatt `data/` som «cv/: CV-er fra Drive» og mangler `cvs/`.

**Verifisering:**

1. Søket etter de slettede og flyttede stiene gir treff bare i historiske løsningsnotater, i ARCHIVE.md og i CLAUDE.md. CLAUDE.md har bare `background/new/cvs/foo.docx` som et generelt eksempel på speiling av undermapper, og den utdaterte `data/`-linjen nevnt i punkt 13. De siste treffene i skillen, README og nedlastingsskriptet ble ryddet i T15.
2. `background/new/` er tom.
3. `check_cv_md.py cvs/*/*.md`: 20 filer, 0 avvik. CV og visittkort for Pål Nødseth er bygget fra `cvs/`, og senere alle 20 med `build_employee_cvs.py`.
4. `pytest --timeout=5`: 97 passed etter oppryddingen, og 391 etter T14 og T15.
5. TASKS.md har bare T14–T16. ARCHIVE.md har T1–T13 i stigende rekkefølge (20 overskrifter med deloppgaver).

**Faktisk innsats:** 4m 36s (veggklokke) mot 34 min estimert. Alle punktene var konkret beskrevet, og bare sammenligningen av innboksfilene krevde et lite skript.

**Kobling:** følger opp T10, T11, T12 og T13. Henger sammen med T14 (byggeskriptet bruker `cvs/` og ignoreringsreglene) og T15 (`cv_sources.csv` og nedlastingen fra Drive).

**Berørte filer:** `cvs/` (ny, fra `data/cv/`), `background/cvs/` og `background/new/cvs/` (slettes), `background/new/*`, `background/visualprofile/**`, `background/customers.md`, `background/projects.md`, `background/2026-09-22_startups.md`, `temp/`, `notes.txt`, `src/` (gamle CV-skript), `tests/`, `.gitignore`, `README.md`, `TASKS.md`, `ARCHIVE.md`, og `CLAUDE.md` (bare med eget ja)

### T17 [x] Rydde bort grunnlaget for den gamle visuelle profilen

`background/visualprofile/` er på 492 MB. Den inneholder leveransen fra Neue (2021) med Markdown-konverteringer, byråets logo- og grafikkfiler (Brand assets), Google Slides-malen, CV-malen fra 2023 og fontarkivet. Den reviderte profilen i `deliverable/visualprofile/` er ferdig og bruker bare egne filer: de rensede SVG-ene i `profile/assets/`, fotoene i `profile/images/` og fontarkivet. Alle originalene ligger på Google Drive. Repoet har ingen commits ennå, så nå kan den halve gigabyten holdes ute av git-historikken for godt.

Det som er undersøkt (2026-11-13):

- **Brand assets (12 MB)** består av 7 EPS-filer (7,0 MB), 16 JPG/PNG (4,7 MB), 8 SVG (10 KB), to Affinity Designer-filer, to tomme mapper og en lenke til fontprodusenten. Formene i EPS-filene ble rendret og lagt oppå de rensede SVG-ene: logo og symbol overlapper 98–99 %, mønsteret 95 %. Det samme avviket kommer mot byråets egne SVG-er, så det skyldes rendringen av EPS, ikke ulik form. CMYK-variantene har samme form som RGB, og CMYK-verdiene står i `profile/colors.json`. Alle 8 SVG-ene (også den hvite logoen, `KW_logo copy.svg`, og symbolene med grønn strek) er dekket av SVG-ene i `profile/assets/`. Ingen skript eller dokumenter bruker Brand assets.
- **Markdown-konverteringene** av Neue-leveransen og Slides-malen var arbeidsgrunnlaget for den nye profilen. Ingen bygg leser dem. Bare eksempler i README og i hjelpeteksten til `src/extract_visualprofile.py` og `src/build_md_pdf.py` viser til dem.
- **Fontarkivet** (0,8 MB) brukes av alle byggene (`src/build_targets.py`, `src/build_presentation.py`) og beholdes.

**Endringer:**

1. **Slett `background/visualprofile/Brand assets/`** i sin helhet.
2. **Slett alt annet i `background/visualprofile/` enn `Fonts/`:** `neue-delivery/` (originaler, Markdown-konverteringer, `_image_text.md` og `_media/`-mapper, notatene til nettsiden), `Google slides template/`, og CV-malen fra 2023 (`.docx`, `.pdf`, `2026-11-11_cv_mal_2023.md` og `_media/`).
3. **Behold** `background/2026-11-11_kodeworks_no_design.md` og skjermbildene i `background/2026-11-11_kodeworks_no_design_media/`.
4. **Verktøyene for uttrekk og kontroll** (`src/extract_visualprofile.py`, `src/build_md_pdf.py`, `src/compare_md_pdf.py`) beholdes som generelle verktøy for innboksen. Eksemplene i hjelpetekstene deres byttes til generelle stier i `background/new/`.
5. **README** beskriver tilstanden etter slettingen: mappeoversikten (`background/visualprofile/` har bare fontarkivet), avsnittene om uttrekk fra PDF og kontroll-PDF, og innledningen til «Visuell profil» der den nevner grunnlaget fra 2021.
6. **CLAUDE.md** beskriver tilstanden etter slettingen (brukeren har bedt om det i samtalen 2026-11-13): mappeoversikten får `background/visualprofile/` (bare fontarkivet), `cvs/` og riktig beskrivelse av `data/`.

**Verifisering:**

1. `background/visualprofile/` inneholder bare `Fonts/`. Mappen er under 1 MB.
2. Søk etter `Brand assets`, `neue-delivery`, `Google slides template`, `brand_guidelines`, `stratplatt` og `cv_mal_2023` gir bare treff i historiske løsningsnotater og i ARCHIVE.md.
3. Alle byggeskriptene kjøres på nytt med `--force`, gruppe for gruppe, så ingen kommando går over 2 minutter: `uv run python src/build_all.py --force --only <gruppe>` for `assets`, `profile`, `cv`, `presentation`, `document`, `business-card` og `overview`, og `uv run python src/build_employee_cvs.py --force <navn …>` i puljer. Alle bygg og kontroller består, og fontvakten melder ingen fonter utenfor byggemappen og TeX-trærne.
4. `pytest --timeout=5` består.
5. README og CLAUDE.md er lest gjennom: ingen henvisninger til slettede filer, og kommandoene i de endrede avsnittene virker som de står.

**Estimert innsats:** 34 min

**Løsning (2026-11-13):**

- **Slettet** fra `background/visualprofile/`: `Brand assets/`, `neue-delivery/` (originaler, Markdown-konverteringer, `_image_text.md`, `_media/`-mapper og notatene til nettsiden), `Google slides template/`, og CV-malen fra 2023 (`.docx`, `.pdf`, `.md` og `_media/`). Mappen gikk fra 492 MB til 0,8 MB. Bare `Fonts/` er igjen: begge font-zipene og lisensene, med konverteringene av lisensene.
- **Beholdt:** `background/2026-11-11_kodeworks_no_design.md` med skjermbildene.
- **Verktøyene:** hjelpetekstene i `src/extract_visualprofile.py` og `src/build_md_pdf.py` bruker generelle eksempler i `background/new/` i stedet for designmanualen. `src/compare_md_pdf.py` hadde ingen slike eksempler.
- **README:** mappeoversikten viser `background/visualprofile/Fonts/`. Avsnittene om uttrekk og kontroll-PDF har generelle eksempler, og tallet for den største PDF-en er gjort om til et eksempel. Innledningen til «Visuell profil» sier at profilen står på egne ben, og at originalene fra 2021 ligger på Google Drive.
- **CLAUDE.md:** mappeoversikten har nå `background/visualprofile/Fonts/`, `cvs/`, `tmp/`, riktig beskrivelse av `data/` og en henvisning til `build_all.py`.

**Verifisering:**

1. `background/visualprofile/` inneholder bare `Fonts/` og er på 803 KB.
2. Søk etter `Brand assets`, `neue-delivery`, `Google slides template`, `brand_guidelines`, `stratplatt`, `cv_mal_2023` og `CV-mal 2023` gir bare treff i ARCHIVE.md, i løsningsnotatene til T16 og i denne oppgaveteksten.
3. Alle 65 PDF-er er bygget på nytt med `--force` etter slettingen. Alle bygg og kontroller besto, CV-kontrollen ga 0 avvik, og fontvakten meldte ingenting. Sammenlignet med PDF-ene fra før er alle 65 visuelt identiske, med samme tekst og samme fonter. **Avvik underveis:** fire puljer for de ansatte ble sendt samtidig i stedet for etter hverandre. De konkurrerte om maskinen, tre ble stoppet av tidsgrensen, og den fjerde gikk over i bakgrunnen og ble ferdig der. Ett avbrutt bygg etterlot en arbeidsmappe med den utpakkede fonten i `tmp/`, som ble slettet. Arbeidet ble stanset og rapportert til brukeren, og fortsatte etter brukerens «Kjør ferdig». De åtte personene med PDF-er fra før slettingen ble så bygget med `--force`, én kommando om gangen. Til slutt var ingen av de 65 PDF-ene eldre enn slettingen.
4. `pytest --timeout=5`: 419 passed.
5. README og CLAUDE.md er gjennomgått: ingen henvisninger til slettede filer er igjen. Eksemplene for uttrekk og kontroll-PDF bruker plassholdere. Selve verktøyene ble kjørt på en testfil under `tmp/` i T18.

**Faktisk innsats:** 42m 25s (veggklokke) mot 34 min estimert. Inkludert er stansen etter at kommandoen gikk over i bakgrunnen, og ventetiden til brukeren svarte. Selve arbeidet tok omtrent like lang tid som estimert.

**Kobling:** følger opp T9 (konverteringen av den visuelle profilen), T10 (den reviderte profilen) og T16 (oppryddingen).

**Berørte filer:** `background/visualprofile/` (alt unntatt `Fonts/` slettes), `src/extract_visualprofile.py`, `src/build_md_pdf.py`, `src/compare_md_pdf.py` (hjelpetekst), `README.md`, `CLAUDE.md`, `TASKS.md`

### T18 [x] Arbeidsmapper for scriptene i `tmp/` i prosjektet

Regelen i CLAUDE.md sier at scripts i `src/` legger arbeidsmapper og mellomfiler i `tmp/` i prosjektroten (git-ignorert), og ikke i systemets midlertidige mappe, der vi selv velger hvor filene havner. Installerte programmer (uv, LuaLaTeX, pytest, pandoc o.l.) kan beholde sine vanlige hurtigbuffere og midlertidige mapper. Testene trenger derfor ikke endres.

Ni scripts bruker i dag `tempfile` med systemets standardmappe (sjekket 2026-11-13):

| Script | Bruk |
|---|---|
| `src/build_business_card.py` | `mkdtemp` for LaTeX-bygget, pakker ut fontfila |
| `src/build_document.py` | `mkdtemp` for LaTeX-bygget, pakker ut fontfila |
| `src/build_presentation.py` | `mkdtemp` for LaTeX-bygget, pakker ut fontfila |
| `src/build_profile_manual.py` | `TemporaryDirectory` for LaTeX-bygget, pakker ut fontfila |
| `src/build_cv_pdf.py` | `TemporaryDirectory` for LaTeX-bygget |
| `src/build_cv_business_cards.py` | `TemporaryDirectory` for mellomfila til hvert kort |
| `src/build_md_pdf.py` | `TemporaryDirectory` for kontroll-PDF-en |
| `src/check_document_pdf.py` | `TemporaryDirectory` for kontrollen |
| `src/extract_visualprofile.py` | `TemporaryDirectory` for uttrekket |

De tre som bruker `mkdtemp`, rydder bare opp når bygget lykkes og `--keep-build` ikke er satt. Ved feil blir den utpakkede, lisensierte fontfila liggende.

**Endringer:**

1. **Felles hjelpefunksjon** i `src/project_tmp.py`: en context manager `work_dir(prefix, keep=False)` som oppretter en unik mappe under `<prosjektrot>/tmp/` og sletter den når blokken avsluttes, også ved feil. Med `keep=True` blir mappen liggende, og stien skrives ut (for `--keep-build`). Prosjektroten finnes fra scriptets plassering, ikke fra arbeidskatalogen.
2. **De ni scriptene** bruker `work_dir` i stedet for `tempfile`. `--keep-build` og `--keep` virker som før, men mappen ligger i `tmp/`.
3. **Fontvakten** (`src/font_guard.py`) godtar fortsatt fonter fra byggemappen når den ligger under `tmp/`.
4. **Test** `tests/test_project_tmp.py`: `work_dir` lager mappen under `tmp/` og sletter den etter normal avslutning og etter et unntak, men beholder den med `keep=True`. En annen test feiler hvis et script i `src/` importerer `tempfile`.
5. **README:** «Konvensjoner» (eller tilsvarende sted) sier at arbeidsmapper ligger i `tmp/`, og mappeoversikten får `tmp/`.

**Verifisering:**

1. `pytest --timeout=5` består.
2. Alle byggene kjøres på nytt med `--force`, gruppe for gruppe, så ingen kommando går over 2 minutter: `uv run python src/build_all.py --force --only <gruppe>` for alle grupper, og `uv run python src/build_employee_cvs.py --force <navn …>` i puljer. Alle bygg og kontroller består, og fontvakten melder ingen fonter utenfor byggemappen og TeX-trærne.
3. `src/build_md_pdf.py` og `src/extract_visualprofile.py` kjøres på hver sin fil i en testmappe under `tmp/` og virker.
4. Etter byggene finnes ingen nye `kw*`-mapper i systemets midlertidige mappe, og `tmp/` har ingen gjenværende arbeidsmapper.
5. Et bygg med `--keep-build` lar mappen ligge i `tmp/` og skriver ut stien. Et bygg som feiler med vilje (f.eks. en kilde med ugyldig LaTeX i en testfil under `tmp/`), etterlater ingen mappe.

**Estimert innsats:** 21 min

**Løsning (2026-11-13):**

- **`src/project_tmp.py`** (ny): `work_dir(prefix, keep=False)` lager en unik mappe under `<prosjektrot>/tmp/` og sletter den når blokken avsluttes, også ved feil. `mkdtemp(prefix)` lager en mappe som scriptet selv sletter. Prosjektroten finnes fra modulens plassering, ikke fra arbeidskatalogen.
- **De ni scriptene** bruker modulen i stedet for `tempfile`. `build_business_card.py`, `build_document.py` og `build_presentation.py` bruker `mkdtemp` med sin eksisterende `finally`-blokk og `--keep-build`. De seks andre bruker `work_dir`. Ingen av dem importerer `tempfile` lenger.
- **Rettelse av oppgaveteksten:** de tre scriptene med `mkdtemp` ryddet allerede opp i en `finally`-blokk, også ved feil. Fontfila ble altså ikke liggende igjen ved feil. Endringen gjelder bare hvor arbeidsmappen ligger.
- **Fontvakten** trengte ingen endring. Den godtar fonter fra arbeidsmappen, uansett hvor den ligger.
- **`tests/test_project_tmp.py`** (ny, 4 tester og én parametrisert test per script i `src/`): mappen lages under `tmp/`, slettes etter normal avslutning og etter et unntak, og beholdes med `keep=True`. Ingen script utenom `project_tmp.py` importerer `tempfile`, kaller `gettempdir()` eller skriver til `/tmp/`.
- **README:** ny konvensjon «Midlertidige filer», `tmp/` og `project_tmp.py` i mappeoversikten, og omtalen av byggemappene for profilmanualen og presentasjonen sier `tmp/`.

**Verifisering:**

1. `pytest --timeout=5`: 419 passed.
2. Alle 65 PDF-er bygget med `--force`: malgruppene i to kjøringer, de ansatte i fem puljer på fire. Ingen feil, alle kontroller besto, og CV-kontrollen ga 0 avvik i 20 filer. Fontvakten meldte ingenting. De nye PDF-ene ble sammenlignet med kopiene fra før endringen: alle 65 rendres piksel for piksel likt, med samme tekst og samme fonter, og alle er byte-like når dato og dokument-ID er blanket ut.
3. `src/extract_visualprofile.py` og `src/build_md_pdf.py` virket på en testfil under `tmp/`. Selvtesten i `src/check_document_pdf.py` ga «all 10 expected warnings fired».
4. Etter byggene var det 0 `kw*`-mapper i systemets midlertidige mappe og 0 arbeidsmapper igjen i `tmp/`.
5. `build_document.py --keep-build` la mappen i `tmp/kwdoc_…` og skrev ut stien. Et bygg med en udefinert LaTeX-kommando feilet med exitkode 1 og etterlot ingen mappe.

**Faktisk innsats:** 11m 13s (veggklokke) mot 21 min estimert.

**Kobling:** følger opp regelen om å ikke skrive utenfor prosjektet (CLAUDE.md, 2026-11-13). Henger sammen med T14 (byggeskriptet brukes i verifiseringen) og T17 (som kjører alle byggene på nytt og kan gjøres etter denne).

**Berørte filer:** `src/project_tmp.py` (ny), `src/build_business_card.py`, `src/build_document.py`, `src/build_presentation.py`, `src/build_profile_manual.py`, `src/build_cv_pdf.py`, `src/build_cv_business_cards.py`, `src/build_md_pdf.py`, `src/check_document_pdf.py`, `src/extract_visualprofile.py`, `tests/test_project_tmp.py` (ny), `README.md`, `TASKS.md`

### T19 [x] Mindre og mer enhetlige bilder i CV-ene, med felles logobibliotek

CV-mappene i `cvs/` har 82 bilder på til sammen 7,4 MB: 16 foto (6,4 MB) og 66 logoer (1,0 MB). Status per 2026-11-13:

- Fotoet settes inn som 60 × 74 mm (`PHOTO_W`, `PHOTO_H` i `src/build_cv_pdf.py`). Byggeskriptet beskjærer det rundt fokuspunktet og skalerer ned til høyst 1800 piksler bredt. Mange originaler er 2000 piksler eller mer på den lengste siden.
- Fire foto er PNG med gjennomsiktighet (Brage Wichstrøm, Dee Roberts, John Hagen, Thomas Ax Gulbrandsrød), og to av dem er de største filene (1,0 og 1,2 MB). To foto har lav oppløsning: Brage Wichstrøm (367 × 463) og Dee Roberts (521 × 568). Tre foto har EXIF-data, men ingen har GPS-posisjon.
- Logoene vises på inntil 34 × 13 mm (`LOGO_MAX_W`, `LOGO_MAX_H`), med minst 200 dpi (`LOGO_MIN_DPI`). Den største er Brattvaag Electro på 381 KB (1006 × 441). De fleste er under 40 KB.
- Samme kunde ligger i flere versjoner hos flere personer: Sunlit Sea hos seks, Equinor og NTNU hos fem hver, Kongsberg, Enersky, Inatur og Thales hos tre eller fire, og Cisco, Elporten, Lilbit og Skandia Energi hos to. Fire logoer har for lav oppløsning (`cvs/AVVIK.md`): Sunlit Sea, NTNU, Lilbit og AppearTV.

Brukeren har bestemt (2026-11-13): felles logobibliotek ja, en delt mappe er ikke et problem. Fotoene beholder nok oppløsning til annen bruk, nemlig 1200 piksler i bredden på utsnittet.

**Endringer:**

1. **`src/normalize_cv_images.py`** (ny) behandler bildene i `cvs/*/images/` og `cvs/logos/`:
   - **Foto:** JPG med kvalitet 85, sRGB, uten metadata (EXIF, ICC). Gjennomsiktighet flates ut mot hvit bakgrunn. Bildet skaleres ned så det største utsnittet med fotorammens forhold (60:74) blir 1200 piksler bredt, altså inntil 1200 × 1480 for et stående foto. Bilder skaleres aldri opp. Fila beskjæres ikke, så byggeskriptet fortsatt kan flytte utsnittet med `photo_focus`. Bytter fotoet fra `.png` til `.jpg`, rettes henvisningen i CV-fila.
   - **Logoer:** PNG-er og JPG-er skaleres ned så de er høyst 700 × 260 piksler (rundt 500 dpi på største plass). PNG beholder gjennomsiktighet og lagres optimalisert. SVG røres ikke.
   - **Kjøremåte:** standard er tørrkjøring som viser per fil gammel og ny størrelse og pikselmål, og flagger filer som krymper til under 30 % av opprinnelig filstørrelse for inspeksjon. Originalene endres bare med `--apply`. Skriptet er idempotent: en ny kjøring på behandlede bilder endrer ingenting.
2. **Felles logobibliotek `cvs/logos/`:** én fil per kunde, `cvs/logos/<kunde>.<ext>`, med kundenavn i små bokstaver og bindestrek (`equinor.svg`, `sunlit-sea.png`). Helst SVG. Ellers velges den beste versjonen blant CV-ene, og der logoen har for lav oppløsning, hentes en bedre versjon fra kundens nettside, helst SVG. CV-ene viser til logoen som `../logos/<kunde>.<ext>`. Logoer som bare én person bruker, flyttes også dit, så alle logoer ligger på ett sted. `images/` i hver CV-mappe har da bare fotoet. Varianter av samme kunde (Kongsberg, Kongsberg Digital og Kongsberg Satellite Services) holdes som egne logoer.
3. **Byggeskriptet og CV-kontrollen** godtar logoer i `../logos/`: `src/check_cv_md.py` (mønsteret for logostier, og sjekken av at fila finnes), `src/build_cv_pdf.py` (relative stier fra CV-mappa), og endringssjekken i `src/build_employee_cvs.py` (`cvs/logos/` blir en innfil for alle CV-ene).
4. **Kontroll av nye bilder** i `src/check_cv_md.py`: avvik for foto som ikke er JPG, foto med utsnitt over 1200 piksler i bredden eller med metadata, og logoer over 700 × 260 piksler. Da holder formatet seg når utviklerne oppdaterer CV-ene selv.
5. **`cvs/AVVIK.md`:** punktet om logoer med lav oppløsning oppdateres etter hva som ble erstattet. De to fotoene med lav oppløsning står fortsatt som noe konsulenten selv må rette.
6. **Dokumentasjon:** CV-veiledningen (`deliverable/visualprofile/cv/README.md`) beskriver bildeformatet: foto som `images/foto.jpg` i inntil 1200 piksler i bredden på utsnittet, og logoer fra `cvs/logos/`, med regel for navn og størrelse. Mappeoversikten i README får `cvs/logos/`. Malen og eksempelet i `deliverable/visualprofile/cv/` beholder sine egne bilder.

**Verifisering:**

1. Tørrkjøringen viser bare forventede endringer, og ingen fil er flagget uten at den er sett på. Etter `--apply` gir en ny tørrkjøring ingen endringer.
2. `uv run python src/check_cv_md.py cvs/*/*.md`: 0 avvik.
3. `pytest --timeout=5` består, med nye tester for normaliseringen (skalering, utflating av gjennomsiktighet, fjerning av metadata, ingen oppskalering, idempotens) og for logostier i `../logos/`.
4. Alle 18 CV-er og visittkort bygges med `--force`, i puljer på tre og én kommando om gangen. CV-PDF-ene sammenlignes med kopier tatt før endringen: samme antall sider og samme tekst på hver side. Bare foto og logoer får se annerledes ut. Et utvalg sider rendres til PNG og kontrolleres visuelt: fotoene er like skarpe som før, og de nye logoene er minst like gode.
5. Bildene i `cvs/` er til sammen under 3 MB, og ingen logo finnes i mer enn én fil. (Grensen var først 2 MB. Den kom fra et overslag med 900 piksler i fotoutsnittet. Med de 1200 pikslene brukeren valgte, blir et portrett på kvalitet 85 alene 150–300 KB, og tørrkjøringen ga 2,9 MB. Grensen ble rettet under løsningen, 2026-11-13.)

**Estimert innsats:** 55 min

**Løsning (2026-11-13):**

- **Logobiblioteket `cvs/logos/`:** 42 logoer, én fil per kunde, fra 66 filer i personmappene. Der samme kunde fantes i flere versjoner, ble den beste valgt etter et kontaktark: ny Appear-logo i stedet for den gamle lilla, Equinor i rødt og liggende, NTNU uten slagord, Sunlit Sea i sort på gjennomsiktig bakgrunn (de andre hadde gul bakgrunn eller var 200 × 200), ordmerket til Enersky, og versjonene med høyest oppløsning av Cisco, Kongsberg, Lilbit og Skandia Energi. Navnevarianter ble slått sammen (`appeartv` → `appear-tv`, `skandiaenergi` → `skandia-energi`, `thales-norway` → `thales`). Kongsberg, Kongsberg Digital og Kongsberg Satellite Services er egne logoer. Alle 83 logohenvisninger i CV-ene peker nå til `../logos/<kunde>.<ext>`, og `images/` har bare fotoet. **Det ble ikke hentet logoer fra nett:** alle fire logoene med for lav oppløsning hadde en god nok versjon hos en annen person.
- **`src/normalize_cv_images.py`** (ny): foto blir JPG med kvalitet 85, sRGB, uten metadata, gjennomsiktighet lagt på hvitt, og skalert ned så utsnittet med rammens forhold (60:74) er 1200 piksler bredt. Logoer får trimmet kanter og skaleres ned til høyst 700 × 260 piksler. Standard er tørrkjøring, `--apply` endrer filene, og `--self-test` sjekker reglene på syntetiske bilder i `tmp/`. To justeringer etter første tørrkjøring: kvaliteten senkes trinnvis ned til 70 når et foto ellers ville blitt større enn originalen (to foto var hardere komprimert enn kvalitet 85), og skalerte PNG-logoer lagres med palett på 256 farger, fordi fullfarge gjorde noen logoer opptil fire ganger større. Etter første `--apply` endret en ny kjøring tre logoer til, fordi skaleringen myker opp kantpikslene. Skriptet trimmer derfor én gang til etter skaleringen, og er nå idempotent.
- **Resultat:** 40 av 59 filer endret. Fire foto gikk fra PNG til JPG (henvisningene ble rettet automatisk), tre mistet EXIF-data, og åtte ble skalert ned. Bildene i `cvs/` gikk fra 7,4 MB (82 filer) til 2,9 MB (58 filer).
- **`src/check_cv_md.py`:** ny funksjon `image_info` leser format, mål og metadata fra PNG- og JPEG-hodene uten Pillow, som ikke er i prosjektmiljøet. For CV-ene i `cvs/` gir kontrollen avvik for logoer utenfor `../logos/`, foto som ikke er JPG, foto med utsnitt over 1200 piksler eller med metadata, og logoer over 700 × 260 piksler. Malen og eksempelet i `deliverable/visualprofile/cv/` beholder sine egne bilder i `images/`, og reglene gjelder ikke dem. Grensene ligger som konstanter i kontrollen og brukes også av normaliseringen.
- **`src/build_employee_cvs.py`:** `cvs/logos` er innfil for alle CV-ene, så en endret logo bygger CV-ene som bruker den på nytt.
- **Tester:** `tests/test_cv_images.py` (ny, 13 tester): `image_info` på håndlagde PNG- og JPEG-hoder, reglene for foto og logo i `cvs/`, unntaket for malen, at hver logo finnes i én fil og ingen ligger i personmappene, og selvtesten til normaliseringen kjørt i en egen uv-prosess.
- **Dokumentasjon:** `cvs/AVVIK.md` har et nytt fellespunkt om logobiblioteket og et om de to fotoene med lav oppløsning (Brage Wichstrøm, ca. 155 dpi, og Dee Roberts, ca. 220 dpi). Sju punkter om logoer med lav oppløsning og foto i PNG er fjernet eller rettet. CV-veiledningen beskriver mappestrukturen med `cvs/logos/`, fotoformatet, logoreglene og normaliseringen. README har logobiblioteket i mappeoversikten, et avsnitt om `normalize_cv_images.py` og de nye kontrollreglene.

**Verifisering:**

1. Tørrkjøringen viste bare forventede endringer. De 13 flaggede filene (fem foto og åtte logoer som krympet under 30 %) ble kontrollert visuelt før og etter. Det var ingen synlige kompresjonsfeil i nærbilder av ansiktene, og ingen fargefeil i logoene etter palettkonverteringen. Etter `--apply` og rettelsen av trimmingen gir en ny tørrkjøring «0 would change».
2. `check_cv_md.py cvs/*/*.md`: 18 filer, 0 avvik. CV-eksempelet består også.
3. `pytest --timeout=5`: 358 passed (færre enn før, fordi testene som går over filene i `cvs/` har to personer og 27 logofiler mindre).
4. Alle 18 CV-er og visittkort er bygget med `--force`, i seks puljer på tre og én kommando om gangen, uten feil. Mot kopiene fra før har alle samme antall sider, og 17 har identisk tekst på hver side. Hos Dee Roberts er ordene like, men ett avsnitt på side 4 brytes annerledes, fordi Asolvi-logoen ved siden av fikk litt andre mål etter trimmingen. Første og andre side hos John Hagen og Sindre Stephansen er rendret og sammenlignet visuelt: fotoene er like skarpe, og logoene sitter på samme sted og har samme størrelse. Et anslag for største størrelse gir alle logoer minst 205 dpi, så byggeskriptet melder ingen logo med lav oppløsning.
5. Bildene i `cvs/` er på 2,91 MB, under grensen på 3 MB. Ingen logo finnes i mer enn én fil.

**Faktisk innsats:** 13m 50s (veggklokke) mot 55 min estimert. Ingen logoer måtte hentes fra nett, og de fleste valgene kunne gjøres ut fra ett kontaktark.

**Kobling:** bygger på T12 (CV-ene i Markdown) og T16 (CV-ene i `cvs/`). Henger sammen med T14 (`build_employee_cvs.py`).

**Berørte filer:** `src/normalize_cv_images.py` (ny), `src/check_cv_md.py`, `src/build_cv_pdf.py`, `src/build_employee_cvs.py`, `cvs/logos/` (ny), `cvs/*/images/`, `cvs/*/*.md`, `cvs/AVVIK.md`, `tests/test_cv_images.py` (ny), `deliverable/visualprofile/cv/README.md`, `README.md`, `TASKS.md`
