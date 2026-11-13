# ARCHIVE

Løste tasks flyttet fra `TASKS.md` etter eksplisitt beskjed fra brukeren. Søk her før du starter en ny task for å unngå dobbeltarbeid.

## Tasks

### T1 [x] Sammenfatte KodeWorks fra kodeworks.no

Les kodeworks.no og lag et bakgrunnsnotat om selskapet — hva de gjør, tjenester, lokasjoner, teknologier, kunder, verdier. Legges i `background/` med dato-prefix.

**Berørte filer:** `background/2026-09-22_kodeworks_om_selskapet.md`

**Resolution:** WebFetch mot kodeworks.no ga oversikt over tjenester (utvikling, team, AI), lokasjoner (Grønnegata 10 Oslo, Fjordgata 30 Trondheim), teknologistack (React/Next/Vue, Flutter/Swift/Kotlin, TypeScript/Java/Python/C++, Docker/K8s/AWS/GCP/Azure) og en lang liste referansekunder inkl. DNB, Fremtind, Ruter, Statkraft, Thales, Kongsberg, reMarkable, Avinor. Nettsiden oppgir ikke etableringsår, ansattantall eller grunnleggere — henvises videre til andre kilder i `background/`.

### T2 [x] Prosjekt- og kundeoversikt fra CV-er

Gå gjennom alle CV-er i `background/cver/` og trekk ut hvilke prosjekter KodeWorks har levert og for hvilke kunder, med tidspunkt. Produsér to samle-dokumenter i `background/`:

- `projects.md` — prosjekter (navn, kunde, periode, kort beskrivelse, hvem som deltok)
- `customers.md` — kunder (navn, bransje, kort om samarbeidet)

**Berørte filer:** `background/projects.md`, `background/customers.md`, alle `background/cver/*.md`

**Resolution:** Alle 15 CV-er lest og syntetisert sammen med `background/2026-09-22_prosjektoversikt.md`. `customers.md` gruppert per kunde med bransje, engasjement-summary og KW-utviklere. `projects.md` sortert i tre kronologiske bolker: aktive (2024–nå), 2020–2023, og 2015–2019 («KodeWorks som produkt-selskap»-perioden pre-2018). Interne startups (Sunlit Sea, EnerSky, LilBit) og interne produktfase (Hako, Sentry, Fjordgata30.no, Vipps-pinball) skilt ut fra ordinære kundeoppdrag. Historisk overgang fra produkt- til konsulentmodell rundt 2018 dokumentert.

### T3 [x] KodeWorks' medlemskap i ITKO (IT Konsulentselskaper i Oslo)

Les om ITKO / IT Konsulentselskaper i Oslo. KodeWorks er medlem, og er sammenlignbart i størrelse med de andre medlemmene. Dokumenter i `background/` hva ITKO er, formålet, hvem som er medlemmer, og hva KodeWorks får ut av medlemskapet.

**Berørte filer:** `background/2026-09-22_itko_medlemskap.md`

**Resolution:** WebFetch mot itko.no ga medlemskapskriteriene (15–150 ansatte, Østlandet, kjernekompetanse i skreddersydd programvareutvikling, ingen eksisterende medlemmer kan motsette seg opptak). Formålet er faglig/sosialt nettverk der medlemsselskaper kan sette sammen team på tvers for komplekse oppdrag. Konkret medlemsliste er ikke publisert på nettsiden — henvist til `hei@itko.no` for oppdatert oversikt. KodeWorks-fordeler beskrevet: kapasitetsbuffer, referanser, felles anbud.

### T4 [x] KodeWorks-startups: Sunlit Sea og EnerSky

KodeWorks har vært med å grunnlegge Sunlit Sea og EnerSky. Les selskapenes egne nettsider (`sunlitsea.no`, `enersky.no`) for hva de gjør, og bruk proff.no / Brreg for å avklare den formelle eierrelasjonen til KodeWorks-selskapene. Beskriv resultatet i `background/YYYY-MM-DD_startups.md`.

**Berørte filer:** `background/2026-09-22_startups.md`

**Resolution:** WebFetch mot sunlitsea.no + enersky.no + Brreg-oppslag på begge. **Sunlit Sea AS** org.nr. `922 633 924`, stiftet 2019-03-25, adresse Grønnegata 10 Oslo (samme som KodeWorks Oslo). Grunnleggere: Per Lindberg (CEO) og Eirik Larsen (CFO/CDO). **EnerSky AS** org.nr. `934 009 940`, stiftet 2024-08-15, adresse Fjordgata 30 Trondheim (samme som KodeWorks AS + Trondheim + Eiendom). Ingen av selskapene er registrert som formell datter i Brreg (`erIKonsern: false`). Prosjektlogg med KW-konsulenters bidrag over tid dokumentert per startup. Elporten identifisert som forgjenger til EnerSky (samme Elhub-domenekunnskap).

### T5 [x] LilBit / LilDog — historikk, sweat equity, eierandel

KodeWorks har utviklet for **LilBit** (produktnavnet er **LilDog**) siden 2019 gjennom sweat equity-avtaler — konsulentarbeid mot aksjer. Les online for hva LilBit / LilDog er, sammenstill KodeWorks' historikk med selskapet fra CV-er, `background/2026-09-22_prosjektoversikt.md` og andre kilder, og bruk proff.no / Brreg til å slå opp nåværende eierandel KodeWorks har i selskapet. Skriv resultatet i `background/YYYY-MM-DD_lilbit.md`.

**Berørte filer:** `background/2026-09-22_lilbit.md`

**Resolution:** WebFetch mot lilbit.no (redirect til lildog.com) ga produktinfo: GPS-tracker for kjæledyr, 50 000+ solgte enheter, LTE-M + NB-IoT + BLE, CEO Morten Sæthre, pris 499 NOK. KW-historikk sammensatt fra CV-er: Ørjan (10.2019–08.2020 fullstack Android/backend + 03.2023–03.2025 iOS Lildog) og Sindre (06.2020–08.2021 Android). Rebranding Tail it → Lilbit → Lildog dokumentert. **Eierandel ikke bekreftet** — Brreg-søk på «lilbit» ga bare LILBIT HOLDING AS (`989 246 062`, Sola — ikke driftsselskapet), og søk på «tail it» ga ingen treff på det aktuelle selskapet. Notert i deliverable at proff.no aksjonærinfo eller Skatteetatens aksjonærregister bør sjekkes for eksakt eierprosent.

### T6 [x] Eyasys AS — grunnlagt 2010, solgt ~2021, Mobil/Omvendt Voldsalarm for politiet

KodeWorks grunnla Eyasys AS i 2010 sammen med to andre gründere (1/3 aksjer hver). KodeWorks bygde selskapet og solgte seg ut ca. 2021. Kjerneleveransen var utvikling av **Mobil Voldsalarm** og **Omvendt Voldsalarm** for norsk politi — hele veien fra vag kravspesifikasjon til fullt integrert løsning. Løsningen ble senere lisensiert til Eyasys før KW solgte seg ut. Les online om Eyasys, om Mobil/Omvendt Voldsalarm, slå opp Eyasys på proff.no / Brreg for historikk, og skriv en samlet fortelling i `background/YYYY-MM-DD_eyasys.md`.

**Berørte filer:** `background/2026-09-22_eyasys.md`

**Resolution:** Brreg bekreftet EYASYS AS org.nr. `995 572 400`, stiftet 2010-04-30, adresse Fjordgata 30 Trondheim + kontor i Oslo, aktiv per 2026-09-22. WebFetch mot eyasys.no ga produkt-portefølje: Mobil Voldsalarm, Fotlenker (Geosatis), Secure Mobile Video, Eyasys MDM. Wikipedia-oppslag for Omvendt voldsalarm ga lovgrunnlag (strl. § 57 femte ledd — kontaktforbud med elektronisk kontroll) og virkemåte (GPS-fotlenke på gjerningsperson, sonevarsel til politiet). Mobil-voldsalarm-artikkelen på Wikipedia 404'et. Lisensmodell + KW-uttreden ~2021 dokumentert basert på brukerinput; eksakt salgsdato/-pris ikke offentlig og markert som «bør sjekkes internt».

### T7 [x] KodeWorks Eiendom — eiendom siden 2010 (Grønnegata 10 Oslo + Fjordgata 30 Trondheim)

**KodeWorks Eiendom AS** har vært i eiendomsbransjen siden 2010. Kjøpte og rehabiliterte Grønnegata 10 (Oslo-kontoret) — nå coworking-space for KodeWorks + likesinnede selskaper. Har også en stor brygge i Trondheim på Fjordgata 30 — se `../fjordgata30` for det aktive rehabiliteringsprosjektet der. Skriv en samlet oversikt over eiendomsengasjementet i `background/YYYY-MM-DD_eiendom.md`.

**Berørte filer:** `background/2026-09-22_eiendom.md`

**Resolution:** Basert på Brreg-data for KodeWorks Eiendom AS (`920 478 506`, adresse Fjordgata 30 Trondheim) + kunnskap om Grønnegata 10 som Oslo-kontor og delt adresse med KodeWorks Oslo AS + Sunlit Sea AS. Fjordgata 30-delen sammenfattet fra `../fjordgata30/CLAUDE.md`: gammel brygge under rehabilitering til minilager, rammesøknad levert 12.05.2026, tilskudd fra Kulturminnefondet (750k), Byantikvaren (500k), Enova, UNI, med aktiv TBRT-relasjon. MVA-strategi (hybrid modell, Alternativ D) med estimert 5–6 MNOK refusjon i byggefasen kort dokumentert med henvisning til `../fjordgata30/forretningsplan/` for full detalj. Kjøpstidspunkt og totalinvestering for Grønnegata 10 markert som «bør hentes fra egne regnskaper».

### T8 [x] Presentasjon til ITKO-arrangement 22.09.2026 (KodeWorks vertskap)

KodeWorks er vert for ITKO-arrangement i Grønnegata 10 den 22. september 2026 kl 16. Lag en presentasjon på **ca. 15 minutter** der KodeWorks presenterer seg selv og ønsker deltakerne velkommen. Formelt program etter dette inneholder tallpresentasjon fra Marcus, og eventuelle andre medlem-innlegg.

**Bakgrunnsmateriale (allerede i `background/`):**

- `2026-09-22_kodeworks_om_selskapet.md`
- `customers.md`, `projects.md`
- `2026-09-22_startups.md`
- `2026-09-22_lilbit.md`
- `2026-09-22_eyasys.md`
- `2026-09-22_eiendom.md`
- `2026-09-22_itko_medlemskap.md`

**Merk om tidspress:** Arrangementet er 22. september 2026 kl 16 — samme dag som denne tasken opprettes.

#### T8.1 [x] Slide-skjelett med titler og punkter

Lag en `.md`-fil som legger ut slidene for presentasjonen med tittel + bullet-punkter per slide. Innhold-forslag:

- Velkomst + presentasjon av lokalet (Grønnegata 10 som coworking / KodeWorks Oslo-kontor)
- Kort om KodeWorks: fire selskaper (AS, Trondheim, Eiendom, Oslo), tjenester, størrelse
- Historikk: 2010 → i dag, overgang fra produktfirma til konsulentfirma i 2018
- Portefølje-glimt: utvalgte referansekunder (DNB, Equinor, reMarkable, Kongsberg, Statkraft m.fl.)
- Startups vi har vært med å bygge: Sunlit Sea, EnerSky, LilDog (sweat equity-modellen)
- Eiendomsdelen: Grønnegata 10 + Fjordgata 30 brygge-rehabilitering
- Praktisk info om kveldens program

**Berørte filer:** `deliverable/2026-09-22_itko_presentasjon.md`

**Resolution:** Skjelettet ble strukturert som 13 slides à ~1 min for å treffe 15-min-vinduet med litt luft: (1) Velkommen, (2) Program for kvelden, (3) Kort om KodeWorks, (4) Fire selskaper (tabell m/orgnr), (5) Historisk tidslinje 2010–2024, (6) Tjenester, (7) Teknologistack, (8) Kunder — gruppert per bransje, (9) Startups vi har bygget (Eyasys, Sunlit Sea, EnerSky, LilDog), (10) Eiendom (Grønnegata 10 + Fjordgata 30), (11) Hvorfor vi er med i ITKO, (12) Kveldens formelle program, (13) Takk. Frontmatter satt for Pandoc (title, subtitle, author, date). Én slide per `# H1`. Enkelte formuleringer beholdt i peer-to-peer-tone (ikke sales), inkludert humor-referansen til Marcus' 15/17-tips fra invitasjonen. Klart for utfylling og visuell profilering i T8.2.

#### T8.2 [x] Fullfør presentasjonen med talking points og visuell profil

Bygg videre på skjelettet fra T8.1:

- Fyll ut hver slide med konkret innhold (tall, eksempler, formuleringer).
- Opprett et separat talking-points-dokument (`deliverable/2026-09-22_itko_talepunkter.md`) med utfyllende tekst per slide — det Eirik faktisk sier når hver slide vises. Talking points refererer til slide-nummer/tittel, men er ikke synlig i selve presentasjonen.
- Sørg for at hovedfilen kan konverteres til pen PDF med Pandoc (`--pdf-engine=xelatex`) og at output er visuelt konsistent med KodeWorks' profil (farger, fonter, layout) — sjekk kodeworks.no for referanse.
- Vurder beamer-tema eller egendefinert Pandoc-template. Eventuelt custom LaTeX-header for farge/font.

**Berørte filer:** `deliverable/2026-09-22_itko_presentasjon.md`, `deliverable/2026-09-22_itko_talepunkter.md`, `deliverable/2026-09-22_itko_presentasjon.pdf`.

**Resolution:** KW-profilen ble hentet fra kodeworks.no via curl mot Next.js CSS-chunk: fargepalett `#B6FF9E` (kwgreen accent), `#254333` (dark green), `#35664C` (medium green), `#E8E7E6` (off-white), pluss mørk bakgrunn `#0F1613`. Original font Natural Grotesk er ikke fri; substituert med Inter (installert via TeX Live). Presentasjonen bruker beamer-tema **metropolis** med `titleformat=smallcaps, progressbar=frametitle, block=fill`, og overstyrer alle relevante `\setbeamercolor`-slots til KW-paletten via YAML `header-includes`. Genererer 14-siders 16:9 PDF (1 tittel + 13 slides) med `pandoc <src>.md -t beamer --pdf-engine=xelatex -o <out>.pdf`. Talepunkter i separat fil med detaljert tekst per slide og total tidsbudsjett-tabell (est. 12:40 av 15:00 tilgjengelig). PDF verifisert kompilert uten advarsler.

**Regenerering av PDF:**

```bash
pandoc deliverable/2026-09-22_itko_presentasjon.md \
  -t beamer --pdf-engine=xelatex \
  -o deliverable/2026-09-22_itko_presentasjon.pdf
```

**Resolution (T8 forelder):** Begge subtasks løst. Presentasjonen er klar for kveldens arrangement kl 16. Regenerer PDF med kommandoen over hvis kilde-`.md` endres.

**Tillegg – slettet:** Presentasjonen (`deliverable/2026-09-22_itko_presentasjon.md` og `.pdf`) er slettet etter brukerens beslutning, fordi den ikke hadde et byggescript og PDF-er ikke skal ligge i repoet uten å kunne genereres. Talepunktene (`2026-09-22_itko_talepunkter.md`) er også slettet.

### T9 [x] Visuell profil: konvertere alle dokumenter i `background/visualprofile/` til Markdown med bilder

`background/visualprofile/` inneholder KodeWorks' visuelle profil levert av designbyrået Neue (2021), brand assets, fonter og presentasjonsmaler. Alle dokumentfiler (PDF, DOCX, PPTX) skal konverteres til `.md` som replikerer originaldokumentet: bildene hentes ut til en egen mappe per fil, og `.md`-filen refererer til bildene i riktig rekkefølge sammen med teksten. Når alle filer er konvertert, vurderes dobbeltlagret informasjon (format-varianter av logo/symbol/mønster, overlappende dokumenter) i et eget steg.

**Omfang:**

- PDF: `Brand Guidelines.pdf` (19 s.), `030521_Kodeworks_ID_Elementer_Interiør_komplett.pdf` (79 s.), `210225_Kodeworks_StratPlatt.pdf` (27 s.), `Visittkort.pdf`, `Visittkort_alle.pdf`, fontlisensene (`Desktop-License-*.pdf`, `Web-License-*.pdf`)
- DOCX: `KW letterhead (print).docx`, `KW letterhead (screen).docx`, `Visittkort_alle.docx`, `Untitled document.docx`
- PPTX: `Kodeworks presentasjon.pptx`, `Kodeworks template 2022.pptx`, `Svarmatrise + AI KodeWorks.pptx`
- Rene bildefiler (SVG/PNG/JPG/EPS/EMF), `.ai`, `.afdesign`, `.zip` og `.webloc` er allerede assets og konverteres ikke, men inngår i dobbeltlagrings-vurderingen.

**Berørte filer:** `src/extract_visualprofile.py` (ny), `src/build_md_pdf.py` (ny), `src/compare_md_pdf.py` (ny), `README.md`, `CLAUDE.md`, `background/visualprofile/**/<dato>_<navn>.md` + `<dato>_<navn>_media/` + `<dato>_<navn>.pdf` (15 dokumenter), `background/visualprofile/**/<dato>_<navn>_image_text.md` (4 avskriftsfiler), slettet `background/visualprofile/Leveranse fra Neue/030521_Kodeworks_ID_Elementer_Interiør.pdf`

**Resolution:** Før konvertering ble den korte interiør-PDF-en (49 s., 290 MB) slettet etter brukerens beskjed, siden den komplette utgaven (79 s.) dekker den. Brukeren presiserte metoden: tekst skal ekstraheres (ikke én bildepeker per side), bilder hentes ut separat med `pdftotext`/`pdfimages`-type verktøy, og bildene kan nedskaleres kraftig fordi de bare skal brukes til fargevalg og sammenligning.

`src/extract_visualprofile.py` skrevet: PDF → `pdftotext` per side + `pdfimages` per side, dedup på PDF-objekt-ID, soft masks droppet, nedskalering til 25 % og JPEG q85. DOCX/PPTX → `pandoc --extract-media` + nedskalering. Første versjon brukte `pdfimages -png` og tok 1:43 for 19 sider; bytte til ukomprimert PPM som mellomformat ga 3 sek. Output legges ved siden av originalen med dato fra metadata.

Resultat (alle bildereferanser verifisert mot fil):

| Dokument | Dato | Sider | Unike bilder | Media |
|---|---|---|---|---|
| Brand Guidelines | 2021-05-31 | 19 | 13 | 388 KB |
| Interiør komplett | 2021-05-03 | 79 | 52 | 2,4 MB |
| Strategiplattform | 2021-02-25 | 27 | 1 | 8 KB |
| Visittkort / Visittkort_alle (PDF) | 2021-06-23 | 2 / 8 | 2 / 4 | 96 / 117 KB |
| Fontlisenser desktop / web | 2021-04-27 | 5 / 5 | 0 | – |
| KW letterhead print / screen, Visittkort_alle (DOCX), Untitled document | ukjent | – | 1 / 1 / 3 / 0 | < 50 KB hver |
| Kodeworks presentasjon, template 2022, Svarmatrise + AI (PPTX) | ukjent | – | 6 / 4 / 9 | 140 / 64 / 668 KB |

