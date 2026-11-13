# KodeWorks – Prosjektkontekst

## Hva er dette

Prosjektet er en samling av bakgrunnsmateriale, analyser og leveranser om **KodeWorks AS** og de andre KodeWorks-selskapene. Prosjektet drives av Eirik Larsen. Hensikten er å bygge opp et strukturert kunnskapsgrunnlag — selskapsstruktur, bakgrunn, nøkkeltall, styringsdokumenter — og å produsere leveranser (rapporter, notater, presentasjoner) basert på dette grunnlaget.

Prosjektet er **git-delt** på tvers av flere maskiner (Windows Git Bash, WSL2, Linux). All varig kunnskap må ligge i filer som følger med checkoutet — se «Ingen historikk-fil» og «Auto-memory brukes ikke» under.

Se `TASKS.md` for åpne oppgaver og `ARCHIVE.md` for løste.

---

## Konsernet

Fire selskaper med KodeWorks-navnet er registrert i Brønnøysundregisteret (verifisert 2026-09-22 mot `data.brreg.no`). **Ingen av dem er registrert som del av et formelt konsern** i Brreg (`erIKonsern: false` på alle) — de opererer i praksis som en gruppe, men det er ikke en registrert mor/datter-struktur.

| Selskap | Org.nr. | Adresse |
|---|---|---|
| **KodeWorks AS** | `820 478 452` | Fjordgata 30, 7010 Trondheim |
| **KodeWorks Trondheim AS** | `920 478 492` | Fjordgata 30, 7010 Trondheim |
| **KodeWorks Eiendom AS** | `920 478 506` | Fjordgata 30, 7010 Trondheim |
| **KodeWorks Oslo AS** | `922 070 709` | Grønnegata 10, 0350 Oslo |

Merk at `820 478 452`, `920 478 492`, `920 478 506` og `922 070 709` er **fire forskjellige selskaper** — ikke forveksle. Ved oppslag: prøv proff.no først, deretter Brreg som fallback (`https://data.brreg.no/enhetsregisteret/api/enheter?navn=<navn>`). Bruk «konsern» kun uformelt — ikke som juridisk påstand i leveranser før faktisk konsernstruktur er bekreftet.

**Eirik Larsen** (kontaktperson)

- E-post: eirik.larsen@kodeworks.no
- Telefon: +47 416 70 269

Bruk disse verdiene direkte i leveranser og skjemaer — ikke sett `[SETT INN]`-placeholdere og ikke be brukeren fylle inn manuelt. Verifiser mot Brreg / proff.no ved tvil.

---

## Filer og mapper

```
<prosjektrot>/
├── CLAUDE.md                  – dette dokumentet (prosjektkontekst for AI)
├── README.md                  – oversikt over repo og verktøy
├── background/                – kildedokumenter, analyser, notater
│   ├── new/                   – innkommende filer som ikke er klassifisert ennå
│   └── visualprofile/Fonts/   – profilfonten Non Natural Grotesk med lisenser (brukes av alle byggene)
├── cvs/                       – de ansattes CV-er i Markdown, én mappe per person; oppdateres med commits
├── deliverable/               – ferdige dokumenter (rapporter, notater, presentasjoner; .docx genereres ved behov med Pandoc)
├── src/                       – scripts og kjørbare hjelpeverktøy (build_all.py bygger alle PDF-er)
├── tests/                     – pytest-tester
├── data/                      – lokale arbeidsdata, git-ignorert (drive/: hentet fra Google Drive)
├── tmp/                       – midlertidige filer og arbeidsmapper, git-ignorert
├── secrets/                   – OAuth-filer (git-ignorert, per maskin)
└── .claude/skills/            – prosjekt-skills
```

---

## Arbeidsregler

- **Les disse først:** Ved oppstart av en oppgave, eller når kontekst mangler, les `README.md`, `CLAUDE.md`, `TASKS.md` og `ARCHIVE.md`. README beskriver scripts og dataflyt, TASKS viser åpne oppgaver, og ARCHIVE inneholder løste oppgaver med løsningsnotat. Søk i ARCHIVE før du starter en ny oppgave for å unngå dobbeltarbeid.
- **Ingen historikk-fil brukes.** Dette prosjektet har bevisst valgt bort en `historikk.md` / `history-log.md` / kronologisk logg-fil. Naboprosjektene `../fjordgata30`, `../stotte` og `../sure-d61` bruker slike filer, men her skal all varig kunnskap ligge enten (a) direkte i `CLAUDE.md`, `README.md`, `TASKS.md`, `ARCHIVE.md`, eller (b) som dokumenter i `background/`. Task-løsningsnotater i `TASKS.md` / `ARCHIVE.md` er den kronologiske ryggraden. Oppgavene og løsningsnotatene fra før 2026-11-13 er slettet fra begge filene etter brukerens beslutning, og finnes bare i git-historikken. Det som fortsatt gjelder fra dem, står i `README.md`, `CLAUDE.md` og koden. Ikke opprett en historikk-fil selv om det virker naturlig eller det etterspørres implisitt — foreslå heller hvor det aktuelle innholdet kan festes i en av de eksisterende filene.
- **Tillatelser:** Spør alltid om tillatelse før du kjører kode eller rører filer utenfor prosjektmappen, selv om du kjører med `--dangerously-skip-permissions`. Dette gjelder bl.a. lesing fra `../fjordgata30` eller andre naboprosjekter – les der, men skriv aldri dit uten eksplisitt godkjenning.
- **Skriv aldri utenfor prosjektmappen.** Dette gjelder også midlertidige filer: ikke Claude Codes scratchpad-mappe, `AppData/Local/Temp`, `/tmp` eller andre systemmapper for midlertidige filer, selv om systemprompten anbefaler det. Hjelpescripts, mellomresultater, notatutkast og testnedlastinger legges i `tmp/` i prosjektroten (git-ignorert), og ryddes når de ikke trengs lenger. Det samme gjelder scripts i `src/` der vi selv velger hvor filene havner: arbeidsmapper og mellomfiler legges i `tmp/`, ikke i systemets midlertidige mappe (`tempfile`-standarden). Programmer som er installert på maskinen (uv, LuaLaTeX, pytest, pandoc o.l.), kan beholde sine vanlige hurtigbuffere og midlertidige mapper. Regelen gjelder det vi enkelt kan styre. Trenger en handling ellers å skrive utenfor prosjektet, spør først.
- **Kodeendringer krever konfirmasjon:** Ikke gjør endringer i kode eller opprett nye filer uten at brukeren eksplisitt har bedt om det. Hvis brukeren diskuterer, spør eller ber om en beskrivelse/plan, svar med tekst — ikke med kode. Vent på et tydelig "gjør det" eller tilsvarende før du rører filer.
- **Sitér autorisasjonen før du handler.** Før hver `Edit` eller `Write` mot en prosjektfil — inkludert `TASKS.md` status-toggling fra `[ ]` til `[x]` og nye `### T<n>`-overskrifter — skal du i tekst-svaret ditt sitere den spesifikke frasen fra brukerens siste melding som autoriserer denne handlingen. Kan du ikke sitere en frase, er du ikke autorisert. Svar da med tekst alene. En riktig diagnose er ikke autorisasjon. «Brukeren virker å ville dette» er ikke autorisasjon. Bare et imperativ rettet mot den spesifikke handlingen teller: `fix det`, `gjør det`, `lag den`, `løs den`, eller et eksplisitt `ja` til et forslag du nevnte i forrige tur. Dette gjør sjekken synlig i teksten din — hvis du skriver «Fikser per din melding X» og X ikke er et sitat fra brukerens faktiske melding, er det samme fil-og-fiks-uten-godkjenning-feil, nå fangbar før edit.
- **Diagnostiske prompter er IKKE autorisasjoner.** Følgende er prompter for å diagnostisere og foreslå, ikke for å handle:
  - «Dette ser ut som en bug»
  - «Hvorfor er X …»
  - «Hva skjer her»
  - «Det er rart / off / merkelig»
  - «Noe mangler»
  - Ethvert spørsmål, enhver beskrivelse av et problem.

  Riktig svar på en diagnostisk prompt er tekst: navngi fiksen i én linje, spør «file and fix?», vent på et ja. Aldri file, aldri rediger kode, aldri marker en task som gjort i samme tur som diagnosen.