Kjente begrensninger:

- DOCX/PPTX fra Google-eksport mangler `docProps/core.xml`; dato-prefix er dagens dato (2026-11-11) og «ukjent» er notert i filen. Kan omdøpes hvis riktig dato blir kjent.
- I letterheads og `Visittkort_alle.docx` er bildene referert med `<img src>` (HTML-tabeller fra pandoc), ikke `![]()`. En tidligere versjon av dette notatet påsto at de ikke var referert — det var feil; referansesjekken så bare etter `![]()`.
- Originalene er ikke slettet. Vurdering av dobbeltlagret informasjon og hva som skal beholdes (og git-størrelse, ~491 MB i mappen) gjenstår som eget steg.

**Resolution (vektorgrafikk, tillegg):** Første runde hentet bare rasterbilder, fordi vektorgrafikk ikke er egne objekter i PDF-en, men tegneoperasjoner i sidens innholdsstrøm. Brukeren ba om at all vektorgrafikk ekstraheres som SVG som del av samme task. Løst med PyMuPDF `page.get_drawings()`: hver tegning (linjer, Bézier-kurver, rektangler, firkanter med fyll, strek, opasitet, even-odd, linjeender/-skjøter, stiplinger) skrives som `<path>`, og tegninger som overlapper eller ligger tett grupperes til én figur = én frittstående SVG (`vec_<sha1>.svg` i mediemappen, dedup på innhold, referert i `.md` per side etter bildene). SVG-ene inneholder bare vektorgrafikk — ikke tekst eller raster.

Gruppering kalibrert visuelt mot rendrede sider (side 2, 4, 9 og 15 i Brand Guidelines, side 7 i interiør-PDF-en, side 1 i visittkort):

- Bakgrunner (> 80 % av siden) og enkle rektangel-paneler (> 15 %) grupperes ikke, ellers smelter alt oppå dem sammen til én figur.
- Avstandsgrense mellom figurer: maks(2 pt, min(0,4 × høyden til den laveste, 50 pt)). Den relative delen holder outlinet navnetrekk «KodeWorks» samlet som én figur (fast 2 pt delte det i ti bokstaver); taket på 50 pt holder separate symboler og fargeprøver fra hverandre.
- Rektangel-orientering respekteres i path-data, slik at hull i nonzero-fyll (rammen rundt den hvite fargeprøven) ikke fylles.
- PyMuPDF sin innebygde `cluster_drawings()` ble forkastet: den hang over 2 min på interiør-PDF-en. Egen sweep + union-find bruker under 1 sek.

Resultat: Brand Guidelines 36 SVG-er, interiør 55, strategiplattform 19, visittkort 4 / 10, fontlisenser 11 / 12. Alle referanser verifisert mot fil. Gjenstående begrensninger: gradienter (shadings) og klippebaner er ikke med i `get_drawings()`, så figurer som er klippet i originalen kan vises større; nærliggende, men separate figurer (f.eks. visittkort-mockups side om side) kan havne i samme SVG.

**Tillegg – CV-mal 2023:** `background/visualprofile/CV-mal 2023.docx` ble lagt inn etterpå og konvertert med samme script → `background/visualprofile/2026-11-11_cv_mal_2023.md` + `2026-11-11_cv_mal_2023_media/` (3 bilder: profilbilde-plassholder, KW-logo, prosjektlogo-plassholder). Malen består av sammenslåtte tabellceller (forside med kontaktinfo, «Om», teknisk kompetanse; prosjektblokker; arbeidserfaring, utdanning, sertifiseringer) og bruksveiledning for hvordan malen fylles ut. Pandoc skriver tabellene med `rowspan`/`colspan` som HTML, så bildene er referert med `<img src>` i stedet for `![]()` — alle tre stiene verifisert. Fila mangler `docProps/core.xml`; dato-prefix er dagens dato selv om navnet tilsier 2023.

**Tillegg – PDF av alle .md og sammenligning med originalene:** Brukeren ba om PDF av alle 15 `.md`-filene og en sammenligning med originalene, med krav om at samme informasjon skal kunne leses ut (ikke eksakt layout). Nye scripts: `src/build_md_pdf.py` (Markdown → HTML → PDF med xelatex; SVG → PDF via PyMuPDF fordi `rsvg-convert` mangler) og `src/compare_md_pdf.py` (tekstdekning mot originalens tekst hentet uavhengig av pandoc, og antall rasterbilder). PDF-ene ligger ved siden av `.md`-filene.

Sammenligningen avdekket fire feil, alle rettet:

1. **Linjeskift `\r\r\n` i 14 av 15 `.md`-filer.** Pandoc og pdftotext skriver CRLF på Windows, og `write_text` gjorde hver `\n` om til `\r\n` én gang til. Pandoc tålte det ved direkte lesing, men Python (og andre verktøy) leser `\r\r\n` som to linjeskift, noe som brøt pipe-tabeller og HTML-tabeller. Rettet i `extract_visualprofile.py` (normaliserer til `\n`, skriver alltid LF); alle 15 filer regenerert, 0 CR verifisert.
2. **Topp- og bunntekst manglet i DOCX-konverteringen** (CV-malen: «Erfaring», «Generelt», bunntekst-bildet med grønn kant og navnetrekk). `extract_visualprofile.py` henter nå tekst og bilder fra `word/header*.xml`/`footer*.xml` selv.
3. **Overskrifter i tabellceller ble borte i PDF** (CV-malens SPRÅK OG RAMMEVERK / PLATTFORM, TECH & VERKTØY / METODE): LaTeX skriver ikke ut `\paragraph` uten etterfølgende tekst. `build_md_pdf.py` gjør dem om til fet tekst.
4. **Figma-URL delt ved bindestrek** i Brand Guidelines. `build_md_pdf.py` gjør nakne URL-er til lenker; lenkemålet verifisert eksakt.

Sluttresultat (tekstdekning / rasterbilder original → generert):

| Dokument | Tekst | Bilder |
|---|---|---|
| Brand Guidelines | 605/607 (99,7 %)¹ | 13 → 13 |
| Interiør komplett | 709/709 | 52 → 52 |
| Strategiplattform | 848/848 | 1 → 1 |
| Visittkort / Visittkort_alle (PDF) | 15/15 · 56/56 | 2 → 2 · 4 → 4 |
| Fontlisenser desktop / web | 1632/1632 · 1563/1563 | – |
| CV-mal 2023 | 486/486 | 5 → 5 |
| KW letterhead print / screen | 149/149 · 153/153 | 1 → 1 · 1 → 1 |
| Visittkort_alle (DOCX) / Untitled document | 61/61 · 196/196 | 3 → 3 · – |
| Kodeworks presentasjon / template 2022 / Svarmatrise + AI | 116/116 · 130/130 · 335/335 | 6 → 6 · 4 → 4 · 9 → 9 |

¹ Restavviket er figma-URL-en: pdftotext setter inn mellomrom i URL-fonten («ko dewor ks»); lenkemålet i PDF-en er eksakt riktig.

Visuelle stikkprøver (CV-mal, Svarmatrise) bekrefter at innholdet er lesbart. **Gjenstående avvik:** nedskaleringen til 25 % gjør tekst i skjermbilder uleselig — f.eks. kravtabell-skjermbildet i Svarmatrise (`image7.png`, 626×839 → 156×210). Teksten i slike bilder finnes ikke som tekst i originalen heller, så den fanges ikke av tekstdekningen.

**Tillegg – avskrift av tekst i bilder:** Brukeren valgte å hente teksten fra originalbildene i full oppløsning i stedet for å endre skaleringen, og deretter slette originalbildene igjen. OCR-verktøy (tesseract/ocrmypdf) finnes ikke på maskinen; teksten ble derfor avskrevet visuelt av AI-assistenten fra bildene i full oppløsning (hentet midlertidig til scratchpad med `pdfimages` / fra OOXML-zip, slettet etterpå — kildedokumentene er urørt).

Utvalg: alle 101 rasterbilder ble gjennomgått på kontaktark. Med avskrift (17 bilder): Svarmatrise `image4.png` (CV-utdrag Siqitech), `image5.png` (CV-forside), `image7.png` (svarmatrise-tabell); strategiplattform `img_41.jpg` (stemningsord); interiør `img_117.jpg` (Figma-tekststiler), `img_151.jpg` (generator), `img_160.jpg` (character count-diagram), `img_267.jpg` (Instagram-mockup), `img_343.jpg` / `img_355.jpg` (plantegninger), `img_441.jpg` (Teppeabo-produktside), `img_686.jpg` (sofamål); Brand Guidelines `img_8262/8263/8264.jpg` (nettside- og kort-mockups), `img_8292.jpg` / `img_8296.jpg` (samme som interiør `img_160` / `img_151`). Ikke tatt med: rene logoer/navnetrekk, fotografier uten tekst, og skjermbilder som ikke ble nedskalert og er lesbare (tweet `image6.png`, kravtabell `image9.png`).

Avskriftene ligger i søskenfiler `<stem>_image_text.md` (én `## <bildefilnavn>`-seksjon per bilde) som `extract_visualprofile.py` aldri overskriver, og som flettes inn som sitatblokk «**Tekst i bildet:**» etter første referanse til bildet ved hver kjøring. Nye filer: `background/visualprofile/Google slides template/2026-11-11_svarmatrise_ai_kodeworks_image_text.md`, `background/visualprofile/Leveranse fra Neue/2021-02-25_kodeworks_stratplatt_image_text.md`, `…/2021-05-03_kodeworks_id_elementer_interioer_komplett_image_text.md`, `…/2021-05-31_brand_guidelines_image_text.md`. De fire dokumentene ble regenerert (17/17 avskrifter flettet inn) og PDF-ene bygget på nytt; tekstdekning fortsatt 100 %. Emoji i Instagram-mockupen er skrevet med ord, siden Arial mangler glyfene. `build_md_pdf.py` krasjet på utskrift av advarsler med tegn utenfor konsollens tegnsett (PDF-en ble likevel laget) — rettet med `errors="replace"` på stdout/stderr.

### T10 [x] Revidert visuell profil og maler for KodeWorks

KodeWorks' visuelle profil ble levert av designbyrået Neue i 2021 (designmanual, strategiplattform, interiørkonsept, visittkort, brevark) og er senere supplert med en CV-mal (2023), en presentasjonsmal (2022) og nettsiden kodeworks.no. Profilen skal revideres, og et sett med maler skal lages på grunnlag av den reviderte profilen: CV-mal, visittkort, presentasjonsmal og mal for salgsbrev til kunder. Målet er et helhetlig, moderne og praktisk brukbart uttrykk som bygger videre på 2021-profilen — ikke en ny merkevare.

Tasken løses som én familie i rekkefølge: den reviderte visuelle profilen først, deretter de fire malene, som alle bygger på den. En instruksjon om å løse samletasken betyr hele familien fra start til slutt, uten stopp mellom subtaskene; en instruksjon om å løse én subtask betyr bare den (og forutsetter at profilen er ferdig, med mindre subtasken er profilen selv).

**Kjent om dagens profil (utgangspunkt, verifiseres mot kildene):**