- **Følg konvensjoner skrevet denne sesjonen.** Ikke avvik fra en regel eller konvensjon som er skrevet inn i `CLAUDE.md`, `README.md`, eller et task-løsningsnotat i den pågående samtalen. Ingen «one-off pragmatisk» unntak, selv når avviket er beleilig eller ser tryggere ut. Hvis regelen viser seg å være feil: løft konflikten til brukeren og spør før du avviker — ikke stille bypasse og notere det som et «one-off» i et løsningsnotat.
- **Estimer tidsforbruk før du starter:** Før du iverksetter en oppgave, vurder kompleksiteten og gi et grovt estimat på tidsforbruk (f.eks. "dette tar ~30 sekunder" eller "dette er en stor operasjon som kan ta 5–10 minutter"). Hvis estimatet er over ~2 minutter, krev eksplisitt konfirmasjon fra brukeren før du starter — selv om du allerede har fått en generell "gjør det". Unntak: en filed task med `**Estimert innsats:**` som brukeren ber deg løse — da er estimatet allerede bekreftet (se «Task-utførelse»).
- **Task-dokumentasjon:** Når en oppgave er løst, dokumenter løsningen under oppgavens kontekst-seksjon i `TASKS.md` og marker statusen som `[x]`. Ikke bare oppdater status uten å notere hva som ble gjort og hvilke filer som ble opprettet/endret.
- **Task-nummerering:** Før du oppretter en ny task, finn høyeste eksisterende T-nummer på tvers av **begge** `TASKS.md` og `ARCHIVE.md`: `grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1`. Bruk neste ledige nummer. Et nummer gjenbrukes aldri, også når eldre tasks er slettet fra filene.
- **Task-sortering:** Tasks i `TASKS.md` og `ARCHIVE.md` skal alltid være sortert stigende på T-nummer. Når du oppretter en ny task, sett den inn på riktig plass i rekkefølgen – ikke legg den til sist uten å sjekke nummeret. Subtasks (`T<n>.<m>`) sorteres under sin hovedtask.
- **Ikke referer til task-IDer i prosa:** Skriv aldri «T<n>-avtalen», «per T<n>», «under T<n>» eller lignende — verken i chat, i beskrivelser i `TASKS.md`, i `deliverable/` eller i dokumenter i `background/`. Task-IDer er interne anker og hører kun hjemme (a) som `### T<n>`-overskrift på selve tasken, (b) i **Berørte filer**- og **Kobling**-blokkene på tasken, (c) i commit-meldinger, og (d) i kodekommentarer der en spesifikk beslutning må siteres. Alle andre steder: navngi konseptet.
- **Arkivering av tasks:** Løste tasks flyttes fra `TASKS.md` til `ARCHIVE.md` kun når brukeren eksplisitt ber om det. Aldri arkiver på eget initiativ. Søk alltid i `ARCHIVE.md` før du starter en oppgave for å unngå dobbeltarbeid.
- **Ikke start tasks automatisk:** Begynn aldri på en task uten eksplisitt instruksjon fra brukeren i den pågående samtalen. Når en task er ferdig, vent på neste instruksjon – ikke velg og begynn på den neste tasken på egenhånd.
- **README-oppdatering:** Vurder alltid om `README.md` må oppdateres som del av å løse en oppgave. Nye scripts, endrede filnavn, endret filstruktur eller nye avhengigheter skal alltid reflekteres i README.
- **PDF-konvertering:** Bruk alltid `pdftotext` (eller tilsvarende CLI-verktøy) via Bash for å konvertere PDF til tekst. Bruk aldri Read-verktøyet side for side på PDF-filer – det er svært kostbart og mister strukturert tekst. Eksempel: `pdftotext -layout "filnavn.pdf" - > filnavn.txt`
- **Python-kommando (plattformavhengig):** På **Windows**: bruk alltid `uv run python` – aldri `python3` eller `uv run python3` (disse feiler med «Python ble ikke funnet»). På **Linux/macOS**: `python3` fungerer direkte. `uv run python` fungerer på begge plattformer og er trygt å bruke uansett. Bruk Bash-verktøyet, ikke PowerShell, for Python-kjøring.
- **Plattform og skallmiljø varierer:** Brukeren jobber på tvers av Windows (Git Bash, Cygwin, WSL2) og Linux på ulike maskiner. Anta aldri et bestemt operativsystem, skallmiljø eller filsti. Unngå Cygwin-spesifikke stier (`/cygdrive/c/...`). Bash-verktøyet er satt til prosjektmappen — bruk `cd` kun når strengt nødvendig, og bruk da relative stier eller stier som fungerer i Git Bash/Linux (`/c/dev/...` el. absolutte Linux-stier). Memory-filer (`.claude/projects/.../memory/`) er lokale per maskin og følger ikke med git-commits — skriv aldri maskin- eller OS-spesifikke antakelser til memory.
- **Spør før suboptimal fremgangsmåte:** Hvis du ser at du er i ferd med å gjøre noe på en ineffektiv måte (mange trinn, store tokenkostnader, omveier), stopp og spør brukeren om de er sikre på at de vil at du skal fortsette slik – selv om du kjører med `--dangerously-skip-permissions`.
- **Ikke bruk multiple choice-dialogen (`AskUserQuestion`).** Still spørsmål som vanlig tekst i svaret, og vent på brukerens svar i neste melding.
- **Kode og parametere på engelsk:** All kode skrives på engelsk – variabelnavn, funksjonsnavn, kommentarer i koden, og CLI-argumenter/flagg til scripts (f.eks. `--from`, `--to`, `--limit`, ikke `--fra`, `--til`, `--antall`). Dokumentasjon (README-er, veiledningene til malene, skill-oversikten) skrives på engelsk. Leveranser og rapporter til brukere/interessenter (CV-er, brev, presentasjoner, notater i `background/`) skrives på norsk. Mappenavn i dette prosjektet er også engelske (`background/`, `deliverable/`, `src/`).
- **Scripts samles i `src/`:** Alle Python-scripts og andre kjørbare hjelpescripts legges alltid i `src/`-mappen, uavhengig av hvilken del av dokumentasjonen de tilhører. Scripts skrives med stier relative til prosjektroten og kjøres alltid derfra (`uv run python src/navn.py`). Ikke legg scripts i undermapper som `background/`, `deliverable/` o.l.
- **Dato-prefix på filer i `background/`:** Alle nye filer som legges i `background/` skal ha dato-prefix på formen `YYYY-MM-DD_beskrivelse.ext` (f.eks. `2026-09-22_notat_konsernstruktur.md`). Dato = dokumentets egen dato (utstedt / skrevet / sendt), ikke dagen filen ble arkivert. Hvis dokumentets dato er ukjent: bruk dagens dato som best-known fallback og noter usikkerheten i filkroppen. Eksisterende filer uten dato-prefix skal omdøpes ved neste berøring.
- **`background/new/` er en ren innboks — ingen filer opprettes DIT.** `background/new/` inneholder kun ubehandlete originaler (typisk `.docx`, `.pdf`, `.pptx`, `.xlsx`, bilder) som brukeren har droppet inn. Når du konverterer en fil i innboksen til `.md`, skal `.md`-filen skrives **direkte til `background/`** — aldri til `background/new/` først. Undermappestrukturen speiles: `background/new/cvs/foo.docx` → `background/cvs/YYYY-MM-DD_foo.md`. Opprett undermappen i `background/` hvis den ikke finnes. Ikke bruk en to-stegs «konverter til innboks, deretter flytt»-tilnærming — det er en gammel feilkilde og etterlater alltid rot.
- **Ved sesjonsstart:** sjekk om `background/new/` (eller noen `background/new/<undermappe>/`) inneholder ubehandlete filer. Hvis ja: list dem og spør brukeren om de skal prosesseres — ikke prosessér på eget initiativ.
- **"Nye oppgaver"-seksjonen i TASKS.md:** Når `TASKS.md` leses, sjekk alltid om `## Nye oppgaver` inneholder uprosesserte punkter (bullet-linjer). Hvis det finnes slike punkter: spør brukeren om de skal prosesseres. Prosessering betyr å konvertere hvert punkt til en nummerert T-task med beskrivelse og slette punktet fra seksjonen.
- **Git og gh er ALDRI tillatt uten eksplisitt tillatelse i den aktuelle samtalen:** Kjør aldri `git`, `gh` eller andre kommandoer som invoker git (inkludert scripts som kaller git internt, og sammensatte Bash-kommandoer der git inngår noe sted – `pwd && git ...` er like forbudt som ren `git ...`). Dette gjelder **alle** operasjoner, også «harmløse» lese-kommandoer: `git status`, `git diff`, `git log`, `git branch`, `git show`, `git ls-files`, `git rev-parse`, `git worktree list`, `gh pr list`, `gh issue view` osv. Før hver Bash-kommando, sjekk eksplisitt om `git` eller `gh` inngår noe sted – hvis ja, stopp og spør om tillatelse, selv om du trenger info raskt. Det er kombinasjonen «trygg lese-kommando» + «rask svar trengs» som er autopilot-fellen. Trenger du info som kunne kommet fra git: bruk Read/Glob/Grep, eller spør brukeren om å lime inn output.
- **Ikke konverter til docx automatisk:** Generer aldri `.docx` av en leveranse (verken via Pandoc eller annet) som del av en task – heller ikke når et eksisterende docx-vedlegg endres og «burde regenereres for konsistens». Markdown-kilden er leveransen; konvertering til docx skjer **kun når brukeren eksplisitt bestiller det**. Ved tvil: nevn at docx ikke er regenerert i sluttoppsummeringen, så brukeren selv kan bestille det.
- **Pandoc er valgt konverteringsverktøy** for `.docx`, `.pptx` og `.pdf`. Bruk pandoc-kommandoer direkte (`pandoc input.md -o output.docx` osv.) når brukeren bestiller konvertering. Ikke foreslå alternative pipelines (LibreOffice, Word-COM, weasyprint, etc.) uten at pandoc-veien er testet og avvist først. PDF-konvertering krever en separat engine (pdflatex/xelatex/wkhtmltopdf) – hvis ingen er tilgjengelig, lever docx og overlat PDF-konvertering til bruker i Word/Office.
- **Installasjon av systempakker eller verktøy krever eksplisitt tillatelse:** Kommandoer som installerer eller endrer systemnivå (`tlmgr install`, `apt install`, `pip install --system`, `pip install --user`, `npm install -g`, `choco install`, `winget install`, `uv tool install`, `cargo install`, `gem install` osv.) krever alltid eksplisitt godkjenning i den aktuelle samtalen — også når et verktøy mangler for å fullføre den etterspurte oppgaven. Stopp og spør. Å installere «bare det som mangler» er nettopp autopilot-fellen i «Spør før suboptimal fremgangsmåte»-regelen.
- **`rm` og andre destruktive operasjoner krever eksplisitt tillatelse for filer jeg ikke selv har opprettet i den aktuelle samtalen.** Før hver `rm`, `mv --force`, `> fil` (overskriv) eller lignende: sjekk om filen er noe jeg selv har generert i denne sesjonen. Hvis ikke — stopp og spør. Signaler på at filen er brukerens (og skal ikke røres): filstørrelse eller endringsdato som avviker fra min egen output, filnavn som ikke matcher min pipeline, filer som «virker rare å ha» i mappen. Å rydde bort «noe som ikke skulle vært der» er autopilot-fellen: brukeren kan ha lagt inn filen med hensikt. Å slette er verre enn å la ligge — spør heller.
- **Orgnr hentes fra proff.no:** Når du trenger et selskaps organisasjonsnummer, slå opp på **proff.no** først (f.eks. `https://www.proff.no/selskap/<firmanavn>/...`). Hvis proff.no ikke er tilgjengelig (WebFetch feiler pga. JavaScript-rendring, anti-bot eller lignende), bruk **Brønnøysundregisteret** som fallback via `https://data.brreg.no/enhetsregisteret/api/enheter?navn=<firmanavn>`. Hvis heller ikke Brreg gir treff, rapportér til brukeren i chat i stedet for å gjette eller la feltet stå tomt.
- **Rydd opp etter agent-invokasjoner:** Ved tasks som invokerer `Agent`-tool (særlig med `isolation: "worktree"`), sjekk alltid på slutten at `.claude/worktrees/agent-*`-mappene er ryddet. Claude Code-harness rydder normalt automatisk etter agents som ikke gjorde endringer, men det feiler av og til. Når task er ferdig og agentbidrag er konsolidert tilbake til hovedbranchen: list `.claude/worktrees/` og slett gjenstående `agent-*`-mapper relatert til tasken. Dokumentér i task-løsningsnotatet at oppryddingen er gjort.
- **`Agent`-tool krever eksplisitt tillatelse per spawn.** Hvert `Agent`-kall oppretter en git-worktree, som uavhengig bryter git-regelen over; agenten bruker også tokens utenfor din synlige kontekst. Spør før hver spawn — ingen stående godkjenninger, ingen «read-only»-unntak. Hvis brukeren gir tillatelse, teller opprydding av `.claude/worktrees/agent-*`-mappen etterpå fortsatt som en git-operasjon og må også godkjennes individuelt. **Eneste unntak:** tasks med en `**Arbeidsmetode: agent-orkestrering**`-seksjon — se «Agent-orkestrerte tasks» under.
- **Agent-tool oppretter alltid worktrees – planlegg for opprydding:** `Agent`-tool i Claude Code (denne harness-versjonen) oppretter en worktree per spawn uansett, også uten at `isolation: "worktree"` settes eksplisitt. `isolation`-parameteren har bare `"worktree"` som mulig verdi, så det er ingen «ikke-worktree»-modus tilgjengelig. Dette gjelder også agenter som bare leser filer. Konsekvens: hver gang `Agent` invokeres, må det planlegges for opprydding etter at tasken er ferdig (Claude Code-harnessen rydder ikke alltid pålitelig). Etter sesjonen er avsluttet og pid er død, kan worktrees ryddes med: `git worktree repair` → `git worktree unlock` → `git worktree remove --force` → `git branch -D` (og `git worktree prune` til slutt). For Cygwin/Windows-mismatch: kjør oppryddingen i Git Bash, ikke Cygwin.
- **Bildegrid i rapporter (universelt format):** Bilder i rapporter og notater skal presenteres i **Markdown pipe-tabeller** — ikke raw LaTeX (`\begin{minipage}`) og ikke raw HTML (`<div style="grid">`). Grunn: pipe-tabeller rendrer likt i **alle tre** relevante formater — pandoc → PDF (via xelatex), pandoc → DOCX og VS Code Markdown preview. Raw LaTeX fungerer bare i PDF; raw HTML fungerer bare i VS Code. Standard-oppsett per grid-rad: header-rad med bilder (`![](../background/xxx.jpg)`), separator med `:---:` for sentrering, body-rad med *italic caption*. To bilder per rad gir grid-lignende layout og passer 4–6 bilder per side. Aksepter at tabellrammer vises i noen formater — kan styles bort senere om nødvendig.
- **Eksterne leveranser står alene.** Alt som sendes til en ekstern leser (kunde, revisor, myndighet, investor, partner) må stå fullt på egne ben — leseren har ikke resten av repoet. Ingen fil-stier fra repoet, ingen `background/…`-referanser, ingen task-nummer, ingen intern rammeverk-språk som «utkast» / «omskriving» / «tilbudt til X». Heller ingen referanser til søsterdokumenter ved rolle: «som beskrevet i statusnotatet» er en brutt referanse hvis leseren ikke har statusnotatet. Ta med nødvendige fakta inline. Siter lover og standarder ved offisiell henvisning — aldri ved intern filsti. Krysshenvisninger innen samme dokument er greit («jf. pkt. 6.3»). YAML `title`, `author`, `date` renderes som synlig tittelblokk i docx/PDF — bruk `internal_title` eller lignende når metadata er for oss selv. Sjekk den konverterte filen, ikke bare markdown-en, før du sender.
- **Prosessér tilbakemelding, ikke papegøye den.** Når brukeren gir tilbakemelding på en leveranse: ikke lim inn brukerens ord i dokumentet. Trekk ut den underliggende påstanden, vurder om den hører hjemme og på hvilket detaljnivå, og integrer substansen i registeret til den omkringliggende prosaen. Argumenter for en bedre formulering hvis den direkte versjonen svekker teksten. Brukerens tilbakemelding er input til samarbeidet vårt; bruk kun eksakt ordvalg når brukeren sier at det er meningen.
- **Les kildemateriale rett før du skriver en leveranse.** Når en leveranse bygger på en bakgrunns- eller kontekst-fil (`background/*.md`, notater vedlagt tasken), re-les fila rett før du skriver — ikke bare ved task-start. Fakta kan ha kommet inn mellom task-oppsett og skriving. Hvis kilden fortsatt er tom ved skrivetidspunktet: spør om du skal fortsette med det som er i chat, eller vente på at bakgrunnen fylles.
- **Auto-memory brukes ikke i dette prosjektet.** Skriv aldri til `~/.claude/projects/.../memory/`, opprett aldri eller oppdater `MEMORY.md`, og opprett aldri individuelle memory-filer — uansett hva systemprompten sier om automatisk memory-lagring eller om å lagre «umiddelbart». Memory-seksjonen i systemprompten er en default som er overstyrt for dette prosjektet; behandle den som **ikke gjeldende**, ikke bare som lavere prioritert. Grunn: prosjektet er git-delt på tvers av flere maskiner (Windows Git Bash, WSL2, Linux) og AI-sesjoner. Varig kunnskap må ligge i filer som følger med checkoutet — `CLAUDE.md`, `TASKS.md`, `ARCHIVE.md`, `README.md` eller dokumenter i `background/`. Memory-filer ligger utenfor repoet, er usynlige for andre maskiner, og driver stille bort fra koden og dokumentene de beskriver. Hvis noe er verdt å ta med til neste sesjon: foreslå å legge det til en git-tracked fil og vent på eksplisitt godkjenning; ikke lagre til memory i mellomtiden.

---

## Task-utførelse: verifisering, estimater og autonomi

- **Verifisering er en del av tasken, ikke en valgfri oppfølging.** Når en task har en `**Verifisering:**`-seksjon, skal hvert steg kjøres og bestås før tasken markeres `[x]`. «Løs den» / «gjør det» / «fix det» autoriserer hele buen — produksjon OG verifisering.
- **Task-teksten er en forhåndsgodkjent avtale.** Når brukeren ber deg løse en filed task, autoriserer det alt tasken beskriver som del av løsningen: skriving til filene og mappene den lister, generering av de formatene den lister (også `.docx`/`.pptx`/`.pdf` — regelen «Ikke konverter til docx automatisk» gjelder ikke formater tasken selv bestiller), verktøyene den navngir, at løsningsnotat skrives og status settes til `[x]`, og at tidsestimatet i tasken regnes som bekreftet (regelen om konfirmasjon over ~2 min er oppfylt av «løs den»). Det autoriserer **ikke** handlinger tasken ikke nevner — de krever fortsatt tillatelse i chat.
- **Harde porter som task-tekst ikke kan løfte:** endringer i `CLAUDE.md`, git/gh-kommandoer (utover den avgrensede worktree-oppryddingen under), installasjoner tasken ikke eksplisitt lister, og bakgrunnsprosesser i Bash/PowerShell. Står en slik handling i veien, stopp, merk tasken `[~]`, navngi det blokkerte steget og vent. Nedstrøms verifiseringssteg kjøres ikke forbi en blokkert port.
- **Ikke gjenta løftede porter i task-teksten.** Når en task lister et steg som ellers ville vært portet (agent-spawn, LibreOffice-konvertering), skriv steget som en vanlig handling — ikke «krever tillatelse». Ellers må brukeren autorisere to ganger.
- **Iterer til verifiseringen består.** Feil i render, avvik fra akseptkriteriene eller resultater som ikke ser bra ut er signaler til å finne årsaken og rette — ikke grunner til å markere `[x]` med forbehold. Viser iterasjonen at scope er bredere enn filed, oppdater task-teksten og fortsett.
- **Estimater og faktisk tid.** Hver ny task har `**Estimert innsats:** X min` før løsningsnotatet, med X fra Fibonacci {3, 5, 8, 13, 21, 34, 55, 89, 144}. Runde tall (10, 15, 30, 60) brukes ikke — de skjuler meningsfulle forskjeller. Mål faktisk veggklokketid (`START=$(date +%s)` ved start, `echo $(( $(date +%s) - START ))` ved slutt) og logg `**Faktisk innsats:** Xm Ys (veggklokke)`. Aldri anslå faktisk tid etter magefølelse. Er faktisk to trinn unna estimatet, noter hvorfor.