- Farger fra designmanualen: MAIN GREEN `#B6FF9E` (RGB 182, 255, 158 · CMYK 31/0/40/0 · PMS 2267 C/U neon), MAIN GREY `#E8E7E6` (RGB 232, 231, 230 · CMYK 8/6/7/0 · PMS 179-2 C/U), støttefarger svart og hvit. Manualen advarer om at grønnfargen varierer mye mellom flater og må testes. Nettsiden bruker i tillegg mørkegrønn `#254333`, mellomgrønn `#35664C` og nesten-svart bakgrunn `#0F1613` — disse finnes ikke i 2021-manualen og må vurderes.
- Profilfont: Non Natural Grotesk (Non Foundry / Type Department), fem vekter (Thin, Light, Regular, Medium, Bold) som OTF. Fallback-font i Office: Arial.
- Grafiske elementer: navnetrekket «KodeWorks», logosymbolet «KW» (resultat av samskaping i Slack), «det femte elementet» / «seismografen» (generert fra KodeWorks' Slack-aktivitet: høy tegnmengde gir tykk strek, lav gir tynn; generator med tidsperiode, formater EPS/PNG/SVG/MP4, farger grønn/svart), venstre-/midt-/høyrejustert grid.
- **Fontlisensen (desktop) begrenser bruken:** fonten kan bygges inn i PDF/PS/EPS, men **ikke** i andre formater — altså ikke innebygd i `.docx`/`.pptx`. Lisensen dekker ikke logobruk, ikke webfont-konvertering, og ikke installasjon på servere tilgjengelige fra internett. Lisensen dekker «1 commercial project». Malene i denne familien settes derfor direkte til PDF med fonten innebygd, lastet fra den lisensierte font-fila i repoet. Ingen leveranse og intet bygg forutsetter at profilfonten eller andre fonter er installert på maskinen, verken på Windows, i WSL2 eller på Linux.

**Kildemateriale (les før arbeidet starter):**

- `background/visualprofile/neue-delivery/2021-05-31_brand_guidelines.md` (+ `_media/`, `_image_text.md`, `.pdf`) — designmanualen. Originalen `Brand Guidelines.pdf` kan rendres side for side med PyMuPDF for visuell referanse.
- `background/visualprofile/neue-delivery/2021-02-25_kodeworks_stratplatt.md` — strategiplattform (verdier, posisjonering, stemningsord).
- `background/visualprofile/neue-delivery/2021-05-03_kodeworks_id_elementer_interioer_komplett.md` — interiørkonsept (fargebruk i rom, lys, materialer).
- `background/visualprofile/neue-delivery/` — letterheads, visittkort (PDF og DOCX), Neue-presentasjonen; `background/visualprofile/Google slides template/` — presentasjonsmal 2022 og svarmatrise; `background/visualprofile/2026-11-11_cv_mal_2023.md` og originalen `CV-mal 2023.docx`.
- `background/visualprofile/Brand assets/` — logo, symbol og mønster som SVG (bruk SVG-variantene; EPS/JPG/PNG er formatvarianter av de samme motivene).
- `background/visualprofile/Fonts/Non Natural Grotesk/` — fontfiler (zip) og lisenser (`*_license_*.md`).
- `background/2026-09-22_kodeworks_om_selskapet.md`, `background/2026-09-22_webside_tekst_grunnlag.md`, `background/2026-09-22_kw_masterpresentasjon.md`, `background/2026-09-22_customers.md`, `background/2026-09-22_projects.md`, `background/cvs/*.md` — innhold og tone, og realistiske eksempeldata.
- `deliverable/2026-09-22_itko_presentasjon.md` — eksisterende beamer-tema i KW-farger (metropolis).
- **Nåværende nettside kodeworks.no** — det mest oppdaterte uttrykket profilen har i praksis. Orkestratoren besøker nettsiden (WebFetch, og `curl` mot HTML/CSS for faktiske fargeverdier, fonter, størrelser, avstander og komponenter), og dokumenterer designet i `background/<dato>_kodeworks_no_design.md`: farger med bruk, typografi (fonter, vekter, størrelser, linjeavstand), layout og grid, komponenter (navigasjon, knapper, kort, bunntekst), bildebruk og bruk av grafiske elementer. Notatet er input til alle workere og subtasks, og skal leses på linje med 2021-manualen.

**Arbeidsmetode: agent-orkestrering**

Gjelder hele familien og hver subtask. Se også «Agent-orkestrerte tasks» i `CLAUDE.md`.

1. **Orkestrator = hovedsesjonen.** Hovedsesjonen (som kjører på beste tilgjengelige modell med høy effort) er selv orkestratoren. Det spawnes **ingen** egen orkestrator-agent — workerne ligger direkte under hovedsesjonen, uten et mellomliggende lag. Hovedsesjonen eier planlegging, egen research (f.eks. nettsiden), konsolidering, kvalitetsvurdering og iterasjon. Der denne teksten sier «orkestratoren», menes hovedsesjonen.
2. **Workere.** Orkestratoren spawner 3 workere per runde (`Agent`, `subagent_type: general-purpose`, billigere modell — per 2026-11 `model: sonnet` — og `effort: medium`), parallelt i samme melding. Hver worker får et eget perspektiv; standardsettet er:
   - **Merkevare og kontinuitet** — tro mot 2021-profilen og strategiplattformen; gjenkjennelighet; hva som skal bevares.
   - **Formgiver** — typografi, grid, luft, hierarki, moderne uttrykk; hvordan det femte elementet og grønnfargen brukes med måte.
   - **Praktisk bruk og produksjon** — skal fungere på trykk og på skjerm, og bygges likt på Windows, WSL2 og Linux uten installerte fonter. Videre kontrast (WCAG AA for tekst), lisensbegrensningene, og at en konsulent faktisk klarer å fylle ut malen (Markdown-kilden).

   Orkestratoren kan justere perspektivene per subtask og skal skrive briefen slik at workeren står på egne ben: mål, kildefiler med absolutte stier, akseptkriterier, output-mappe, og krav om selvkontroll (punkt 4).
3. **Egne mapper.** Hver worker skriver kun til `temp/T10.x/round<N>/<perspective>/` (absolutt sti i hovedcheckouten, uavhengig av om agenten kjører i en worktree). Orkestratoren skriver det konsoliderte resultatet til subtaskens leveransemappe under `deliverable/visualprofile/`. Ingen worker skriver i en annen workers mappe eller i leveransemappen.
4. **Visuell selvkontroll — både worker og orkestrator.** Ingen leveranse vurderes uten at den er rendret og sett på (se også kvalitetskravet i punkt 8). **LibreOffice brukes ikke i denne task-familien**, verken til produksjon, konvertering eller kontroll. Brukeren besluttet det etter versjon 2 av CV-malen: `.docx` rendret gjennom LibreOffice ga dårlig typografi og kornete rastergrafikk. LibreOffice er fortsatt et tillatt verktøy i prosjektet ellers. Leveranser settes direkte til PDF: Markdown → PDF med pandoc/lualatex, SVG → PDF og PDF → PNG med PyMuPDF, og PNG-ene leses med Read-verktøyet. **Fonter lastes bare som filer:** profilfonten fra den lisensierte zip-en i repoet (fontspec `Path=`, pakket ut i byggemappen) og andre fonter fra TeX Live. Det brukes aldri fonter som er installert i operativsystemet, f.eks. Windows sin fontmappe, og fonter installeres aldri for å bygge eller kontrollere. Hvert LaTeX-bygg kjører `src/font_guard.py`, som stopper bygget hvis en font kommer fra et annet sted. Kritiske ting sjekkes eksplisitt: farger, font (`pdffonts`), marger og utfallende kant, at tekst ikke flyter over, at logo/symbol er skarpe, og at resultatet stemmer med intensjonen i subtasken.
5. **Konsolidering og iterasjon — til det er vakkert.** Orkestratoren leser alle workerbidrag (både filene og de rendrede sidene), velger og kombinerer, og produserer en konsolidert versjon som også rendres og kontrolleres. Det er ingen fast grense for antall runder: subtasken er ikke ferdig før orkestratoren selv, ved kritisk gjennomgang, mener resultatet er **vakkert** — ikke bare korrekt — og kvalitetskravet i punkt 8 er oppfylt. Brukeren skal ikke behøve å påpeke det som er åpenbart (kornete grafikk, uskarp logo, løs sperring, rotete linjer, grå kanter, dårlig luft). Orkestratoren vurderer resultatet slik en kresen grafisk designer ville gjort, og er streng mot eget arbeid.
6. **Shell-regler gjelder også agentene:** foreground, under 2 minutter per kommando, `uv run python`, ingen git (unntatt worktree-oppryddingen i punkt 7), og ingen installasjoner utover PEP 723-avhengigheter via `uv` (f.eks. `pymupdf`, `Pillow`). Fonter installeres aldri.
7. **Avslutning.** Når en subtask er ferdig: slett `temp/T10.x/` unntatt filer løsningsnotatet viser til, rydd `.claude/worktrees/agent-*` med de avgrensede git-kommandoene, skriv løsningsnotat (hva som ble laget, hvilke valg orkestratoren tok og hvorfor, antall runder, faktisk tid), oppdater `README.md` hvis nye scripts eller mapper er kommet til, og marker `[x]`.
8. **Kvalitetskrav og visuell gjennomgang.** (a) Se på hver side både i helhet (~70 dpi) og i **detalj (200–300 dpi)** på typografi, logo, grafiske elementer og kanter — feil som kornete raster, grå kanter, myk logo og løs sperring er usynlige i lav oppløsning. (b) Grafiske elementer (logo, symbol, seismograf) skal være **vektor** i sluttresultatet, aldri rasterbilder. (c) Typografien skal være satt av en motor med god kerning og bindestreksdeling, ikke av en kontorpakke-konvertering. Bruk **lualatex**, ikke xelatex: xelatex-formatet i denne TeX-installasjonen har ingen bokmålsmønstre og faller stille tilbake til engelsk deling («pros-jek-tbeskriv-else»), også med babel `norsk`. lualatex med polyglossia `\setmainlanguage{nb}` laster `hyph-nb` ved kjøring. Profilfonten har svake kerningpar rundt **j** (sj, kj, zj …) og **r–f**; bruk de felles rettingene i `src/profile_manual/kernfix.json` (kern-features `kwfr`/`kwfl`/`kwfm` via luaotfload, se `fonts.tex` og `src/build_cv_pdf.py`) og kontroller «prosjekt», «Introduksjon» og «Arbeidserfaring» i 300 dpi. (d) Sammenlign mot referansen (2021/2023-materialet og profilmanualen) side om side og spør: ser dette bedre ut enn originalen? Hvis ikke, er det ikke ferdig.
9. **Læringslogg mellom iterasjonene.** Orkestratoren fører `temp/T10.x/LEARNING.md`: for hver runde hva som ble laget, hvilke feil som ble funnet (med skjermutsnitt-filnavn), rotårsaken, og hva som endres — i leveransen og i **arbeidsmetoden** (workernes brief, perspektiver, sjekklister, modell/effort hvis en worker gjentatte ganger feiler). Neste rundes brief bygger eksplisitt på loggen, slik at samme feil ikke gjentas. Varige lærdommer for resten av familien føres inn i task-teksten (dette punktet eller subtaskens kriterier) før subtasken markeres `[x]`, og oppsummeres i løsningsnotatet.

   Lærdommer fra CV-malen: (a) Kjør tre parallelle workere bare i første runde, mens retningen er åpen. Når et grunnlag er valgt, viderefører én worker (med konteksten intakt) arbeidet og tar inn det beste fra de andre. Parallelle forslag etter det koster mye og tilfører lite. (b) Workerbriefen må si «én fil per kommando, `timeout 100` foran tunge kommandoer». En samlet byggekommando for alle testfiler gikk over 2 minutter. (c) Når et verktøy forkastes, fjern det fra alle steder workerne leser instruksjoner: task-tekst, spesifikasjon og brief. (d) Typografiske detaljer som bare synes i 300 dpi må stå som egne punkter i briefen: kerningpar, hengende skilletegn ved linjebrudd i lister, deling ved ordskjøt (`\hyphenation{}` etter `\begin{document}`, ellers bindes den til feil språk), enkeltord alene sist i avsnitt. (e) Lengderobusthet testes med innhold i flere størrelser (0, 2, 5, 8, 10, 13 elementer og en torturtest med spesialtegn og overlange ord), og byggescriptet bør selv velge tetthet slik at ingen side blir nesten tom. (f) Eksempler med ekte personer skal ikke få et foto eller en kundelogo som ikke hører til dem. Bruk plassholder og test feltet med egne testfiler. (g) Test malen mot ekte innhold tidlig. De 20 ekte CV-ene avslørte svakheter som syntetiske tester ikke fanget: logo- og fotoformater, lange perioder, innhold uten felt og engelsk tekst. Etter første fulle gjennomgang brukes et representativt utvalg på 6–9 filer per runde, og hele korpuset kjøres bare til slutt. Ellers tar hver runde 20–35 minutter. Si fra når estimatet sprekker. (h) Ingenting i byggene kan avhenge av operativsystemet eller av installerte fonter. Fonter lastes som filer fra repoet eller TeX Live, og `src/font_guard.py` håndheves i hvert LaTeX-bygg. Å avinstallere fonter for å teste er ikke en metode. (i) Kildeformatet for maler er Markdown (brukerens beslutning). Hold formatet (parser) og datamodellen (bygg) adskilt. (j) Autotilpasning som optimerer sidetall og fyllgrad, må også vekte layoutkvalitet. Den foretrukne layouten er en hard preferanse, og strengere regler ett sted kan gi tilbakeskritt et annet sted. Se derfor på hele testsettet etter hver regelendring.

**Felles akseptkriterier for alle maler:**

- Bygger synlig på den reviderte profilen (farger, font, grafiske elementer) og er konsistente med hverandre.
- Respekterer fontlisensen: fonten bygges bare inn i PDF. Ingen leveranse forutsetter installerte fonter, og bygget gir samme resultat på Windows, WSL2 og Linux (fontkontrollen i `src/font_guard.py` består).
- Har et utfylt eksempel med realistisk innhold i tillegg til den tomme malen, og er rendret til PDF som er kontrollert visuelt.
- Står på egne ben for en mottaker utenfor repoet (jf. «Eksterne leveranser står alene» i `CLAUDE.md`): ingen interne stier, task-nummer eller utkast-språk i selve malene.
- Har en kort bruksveiledning (`README.md` i leveransemappen, på norsk) for den som skal bruke malen.

**Verifisering (familien):**

1. Hver subtasks egne verifiseringssteg er bestått.
2. Et samlet oversiktsark (`deliverable/visualprofile/oversikt.pdf`) med én side per leveranse er rendret og kontrollert visuelt av orkestratoren, og viser at leveransene henger sammen.
3. `.claude/worktrees/` inneholder ingen `agent-*`-mapper fra tasken.

**Estimert innsats:** sum av subtaskene, 288 min (89 + 55 + 34 + 55 + 55). Med parallelle workere blir veggklokketiden trolig lavere enn summen.

**Kobling:** bygger på T9 (konvertert kildemateriale i `background/visualprofile/`); bruker metodikk fra T8 (KW-farger fra kodeworks.no, beamer-tema).

**Berørte filer:** `deliverable/visualprofile/**`, `temp/T10.*/` (midlertidig), `README.md`, `TASKS.md`, `src/build_visualprofile_overview.py`, `src/build_cv_business_cards.py`, `tests/test_cv_business_cards.py`, `deliverable/visualprofile/oversikt.pdf`

**Faktisk innsats:** summen av subtaskenes faktiske tid står i hver av dem. Avslutningen av familien (oversiktsark, visittkort fra CV-ene, detaljgjennomgang av visittkortet og opprydding) tok 9m 35s fram til løsningsnotatet (veggklokke).

**Resolution:** Alle fem subtaskene er løst:
- revidert profil og profilmanual;
- CV-mal (Markdown → PDF);
- visittkort, også fra CV-filene;
- presentasjonsmal;
- dokumentmal med brev som variant.

Avslutningen av familien:
- **Oversiktsark:** nytt `src/build_visualprofile_overview.py` lager `deliverable/visualprofile/oversikt.pdf`, fem A4-sider på tvers, én per leveranse:
  - profilmanualen: omslag, innhold, palett og bruk av seismografen;
  - CV-eksempelet: forside, prosjekter og «Generelt»;
  - visittkortet: forside og bakside;
  - presentasjonen: åpning, innhold, seksjonsskille og avslutning;
  - dokumentmalen: brev og utlysning.

  Sidene settes inn som vektor (`show_pdf_page`), med overskrifter i profilfonten fra den lisensierte zip-en.
- **Visittkortet:** detaljgjennomgangen og sammenligningen med 2021-kortet er gjort i ettertid, og visittkort lages nå også fra CV-ene (se tillegget i visittkortoppgaven).
- **Åpne punkter fra CV-malen og presentasjonsmalen er lukket:**
  - profilmanualens fontråd og CLAUDE.md ble rettet underveis (se tilleggene i profiloppgaven og i oppgaven om engelske navn);
  - de fire byggemappene med utpakkede fontfiler fra presentasjonsbygget (`kwdeck_*`), og én fra et avbrutt CV-bygg (`kwcv_*`), er slettet fra systemets midlertidige mappe.
- **Engelske navn:** fargefila, arbeidsmappene og læringsloggen har fått engelske navn etter visittkortet (se oppgaven om engelske navn).

Verifisering (familien):
1. Hver subtasks egne verifiseringssteg er bestått (se de enkelte løsningsnotatene). For visittkortet er detaljgjennomgangen i 300 dpi og sammenligningen med 2021-kortet tatt igjen.
2. `deliverable/visualprofile/oversikt.pdf` er bygget og alle fem sider er lest.
   - Leveransene henger sammen: samme palett, samme font, samme navnetrekk og seismograf, og samme rutenett i CV og dokument.
   - `pdffonts` viser bare NON Natural Grotesk.
   - Det eneste rasterinnholdet er foto og kundelogoer i CV-eksempelet.
3. `.claude/worktrees/` finnes ikke, så ingen `agent-*`-mapper ligger igjen.

`pytest --timeout=5` består med 107 tester.


#### T10.1 [x] Revidert visuell profil

Lag en revidert profilmanual som erstatter 2021-manualen som referanse for alle maler. Den skal beskrive og vise: logo og symbol (varianter, frisone, minstestørrelse, bruk på lys/mørk/grønn bakgrunn), fargepalett (primær og sekundær, med HEX/RGB/CMYK/PMS, og en avklaring av nettsidens mørkegrønne farger mot 2021-paletten), typografi (Non Natural Grotesk-vektene, hierarki for overskrifter og brødtekst, Arial-fallback), det femte elementet / seismografen (når og hvordan det brukes), grid og layoutprinsipper, bildebruk, og eksempler på anvendelse.

**Leveranse:** `deliverable/visualprofile/profile/` med `profilmanual.md` → `profilmanual.pdf` (fonten innebygd), `farger.md` (palett som tabell, også maskinlesbar `farger.json`), og `assets/` med de SVG-ene malene skal bruke (kopier fra `Brand assets/`, renset og navngitt konsekvent).

**Akseptkriterier:** Fargekontrast for tekst på hver tillatt bakgrunn er oppgitt og oppfyller WCAG AA der fargen er tiltenkt brødtekst. Designet på nåværende kodeworks.no er kartlagt (notat i `background/`) og brukt som input. Manualen tar stilling til hver forskjell mellom 2021-manualen og nettsiden — farger, typografi, layout og grafiske elementer — (beholde, endre eller forkaste, med begrunnelse). Hver regel i manualen er vist med et eksempel.

**Verifisering:**

1. `profilmanual.pdf` rendret; `pdffonts` viser Non Natural Grotesk innebygd.
2. Alle sider konvertert til PNG og lest med Read av orkestratoren; farger, logo og eksempler ser riktige ut.
3. Kontrastverdiene i `farger.md` er beregnet med script (ikke anslått), og scriptet ligger i `src/` hvis det er gjenbrukbart.

**Estimert innsats:** 89 min

**Faktisk innsats:** 41m 48s (veggklokke, fra første start; inkluderer ca. 4 min for et stoppet første forsøk)

**Berørte filer:** `deliverable/visualprofile/profile/**` (`profilmanual.md`, `profilmanual.pdf`, `farger.md`, `farger.json`, `assets/` med `pdf/` og `png/`, `images/`), `background/2026-11-11_kodeworks_no_design.md` + `background/2026-11-11_kodeworks_no_design_media/`, `src/build_profile_manual.py`, `src/profile_manual/` (`template.tex`, `layout.tex`, `colors.tex`, `fonts.tex`, `filter.lua`), `src/export_profile_assets.py`, `src/wcag_contrast.py`, `README.md`, `TASKS.md`

**Resolution:** Første forsøk brukte en egen orkestrator-agent under hovedsesjonen; brukeren stoppet det etter ca. 3 minutter (ingen workere var startet) og presiserte at hovedsesjonen selv er orkestrator med workerne direkte under seg, og at designet på kodeworks.no skulle kartlegges som input. Arbeidsmetoden i familien ble oppdatert tilsvarende. Fontene og referanserendringene av 2021-manualen fra det stoppede forsøket ble gjenbrukt.

Nettsiden ble kartlagt av orkestratoren: CSS-variabler og -regler hentet med `curl` fra Next.js-stilarkene (farger `#B6FF9E`, `#35664C`, `#254333`, `#FAD5D5`, `#E8E7E6`, `#666`; Non Natural Grotesk Light/Regular som webfont, Light overalt; mål 1400/1100 px, gutter 30/20 px, luft 60/120 px; rektangulære knapper i mørkegrønn), og skjermbilder tatt med Edge headless. Fordi innholdet tones inn ved scroll og toppseksjonen er 100 vh, ble skjermbildene av hele siden tatt fra en lokal kopi med animasjoner av og vh-enheter erstattet. Resultatet ligger i `background/2026-11-11_kodeworks_no_design.md`.

To runder med 3 workere (Sonnet, medium effort), parallelt:

- **Runde 1** (byggesteiner): merkevare/kontinuitet skrev et beslutningsdokument per element (2021 mot nettsiden: beholde/endre/forkaste med begrunnelse); formgiver laget layoutsystemet (16:9, 297 × 167 mm, grått bunnfelt som i 2021, pandoc + Lua-filter + LaTeX-mal, fonten fra fil med fontspec `Path=`); produksjon renset alle SVG-ene (de «grønne» filene fikk farge fra en CSS-klasse som PyMuPDF ignorerer og ble tegnet svarte — nå eksplisitt `fill`; «KW_logo copy.svg» viste seg å være hvit variant), målte frisone/minstestørrelse fra geometrien, og skrev kontrastscriptet.
- **Orkestratorens beslutninger mellom rundene** (skrevet i en felles spesifikasjon): Regular i brødtekst og Light fra ingress og opp (nettsiden har Light overalt, som taper lesbarhet i små størrelser); dypgrønn `#254333` beholdes med rollen mørk flate (merkevare ville forkaste den); lysegrønn og mørkegrønn tillates begge veier (merkevare forbød én retning, men kontrast er symmetrisk, 5,64:1); `#0F1613` droppes; CMYK grønn rettet fra 31/0/46/0 til 31/0/40/0.
- **Runde 2** (ferdige seksjoner): formgiver — omslag, innhold, Logo, Grafiske elementer, og utvidet systemet (✓/✕-merker, tabeller, målsetting, innholdsside med automatiske sidetall, webkomponenter); merkevare — Introduksjon, Farger, Foto (KodeWorks' egne bilder fra nettsiden), Tone; produksjon — Typografi, Anvendelse, Produksjon.

Konsolidering (orkestrator): seksjonene satt sammen til `profilmanual.md` (navnekollisjon mellom workernes lokale makroer `\kwchip`/`\kwcap` løst med suffiks, gamle assetnavn byttet, etikett for innholdssiden lagt på Tone-siden), byggescriptet flyttet til `src/` og gjort uavhengig av arbeidsmappen (fonter pakkes ut fra den lisensierte zip-en, bygg i midlertidig mappe). Gjennomgang av alle 40 sider avdekket og rettet: bildetekst under grafikk (Feil bruk), motstridende regel om grønt navnetrekk (Filoversikt), grønt-strek-symbol oppført som tillatt på grå (1,05:1), og at filformatsiden viste til PNG/PDF-filer som ikke fantes — løst med `src/export_profile_assets.py`, som eksporterer alle SVG-er til `assets/pdf/` og `assets/png/`.

Verifisering:

1. `profilmanual.pdf` bygget (40 sider, 16:9); `pdffonts` viser Non Natural Grotesk Light, Regular, Medium, Thin og Bold innebygd (Thin/Bold bare på sidene som viser at de ikke brukes), pluss Arial på fallback-sammenligningen.
2. Alle 40 sider rendret til PNG og lest; rettede sider rendret og lest på nytt.
3. Kontrasttallene er beregnet med `src/wcag_contrast.py` fra `farger.json` (kontroll: svart/hvit 21,00:1, `#666` på hvit 5,74:1) og er de samme i manualen og i `farger.md`.

Oppfyllelse av akseptkriteriene: kontrast for hver tillatt bakgrunn står i manualen (side «Kontrast» og bakgrunnssidene for logo) og i `farger.md`; nettsiden er kartlagt og brukt; «Hva er nytt»-siden og hver seksjon tar stilling til forskjellene 2021/nettsiden; hver regel har et eksempel (✓/✕-fliser, mockups, målsatte diagrammer).

Opprydding: `temp/T10.1/` slettet. Ingen `.claude/worktrees/agent-*` ble opprettet (agentene kjørte uten worktree i denne harness-versjonen).

Åpne punkter (står også i manualen): forenklet symbol for bruk under 80 px høyde er ikke tegnet; CMYK/PMS for svart, mørkegrønn, dypgrønn, rosa og mørkegrå er forslag som må verifiseres av trykkeri, og PMS «179-2» for grå er ikke et standard Pantone-navn; fontlisensen gjelder ett selskap og dekker ikke webfont — dekning for alle KodeWorks-selskapene og for nettsidens webfont bør avklares med leverandøren; det er ikke bekreftet at seismograf-generatoren er i drift; samtykke for personene på bildene fra nettsiden bør bekreftes før manualen brukes eksternt; egne foto av Trondheim-kontoret mangler (nettsiden har bare en 3D-visualisering).

**Tillegg – rettinger under CV-malen:** (1) Fontregel for maler: manualen sa at redigerbare filer settes i Arial; rettet til familiens regel (stilene refererer profilfonten ved navn, Arial som erstatning og temafont) på sidene «Fallback og lisens», «Fontlisens i praksis» og «Sjekkliste før utsending». (2) Seismografen: regelen «ikke på tekstrike brevark» var for streng og fjernet et karakteristisk element fra CV-malen; nå tillatt som ramme i kanten og ved seksjonsstart på tekstrike dokumenter, også grønn på hvit/grå, men aldri bak eller gjennom tekst («Bruk av seismografen»-teksten og ✕-flisen «Grønn på hvit, stort motiv»); brevark-mockupen på «Visittkort og brevark» viser rammen i bunnteksten (grafikken `images/ramme-bunn.png` fra CV v2). Manualen er bygget på nytt (40 sider) og de endrede sidene er lest.
**Tillegg – fontregler uten installert font:** Brukeren slo fast at repoet er stedet der KodeWorks' visuelle materiale genereres som PDF, og at ingenting kan avhenge av fonter installert på maskinen. Manualen er skrevet om på fire sider. «Fallback og lisens»: regelen for materiale sier nå at CV, presentasjon, dokument og brev skrives i Markdown og bygges til PDF med fonten fra fontfila. Office og Google viser Arial, og det som sendes ut i KodeWorks' navn, lages fra malene. «Presentasjon»: merknaden om skrift er rettet. «Fontlisens i praksis»: fonten hentes fra fontfila og aldri fra maskinen, og konsulenter lager materialet fra malene. «Sjekkliste før utsending»: punktene om mal, skrift og metadata er rettet. Manualen er bygget på nytt (40 sider) og de fire sidene er lest. Samtidig ble CLAUDE.md og README rettet: fontinstallasjon er fjernet som tillatt handling (LibreOffice er fortsatt tillatt generelt), og standardkommandoen for Markdown → PDF bruker lualatex, `lang=nb` og fonter fra TeX Live (TeX Gyre Termes, DejaVu Sans Mono) i stedet for systemfontene Times New Roman og Consolas.

#### T10.2 [x] Revidert CV-mal

Lag en revidert CV-mal basert på strukturen i CV-mal 2023 (forside med foto, kontaktinfo, «Om», teknisk kompetanse; prosjektblokker; arbeidserfaring, utdanning, sertifiseringer) og den reviderte profilen. Malen må være enkel å fylle ut for konsulenter i Word og Google Docs, og tåle varierende lengde (fra 2 til 10+ prosjekter).

**Leveranse:** `deliverable/visualprofile/cv/` med `cv-mal.docx` (tom mal), `cv-eksempel.docx` (fylt ut med realistisk innhold fra en av CV-ene i `background/cver/`), begge rendret til PDF, og `LESMEG.md`.

**Akseptkriterier:** Fungerer med Arial når profilfonten ikke er installert. Prosjektblokker kan kopieres uten at layouten brekker. Lange beskrivelser flyter til neste side uten å ødelegge tabellstrukturen. Ingen innebygd font.

**Verifisering:**

1. Begge `.docx` rendret til PDF med LibreOffice, både med profilfonten installert og med Arial-fallback (fonten midlertidig avinstallert for gjeldende bruker, eller malen kopiert med fontnavn byttet); alle sider lest med Read.
2. Eksempelet testet med minst 8 prosjektblokker; ingen sider med brutt layout.
3. `.docx` inspisert med `python-docx`: ingen innebygde fonter (`word/fonts/` finnes ikke i zip-en).

**Estimert innsats:** 55 min

**Faktisk innsats:** 12m 58s (veggklokke)

**Berørte filer:** `deliverable/visualprofile/cv/**` (`cv-mal.docx`, `cv-eksempel.docx`, `cv-mal.pdf`, `cv-eksempel.pdf`, `LESMEG.md`, `kilde/cv-mal.json`, `kilde/cv-eksempel.json`), `src/build_cv.py`, `src/check_cv_docx.py`, `src/arial_fallback.py`, `deliverable/visualprofile/profile/profilmanual.md` + `.pdf` (fontregel for maler), `README.md`, `TASKS.md`

**Resolution:** Orkestratoren (hovedsesjonen) leste familienavnene ut av OTF-filene (`NON Natural Grotesk` for Regular/Bold, `NON Natural Grotesk Light`, `NON Natural Grotesk Medium`), installerte de fem fontene for gjeldende bruker (kopi til `%LOCALAPPDATA%\Microsoft\Windows\Fonts` + HKCU-register) og bekreftet at LibreOffice rendrer med dem. CV-mal 2023 ble rendret som referanse. En felles spesifikasjon fastsatte font- og fallbackmekanisme (familienavn i stilene, `w:altName` Arial i fonttabellen, Arial som temafont, ingen innebygging), robusthetskrav for Word/Google Docs og et JSON-innholdsformat, slik at generator og innhold kunne lages parallelt.

Runde 1, tre workere (Sonnet, medium) parallelt: formgiver laget generatoren (`build_cv.py`, python-docx) med navngitte stiler, grått forsidepanel med grønn strek, seksjonstitler i mørkegrønn, prosjektblokker som overskrift + tabell med grønn venstrekant, og topp-/bunntekst med navnetrekk og adresser; merkevare/innhold laget eksempelet fra CV-en til Pål Nødseth (8 prosjekter, fakta beholdt, språket strammet inn), den tomme malteksten med veiledning, en skriveveiledning og en sjekkliste for merkevaren; produksjon laget kontrollscriptet (`check_cv_docx.py`), Arial-kopiscriptet (`arial_fallback.py`) og brukerveiledningen. Kontrollscriptet ga 7 FAIL på 2023-malen (innebygde fonter, Calibri-tema, flytende bilde, farge utenfor palett) og 2 FAIL på første versjon av den nye generatoren (Courier og blåtoner fra python-docx' ubrukte standardstiler).

Runde 2 (formgiver): ubrukte standardstiler fjernet, kantlinjer satt direkte på cellene for Google Docs, `cantSplit` bare på de korte tabellene, ingen hardkodede stier, ny fotoplassholder («Bilde 1:1 · Erstatt bilde»).

Konsolidering (orkestrator): scriptene flyttet til `src/`, JSON-kildene lagt i `kilde/`, mal og eksempel bygget. Gjennomgangen avdekket en tom ekstra side til slutt i begge dokumentene med profilfonten (ikke med Arial): LibreOffice ga det påkrevde tomme sluttavsnittet etter siste tabell for stor høyde. Rettet i `build_cv.py` ved å sette avsnittsmerket i Arial 1 pt (eksperiment bekreftet at både fjerning og Arial-variant løser det; Arial-varianten beholder avsnittet Word krever). `LESMEG.md` satt sammen av bruker- og skriveveiledningen, med filnavn, seksjonsnavn, etiketter og stilnavn som generatoren faktisk lager.

Konsistens med profilen: profilmanualen sa at redigerbare filer settes i Arial, mens familiens task-tekst sier profilfont ved navn med Arial som reserve. Manualens sider «Fallback og lisens», «Fontlisens i praksis» og «Sjekkliste før utsending» ble rettet til regelen i task-teksten, og manualen bygget på nytt (40 sider, sidene lest).

Verifisering:

1. Begge `.docx` rendret med LibreOffice med profilfonten (mal 2 sider, eksempel 4 sider; `pdffonts`: NON Natural Grotesk Light/Regular/Medium + Arial for kuletegnet) og som Arial-kopier via `arial_fallback.py` (mal 2, eksempel 4 sider; bare ArialMT). Alle sider lest.
2. Eksempelet har 8 prosjektblokker; lange beskrivelser flyter over sideskift med tabellen og den grønne kanten intakt. Kopiering av blokker simulert ved å duplisere overskrift + tabell tre ganger i malen: 4 sider, ingen brutt layout, kontrollscriptet fortsatt 0 FAIL.
3. `check_cv_docx.py` på begge: 0 FAIL, 1 WARN (bevisst `cantSplit` på de korte tabellene); `word/fonts/` finnes ikke i noen av zip-filene.

Opprydding: `temp/T10.2/` slettet; ingen `.claude/worktrees/agent-*` opprettet. Profilfonten er fortsatt installert for gjeldende bruker, fordi de neste subtaskene (presentasjon, brev) trenger den for rendering.

Åpne punkter: malen er bare rendret i LibreOffice, ikke åpnet i Microsoft Word eller importert i Google Docs — kopiering av blokker, stilnavn etter Google-konvertering og Words navigasjonsrute bør prøves manuelt; eksempelet bruker Påls ekte telefonnummer og e-post fra CV-kilden (internt bruk; bytt til plassholdere hvis eksempelet deles eksternt); fotoplassholderen må erstattes med eget bilde.

**Tillegg – versjon 2 med seismografen som ramme:** Brukeren påpekte at seismografen (tynne og tykke grønne streker), som var en karakteristisk del av CV-malen fra 2023, manglet. Årsaken var orkestratorens egen spesifikasjon for versjon 1 («seismografen brukes ikke — CV er et tekstrikt dokument»), avledet av en for streng manualregel. 2023-malen brukte den ikke bak tekst, men som en ramme: bånd ved seksjonsstart, lukkende figur med navnetrekket nederst, L-ramme rundt bildet. Brukeren ba om et nytt forsøk i en egen mappe, med versjon 1 bevart. Versjon 1 i `deliverable/visualprofile/cv/` er urørt.

Runde 1, tre workere (Sonnet, medium) med hvert sitt rammekonsept: formgiver — sikksakk-stripe i høyre marg på alle sider via forankret bilde i toppteksten (forkastet: leste som en revet kant, ikke som seismografen, og krever forankring); kontinuitet — 2023-rammen gjenskapt helt inline (valgt som grunnlag); produksjon — stripe i toppteksten ved navnetrekket på alle sider pluss bånd ved alle seksjoner, og en gjenbrukbar stripegenerator (forkastet som uttrykk: for urolig; generatoren beholdt). Runde 2 (kontinuitet): bånd bare ved «Prosjekter» og «Arbeidserfaring» (som «Erfaring»/«Generelt» i 2023), frisone mellom avslutningens tykke strek og navnetrekket (første versjon lot streken berøre bokstavene — samme feil som manualen viser under «Feil bruk»), tynn diagonal 0,4 mm for synlighet. Avslutningsfiguren som siste avsnitt i brødteksten viste seg skjør (havnet alene på en ny side i malen; eksempelet krevde presset bunnmarg). Runde 3 (orkestratorens beslutning): avslutningsfiguren flyttet inn i bunnteksten på hver side, så rammen lukkes på alle sider og aldri blir foreldreløs; navnetrekket fjernet fra toppteksten (ellers to logoer per side, og 2023 hadde navnetrekket nederst); marger og luft tilbake til versjon 1.

Leveranse i `deliverable/visualprofile/cv_v2/`: `cv-mal.docx`/`.pdf`, `cv-eksempel.docx`/`.pdf`, `LESMEG.md` (versjon 1-veiledningen pluss avsnitt om seismograframmen), `kilde/` (samme JSON som versjon 1), `grafikk/` (`seksjon-strek` og `avslutning`, PNG 300 dpi + SVG). Scripts: `src/build_cv_v2.py` (med `--graphics`), `src/gen_cv_seismograph.py` (CV-grafikken), og `src/seismograph.py` (generell stripegenerator for senere maler; røyktestet).

Verifisering versjon 2: mal 2 sider og eksempel 4 sider både med profilfont og Arial-kopi; alle sider lest; zoom på bunntekst og bånd bekrefter at ingen strek krysser tekst eller logo; `check_cv_docx.py` 0 FAIL (1 WARN, bevisst `cantSplit`), ingen forankrede bilder, ingen `word/fonts/`; kopiering av prosjektblokker simulert (5 blokker → 4 sider, ramme og bånd intakte).

Profilmanualen er justert tilsvarende (se tillegg under profilen): regelen for seismografen tillater den nå som ramme i kanten og ved seksjonsstart på tekstrike dokumenter, også grønn på hvit/grå, men aldri bak eller gjennom tekst; brevark-mockupen viser rammen i bunnteksten.

**Faktisk innsats versjon 2:** 24m 3s (veggklokke)

**Versjon 3 — gjeldende spesifikasjon (erstatter docx-sporet):** Brukeren vurderte v2 som kornete og stygg: Word/LibreOffice-sporet gir rastergrafikk med grå kanter, myk logo, løs sperring og et «Word-tabell»-preg. Brukerens beslutning: dropp rendering i LibreOffice og dropp `.docx` som vei. Mappestrukturen er endret av brukeren: `deliverable/visualprofile/cv/cv_v1/` og `cv_v2/` (urørt); v3 lages i `deliverable/visualprofile/cv/`. Brukerens referanse er originalen eksportert fra Google Drive: `background/new/CV-mal 2023.pdf` (4 sider; foto med grønn L-ramme, KW-symbol og navn til høyre på forsiden, «Om» og teknisk kompetanse i to kolonner, seksjonsstart «Erfaring»/«Generelt» med tykk grønn strek og fallende tynn diagonal, prosjektblokker med grønn venstrekant, grå etiketter og **kundelogo øverst til høyre i hver blokk**, lukkende figur med navnetrekket nederst på siste side).

- **Format og verktøy:** CV-innholdet skrives som strukturert tekst (YAML; samme felt som JSON-formatet fra v1/v2, pluss valgfri `logo` per prosjekt) og settes direkte til PDF med xelatex (profilfonten fra den lisensierte zip-en via fontspec `Path=`; innbygging i PDF er tillatt), samme verktøykjede som profilmanualen. All grafikk er vektor: seismograf, L-ramme og linjer tegnes i TikZ (eller SVG → PDF), logo og symbol fra profilens SVG-er via PDF. Ingen rastergrafikk utenom fotoet. Ingen `.docx`, ingen LibreOffice.
- **Leveranse:** `cv_v3/` med `cv-mal.yaml` + `cv-mal.pdf` (tom mal med veiledning), `cv-eksempel.yaml` + `cv-eksempel.pdf` (Pål Nødseths CV fra v1/v2, 8 prosjekter), `LESMEG.md` (hvordan en konsulent fyller ut YAML-fila og bygger PDF, skriveveiledning, sjekkliste), byggescript i `src/` (f.eks. `src/build_cv_pdf.py`) med mal/stil i `src/` (f.eks. `src/cv_pdf/`).
- **Akseptkriterier:** (1) **Vakkert** etter punkt 5 og 8 i arbeidsmetoden: orkestratoren skal ved gjennomgang i 70 dpi og 200–300 dpi mene at resultatet ser bedre ut enn 2023-originalen; ingen kornete raster, grå kanter eller myk logo; god sperring og bindestreksdeling; rolig, presis rytme i luft og linjer. (2) Seismografen som ramme etter 2023-prinsippet (aldri bak eller gjennom tekst, frisone rundt navnetrekket), kundelogo-plass i prosjektblokkene. (3) Robust for lengde: 2 til 10+ prosjekter, lange beskrivelser flyter over sideskift med rammen intakt, ingen tomme eller nesten tomme sider, ingen foreldreløse titler eller avslutningsfigurer. (4) Profilreglene: farger, typografi (Light titler, Regular brødtekst, Medium utheving), kontrast.
- **Verifisering:** (1) Eksempel og mal bygget; `pdffonts` viser bare NON Natural Grotesk (innebygd). (2) Alle sider lest i 70 dpi og utsnitt av typografi, seismograf, logo og prosjektblokk lest i 200–300 dpi. (3) Lengdetest: et ekstra testinnhold med 12 prosjekter og ett svært langt prosjekt bygget og lest. (4) Læringslogg (`temp/T10.2v3/LAERING.md`) viser rundene, feilene og hvordan arbeidsmetoden ble justert; lærdommer for resten av familien er ført inn i arbeidsmetoden.

**Estimert innsats versjon 3:** 89 min

**Faktisk innsats versjon 3:** 71m 30s (veggklokke, inkluderer overføring av kerningrettingene og bytte til lualatex i profilmanualen)

**Berørte filer versjon 3:** `deliverable/visualprofile/cv/` (`cv-mal.yaml`, `cv-mal.pdf`, `cv-eksempel.yaml`, `cv-eksempel.pdf`, `LESMEG.md`), `src/build_cv_pdf.py`, `src/cv_pdf/cv-style.tex`, `src/profile_manual/kernfix.json` (ny, delt), `src/profile_manual/fonts.tex`, `src/build_profile_manual.py`, `deliverable/visualprofile/profile/profilmanual.pdf`, `README.md`, `TASKS.md`

**Resolution versjon 3:** Fire runder, orkestrert fra hovedsesjonen med workere på Sonnet/medium. Læringsloggen ble ført mellom rundene og er oppsummert her. Arbeidsmappen er slettet.

- **Runde 1** hadde tre parallelle workere. Formgiveren satte den mest raffinerte typografien: grå etiketter i små versaler, navn i Light, rolle i mørkegrønn, prosjektnavn i Medium, løpende fot og ett konsekvent seismografmotiv. Den ble valgt som designgrunnlag. Kontinuitetsvarianten var en trofast, men mindre gjennomarbeidet 2023-kopi. Produksjonsvarianten hadde den beste robustheten: escaping av spesialtegn, valgfrie felt, navn som krymper ved behov, bunnfigur bare på siste side og automatisk tetthet når siste side blir nesten tom.
- **Runde 2:** formgiveren tok inn robustheten fra produksjonsvarianten og lot «Generelt» flyte etter siste prosjekt i stedet for å tvinge sideskift. Orkestratoren fant to ting. xelatex delte norsk tekst med engelske mønstre, og fonten hadde et kerninghull i r–f («Arbeidser faring»). Orkestratoren testet lualatex, som laster bokmålsmønstrene riktig.
- **Runde 3:** motoren ble byttet til lualatex med polyglossia. En kerningrevisjon med fontTools/HarfBuzz fant at **j** har stor venstre sidelager (sj, kj, zj …) og at r–f var svakt. Begge ble rettet med egne kern-features. Forsiden avsluttes nå med et rolig seismografbånd, eller så starter «Erfaring» på forsiden når det er plass. Malen ble 2 sider.
- **Runde 4** var ren polering. Skilleprikken i nøkkelordlister forsvinner ved linjebrudd. Delingsstraffen ble økt, og en liste fikk vanlige sammensetninger til å deles ved ordskjøten («forretnings-siden»). Nøkkelordraden holdes sammen med beskrivelsen, de to siste ordene i avsnitt og kulepunkter bindes sammen, og kompetansekolonnene ble bredere.

Orkestratoren vurderte runde 4 som vakker og bedre enn 2023-originalen. Typografien er presis i 300 dpi, all grafikk er vektor, rytmen i luft og linjer er rolig, og sideskiftene er gode.

Konsolidering: byggescriptet ble flyttet til `src/build_cv_pdf.py`, med stil i `src/cv_pdf/`. Kerningrettingene ligger i `src/profile_manual/kernfix.json` og deles med profilmanualen. Malen fikk en kort veiledning øverst i YAML-fila. `LESMEG.md` dekker utfylling, feltene, skriveregler for YAML, logo og foto, hvordan oppsettet tilpasser seg innholdet, skriveråd og en sjekkliste.

Eksempelet leveres uten foto og uten kundelogoer. Portrettet i bildebanken er ikke bekreftet å være Pål, og KodeWorks-logoen som «kundelogo» ville vært misvisende. Begge feltene er testet med egne testfiler, også med relative stier.

Profilmanualen bruker nå også lualatex og kerningrettingene. Før viste skillesidene «Introduks jon» og «Produks jon», og den norske teksten ble delt med engelske mønstre. Manualen er bygget på nytt (40 sider) og alle sider er lest.

Verifisering:

1. Mal (2 sider) og eksempel (4 sider) er bygget. `pdffonts` viser bare NON Natural Grotesk Light, Regular og Medium, innebygd.
2. Alle sider er lest i ca. 70 dpi. Utsnitt i 300 dpi er lest av forsidetopp, «Om» og kompetanse, seksjonsstart med seismograf, prosjektblokk med logo, bunnfigur med navnetrekk, sideskift midt i et prosjekt, nøkkelordlister med linjebrudd og orddeling. Kerningen er kontrollert med et før/etter-ark for alle tre vektene.
3. Lengdetester er bygget og lest:
   - 13 prosjekter med ett svært langt: 7 sider, siste side 87 % full.
   - 10 prosjekter: 5 sider, 58 %.
   - 5 prosjekter: 3 sider, 96 %.
   - 2 prosjekter: 3 sider, 65 %.
   - Ingen prosjekter: 1 side.
   - Torturtest med spesialtegn, emoji, overlange ord og URL-er, 40 kulepunkter og manglende felt: 4 sider. Manglende glyfer og bilder gir advarsel, ikke feil.

   Ingen side er under 58 % full, og ingen titler eller avslutningsfigurer står alene.
4. Lærdommene for resten av familien er ført inn i arbeidsmetoden (punkt 4, 8c og 9): lualatex, kerningrettinger, én worker etter valgt retning, kommandoregler, typografiske 300 dpi-punkter, lengdetester og foto/logo i eksempler med ekte personer.

Opprydding: `temp/T10.2v3/` er slettet. `.claude/worktrees/` finnes ikke, så ingen agent-worktrees ble opprettet.

Åpne punkter:
- Eksempelet bruker Påls ekte telefonnummer og e-post. Bytt til plassholdere hvis det deles eksternt.
- Bygging krever TeX Live med lualatex og prosjektets fontzip. Konsulenter uten dette må få CV-en bygget av den som har ansvar for profilen.
- Med 2 prosjekter står «Generelt» på egen side (65 % full). Det er akseptabelt, men kunne vært delt over to sider.
- Fotoet beskjæres alltid fra midten.
- `cv_v1/` og `cv_v2/` er urørt.

**Tillegg – videreutvikling mot ekte CV-er, Markdown og plattformuavhengighet:** Brukeren åpnet oppgaven igjen: «Hvis det kan være penere må du jobbe videre», og pekte på CV-ene i datamappen som variasjonstest. Underveis kom to beslutninger fra brukeren:
- Ingenting i byggene kan avhenge av Windows eller av installerte fonter, og brukeren skal ikke måtte avinstallere en font for å bevise det.
- Kildeformatet skal være Markdown: «Bruk .md som format. Det er det vi kommer til å bruke på sikt.»

*Plattformuavhengighet.* Tre avhengigheter ble funnet og fjernet:
- Profilmanualen hentet Arial fra Windows sin fontmappe. Nå brukes TeX Gyre Heros fra TeX Live, som har samme tegnbredder og kopieres inn i byggemappen.
- Kontrollskriptet for Markdown brukte Arial og Consolas fra systemet, og xelatex. Nå brukes lualatex, TeX Gyre Heros og DejaVu Sans Mono som filer, og norsk orddeling. Alle 15 kontroll-PDF-ene er bygget på nytt.
- CV-generatorene for versjon 1 og 2 slo opp `arial.ttf` i systemet. Nå brukes Pillows egen skalerbare font.

Ny `src/font_guard.py`: LuaTeX skriver filnavnet til hver font den laster, og bygget stopper hvis en font ligger utenfor byggemappen eller TeX-trærne. Recorder-fila er ikke nok, fordi fonter lastet med `Path=` ikke står der. Kontrollen er koblet inn i profilmanualen, CV-malen og kontroll-PDF-ene. Negativtest: manualen med Arial fra Windows stoppes, og meldingen navngir fila. Ny `tests/test_platform_independence.py` (statisk søk etter OS-fontstier og systemfonter i byggekildene, samt test av kontrollen).

*Markdown som kildeformat.* Ny `src/cv_markdown.py` leser og skriver CV-en som Markdown, og testes i `tests/test_cv_markdown.py`.
- `#` er navnet, avsnittet under er tittelen, og en kontaktliste har formen «Etikett: verdi».
- `##`-seksjoner, og `###` per kompetansegruppe og prosjekt. Prosjektet har en metadataliste og en linje «Nøkkelord:».
- «Generelt»-rader skrives som `periode | navn | sted`. Ukjente `##`-titler blir egne lister.
- Engelske etiketter og overskrifter gir engelsk CV. HTML-kommentarer kan brukes til veiledning.

Byggescriptets datamodell er uendret, så formatet kunne byttes midt i en runde uten å forstyrre arbeidet med oppsettet. Rundtur YAML → Markdown → data ga ingen avvik på alle 29 korpusfilene. Fire feil ble funnet og rettet underveis:
- komma inne i parenteser i nøkkelord;
- kompetanse-elementer som er hele setninger;
- avsnitt under arbeidsforhold;
- rader med bare periode.

*Runde 5* (tre parallelle workere, Sonnet/medium): alle 20 ekte CV-er (Word og PDF) ble konvertert trofast, med foto og kundelogoer pakket ut fra originalene, og bygget. Funn, verst først:
- logoer med svært ulik visuell tyngde;
- liggende foto og helfigur som ikke fylte rammen;
- periodekolonnen i «Generelt» som kolliderte;
- prosjekter delt med enslige rester;
- verv og foredrag under «Sertifiseringer»;
- norsk orddeling av engelske ord;
- tetthet 3 som krympet teksten.

*Runde 6–9* (formgiveren fra runde 1–4, med hele korpuset som testsett, fra runde 9 et representativt utvalg på 9 filer):
- **Logoer:** trimmes (hvit, nesten hvit og gjennomsiktig kant, og tegningens utstrekning for SVG), skaleres etter optisk areal innenfor 13 × 34 mm, skjules når kunden er KodeWorks, og gir advarsel ved lav oppløsning.
- **Foto:** fyller alltid rammen, med fokus i øvre del og der bildet har mest detaljer. `Fotofokus` overstyrer.
- **«Generelt»:** venstrestilte kolonner, felles for alle listene og målt etter naturlige bredder. Overskuddet går til midtkolonnen. Lange perioder brytes ved parentesen, og korte lister deles aldri.
- **Sideskift i prosjekter:** toppen holdes sammen med to beskrivelseslinjer, og det er minst to linjer på hver side av et skift. Runde 6 krevde tre linjer, og det ga 25 % tomrom nederst på sidene.
- **Forside:** tospaltet er førstevalg. Stablet brukes når «Om» er lang, og kompetansen deles bare mellom grupper. Manglende felt gir ikke hull.
- **Tetthet:** bare 1 og 2, så brødteksten alltid er 9,5 pt. Autotilpasningen prøver seks varianter og vekter forsidekvaliteten tyngst.
- **Nye felt:** egne lister med tittel, beskrivelse på arbeidsforhold, kulepunkter i «Om», **fet** og mellomtitler, engelsk språk og fotofokus.
- **Orddeling:** ingen orddeling i kompetanse og nøkkelord, og URL-er brytes ved skråstrek.

Orkestratoren fant to tilbakeskritt mellom rundene og fikk dem rettet: Ninas forside ble 60 % tom i runde 6, og Påls kompetanse ble delt over sideskift i runde 7. Ved konsolideringen rettet orkestratoren også at datokolonnen var smalere enn datoer som ikke kan brytes. Det ga en boks som stakk 2 mm ut, og kolonnen dimensjoneres nå etter den bredeste av dem.

*Leveranse* (erstatter YAML-filene):
- `cv-mal.md` med veiledning i kommentarer;
- `cv-eksempel.md` med Påls eget portrett og kundelogoene fra hans CV på Drive, i `images/`;
- `cv-mal.pdf` (2 sider) og `cv-eksempel.pdf` (4 sider, siste side 94 %);
- `LESMEG.md`, skrevet om for Markdown.

Verifisering:
1. Hele korpuset er bygget fra Markdown med det konsoliderte skriptet: 20 ekte CV-er, 8 tester og eksempelet, alle uten feil.
   - `pdffonts` viser bare NON Natural Grotesk i alle 29.
   - Alle sider er sett i oversiktsark, og utsnitt i 300 dpi er lest av logoer, foto, «Generelt», sidebunner og forsider.
   - Ingen midtside er under 50 %. Laveste siste side er 37 % (13 prosjekter) og 38 % (bare navn, én side).
2. Eksempelet og malen er bygget i leveransemappen. Utsnitt av forside og prosjektblokk er lest i 200 dpi.
3. `pytest` består med 47 tester.

**Faktisk innsats videreutvikling:** 101m (veggklokke, fem trinn over estimatet på 30–40 min, som ikke ble justert da det sprakk). Årsak: hver runde bygget hele korpuset (28–29 filer, opptil seks varianter hver). Etter at brukeren påpekte det, ble testsettet snevret inn fra runde 9.

**Berørte filer videreutvikling:**
- leveransen: `deliverable/visualprofile/cv/` (`cv-mal.md`, `cv-eksempel.md`, PDF-ene, `images/`, `LESMEG.md`; YAML-filene er fjernet);
- CV-bygget: `src/build_cv_pdf.py`, `src/cv_pdf/cv-style.tex`, `src/cv_markdown.py` (ny), `src/font_guard.py` (ny);
- profilmanualen: `src/build_profile_manual.py`, `src/profile_manual/template.tex`, `deliverable/visualprofile/profile/profilmanual.md` og `.pdf`;
- kontroll-PDF-er og eldre generatorer: `src/build_md_pdf.py` (de 15 kontroll-PDF-ene i `background/visualprofile/` er bygget på nytt), `src/build_cv.py`, `src/build_cv_v2.py`;
- tester: `tests/test_platform_independence.py` og `tests/test_cv_markdown.py` (nye);
- `README.md`, `TASKS.md`.

Opprydding: `temp/T10.2v3b/`, med korpuset av personopplysninger, er slettet. `.claude/worktrees/` finnes ikke.

Åpne punkter:
- ~~Profilmanualens råd «eksporter fra en maskin der profilfonten er installert», og Word-regelen med profilfont og Arial-reserve, strider mot prinsippet om plattformuavhengighet.~~ Løst: manualen er skrevet om (se tillegget «fontregler uten installert font» i profiloppgaven).
- ~~CLAUDE.md nevner fortsatt fontinstallasjon og LibreOffice som tillatte verktøy, og systemfonter i PDF-standardkommandoen.~~ Løst med brukerens ja: fontinstallasjon fjernet, LibreOffice beholdt som tillatt generelt, standardkommandoen bruker fonter fra TeX Live.
- Fotofokus er en heuristikk, ikke ansiktsgjenkjenning.
- Enkelte originale logoer har lav oppløsning (advarsel gis).

**Tillegg – opprydding:** Brukeren godkjente versjon 3 («CV malen er god») og ba om at versjon 1 og 2 fjernes. `deliverable/visualprofile/cv/cv_v1/` og `cv_v2/` (Word-filer, PDF-er, JSON-kilder, grafikk) er slettet, og README har nå en kort merknad i stedet for de to avsnittene. Generatorene i `src/` (`build_cv.py`, `build_cv_v2.py`, `gen_cv_seismograph.py`, `check_cv_docx.py`, `arial_fallback.py`) er beholdt inntil videre. `seismograph.py` er generell og beholdes.
**Tillegg – mappenavn:** Brukeren påpekte at `deliverable/visualprofil` blandet norsk og engelsk, og at `cv_v3` var et levn. Mappen heter nå `deliverable/visualprofile/`, i samsvar med `background/visualprofile/`, og CV-malen ligger direkte i `deliverable/visualprofile/cv/`. Stiene er oppdatert i alle scripts i `src/`, i testen, i README, i oppgaveteksten og i malens kommentar. Første forsøk på å gi mappen nytt navn feilet med «Permission denied», fordi en prosess hadde CV-mappen åpen. Innholdet ble derfor flyttet over til en ny mappe, og den tomme gamle mappen ble slettet etterpå. Kontrollert: `pytest` (51 tester), profilmanualen, CV-mal og -eksempel, presentasjons- og dokumentmalen er bygget på nytt, og presentasjonskontrollen gir 12 PASS. Deretter fikk også undermappene engelske navn, i tråd med regelen om engelske mappenavn (brukerens ja): `profil` → `profile`, `presentasjon` → `presentation`, `dokument` → `document`, `bilder` → `images` (i `profile/`, `cv/` og `presentation/`) og `profile/assets/presentasjon` → `presentation`. Bildestier i malene, eksemplene og veiledningene, i scripts, tester, README og oppgaveteksten er oppdatert. Filnavn er uendret. Alt er bygget på nytt uten feil: profilmanualen, CV-mal og -eksempel, begge presentasjonene (presentasjonskontrollen gir 12 PASS), alle fire dokumentmalene og asset-eksporten (13 filer). 51 tester består.

#### T10.3 [x] Visittkort

Lag revidert visittkort (forside og bakside) i trykkeklart format, basert på 2021-visittkortene og den reviderte profilen. Eksempel for kontaktpersonen i `CLAUDE.md`, pluss en mal for andre ansatte.

**Leveranse:** `deliverable/visualprofile/business-card/` med:
- trykk-PDF per variant: 85 × 55 mm, 3 mm utfallende kant, skjæremerker, fonten innebygd og CMYK-verdier fra profilen dokumentert;
- en skjermversjon (PNG);
- malen, med kildefil i Markdown og byggescript i `src/` (samme verktøykjede som de andre malene: lualatex, fonten fra den lisensierte font-fila i repoet, fontkontrollen i `src/font_guard.py`);
- `LESMEG.md` med hvordan et nytt kort lages og bestilles.

Bygget skal virke likt på Windows, WSL2 og Linux, og bruker aldri fonter som er installert i operativsystemet.

**Akseptkriterier:** Riktig trimformat og utfallende kant. Tekst innenfor sikker sone, minst 3 mm fra trimkanten. En eventuell QR-kode er skannbar og peker til riktig adresse. Et nytt kort lages ved å endre navn, tittel og kontaktinformasjon på ett sted i Markdown-kilden.

**Verifisering:**

1. PDF-sidestørrelse og bleed kontrollert programmatisk (PyMuPDF: mediabox/trimbox).
2. `pdffonts` viser bare profilfonten, innebygd, og fontkontrollen (`src/font_guard.py`) består i bygget.
3. Begge sider rendret til PNG og lest med Read; et nytt kort generert for en fiktiv ansatt for å bevise at malen virker.

**Estimert innsats:** 34 min

**Faktisk innsats:** 8m 33s (veggklokke) fram til løsningsnotatet. Avviket på flere trinn under estimatet skyldes at verktøykjeden (fontutpakking, kerningrettinger, fontkontroll) kunne gjenbrukes fra presentasjonsbygget, og at profilmanualens visittkortside allerede ga mål og plassering.

**Berørte filer:** `deliverable/visualprofile/business-card/` (`visittkort-mal.md`/`.pdf`/`.png`, `visittkort-eksempel.md`/`.pdf`/`.png`, `LESMEG.md`), `src/build_business_card.py`, `src/business_card/card.tex`, `README.md`, `TASKS.md`

**Resolution:** Designet følger profilmanualens visittkortside, som er den reviderte formen av kortet fra 2021. Forsiden er grå med svart navnetrekk, 40 mm bredt og 6 mm fra øvre og venstre kuttkant. Kontaktblokken står nederst til venstre, 6 mm over nedre kuttkant: navn i Medium 9 pt, resten i Regular 8 pt. Baksiden er grønn med svart symbol, 28 mm høyt og midtstilt.

Et kort er en Markdown-fil der bare YAML-hodet brukes: `name` (påkrevd), `title`, `phone`, `email`, `web`. Felt som utelates, faller bort uten at resten flytter seg. Kontaktblokken er bunnjustert, og luften over kontaktlinjene settes bare når minst én slik linje følger. `build_business_card.py` fyller malen `card.tex` med pandoc og setter den med lualatex. Fontutpakking, kerningrettinger og fontkontroll importeres fra presentasjonsbygget.

Bygget kjører to ganger. Trykk-PDF-en lages i CMYK fra `farger.json`: arket er 105 × 75 mm, TrimBox er 85 × 55 mm og BleedBox ligger 3 mm utenfor, og skjæremerkene står i registreringsfarge utenfor den utfallende kanten. Navnetrekk og symbol skrives om fra RGB-svart til 100 % K. Skjermversjonen lages i profilens RGB-farger, fordi den første versjonen, rendret fra CMYK-fila, ga en matt grønnfarge. Neongrønnfargen kan ikke gjengis i CMYK; `LESMEG.md` anbefaler derfor Pantone 2267 som spotfarge for baksiden og dokumenterer CMYK- og PMS-verdiene, merket der de er forslag.

Kontrollene i bygget gir varsel og exit 1. De sjekker arkstørrelse, trimboks og utfallende kant; at tekst står minst 3 mm innenfor kuttkanten og minst 5 mm under navnetrekket; at bare profilfonten brukes og er innebygd; at det ikke finnes rasterbilder; og at ingenting tegnes eller skrives i RGB eller gråtone. LuaTeX setter selv en gråtone-svart i fargestakken mellom objekter. Fargekontrollen slår derfor bare ut når noe faktisk tegnes mens en ikke-CMYK-farge er aktiv. Den er også testet mot den originale RGB-logoen, og der slår den ut. Lange titler brytes over flere linjer.

Ingen QR-kode: profilmanualen viser kortet uten, og nettadressen står på kortet.

Tittelen på eksempelkortet, «Seniorkonsulent / daglig leder», er hentet fra 2021-kortet med skrivefeilen rettet, og bør bekreftes.

Verifisering:
1. PyMuPDF: arket er 105,00 × 75,00 mm, trimboksen 85,00 × 55,00 mm og den utfallende kanten 3,00 mm på alle fire sider, på begge sider av både malen og eksempelet. Minste avstand fra tekst til kuttkant er 5,48 mm.
2. `pdffonts` viser bare NONNaturalGrotesk-Medium og -Regular, innebygd som delsett. Fontkontrollen består i hvert bygg.
3. Hele trykkarket med skjæremerker og PNG-ene for malen og eksempelet er rendret og lest. Kort for en fiktiv ansatt (langt navn med bindestrek og Ø, langt e-postnavn, uten tittel) ble bygget uten varsel. Det samme gjaldt en tittel som brytes over to og fire linjer. En tittel på seks linjer ga varsel om avstanden til navnetrekket, med exit 1. Testkortene ligger bare i sesjonens midlertidige mappe.
4. `pytest`: 67 tester består, også testen for plattformuavhengighet.

`.docx` er ikke aktuelt for denne leveransen.

**Tillegg – detaljgjennomgang, visittkort fra CV-ene og språk:** Kortet ble først laget uten familiens arbeidsmetode (tre workere og læringslogg), og uten gjennomgang i 200–300 dpi eller sammenligning med selve 2021-kortet. Det ble tatt igjen av orkestratoren.

- **Detaljgjennomgang** av utsnitt i 300 dpi av navnetrekk, kontaktblokk og symbol: skarp vektorgrafikk og tekst, riktig kerning, symbolet står midt på baksiden.
- **Sammenligning med 2021-kortet** (`background/visualprofile/neue-delivery/Visittkort.pdf`): kortet følger bevisst profilmanualens reviderte form, med grå forside, stort svart navnetrekk, kontaktblokken nederst og grønn bakside med symbolet. 2021-kortet hadde seismografen på den grå siden og liten kontakttekst på den grønne. Det nye kortet har tydeligere rekkefølge (navnet i Medium) og telefonnummer med landkode.
- **Konklusjon:** ingen feil funnet. Ingen ny runde med workere ble kjørt.
- **Visittkort fra CV-ene:** brukeren ba om at visittkortene også kan lages fra CV-filene i Markdown. Nytt `src/build_cv_business_cards.py`:
  - leser navn, tittel, telefon og e-post med `src/cv_markdown.py`, med nettadressen `kodeworks.no` fast;
  - skriver kortfila og bygger med `src/build_business_card.py`, så oppsettet og trykkontrollene finnes bare ett sted;
  - legger `visittkort-<navn>.pdf` og `.png` ved siden av hver CV, eller i `--out`; `--dry-run` viser feltene;
  - har tester i `tests/test_cv_business_cards.py`.

  Alle 20 kort i `data/cv_md/` er bygget og består trykkontrollen. Lasses lange tittel brytes innenfor sikker sone, og Nina og Jonas får kort uten de feltene CV-en mangler.
- **Språk:** byggescriptet har engelske meldinger, og veiledningen heter `README.md` (se tillegget i oppgaven om engelske navn).


#### T10.4 [x] Presentasjonsmal

Lag en revidert presentasjonsmal basert på presentasjonsmalen fra 2022, Neue-presentasjonen og den reviderte profilen, med typiske lysbildetyper: tittel, seksjonsskille, tekst, tekst + bilde, to kolonner, sitat, nøkkeltall, kundelogoer/referanser, avslutning/kontakt.

**Format: bare PDF (brukerens beslutning, erstatter `.pptx`-sporet).** LibreOffice er forbudt i familien (punkt 4 i arbeidsmetoden), og uten den kan en `.pptx` ikke kontrolleres visuelt. Brukeren valgte derfor å droppe `.pptx`/Google Slides helt: presentasjoner skrives i Markdown og settes direkte til PDF med pandoc + lualatex (beamer med eget KodeWorks-tema; lualatex fordi den installerte xelatex mangler norsk orddeling, og for å gjenbruke profilmanualens fontoppsett med kerning-rettinger), samme verktøykjede som profilmanualen og CV-malen versjon 3. Ingen `.pptx`, ingen LibreOffice, PowerPoint-COM, unoconv eller andre kontorpakke-rendrere — heller ikke for workerne. Arbeidet fra første runde med `.pptx`-generator (layoutnavn, pandoc-funn, SVG → DrawingML) brukes ikke videre.

**Leveranse:** `deliverable/visualprofile/presentation/` med `presentasjonsmal.md` + `.pdf` (mal som viser og forklarer alle lysbildetypene), `eksempel.md` + `.pdf` (realistisk KodeWorks-innhold, alle lysbildetypene), og `LESMEG.md` (hvordan en konsulent skriver en presentasjon i Markdown og bygger PDF, Markdown-syntaksen for hver lysbildetype, sjekkliste). Byggescript i `src/` (f.eks. `src/build_presentation.py`) med tema og Lua-filter i `src/` (f.eks. `src/presentation/`).

**Akseptkriterier:** (1) **Vakkert** etter punkt 5 og 8 i arbeidsmetoden: ved gjennomgang i 70 dpi og 200–300 dpi skal orkestratoren mene at resultatet ser bedre ut enn 2022-malen og Neue-presentasjonen; ingen kornete raster, grå kanter eller myk logo; god sperring; rolig rytme i luft og linjer. (2) Alle lysbildetypene finnes og kan lages fra vanlig pandoc-Markdown (attributter/klasser der det trengs): tittel, seksjonsskille, tekst, tekst + bilde, to kolonner, sitat, nøkkeltall, kundelogoer/referanser, avslutning/kontakt. (3) Profilreglene: farger, typografi (Light titler, Regular brødtekst, Medium utheving), fargeutheving i titler, seismografen aldri bak tekst, kontrast. (4) Robust: lange titler, mange punkter og manglende felt gir ikke overflyt eller ødelagt layout. (5) All grafikk er vektor (logo, symbol, seismograf fra profilens SVG-er via PDF); bare foto er raster. Fonten er innebygd i PDF-en (tillatt etter lisensen).

**Verifisering:**

1. Mal og eksempel bygget; `pdffonts` viser bare NON Natural Grotesk (innebygd).
2. Alle sider lest i 70 dpi, og utsnitt av typografi, logo, seismograf og footer lest i 200–300 dpi.
3. Robusthetstest: et testdeck med lang tittel, mange punkter, manglende felt og alle lysbildetypene bygget og lest.
4. PyMuPDF bekrefter at logo/symbol/seismograf er vektor (ingen rasterbilder utenom foto).
5. Læringslogg (`temp/T10.4/LAERING.md`) viser rundene, feilene og hvordan arbeidsmetoden ble justert.

**Estimert innsats:** 55 min

**Faktisk innsats:** 107m 55s (veggklokke). Inkluderer venting på to avklaringer underveis (forbudet mot LibreOffice og valg av format) og en forkastet første runde med `.pptx`; det forklarer avviket på nesten to trinn fra estimatet.

**Berørte filer:** `deliverable/visualprofile/presentation/**` (`presentasjonsmal.md`/`.pdf`, `eksempel.md`/`.pdf`, `LESMEG.md`, `images/foto_team1.jpg`, `images/foto_team3.jpg`), `src/build_presentation.py`, `src/check_presentation_pdf.py`, `src/presentation/` (`beamerthemekodeworks.sty`, `filter.lua`, `template.tex`, `kernfix.json`), `temp/T10.4/LAERING.md`, `README.md`, `TASKS.md`

**Resolution:** Første runde fulgte den opprinnelige task-teksten (`.pptx`-mal med lysbildemaster). Tre workere (Sonnet, medium) laget en python-pptx-generator med elleve layouter, en SVG → DrawingML-konverter, et kontrollscript og eksempelinnhold. Briefen tillot LibreOffice for visuell kontroll; orkestratoren hadde lest arbeidsmetoden ved sesjonsstart, før forbudet mot LibreOffice ble lagt inn fra den parallelle CV-sesjonen, og leste den ikke på nytt før briefen. Én worker kjørte LibreOffice én gang før stoppbeskjeden nådde fram. Forbudet ble deretter lagt inn i denne subtasken, og fordi en `.pptx` ikke kan kontrolleres visuelt uten en kontorpakke, valgte brukeren bare PDF. `.pptx`-arbeidet ble forkastet; bare innholdet fra første runde ble gjenbrukt.

Andre runde (PDF-sporet), tre workere parallelt: formgiver laget beamer-temaet og Lua-filteret (absolutt plassering i mm, Markdown-klasser per lysbildetype); produksjon laget byggescriptet (fonter fra den lisensierte zip-en, vektorgrafikk fra profilens SVG-er, lualatex to ganger, varsler med lysbildetittel), PDF-kontrollen og et robusthetsdeck; merkevare skrev eksempelet (14 lysbilder, fakta kontrollert mot kildene, tall merket 2023), malen og veiledningen. Produksjonsworkerens integrasjonsfunn (unicode-math/`Path=`, babel lastes av pandoc, `\fontsize` må settes eksplisitt) ble sendt videre til formgiveren mens den arbeidet.

Foto: profilens bilder er 1400 px brede. Etter tips fra brukeren ble originalene hentet fra kodeworks.no (`/static/photos/`, 2000–4096 px). Prosjektbildene på nettsiden og i masterpresentasjonen ser ut som stockfoto med ukjent rett og brukes ikke. Kundelogoene finnes bare som små PNG-er, så kundene settes som tekst i fliser.

Konsolidering (orkestrator), feil funnet og rettet: tankestrek ble «--» og apostrofen rett, fordi `\newfontfamily`-fontene manglet `Ligatures=TeX`; «39,7 MNOK» ble satt mindre enn de andre tallene (enheten er flyttet til forklaringen); adressene på avslutningen brøt midt i (to linjer); byggescriptet meldte manglende bilde for et kodeeksempel i et talernotat (kode blankes ut før sjekken); varselet om for mye tekst ble kuttet i loggen (`max_print_line`); `--notes` overskrev den vanlige PDF-en (gir nå `<deck>-notater.pdf`). Robusthetsdecket avdekket at lang åpningstittel kolliderte med presentatør/dato, at mange punkter og langt avsnitt fløt inn i footer og ut av siden, at lange kundenavn gikk ut av flisene, og at avslutning uten kontakter var nesten tom.

Tredje runde (formgiver): innhold måles og settes i 20 pt, så 18 pt, så bredere, og til slutt skalert med varselet «For mye tekst på lysbildet …: del det i to» (skalering valgt framfor klipping, fordi klipping fjerner innhold uten at noen ser det); åpningen er én blokk forankret i bunn med størrelsestrapp 58/44/36 pt; kundeflisene har ingen orddeling og størrelsestrapp 24/20/16 pt; avslutning uten kontakter viser KodeWorks' felles kontaktinformasjon; kern-par foran kolon (bl.a. «r:» −40) etter måling. `LESMEG.md` ble rettet mot faktisk oppførsel (logoer bare som PDF, enhet i forklaringen, krymping og varsel, bildeoppløsning, navnet på notatversjonen).

Verifisering:

1. Mal (10 sider) og eksempel (14 sider) bygget fra prosjektroten med `src/build_presentation.py`; `pdffonts` viser bare NON Natural Grotesk Light, Regular og Medium, innebygd. `check_presentation_pdf.py`: 0 WARN, 0 FAIL på begge.
2. Alle sider lest i 70 dpi; utsnitt i 200–300 dpi av åpning, footer med navnetrekk, nøkkeltall, seismograf og punkttegn/tankestrek lest. Sammenlignet med 2022-malen og Neue-presentasjonen: tydeligere hierarki, fargeutheving, gjennomgående footer, vektorgrafikk og bedre luft.
3. Robusthetsdecket (16 sider: tittel på tre linjer, åtte punkter med to nivåer, svært langt avsnitt, sitat uten kilde, ett og fire nøkkeltall, åtte lange kundenavn, `.image` uten bilde, avslutning uten kontakter, YAML uten undertittel og dato) bygget og lest: ingen overflyt, kontrollen 0 FAIL, og byggescriptet varsler de to bevisst overfylte lysbildene.
4. PyMuPDF: de eneste rasterbildene er de to fotoene (2000 × 1333); navnetrekk, symbol og seismograf er vektor.
5. Læringsloggen `temp/T10.4/LAERING.md` viser de tre rundene, feilene, rotårsakene og endringene i arbeidsmetoden.

Varige lærdommer for resten av familien: (1) les arbeidsmetoden i `TASKS.md` på nytt rett før hver brief, fordi andre sesjoner endrer den; (2) sett `Ligatures=TeX` på alle fontspec-familier; (3) absolutt plassering krever måling av innhold og et testdeck som presser layouten; (4) høyoppløste originalfoto finnes på kodeworks.no; (5) send integrasjonsfunn mellom workere mens de arbeider.

Opprydding: `temp/T10.4/` slettet unntatt `LAERING.md`. `.claude/worktrees/` finnes ikke (ingen agent-worktrees opprettet). Fire midlertidige byggemapper (`kwdeck_*`, med utpakkede fontfiler) fra workernes `--keep-build` ligger i systemets temp-mappe; workerens sletting ble avvist av tillatelsessystemet, og sletting venter på brukerens svar. Slettet ved avslutningen av familien (se løsningsnotatet for samleoppgaven).

Åpne punkter: profilmanualens side «Presentasjon» sier fortsatt at PowerPoint og Google Slides bruker Arial, og beskriver ikke PDF-sporet — bør rettes i manualen; kerningtabellen ligger både i `kernfix.json` og innebygd i temaets `.sty`; tabeller og kodeblokker er ikke stilet eller testet i målingen; kundelogo-lysbildet (`.logos`) er ikke testet med ekte logofiler; samtykke for personene på fotoene bør bekreftes før ekstern bruk; tallene i eksempelet er fra 2023.

#### T10.5 [x] Dokumentmal for A4, med brev som variant

Lag én felles mal for A4-dokumenter fra KodeWorks, med salgsbrev / henvendelser til kunder som én variant. Bakgrunnen er at utlysninger av konsulentoppdrag, salgsbrev, tilbud og notater har nesten samme grunnform: navnetrekk, tittel, en blokk med fakta, brødtekst med overskrifter og lister, og avsender eller kontaktperson til slutt. Én mal per dokumenttype ville gi mange nesten like maler som glir fra hverandre. Nye behov legges derfor inn som elementer i den felles malen, ikke som lokale løsninger i hvert dokument, og malen vokser etter hvert som flere dokumenttyper tas i bruk.

Malen bygger på 2021-brevarkene (print og skjerm), den reviderte profilen og CV-malen versjon 3, som er familiens A4-uttrykk (marger, grønn L-ramme og seismografstrek, Light-overskrifter, små etiketter i Medium med sperring, grønne punkttegn, avslutningsfigur med navnetrekket). Maskineriet fra presentasjonsmalen og CV-malen gjenbrukes: fonten fra den lisensierte zip-en, `kernfix.json`, `font_guard.py`, vektorgrafikk fra profilens SVG-er og pandoc → lualatex.

**Varianter:**

- **Brev:** brevhode med navnetrekk, avsender og mottaker, dato, «Deres ref.» / «Vår ref.» (valgfrie), emne, brødtekst, hilsen og signatur (navn, tittel, kontaktinfo), og bunntekst med selskapsinformasjon (selskapsnavn, org.nr. og adresser fra `CLAUDE.md`; avsenderselskap velges i YAML blant de fire selskapene, KodeWorks AS som standard).
- **Dokument:** tittel og eventuelt undertittel, faktaboks, brødtekst og kontaktblokk, uten mottakerfelt. Typiske bruksområder er utlysning av konsulentoppdrag, notat og tilbud.

**Elementer begge varianter har:** overskrifter i to nivåer, punktlister og nummererte lister, utheving, faktaboks, to kolonner (for eksempel «Må ha» og «Fint å ha»), kontaktblokk, enkel tabell og topp-/bunntekst som gjentas riktig fra side 2. Faktaboksen lages automatisk av linjer på formen `**Etikett:** verdi` rett etter tittelen, slik at et vanlig Markdown-dokument bygger pent uten ekstra markering; de andre elementene markeres med pandoc-klasser (`::: {.columns}` o.l.).

**Format: bare PDF.** Arbeidsmetoden forbyr LibreOffice i familien (punkt 4), og uten den kan en `.docx` ikke kontrolleres visuelt. CV-malen og presentasjonsmalen har av samme grunn gått over til Markdown → PDF etter brukerens beslutning, og denne malen følger det. Fontlisensen tillater dessuten innebygd font bare i PDF. Ingen `.docx`, ingen LibreOffice, Word-COM eller andre kontorpakke-rendrere — heller ikke for workerne. Trengs en Word-variant senere, bestilles den som egen oppgave.

**Leveranse:** `deliverable/visualprofile/document/` med `dokumentmal.md` + `.pdf` (mal som viser og forklarer alle elementene), `brevmal.md` + `.pdf` (tom brevmal), `eksempel-brev.md` + `.pdf` (realistisk salgsbrev om et KodeWorks-tilbud, i prosjektets tone: konkret og faktabasert, minst én variant over to sider), `eksempel-utlysning.md` + `.pdf` (bygget på utlysningen av Android-oppdraget i `deliverable/`), og `LESMEG.md` (hvordan en konsulent skriver og bygger et dokument eller brev, syntaksen for hvert element, sjekkliste). Byggescript i `src/` (`src/build_document.py`) med stil og Lua-filter i `src/document/`.

**Akseptkriterier:** (1) **Vakkert** etter punkt 5 og 8 i arbeidsmetoden: ved gjennomgang i 70 dpi og 200–300 dpi skal orkestratoren mene at resultatet ser bedre ut enn 2021-brevarkene og er i familie med CV-malen versjon 3. (2) Begge variantene og alle elementene over kan lages fra vanlig pandoc-Markdown. (3) Brevhode og bunntekst ligger i topp-/bunntekst og gjentas riktig fra side 2; selskapsinformasjonen er korrekt. (4) Robust: lange titler, lange mottakeradresser, manglende felt, mange punkter og flere sider gir ikke overflyt eller ødelagt layout. (5) All grafikk er vektor; fonten er innebygd i PDF-en (tillatt etter lisensen); bare NON Natural Grotesk brukes. (6) Den opprinnelige utlysningsfila i `deliverable/` bygger uendret med malen, som bevis på at et vanlig Markdown-dokument fungerer. (7) Eksemplene står på egne ben for en ekstern mottaker.

**Verifisering:**

1. Alle leveransene bygget; `pdffonts` viser bare NON Natural Grotesk (innebygd).
2. Alle sider lest i 70 dpi, og utsnitt av brevhode, faktaboks, lister, kontaktblokk og bunntekst lest i 200–300 dpi.
3. Robusthetstest: testdokumenter med lang tittel, lang mottakeradresse, manglende felt, mange punkter, tabell og tre sider bygget og lest.
4. Org.nr. og adresser i bunnteksten kontrollert mot `CLAUDE.md`.
5. PyMuPDF bekrefter at all grafikk er vektor (ingen rasterbilder).
6. Læringslogg (`temp/T10.5/LAERING.md`) viser rundene, feilene og hvordan arbeidsmetoden ble justert.

**Estimert innsats:** 55 min (utvidet fra 34 min da brevmalen ble gjort til en felles dokumentmal)

**Kobling:** utvidet etter at utlysningen av Android-oppdraget (`deliverable/2026-11-11_konsulentoppdrag_android_kotlin.md`) viste at dokumenttypene deler grunnform; bygger på T10.2 (CV-mal v3) og T10.4 (presentasjonsmal).

**Faktisk innsats:** 44m 31s (veggklokke, inkludert utvidelsen av oppgaveteksten)

**Berørte filer:** `deliverable/visualprofile/document/**` (`dokumentmal.md`/`.pdf`, `brevmal.md`/`.pdf`, `eksempel-brev.md`/`.pdf`, `eksempel-utlysning.md`/`.pdf`, `LESMEG.md`), `src/build_document.py`, `src/check_document_pdf.py`, `src/document/` (`kwdocument.sty`, `filter.lua`, `template.tex`), `temp/T10.5/` (`LAERING.md`, `spesifikasjon.md`, `tester/`), `README.md`, `TASKS.md`

**Resolution:** Oppgaveteksten ble først utvidet fra salgsbrevmal til felles A4-dokumentmal med brev som variant, og formatet ble satt til bare PDF i tråd med arbeidsmetoden og de to andre malene. Orkestratoren leste arbeidsmetoden på nytt, gjennomgikk 2021-brevarkene og CV-malen versjon 3 (rendret), og skrev en felles spesifikasjon (`temp/T10.5/spesifikasjon.md`) med Markdown-kontrakten (YAML-felt, automatisk faktaboks, klasser), selskapsdata og teknisk grunnlag, slik at tre workere kunne arbeide parallelt.

Runde 1, tre workere (Sonnet, medium) parallelt: formgiver laget stil, Lua-filter og byggescript (gjenbruker hjelpefunksjonene i `build_presentation.py` ved import, håndhever `font_guard.py`); produksjon laget kontrollscriptet med selvtest og et robusthetskorpus på ni testdokumenter; merkevare skrev eksempelbrevet (fiktiv mottaker, kontrollert mot Brreg: ingen treff), utlysningseksempelet, de to tomme malene og LESMEG. Produksjonens og merkevarens anbefalinger ble sendt til formgiveren mens den arbeidet (regel for faktaboksen, tittel i både YAML og `#`, varsler, bunntekstsone, ingen «Norge»-linje og intet komma etter hilsenen).

Orkestratorens gjennomgang (70 dpi og 220–300 dpi) fant og fikk rettet i runde 2 (formgiver alene, med konteksten intakt): fet skrift forsvant i listepunkter (sans-familien manglet fet vekt), emnelinjen kolliderte med lang mottakerblokk, enkeltord alene på siste tittellinje, topptekst kuttet midt i, telefonnummer i signaturen trukket ut i margen (microtype-protrusjon), ulik L-ramme mellom sidene og ulik stil på kontaktblokker. Ved konsolideringen ble filene flyttet til `src/`, og orkestratoren rettet selv: hilsen og signatur kunne havne alene på en ny side (siste avsnitt og overskriften foran holdes nå sammen med signaturen), eksempelbrevet var tre sider (kortet til to), «I dag er vi 27 utviklere» var et 2023-tall (omskrevet med årstall), plassholdere i brevmalen ga enkeltord på egen linje, «1 sider» i byggemeldingen, og LESMEG ble rettet mot faktisk oppførsel.

Utformingen: venstremarg 20 mm og tekstspalte 145 mm som i CV-malen, Light-titler, Regular brødtekst 10/14,4 pt, Medium utheving og etiketter i versaler med sperring. Brevet har navnetrekk øverst til venstre, returadresse og mottaker plassert for vinduskonvolutt, dato og referanser øverst til høyre, og emnelinje i Light. Faktaboksen står på grå flate med grønn venstrekant. Bunnteksten viser selskap, org.nr., begge kontoradresser, kodeworks.no og sidetall (ved flere sider), med grønn L-ramme og seismografstrek på første og siste side. Grønt brukes bare som aksent.

Verifisering:

1. Alle fire leveranser bygget fra prosjektroten med `src/build_document.py` uten varsler (eksempelbrev 2 sider, utlysning 2, dokumentmal 2, brevmal 1). `pdffonts` viser bare NON Natural Grotesk Light, Regular og Medium, innebygd. `check_document_pdf.py`: 0 WARN, 0 FAIL på alle.
2. Alle sider lest i 70 dpi; utsnitt i 220–300 dpi av brevhode, faktaboks, nummerert liste med fet innledning, to kolonner, overskrifter, kontaktblokk og bunntekst med ramme. Sammenlignet med 2021-brevarkene: tydelig hierarki, ryddig brevhode og bunntekst med korrekt selskapsinformasjon, vektorgrafikk og i familie med CV-malen.
3. Robusthetskorpuset (`temp/T10.5/tester/`, ti filer: kort brev, brev over tre sider, brev uten felt, sju linjers mottaker med to avsendere, alle elementer, uten YAML, 25 punkter med overlange ord og spesialtegn, tom, Oslo-selskap, fet og kursiv i alle elementer) bygget og lest: ingen overflyt, forventede varsler (manglende felt, «✓» som fonten mangler), kontrollen 0 FAIL. Den uendrede utlysningsfila i `deliverable/` bygger til to sider uten varsler, med automatisk faktaboks og kontaktblokk.
4. Org.nr. og adresser for alle fire selskaper i `filter.lua` er kontrollert mot `CLAUDE.md`, og kontrollscriptet bekrefter bunnteksten på hver side for valgt selskap.
5. PyMuPDF: ingen rasterbilder i noen av leveransene; navnetrekk, ramme og strek er vektor.
6. Læringsloggen `temp/T10.5/LAERING.md` viser rundene, feilene, rotårsakene og lærdommene.

Varige lærdommer for familien (også i læringsloggen): (1) en felles spesifikasjon av kildeformatet gjør at innhold, kontroll og stil kan lages parallelt; (2) workere må rendre på nytt etter hver endring, fordi en gammel PNG skjulte en manglende ramme; (3) fet skrift må testes i alle elementer, fordi en fontfamilie uten fet vekt faller stille tilbake til Regular; (4) slutten av et brev (siste avsnitt, hilsen og signatur) må holdes samlet.

Opprydding: workermappene i `temp/T10.5/runde1/` er slettet; `LAERING.md`, `spesifikasjon.md` og testkorpuset i `tester/` er beholdt for senere utvidelser av malen. Ingen byggemapper fra dokumentbygget ligger igjen i systemets temp-mappe. `.claude/worktrees/` finnes ikke.

Åpne punkter: malen er ikke testet med bilder eller med en lang tabell som brytes over sider; fonten mangler blant annet «✓» (bygget varsler og utelater tegnet); tallene i eksempelbrevet er fra 2023; presentasjonsbygget bruker fortsatt ikke `font_guard.py`; hjelpefunksjonene deles ved import fra `build_presentation.py` og bør på sikt flyttes til en felles modul; profilmanualen omtaler ikke dokumentmalen. Ingen Word-variant er laget; den må eventuelt bestilles som egen oppgave.

### T11 [x] Script for nedlasting av CV-er fra Google Drive

Ansattes CV-er ligger som Google-dokumenter på Drive. Lag et script som laster dem ned til en arbeidsmappe i repoet, slik at CV-grunnlaget i `background/cver/` kan oppdateres. Bruk scriptet til å laste ned alle CV-ene, og lag en prosjekt-skill som beskriver prosedyren. Som del av arbeidet settes et Python-prosjektmiljø opp (pyproject, låste avhengigheter, tester, venv per OS), etter mønster fra naboprosjektene `../jobs` (Drive-nedlasting, OAuth, CV-liste) og `../fjordgata30` (venv per OS, skills-mappe).

**Verifisering:**

1. Enhetstester for de rene funksjonene består med `pytest --timeout=3`.
2. Alle CV-er i lista lastes ned uten feil til `data/cv/`, og filene er gyldige `.docx`/`.pdf`.
3. Fildatoen på hver fil er lik «sist endret» på Drive.
4. Ny kjøring laster ikke ned CV-er som er uendret på Drive.

**Estimert innsats:** 13 min

**Faktisk innsats:** 3m 56s (veggklokke, før løsningsnotatet ble skrevet)

**Kobling:** gjenbruker nedlastingslogikk fra `../jobs/src/jobs/drive_download.py`; nedlastede filer er kilde for videre konvertering til `background/cver/` etter samme mønster som T2.

**Berørte filer:** `src/download_cvs.py` (ny), `tests/test_download_cvs.py` (ny), `cv_sources.csv` (ny), `pyproject.toml`, `uv.lock`, `.python-version`, `.gitignore` (nye), `secrets/credentials.json` + `secrets/token.json` (git-ignorert), `data/cv/` (20 filer, git-ignorert), `.claude/skills/last-ned-cver/SKILL.md` + `.claude/skills/README.md` (nye), `README.md`, `CLAUDE.md`, `TASKS.md`

**Resolution:** Python-miljø: `pyproject.toml` (ikke-pakke, Python ≥ 3.11) med Google API-bibliotekene som avhengigheter og `pytest` + `pytest-timeout` som dev-gruppe; `uv sync` laget `.venv` og `uv.lock`. Scripts med PEP 723-blokk (visuell profil, CV-generering) er urørt og kjører fortsatt i egne miljøer. Venv per OS fra fjordgata30 er tilpasset: Windows bruker uv-standarden `.venv` (så verktøy og AI-sesjoner uten ekstra miljøvariabel treffer riktig mappe), WSL2/Linux bruker `.venv-linux` via `UV_PROJECT_ENVIRONMENT`. Oppsett, aktivering og tester er dokumentert i README «Python-oppsett»; CLAUDE.md har fått en kort regel om prosjektmiljø, venv per OS og skills-mappen.

`src/download_cvs.py` leser `cv_sources.csv` (kopi av CV-lista i `../jobs`, 20 personer, `Name;Link;Intern;`), henter metadata per fil og eksporterer Google-dokumenter som `.docx` (valgfritt `pdf`/`txt`/`odt`); opplastede filer lastes ned uendret. Filnavn er dokumentnavnet på Drive. Standard målmappe er `background/new/cver/<dagens dato>/`, slik at eldre nedlastinger i innboksen aldri overskrives; eksisterende filer hoppes over uten `--overwrite`. OAuth-klient og token ble kopiert fra `../jobs/secrets/` til git-ignorert `secrets/`; tokenet lastes uten å snevre inn scope, så det fungerer uten ny godkjenning. Ny godkjenning ber bare om `drive.readonly`.

Verifisering:

1. 9 tester (fil-ID fra ulike lenkeformer, filnavnrensing, filendelse, CSV-lesing) består på 0,6 sek.
2. Alle 20 CV-er lastet ned til `background/new/cver/2026-11-11/` (0 feil): 18 eksportert som `.docx`, én opplastet `.pdf` (Jonas Dalseth), og to dokumenter som ikke heter «Master CV»: `CV_Eirik_Larsen.docx` og `Oppsummering - Nina Johannessen.docx` (7 KB — trolig et sammendrag, ikke full CV). `file` bekrefter gyldige Word/PDF-filer. Fem personer er nye mot september-settet: Eirik Larsen, Filip Henrik Larsen, Lars Ødegaard, Nina Johannessen og Jonas Dalseth.
3. Ny kjøring med navnefilter ga `SKIP` på alle tre treff. Konsollen viste æøå feil på Windows; rettet ved å sette stdout/stderr til UTF-8.

**Tillegg – målmappe og fildato:** Brukeren presiserte at `background/new/` ikke er riktig sted for nedlastede filer: CV-ene skal ligge i `data/cv/`, én flat mappe uten undermapper, og `data/` skal være utenfor git. Fildatoen skal vise når CV-en sist ble endret, i samsvar med endringsdatoen på Google Drive. Endret i `download_cvs.py`: standard `--out` er `data/cv`; metadata henter også `modifiedTime`, og filens mtime settes til den etter nedlasting. Med riktig fildato kan scriptet avgjøre om en fil er utdatert: den lastes ned på nytt bare når den mangler eller tidspunktet avviker fra Drive (toleranse 1 sek); `--force` laster ned alt. Dette erstatter `--overwrite`/hopp-over-oppførselen, som ellers ville latt utdaterte versjoner bli liggende i en flat mappe. `data/` lagt i `.gitignore`. To nye tester (tidspunkt-parsing og sammenligning) — 11 tester består. Alle 20 CV-er lastet ned til `data/cv/` (endringsdatoer fra 2021-08-09 til 2026-09-22, som stemmer med datoene scriptet rapporterte fra Drive); ny kjøring ga 0 nedlastet, 20 hoppet over. Datomappen `background/new/cver/2026-11-11/` fra første kjøring slettet. README, skill-en og mappeoversikten i CLAUDE.md oppdatert.

Ikke gjort (ikke bestilt): konvertering av de nye filene til Markdown i `background/cver/`, og opprydding av september-originalene i `background/new/cver/`.

### T12 [x] Konvertere alle CV-er til Markdown i malformatet (engangsjobb)

Fremover skal CV-ene ligge som Markdown på Google Drive. PDF lages ved å synke fra Drive og kjøre byggescriptet for CV-malen. Denne oppgaven er overgangen: alle de 20 CV-ene i `data/cv/` (18 Word-filer og én PDF, lastet ned fra Drive) skal konverteres én gang til Markdown i malformatet. Hver fil skal bygges til PDF etter malen uten manuelle grep, og alle filene skal følge de samme konvensjonene, slik at de ser like ut og kan vedlikeholdes på samme måte. Formatet er beskrevet i `src/cv_markdown.py` og i `deliverable/visualprofile/cv/LESMEG.md`. `cv-eksempel.md` i samme mappe er forbildet.

**Leveranse:** én mappe per person i `data/cv_md/` (git-ignorert, fordi CV-ene er personopplysninger), klar til å lastes opp til Drive:

```
data/cv_md/<fornavn-etternavn>/
├── <fornavn-etternavn>.md
├── <fornavn-etternavn>.pdf      – bygget med src/build_cv_pdf.py, for kontroll
└── images/
    ├── foto.jpg                 – portrettet fra originalen (eller ingen fil, og Foto-linjen utelates)
    └── logo-<kunde>.<png|svg>   – kundelogoer fra originalen, ett filnavn per kunde
```

I tillegg skal det lages:
- `src/check_cv_md.py`: kontrollerer at en CV-fil følger konvensjonene under, og skriver avvik per fil;
- en samlet avviksliste `data/cv_md/AVVIK.md` med det konsulentene selv bør rette.

**Konvensjoner (det som gjør filene uniforme):**

1. **Trofast innhold.** Ingen tekst diktes opp, og språket skrives ikke om. Bare form normaliseres. Åpenbare feil i originalen beholdes, men føres i avvikslista. Eksempler: kopierte beskrivelser, nøkkelord fra feil prosjekt og skrivefeil.
2. **Rekkefølge og seksjoner.** Navn (`#`), tittel, kontaktliste, `## Om <fornavn>`, `## Teknisk kompetanse`, `## Erfaring`, `## Arbeidserfaring`, `## Utdanning`, `## Sertifiseringer`, og deretter eventuelle egne lister. Utelat seksjoner som ikke har innhold.
3. **Kontaktlista** har alltid denne rekkefølgen og disse etikettene: Telefon (`+47 000 00 000`), E-post, Erfaring (`N år`), Språk (små bokstaver, kommaseparert) og Foto. Felt som mangler i originalen, utelates.
4. **Prosjekter** står med nyeste først. Overskriften er rollen. Lista under har Kunde, Prosjekt, Periode og Logo i den rekkefølgen. Prosjekt utelates når det er likt kunden. Beskrivelsen kommer deretter, og «Nøkkelord:» står til slutt. Kulepunkter skrives som Markdown-lister, ikke som «\-»-tekst.
5. **Perioder** skrives som `MM.ÅÅÅÅ – MM.ÅÅÅÅ`, `MM.ÅÅÅÅ – nå` eller `ÅÅÅÅ – ÅÅÅÅ`, med tankestrek og mellomrom. «d.d.», «dd» og «present» blir «nå». Tillegg står i parentes etter perioden.
6. **Lister i «Generelt»** har formen `periode | navn | sted`. Verv, foredrag, publikasjoner, utmerkelser, kurs og lignende legges i egne lister med faste titler: «Verv og engasjement», «Foredrag og publikasjoner», «Kurs» og «Utmerkelser». De skal ikke ligge under Sertifiseringer.
7. **Kompetanse** grupperes som i originalen, med originalens gruppenavn i vanlig setningsform («Infrastruktur og DevOps», ikke «INFRASTRUKTUR OG DEVOPS»). Elementene skrives med komma mellom. Hele setninger skrives som punktliste. Duplikater fjernes.
8. **Bilder:** foto og logoer pakkes ut fra originalen. Hver logo kontrolleres visuelt mot riktig prosjekt. Tomme plassholdere (1 × 1 piksel, silhuetter) brukes ikke. Logoer navngis etter kunden (`logo-equinor.png`), og samme kunde bruker samme fil.
9. **Engelsk CV** (hvis noen er det) bruker engelske overskrifter og etiketter. Ellers er alt på norsk.
10. **CV-er som ikke følger 2023-malen** konverteres med skjønn etter de samme konvensjonene, og det som ikke fikk plass, føres i avvikslista. Det gjelder oppsummeringen til Nina Johannessen, legens CV til Lasse Holanger, den eldre CV-en til Eirik Larsen og PDF-en til Jonas Dalseth.

**Arbeidsmetode: agent-orkestrering**

- Hovedsesjonen er orkestrator. Den skriver først `src/check_cv_md.py` og en felles brief med konvensjonene over.
- Deretter kjører tre workere (Sonnet, medium effort) parallelt. Hver konverterer 6–7 CV-er, skriver til sin egen mappe `temp/T12/<a|b|c>/`, bygger hver fil med `src/build_cv_pdf.py` og kjører kontrollscriptet til det ikke gir avvik.
- Orkestratoren går gjennom resultatet: kontrollscriptet på alle 20, oversiktsark av alle PDF-er, og utsnitt av et utvalg på 6. Deretter flytter den filene til `data/cv_md/`, samler avvikslista og sletter `temp/T12/`.
- Workerne følger de vanlige shell-reglene: én fil per kommando, `timeout 100` og ingen git.

**Verifisering:**

1. `src/check_cv_md.py` gir ingen avvik på noen av de 20 filene. Kontrollscriptet har tester i `tests/`, og `pytest --timeout=3` består.
2. Alle 20 bygges til PDF med `src/build_cv_pdf.py` uten feil. `pdffonts` viser bare NON Natural Grotesk. Advarsler (f.eks. logo med lav oppløsning) står i avvikslista.
3. Rundtur: parse → render → parse gir samme data for alle 20.
4. Oversiktsark av alle PDF-er er sett gjennom. Utsnitt av 6 CV-er (Pål, Nina, Lasse, Ørjan, Sindre og Jonas) er lest, og foto og logoer er kontrollert mot riktig prosjekt.
5. Stikkprøve av innholdet: for 3 CV-er er alle prosjekter, perioder og nøkkelord sammenlignet med originalen, uten tap.

**Estimert innsats:** 55 min

**Kobling:** bygger på T10.2 (formatet, `src/cv_markdown.py` og `src/build_cv_pdf.py`) og T11 (originalene i `data/cv/`). Oppfølging, ikke del av denne oppgaven: opplasting av `data/cv_md/` til Drive, og å utvide `src/download_cvs.py` og skillen `download-cvs` til å synke Markdown-filer og bilder fra Drive. Pandoc-utskriftene i `background/cvs/` er ikke i malformatet og røres ikke her.

**Berørte filer:** `data/cv_md/**` (ny, git-ignorert), `src/check_cv_md.py` (ny), `tests/test_check_cv_md.py` (ny), `README.md`, `TASKS.md`

**Faktisk innsats:** 31m 32s (veggklokke)

**Resolution:** Orkestratoren skrev først kontrollskriptet `src/check_cv_md.py`, med 13 tester i `tests/test_check_cv_md.py`. Skriptet kontrollerer:
- seksjonsrekkefølge, «Om <fornavn>» og faste titler på egne lister;
- kontaktliste i fast rekkefølge, med telefon som `+47 000 00 000`, «N år» og språk med små bokstaver;
- prosjekter med nyeste først, felt i rekkefølgen Kunde, Prosjekt, Periode, Logo, og Prosjekt ulik Kunde;
- periodeform;
- kompetansegrupper i setningsform uten duplikater;
- kulepunkter som Markdown-lister;
- bilder i `images/foto.*` og `images/logo-<kunde>.*` som finnes;
- rundtur parse → render → parse.

Eksempelet i leveransen ble rettet til samme konvensjon (`images/foto.jpg`). Så konverterte tre workere (Sonnet, medium) 6–7 CV-er hver etter en felles brief. De hentet tekst med pandoc og pdftotext, pakket ut bildene fra originalene, plasserte logoer etter visuell kontroll mot prosjektene, bygget hver fil og kjørte kontrollscriptet til det ga 0 avvik.

Orkestratorens gjennomgang:
- **Seksjonene** er like på tvers av alle 20.
- **Lasse Holanger:** legestillingene var lagt inn som prosjekter med arbeidsgiveren som «Kunde». De ble gjort om til arbeidsforhold med kulepunktene som beskrivelse.
- **To feil i byggescriptet ble funnet og rettet:**
  - Perioder med tillegg i parentes ble satt som én ubrytbar boks som stakk ut av datokolonnen (Aleksander, Lasse). Nå brytes de alltid foran parentesen, og kolonnen dimensjoneres etter den bredeste ubrytbare delen.
  - Overskriften «Generelt» kunne bli stående alene nederst på en side (Pål, Dee), fordi plassbehovet ikke regnet med at overskriften med båndet er rundt 6 linjer høy.
- **Påstand som ikke lot seg gjenskape:** en worker meldte at et foto med gjennomsiktig bakgrunn ble svart. Bygget legger slike foto på hvit bakgrunn, og en test med originalfila bekreftet det.

Leveranse:
- `data/cv_md/<navn>/` for alle 20, med `<navn>.md`, `<navn>.pdf` og `images/`;
- `data/cv_md/AVVIK.md` med felles punkter (logoer med lav oppløsning, utledede kunder, utelatte feil-logoer, CV-er uten portrett) og én seksjon per person.

Verifisering:
1. `check_cv_md.py` gir 0 avvik på alle 20. `pytest --timeout=3` består med 65 tester.
2. Alle 20 er bygget med `src/build_cv_pdf.py` uten feil og uten bokser som stikker ut.
   - `pdffonts` viser bare NON Natural Grotesk.
   - Advarsler om logoer med lav oppløsning står i avvikslista.
   - En maskinell kontroll fant ingen overskrift alene nederst på en side i noen av de 20 eller i eksempelet.
3. Rundturen er sjekket i kontrollscriptet for alle 20.
4. Oversiktsark av alle PDF-er er sett gjennom. Utsnitt av Pål, Nina, Lasse, Ørjan, Sindre og Jonas er lest, og foto og logoer står på riktige prosjekter.
5. Stikkprøve mot originalen for Pål (8 prosjekter, 59 nøkkelord), Ørjan (10 og 66) og Sindre (17 og 94): alle prosjekter, alle årstall og alle nøkkelord fra originalen finnes i Markdown-fila.

README er oppdatert (kontrollskriptet og `data/cv_md/`). Mal og eksempel i leveransen er bygget på nytt med de rettede reglene. Opprydding: `temp/T12/` er slettet, og `.claude/worktrees/` finnes ikke.

Åpne punkter:
- Konsulentene bør gå gjennom sin seksjon i avvikslista. De viktigste punktene er utledede kunder, første person i «Om», kopierte beskrivelser og nøkkelord, og logoer med lav oppløsning.
- Fortsatt ikke gjort (egne oppfølginger): opplasting til Drive, og synk av Markdown-filer og bilder med `src/download_cvs.py` og skillen `last-ned-cver`.
**Tillegg – malen i samsvar med konvensjonene:** Veiledningen i `cv-mal.md` (HTML-kommentarer) og `LESMEG.md` er oppdatert, så den beskriver nøyaktig det kontrollscriptet sjekker:
- mappe per person med `<navn>.md` og `images/`;
- `images/foto.jpg` og `images/logo-<kunde>.*`;
- kontaktliste i fast rekkefølge;
- Prosjekt utelates når det er likt kunden;
- perioder med «nå»;
- kompetansegrupper i setningsform;
- kulepunkter som Markdown-liste og mellomtittel som `**Tittel**`;
- rader uten periode;
- de fire faste listetitlene, og at Sertifiseringer bare er formelle sertifiseringer;
- kontrollkommandoen.

Innholdet i malen er uendret, og kontrollen gir bare de forventede avvikene for plassholderdatoene («MM.ÅÅÅÅ»). Formateksempelet i `LESMEG.md` gir 0 avvik. Malen er bygget på nytt (2 sider), og alle 65 tester består.

### T13 [x] Engelske navn på alt som ikke er dokumenter

Prosjektets regel er at kode, flagg, mappenavn og annet teknisk er på engelsk, mens dokumentasjon og leveranser er på norsk. En gjennomgang fant flere steder der norsk har sneket seg inn i det tekniske. Alt slikt skal over på engelsk. **Unntatt** er alt brukeren og mottakerne leser som dokument:
- PDF-er og Markdown-kildene som lager dem, f.eks. `cv-mal.md`/`.pdf`, `profilmanual.md`/`.pdf`, `brevmal.md` og `presentasjonsmal.md`;
- dokumenter i `background/` og deres `<filnavn>_media/`-mapper, som følger dokumentnavnet;
- innholdet i dokumentasjonen (README, TASKS, ARCHIVE, veiledninger);
- etikettene i CV-formatet («Kunde», «Prosjekt», «Periode», «Nøkkelord»), som er innholdet i en norsk CV.

**Visittkortet er helt utenfor**, fordi det pågår arbeid med det i en annen chat. Det gjelder `src/business_card/`, `src/build_business_card.py`, `deliverable/visualprofile/business-card/` og visittkortoppgaven. Visittkortet bruker fargefila og arbeidsmetoden i den visuelle profilen. **Punkt 4 og 6 under gjøres derfor først når visittkortoppgaven er markert løst.** Løses denne oppgaven før det, gjøres resten, og oppgaven merkes `[~]` med de to punktene som gjenstående.

**Endringer:**

1. **Mappenavn** (og alle stier som viser til dem, i kode, tester, README, TASKS og dokumenter):
   - `background/cver/` → `background/cvs/` og `background/new/cver/` → `background/new/cvs/`;
   - `background/visualprofile/Brand assets/mønster/` → `pattern/`;
   - `background/visualprofile/Leveranse fra Neue/` → `neue-delivery/`;
   - prosjekt-skillen `.claude/skills/last-ned-cver/` → `download-cvs/`, med navnet i `SKILL.md` og oversikten i `.claude/skills/README.md`. Utløserfrasene i skillen er brukerens egne norske formuleringer og beholdes.
2. **Hjelpetekster til flagg** på engelsk i `src/build_document.py`, `src/build_presentation.py`, `src/check_document_pdf.py` og `src/check_presentation_pdf.py`.
3. **Meldinger skriptene skriver ut** (feil, advarsler, kontrollresultater, oppsummeringer) på engelsk i alle skript, så alle er like:
   - `src/build_document.py`, `src/build_presentation.py`, `src/check_document_pdf.py`, `src/check_presentation_pdf.py`;
   - `src/check_cv_md.py`, `src/wcag_contrast.py`, `src/extract_visualprofile.py`.

   Tekst som havner i en PDF eller i et Markdown-dokument, er innhold og forblir norsk, f.eks. overskriftene `## Side {n}` og «Topp- og bunntekst» i konverterte dokumenter, og kontrastmatrisen i `farger.md`. Tester som sjekker meldingstekst, oppdateres.
4. **Fargefila** (etter visittkortet): `deliverable/visualprofile/profile/farger.json` → `colors.json`, og fargenøklene (`id`) på engelsk (`gronn` → `green`, `gra` → `grey` og så videre), i alle skript og stiler som leser dem. `farger.md` er dokumentasjon og beholder navn og innhold. Feltene `name` og `role` er norsk visningstekst og beholdes.
5. **Valgverdier i dokumentmalen:** `variant: brev` / `variant: dokument` → `letter` / `document` i `src/document/filter.lua`, malene og veiledningen. De gamle norske verdiene godtas fortsatt, med en advarsel, så eksisterende filer virker.
6. **Arbeidsmetoden i den visuelle profilen** (etter visittkortet): arbeidsmappene `temp/T10.x/runde<N>/<perspektiv>/` → `temp/T10.x/round<N>/<perspective>/`, og læringsloggen `LAERING.md` → `LEARNING.md` (punkt 3 og 9 i task-teksten). Historiske løsningsnotater endres ikke.
7. **README for leveransene:** `LESMEG.md` → `README.md` i `deliverable/visualprofile/cv/`, `document/` og `presentation/`, med uendret norsk innhold, og alle henvisninger oppdatert.
8. **Avklares med brukeren før de røres:** `src/tweak_cv.py` og `src/inspect_cv.py` er ikke laget i noen kjent oppgave, er ikke beskrevet i README, og `tweak_cv.py` har norsk CV-tekst skrevet rett inn i koden. Spør om de skal slettes, beholdes eller skrives om.
9. **CLAUDE.md** har et eksempel med `background/new/cver/` → `background/cver/`. Det oppdateres til `cvs` med brukerens eget ja, fordi endringer i CLAUDE.md alltid krever det.

**Verifisering:**

1. Søk etter de gamle navnene (`cver`, `mønster`, `Leveranse fra Neue`, `last-ned-cver`, `farger.json`, `runde<N>`, `LAERING`, `LESMEG`, `variant: brev`) gir bare treff i historiske løsningsnotater og i unntakene over.
2. `pytest --timeout=3` består. En ny test i `tests/test_platform_independence.py` (eller en egen testfil) sjekker at hjelpetekster og meldinger i `src/` ikke inneholder norske bokstaver utenfor innholdsstrenger, og at ingen mappe utenom `background/`-dokumentenes `_media`-mapper har norske tegn eller ord i navnet.
3. Alle bygg kjører på nytt uten feil, med de nye stiene:
   - profilmanualen;
   - CV-mal og -eksempel, og de 20 CV-ene i `data/cv_md/` (kontrollen gir 0 avvik);
   - presentasjons- og dokumentmalene (kontrollskriptene gir ingen FAIL);
   - eksporten av logo- og grafikkfiler;
   - kontrollkonverteringen av Markdown i `background/visualprofile/`.
4. Nedlastingsskriptet kjører med `--dry-run` mot den nye `background`-stien, og skillen virker med nytt navn.
5. Visittkortet er urørt: ingen filer under unntakene er endret.

**Estimert innsats:** 89 min

**Kobling:** følger opp gjennomgangen av språkregelen etter T10.2, T10.4, T10.5 og T12. Punkt 4 og 6 venter på T10.3.

**Berørte filer:** `background/cvs/` (fra `cver/`), `background/new/cvs/`, `background/visualprofile/Brand assets/pattern/`, `background/visualprofile/neue-delivery/`, `.claude/skills/download-cvs/` og `.claude/skills/README.md`, `src/*.py` (stier, hjelpetekster og meldinger), `src/document/filter.lua`, `src/document/kwdocument.sty`, `src/presentation/beamerthemekodeworks.sty`, `deliverable/visualprofile/profile/colors.json` (fra `farger.json`), `deliverable/visualprofile/{cv,document,presentation}/README.md` (fra `LESMEG.md`), dokumentmalene, `tests/`, `README.md`, `TASKS.md`, og `CLAUDE.md` (bare med eget ja)

**Faktisk innsats:** 13m 32s (veggklokke, så langt). Under estimatet fordi oversettelsen av meldinger ble gjort med eksakte token-erstatninger per skript i stedet for manuell redigering.

**Resolution:** Visittkortoppgaven var markert løst da arbeidet startet. Visittkortet er likevel holdt utenfor, som oppgaven sier.

- **Punkt 1, mappenavn:** `background/cver` → `cvs`, `background/new/cver` → `new/cvs`, `Brand assets/mønster` → `pattern`, `Leveranse fra Neue` → `neue-delivery`, `.claude/skills/last-ned-cver` → `download-cvs` (navnet i `SKILL.md`; de norske utløserfrasene er beholdt).
  - Levende henvisninger er oppdatert: README, oversikten over skills, tre dokumenter i `background/` som viser til CV-mappen, docstrings i `src/build_md_pdf.py` og `src/extract_visualprofile.py`, kildelista i arbeidsmetoden for den visuelle profilen og oppfølgingslinja i CV-konverteringen.
  - Historiske løsningsnotater er ikke endret.
- **Punkt 2 og 3, hjelpetekster og meldinger:** oversatt til engelsk i `src/build_presentation.py`, `src/build_document.py`, `src/check_presentation_pdf.py`, `src/check_document_pdf.py` og `src/check_cv_md.py`, i dokumentmalens filter (`src/document/filter.lua`, med prefikset `KWVARSEL:` → `KWWARN:`) og i presentasjonstemaets varsel om for mye tekst.
  - `src/wcag_contrast.py` og `src/extract_visualprofile.py` skriver allerede meldinger på engelsk. Deres norske strenger er dokumentinnhold (kontrastmatrisen, sideoverskrifter) og er beholdt, det samme gjelder norsk innhold som havner i PDF-ene (adresser, etiketter, «-notater.pdf»).
  - Testene for CV-kontrollen er oppdatert til de engelske meldingene.
- **Punkt 5, valgverdier:** dokumentmalen bruker `variant: letter` / `document`. De fire malene og eksemplene, veiledningen og README er oppdatert. `brev` og `dokument` virker fortsatt og gir advarselen «variant: brev is the old Norwegian value; use variant: letter», kontrollert med en kopi av brevmalen.
- **Punkt 6, arbeidsmetoden:** `temp/T10.x/round<N>/<perspective>/` og `LEARNING.md` i punkt 3 og 9. De beholdte læringsloggene fra presentasjons- og dokumentmalen (`temp/T10.4/LAERING.md`, `temp/T10.5/LAERING.md`, `temp/T10.5/spesifikasjon.md`, `temp/T10.5/tester/`) er historiske arbeidsfiler og har fått beholde navnene.
- **Punkt 7, veiledningene:** `LESMEG.md` → `README.md` i `deliverable/visualprofile/cv/`, `document/` og `presentation/`, med uendret innhold. Visittkortets `LESMEG.md` er ikke rørt.
- **Ny test:** `tests/test_english_names.py` sjekker hjelpetekster i alle skript, meldinger i de berørte skriptene (tekst i «…» regnes som innhold) og mappenavn. Negativtest: testen slår ut på visittkortskriptet, som fortsatt har norske hjelpetekster og meldinger.

Verifisering:
1. De gamle navnene finnes bare i historiske løsningsnotater, i denne oppgavens tekst, i visittkortdelen av README og i eksempelet i CLAUDE.md (punkt 9).
2. `pytest --timeout=5` består med 101 tester.
3. Alle bygg er kjørt på nytt uten feil:
   - profilmanualen;
   - CV-mal og -eksempel;
   - begge presentasjonene (11 og 12 PASS) og alle fire dokumentmalene (12 OK hver);
   - eksporten av logo- og grafikkfiler (13);
   - alle 15 kontroll-PDF-ene i `background/visualprofile/`, med `neue-delivery`;
   - kontrollen av de 20 CV-ene i `data/cv_md/`: 0 avvik.
4. `src/download_cvs.py --dry-run` kjører, og skillen er registrert som `download-cvs`.
5. Ingen filer under `src/business_card/`, `src/build_business_card.py` eller `deliverable/visualprofile/business-card/` er endret. Visittkortskriptet lastes fortsatt med det det henter fra presentasjonsbygget, som nå skriver «ERROR:» i stedet for «FEIL:».

**Fullført etter avklaring med brukeren** («Ja fiks, Visittkort tasken er done», «endre claude.md»):
- **Punkt 4, fargefila:** `deliverable/visualprofile/profile/farger.json` → `colors.json`. Fargenøklene er engelske og følger LaTeX-navnene (`green`, `grey`, `black`, `white`, `darkgreen`, `deepgreen`, `pink`, og `darkgrey` for den tekniske fargen).
  - Feltene `name` og `role` er norsk visningstekst og beholdt.
  - Oppdatert: visittkortskriptet (fargedefinisjonene), presentasjonsbygget (fargevarianter av logoene, nå `-deepgreen.pdf` og lignende), dokument- og presentasjonsbygget, presentasjonskontrollen, kontrastskriptet, stilene, README, `farger.md` og visittkortets veiledning.
  - Visittkortene er bygget på nytt og har samme tekst og samme farger som før.
  - Presentasjonene (11 og 12 PASS), dokumentmalene og kontrastmatrisen er bygget på nytt uten feil.
- **Punkt 9:** eksempelet i CLAUDE.md viser nå `background/new/cvs/` → `background/cvs/`.
- **Punkt 8, undersøkt:** `src/inspect_cv.py` og `src/tweak_cv.py` ble laget 21.10.2026 (endringstid), uten oppgave, README-omtale eller løsningsnotat.
  - `inspect_cv.py` skriver ut avsnitt og tabellceller fra en Word-kopi av Jan-Marius Vatles CV i `temp/`.
  - `tweak_cv.py` skriver om «Om»-teksten i den kopien for et oppdrag innen SysML/Cameo (Python, simulering, MATLAB) og legger masteroppgaven til under utdanning, rett i Word-fila.
  - Word-fila finnes ikke lenger, og ingen andre filer i prosjektet viser til skriptene. De er altså engangsskript fra en tidligere økt, og ingen kjent oppgave forklarer dem.
  - Brukeren ba først om å vente med sletting, og bestemte deretter at begge skal slettes. Begge er slettet.

Verifisering etter fullføringen: `pytest --timeout=5` består med 101 tester. `farger.json` og de norske fargenøklene finnes bare i historiske løsningsnotater.

**Faktisk innsats totalt:** 65m 26s (veggklokke fra start, medregnet ventetiden på brukerens svar om punkt 4, 8 og 9).

Åpne punkter:
- ~~Hva som skal skje med de to engangsskriptene for Jan-Marius' CV.~~ Slettet etter brukerens beslutning («de scriptene som tweaker jan marius cv kan du slette»).
- ~~Visittkortskriptet har fortsatt norske hjelpetekster og meldinger.~~ Tatt med etter brukerens beslutning, se tillegget under.

**Tillegg – visittkortet:** Brukeren bestemte at visittkortskriptet tas med i oppgaven («visittkortscriptet kan du nå inkludere i oppgaven og gjøre ferdig»).
- `src/build_business_card.py` har engelske hjelpetekster og meldinger (35 tekster), også etikettene i kontrollmeldingene («front» og «back»). Filnavnene på logoene (`kw-navnetrekk-svart.pdf` og lignende) er beholdt.
- `deliverable/visualprofile/business-card/LESMEG.md` → `README.md`, med henvisningene i fila selv, i kommentaren i `visittkort-mal.md` og i prosjektets README.
- `tests/test_english_names.py` har ikke lenger noe unntak for visittkortet, og skriptet er med blant dem som får meldingene sjekket. Den norske kommentaren i testfila er oversatt.
- Verifisering: begge visittkortene er bygget på nytt, og kontrollen består («Check: trim size 85 × 55 mm, 3 mm bleed, …»). `pytest --timeout=5` består med 99 tester.

**Faktisk innsats, tillegget:** 1m 28s (veggklokke)