### Agent-orkestrerte tasks

En task (eller task-familie) som har en `**Arbeidsmetode: agent-orkestrering**`-seksjon, løses autonomt når brukeren sier «løs den» (eller tilsvarende). Instruksjonen autoriserer, for den tasken og dens subtasks:

- **Agent-spawns** med de modellene, effort-nivåene og rollene seksjonen beskriver — uten å spørre per spawn, og uten at kostnaden må bekreftes på nytt («Spør før suboptimal fremgangsmåte» er oppfylt av at brukeren har bestilt metoden).
- **Agenter som kjører i bakgrunnen og varsler når de er ferdige.** Stopp-regelen for «Running in the background» gjelder Bash/PowerShell-kall, ikke `Agent`-spawns. Vent på varslene; ikke poll. Agentene selv følger samme shell-regler (foreground, under 2 min per kommando).
- **Opprydding av agentenes worktrees**, avgrenset til disse git-kommandoene mot `.claude/worktrees/agent-*` og tilhørende `agent-*`-brancher: `git worktree list`, `git worktree unlock`, `git worktree remove --force`, `git worktree prune`, `git branch -D`. Ingen andre git-kommandoer.
- **Verktøy og installasjoner seksjonen lister**, f.eks. LibreOffice for rendering av `.docx`/`.pptx` til PDF for visuell kontroll (pandoc-veien er testet og avvist for dette formålet: pandoc kan ikke rendre Word/PowerPoint-layout). Fonter installeres aldri: bygg bruker fonter som filer fra repoet eller fra TeX Live, aldri fonter som er installert i operativsystemet.

Orkestratoren er ansvarlig for at resultatet er konsolidert, verifisert visuelt (render til PDF/PNG og les med Read-verktøyet) og dokumentert i løsningsnotatet før tasken markeres `[x]`. Mellomresultater fra workere ligger i egne mapper og slettes eller beholdes slik tasken angir.

---

## Klart språk i chat

Hvert svar i chat skal kunne leses på én gjennomlesning av en leser som ikke har lest task-teksten, filene i repoet eller tidligere svar i samtalen.

1. **Hele setninger.** Ingen telegramstil eller sammenpressede fagfraser der flere udefinerte begreper er stablet i én setning.
2. **Hvert avsnitt står på egne ben.** Viser et avsnitt til «de tre tilfellene», «funnet over» e.l., gjenta hva det er i avsnittet selv.
3. **Forklar fagbegreper første gang de brukes i et svar** — i vanlig norsk, med begrepet i parentes om det hjelper.
4. **Spørsmål som ber brukeren bestemme noe, må gjenta konteksten beslutningen gjelder.** Må brukeren scrolle opp eller åpne en fil for å svare, er spørsmålet feil formulert.
5. **Maks to `kode`-spenn per setning**, og ingen filstier eller linjenumre midt i prosaen — samle referanser i en avsluttende `Referanser:`-linje.
6. **Lengde er ingen grunn til å komprimere.** Klart språk er ofte lengre; det er prisen for lesbarhet. Ber brukeren om kortere svar, gi et kortere svar i klart språk.
7. **Teknisk dybde er opt-in.** Filstier, funksjonsnavn og rå identifikatorer brukes når brukeren ber om det i samtalen («vis koden», «hvilken fil»).

Les svaret på nytt før det sendes, med en leser uten kontekst i tankene. Kan ikke den leseren følge et avsnitt, skriv det om.

---

## Python — kjøremiljø og regler

Dette prosjektet bruker primært Python. Standard-oppsett: **`uv run python`** (fungerer på både Windows og Linux, ingen manuell venv-aktivering nødvendig). Scripts kan deklarere avhengigheter inline via **PEP 723 script metadata**, slik at `uv run script.py` installerer dem i et brukerlokalt ephemeral env — ingen systeminstallasjon kreves.

**Prosjektmiljø og venv per OS:** Felles avhengigheter og dev-verktøy (`pytest`, `pytest-timeout`) ligger i `pyproject.toml` + `uv.lock`; nye legges til med `uv add` (`--dev` for verktøy), aldri med `pip install`. Scripts med PEP 723-blokk kjøres med `uv run src/navn.py` (ellers ignoreres blokken); scripts uten blokk med `uv run python src/navn.py`. Venv er ikke portabel mellom OS: Windows bruker `.venv`, WSL2/Linux bruker `.venv-linux` (via `UV_PROJECT_ENVIRONMENT=.venv-linux` i `~/.bashrc`). Opprett, flytt eller slett aldri en venv-mappe for et annet OS enn det du kjører på. Detaljer: README «Python setup».

**Prosjekt-skills** ligger i `.claude/skills/<navn>/SKILL.md`, med oversikt i `.claude/skills/README.md`. Ny skill: legg den til i oversikten.

**Test-oppsett med pytest:**

- Bruk `pytest` for tester. Alle tester ligger i `tests/` og kjøres fra prosjektroten.
- **Hver `pytest`-invokasjon MÅ inkludere `--timeout=N`**, og hver `pytest`-kall via Bash-tool MÅ sette `timeout=5000` (ms) på selve Bash-kallet. Ingen unntak. En hengende test låser Bash-wrapperen og trigger background-recovery-loop. Default: `pytest --timeout=3` (tre sekunder er nok for de fleste unit-tester). To uavhengige tak: `pytest-timeout` dreper én treg test, Bash-timeout dreper hele skallet hvis noe annet henger. Løft per-test-taket kun når en test er legitimt treg, og løft da Bash-timeout tilsvarende.
- Hvis `pytest-timeout` mangler i miljøet: spør brukeren om å `pip install pytest-timeout` — ikke kjør uten tak.
- **En test som ikke tester noe skal ikke finnes.** Ingen `pytest.skip`, ingen `skipif`, ingen test der alle assertions kan hoppes over ved kjøretid. En skippet test rapporterer verken pass eller fail — den er en sjekk som stille sluttet å gjelde, og suiten viser fortsatt grønt. Hvis en sjekk bare gjelder noen tilfeller: parametrisér over akkurat de tilfellene. Hvis en test trenger en forutsetning: konstruer forutsetningen. Hvis en sjekk har blitt meningsløs: slett den.

**Pre-flight før HVER Bash/PowerShell-kommando** (gå gjennom alle fem, i rekkefølge, hver gang):

1. **`run_in_background`-parameter.** Er den i tool-kallet? Hvis ja — FJERN den. Sett den aldri, ikke engang til `false`. Fraværet er det som garanterer foreground.
2. **`timeout`-parameter.** Er den i tool-kallet? Hvis ja — fjern den (default 120000 ms er riktig) eller bekreft at verdien er `<= 120000`. Verdier over 120000 auto-backgrounder kallet.
3. **Kommandotekst.** Inneholder den `&` (på slutten, ikke `&&`), `Start-Job`, `Start-Process`, `nohup`, `disown`, `screen`, `tmux`, `jobs`, `bg` eller andre detach-mekanismer? Hvis ja — skriv om.
4. **Forventet varighet.** Forventer du at kommandoen tar mer enn 2 minutter? Hvis ja — STOPP. Snevr inn (én test-fil, `-k`-filter, ett script, `--maxfail=1`) eller be brukeren kjøre det selv og lime inn output. Ikke løft timeout som alternativ.
5. **`Monitor`-tool.** Er du i ferd med å kalle `Monitor`? Ikke gjør det. Formålet er å overvåke background-tasks, som du ikke skal opprette.

Hvis et Bash/PowerShell-resultat nevner en task-ID eller sier "Running in the background" av noen som helst grunn: STOPP umiddelbart. (Gjelder ikke `Agent`-spawns i agent-orkestrerte tasks — se «Agent-orkestrerte tasks».) Ikke fortsett som om kallet lyktes. Drep tasken med `TaskStop`, rapportér til brukeren, og re-kjør pre-flight fra steg 4 — reduser scope, ikke prøv igjen med andre flagg på samme overdimensjonerte kommando. Bakgrunnsprosesser hogde CPU/RAM på brukerens PC i tidligere sesjoner til Claude Code måtte drepes.

**Les filen før du rører den. Hver gang.** Ved oppstart av en task, og igjen før hvert skrive-kall, les den AKTUELLE innholdet i hver fil du er i ferd med å endre. Handle aldri på det filen inneholdt tidligere i sesjonen, på det et tool-output viste tidligere, eller på det du husker å ha skrevet. Brukeren jobber i samme repo samtidig, og en fil kan endres mellom to av dine kommandoer. Gjelder spesielt hardt ved gjenoppretting fra backup, re-applisering av en fiks, eller overskriving med en versjon du selv laget — det føles trygt og er det som stille ødelegger andres arbeid.

---

## Dokumentkonvertering (parsing og generering)

Kildedokumenter i `background/` kommer i mange formater. Standard-verktøykjede:

**PDF → tekst (parsing):**

Bruk alltid `pdftotext` via Bash — aldri Read-verktøyet side for side (svært kostbart og mister struktur).

```bash
pdftotext -layout "background/foo.pdf" background/foo.txt
```

`-layout` bevarer kolonner og tabeller rimelig godt. Drop det hvis layouten produserer artefakter. Regenerer tekst-ekstraksjonen når PDF-en endres.

**DOCX / PPTX / ODT / RTF / HTML → Markdown (parsing):**

Bruk Pandoc.

```bash
pandoc "background/new/foo.docx" -o background/new/foo.md --wrap=none
```

**XLSX → data:**

Bruk `openpyxl` fra Python for lesing/skriving av celledata og formler:

```python
# /// script
# dependencies = ["openpyxl"]
# ///
from openpyxl import load_workbook
wb = load_workbook("background/foo.xlsx", data_only=False)  # False = les formler, True = les cached verdier
```

For enkel tabell-utpakking til Markdown: `pandoc` støtter `xlsx` direkte som input, men resultatet er ofte rotete for komplekse ark — foretrekk `openpyxl` + manuell strukturering.

**PDF med innebygde bilder:** `src/extract_visualprofile.py` pakker ut bilder og vektorgrafikk (se README «Document conversion»). Et enklere mønster finnes i `../sure-d61/scripts/extract_pdf_images.py` (les der, skriv aldri dit). JP2 må konverteres til PNG (`convert file.jp2 file.png`) for at Markdown-visere skal vise dem.

**Innkommende filer i `background/new/`:**

Ved sesjonsstart, sjekk om `background/new/` inneholder ubehandlete filer. Hvis ja: list dem og spør brukeren om de skal prosesseres — ikke prosessér på eget initiativ. Prosessering:

1. Konverter til Markdown per pipelinen over (PDF → `pdftotext`, DOCX/PPTX → `pandoc`, bilder beholdes som-er).
2. Legg til en kort preamble på toppen med kildefilnavn og dokumentdato (om kjent).
3. Rename til `YYYY-MM-DD_beskrivelse.md` (dato = dokumentets egen dato, ikke arkiveringsdato).
4. Flytt til `background/` (eller passende undermappe).
5. Fjern midlertidig `.txt` fra `pdftotext` — bare `.md` beholdes.
6. Behold original binær kun hvis den er autoritativ (signerte PDF-er, signerte kontrakter, presentasjoner som skal videre distribueres). Ellers erstatter `.md` originalen.

**Konverterte `.md`-filer må være selvstendige:** Etter konvertering fra `.docx`/`.pdf`/`.xlsx` må resultatet stå på egne ben. Ikke legg til YAML `source:`-felt som peker på originalen, og ikke skriv «konvertert fra `foo.docx`» eller «kildedokumentet inneholder en EMF-tabell». Originalen slettes ofte etter konvertering, så enhver levende referanse blir et brutt peker.

**Markdown → DOCX (generering):**

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.docx
```

Ved tabeller: tabellrammer og kolonnebredder er dårlig som default. For pen output: se `src/format_docx.py` (fra søster-prosjektet `../sure-d61/scripts/format_docx.py` — bruker `python-docx` til å legge til 0.5 pt grå rammer og sette kolonnebredder per fil). Kopiér inn ved behov med `TABLE_WIDTHS_BY_STEM`-dict tilpasset dette prosjektet.

**Markdown → PDF (generering):**

Krever TeX Live med `lualatex`. Fontene er filer fra TeX Live, ikke systemfonter, så kommandoen gir samme resultat på Windows, WSL2 og Linux. Standard-kommando:

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.pdf \
  --pdf-engine=lualatex \
  -V documentclass=scrartcl \
  -V geometry:margin=1in \
  -V lang=nb \
  -V mainfont=texgyretermes-regular.otf \
  -V mainfontoptions="BoldFont=texgyretermes-bold.otf, ItalicFont=texgyretermes-italic.otf, BoldItalicFont=texgyretermes-bolditalic.otf" \
  -V monofont=DejaVuSansMono.ttf \
  --number-sections=false
```

| Flagg | Effekt |
|---|---|
| `--pdf-engine=lualatex` | Unicode-tegn (`≥`, `–`, `€`), OpenType-fonter, og norske orddelingsmønstre lastet ved kjøring. xelatex-formatet har ingen bokmålsmønstre og deler stille med engelske. |
| `-V documentclass=scrartcl` | KOMA-Script article-klasse — renere typografi enn default `article`. |
| `-V geometry:margin=1in` | 1 tomme marg rundt. |
| `-V lang=nb` | Norsk bokmål: orddeling og typografiske konvensjoner. |
| `-V mainfont=texgyretermes-…` | Brødtekst i TeX Gyre Termes (Times-klone fra TeX Live), med fet og kursiv som filer. |
| `-V monofont=DejaVuSansMono.ttf` | Mono-font for kodeblokker fra TeX Live. Default (`Latin Modern Mono`) mangler box-drawing-tegn (├, ─, └, │). |

KodeWorks' visuelle materiale (profilmanual, CV, presentasjon, dokumenter og brev) bygges med egne scripts i `src/` som laster profilfonten fra den lisensierte font-fila i repoet. Se README «Visual profile».

**Mermaid-diagrammer i rapporter:**

Hvis rapporten har `` ```mermaid ``-blokker: bruk `mermaid-filter` (Node-basert Pandoc-filter, gir PNG-render av hvert diagram):

```bash
pandoc deliverable/rapport.md -o deliverable/rapport.docx -F mermaid-filter.cmd
```

Fra Git Bash på Windows må `.cmd`-suffikset være med (Pandoc gjør eksakt filnavn-oppslag og respekterer ikke `PATHEXT`). Fra PowerShell/CMD eller Linux/macOS: `-F mermaid-filter` (uten `.cmd`). Installasjon og Chromium-oppsett: se README.

**Nummer-formatering (NBSP) i PDF-tabeller:**

Norske tusen-separerte tall (`18 570 858`) kan brekke over linjeskift i smale PDF-tabellkolonner. Erstatt space med non-breaking space (NBSP, `U+00A0`) mellom sifre før konvertering. Regex-basert helper kan legges i `src/nbsp_numbers.py` (mønster: `../sure-d61/scripts/nbsp_numbers.py`).

**Bildegrid i rapporter:** Bruk **Markdown pipe-tabeller** — ikke raw LaTeX (`\begin{minipage}`) og ikke raw HTML (`<div style="grid">`). Pipe-tabeller rendrer likt i pandoc → PDF, pandoc → DOCX og VS Code Markdown preview. Raw LaTeX fungerer bare i PDF; raw HTML fungerer bare i VS Code. Standard: header-rad med bilder (`![](../background/xxx.jpg)`), separator med `:---:` for sentrering, body-rad med *italic caption*. To bilder per rad passer 4–6 bilder per side.

---

## Batch-transformasjoner: dry-run + backups

Når du skriver et script som transformerer mange filer med regex/mønster-erstatning, må default være en ikke-destruktiv modus: skriv til `<navn>.cleaned.<ext>`-søsken-filer, eller til en separat output-mappe. Overskriv originalene kun etter at en dry-run har printet per-fil word-count / line-count deltas og et menneske har bekreftet at ingen er overraskende. Enhver enkeltfil som krymper til under ~70 % av original størrelse er et rødt flagg til den er inspisert — en for bred regex kan stille trunkere innhold. Konvensjonen finnes fordi et lignende script i et søsterprosjekt kappet ~90 % av innholdet i to filer på grunn av en signatur-start-regex som matchet Markdown horisontale linjer.

---

## Kompaktering

- Ikke auto-kompaktér samtaler. Si fra når det nærmer seg tid for det.
- Etter en kompaktering, ikke automatisk hopp til tasks og begynn å løse dem — vent på ny instruksjon.

---

## Tone og format

- Alle dokumenter og leveranser skrives på norsk (bokmål). Dokumentasjonen av repoet (README-er, veiledningene til malene) skrives på engelsk.
- Rapporter som skal til eksterne parter formateres i Markdown slik at de ser bra ut konvertert til `.docx` med Pandoc
- Vær konkret og faktabasert – ikke prøv å "selge inn" noe med tomme ord, men la dokumenterte fakta tale for seg
- **Markdown hard linebreak i signaturer, adresser og metadata-blokker.** Enkel newline i Markdown kollapser til én space når fila rendres (VS Code preview, pandoc → PDF/DOCX, GitHub-visning). Signaturer, adresse-blokker, dokument-headere med `**Bold-label:**`-linjer og lignende blir da til én sammenklumpet setning. Bruk backslash `\` på slutten av hver ikke-siste linje i logisk sammenhengende blokker — eller blank linje for full paragrafbrytning. Sjekk før hver `Write`/`Edit` som produserer signatur, header, datotabell kort format eller adresse. Unntak: leveranser som skal *limes inn i webskjema* (ikke rendres) — vurder blank linje istedenfor backslash slik at rå tekst ikke viser `\`-tegn i skjemaet.
- **Ikke navngi brukeren i genererte dokumenter.** `TASKS.md`, `ARCHIVE.md` og notater i `background/` leses som upersonlig referansemateriale — framtidige lesere kan være andre maskiner, andre AI-sesjoner eller en revisor som gjennomgår prosjektet. Skriv «brukeren», «prosjektleder» eller omform passivt heller enn å bruke «Eirik» eller initialene «EL» som subjekt. Unntak: (1) denne `CLAUDE.md`, som er brukerens egne instruksjoner og navngir brukeren for lesbarhet; (2) leveranser til eksterne parter (`deliverable/`, brev, rapporter) der brukeren står som avsender og skal signeres med fullt navn. I chat er «du» greit — regelen gjelder varige filer, ikke samtaler.
