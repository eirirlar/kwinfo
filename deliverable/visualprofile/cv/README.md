# CV-mal for KodeWorks-konsulenter

CV-en skrives som en vanlig Markdown-fil og settes automatisk til en ferdig PDF i KodeWorks' visuelle profil. Du skriver innholdet. Layout, typografi, sideskift, logoer, foto og seismograframmen ordnes av byggeskriptet. Det finnes ingen Word-versjon, fordi profilfonten bare kan bygges inn i PDF.

| Fil | Hva den er |
|---|---|
| `cv-mal.md` | Tom mal med veiledning i kommentarer. Start her. |
| `cv-mal.pdf` | Slik ser malen ut ferdig satt. |
| `cv-eksempel.md` | Utfylt eksempel med åtte prosjekter, foto og kundelogoer. |
| `cv-eksempel.pdf` | Det ferdige eksempelet (fire sider). |
| `images/` | Foto og logoer som eksempelet bruker. |

PDF- og PNG-filene er ikke i git. De bygges fra Markdown-filene med `uv run python src/build_all.py` fra prosjektroten (se «Bygge alt» i prosjektets README).

## Slik lager du din CV

1. Lag én mappe for CV-en under `cvs/`, med navnet ditt i små bokstaver, der æ blir ae, ø blir oe, å blir aa og mellomrom blir bindestrek. Kopier `cv-mal.md` inn i mappen med samme navn, og legg fotoet i undermappen `images/`. Kundelogoene ligger i det felles logobiblioteket `cvs/logos/`, som alle CV-ene deler:

   ```
   cvs/
   ├── logos/
   │   ├── equinor.png
   │   └── ...
   └── ola-nordmann/
       ├── ola-nordmann.md
       └── images/
           └── foto.jpg
   ```

2. Fyll inn. Bruk `cv-eksempel.md` som forbilde for nivå og lengde. Fila kan leses og redigeres i hvilken som helst teksteditor, og forhåndsvises i f.eks. VS Code.
3. Bygg PDF-en og kontroller fila fra prosjektmappen:

   ```bash
   uv run python src/build_employee_cvs.py ola-nordmann          # CV-PDF og visittkort ved siden av CV-en
   uv run python src/check_cv_md.py cvs/ola-nordmann/ola-nordmann.md
   ```

   Kontrollen sjekker at CV-en følger de samme reglene som alle de andre (rekkefølge, etiketter, datoform og bildenavn), og skriver hva som eventuelt må rettes.

   Bygget tar 5–40 sekunder. Det fungerer likt på Windows, Linux og macOS. Det krever bare `uv` og TeX Live med `lualatex`. Profilfonten hentes fra font-fila i prosjektet og trenger ikke være installert på maskinen. Mangler du verktøyene, kan den som har ansvar for profilen bygge CV-en for deg.
4. Les advarslene fra bygget, åpne PDF-en og gå gjennom sjekklisten nederst.

## Formatet

```markdown
# Ola Nordmann

Senior utvikler

- Telefon: +47 000 00 000
- E-post: ola@kodeworks.no
- Erfaring: 8 år
- Språk: norsk, engelsk
- Foto: images/foto.jpg

## Om Ola

Ett til tre avsnitt i tredje person.

## Teknisk kompetanse

### Språk og rammeverk

TypeScript, React, Kotlin

## Erfaring

### Lead-utvikler

- Kunde: Equinor
- Prosjekt: Echo 3D
- Periode: 03.2022 – nå
- Logo: images/logo-equinor.png

Beskrivelse i ett eller flere avsnitt.

- Konkret bidrag
- Konkret bidrag

Nøkkelord: React, TypeScript, Azure

## Arbeidserfaring

- 03.2022 – nå | KodeWorks | Senior utvikler

## Utdanning

- 2015 – 2016 | Business Economics, M.Sc. | Handelshøyskolen BI

## Sertifiseringer

- 2021 | Azure Fundamentals (AZ-900) | Microsoft
```

**Regler:**

- `#` er navnet. Avsnittet rett under er stillingstittelen.
- Lista under tittelen er kontaktinformasjonen, alltid i denne rekkefølgen: Telefon (`+47 000 00 000`), E-post, Erfaring (`N år`), Språk (små bokstaver, komma mellom) og Foto.
- Seksjonene kommer i denne rekkefølgen: `## Om <fornavn>`, `## Teknisk kompetanse`, `## Erfaring`, `## Arbeidserfaring`, `## Utdanning`, `## Sertifiseringer` og eventuelle egne lister. «Om»-teksten står på forsiden, og kulepunkter er lov.
- Under `## Teknisk kompetanse` er hver `###` en gruppe, med gruppenavnet i vanlig setningsform («Infrastruktur og DevOps», ikke store bokstaver). Elementene skrives på én linje med komma mellom. Hele setninger skrives som punktliste. Samme element står bare én gang.
- Under `## Erfaring` er hver `###` ett prosjekt, med rollen som overskrift og nyeste prosjekt først.
  - Lista rett under overskriften er faste felt, i rekkefølgen Kunde, Prosjekt, Periode og Logo.
  - Prosjekt utelates når det er likt kunden.
  - Deretter kommer beskrivelsen, og til slutt én linje som begynner med `Nøkkelord:`.
- I beskrivelser gir `**fet**` uthevet tekst, og et avsnitt som bare er `**Tekst**`, blir en liten mellomtittel. Kulepunkter skrives som Markdown-liste (`- `), ikke som «\-» eller «•».
- I `Arbeidserfaring`, `Utdanning` og `Sertifiseringer` er hver rad `periode | navn | sted`. Mangler perioden, skriver du `- | navn | sted`. Underpunkter (rykket inn to mellomrom) blir en kort beskrivelse av raden. Sertifiseringer er bare formelle sertifiseringer, som AZ-900 og PSM I.
- Andre lister får egen overskrift med en av de faste titlene `## Verv og engasjement`, `## Foredrag og publikasjoner`, `## Kurs` eller `## Utmerkelser`, i samme form. Bruk dem i stedet for å legge slikt under Sertifiseringer.
- Perioder skrives som `MM.ÅÅÅÅ – MM.ÅÅÅÅ`, `MM.ÅÅÅÅ – nå`, `ÅÅÅÅ – ÅÅÅÅ` eller `ÅÅÅÅ`, med tankestrek og mellomrom. Skriv «nå», ikke «d.d.». Tillegg står i parentes etter perioden og brytes pent: `2011 – 2018 (40 % stilling)`.
- Alle felt er valgfrie. Det som mangler, vises ikke og gir ikke hull.
- Kommentarer (`<!-- … -->`) vises ikke i PDF-en.
- **Engelsk CV:** bruk engelske overskrifter og etiketter (`## About Ola`, `## Skills`, `## Experience`, `Customer:`, `Period:`, `Keywords:`, `## Work experience`, `## Education`, `## Certifications`). Da får CV-en engelsk orddeling og engelske etiketter.

## Foto og kundelogoer

- **Foto:** et rolig portrett. Bildet beskjæres automatisk så det fyller rammen, også når det er liggende eller viser hele personen. Havner ansiktet feil, kan du legge til `- Fotofokus: 0.5, 0.3` (vannrett og loddrett punkt som brøk av bildet, der 0, 0 er øverst til venstre).
- **Fotoformat:** fotoet heter `images/foto.jpg` og er en JPG uten metadata (EXIF, fargeprofil), med inntil 1200 piksler i bredden på utsnittet med rammens forhold (60:74), altså inntil 1200 × 1480 for et stående foto. Legg inn fotoet som du har det, og kjør `uv run src/normalize_cv_images.py --apply`: det gjør om til JPG, fjerner metadata, skalerer ned og retter henvisningen i CV-en. Kjør uten `--apply` først for å se hva som blir endret.
- **Logoer:** hver kunde har én logo i `cvs/logos/<kunde>.svg` eller `.png`, med kundenavnet i små bokstaver og bindestrek (f.eks. `cvs/logos/sunlit-sea.png`). CV-en viser til den som `- Logo: ../logos/sunlit-sea.png`. Finnes kunden allerede i biblioteket, bruk den fila. En ny logo legges i biblioteket. Normaliseringsskriptet trimmer kanter og skalerer en PNG ned til høyst 700 × 260 piksler. CV-kontrollen melder avvik for foto og logoer som ikke følger formatet.
- **Malen og eksempelet** i denne mappen har sine egne bilder i `images/` (`images/foto.jpg`, `images/logo-<kunde>.png`), så de kan brukes uten resten av repoet.
- **Logo:** kundens logo vises øverst til høyre i prosjektblokken. SVG er best, PNG bør være minst 600 piksler bred. Hvite og gjennomsiktige kanter trimmes bort, og logoen skaleres så alle logoer får omtrent samme visuelle tyngde. Byggeskriptet advarer når en logo har for lav oppløsning. Når kunden er KodeWorks, vises ingen logo, fordi navnetrekket allerede står nederst i CV-en. Bruk bare logoer kunden selv publiserer.

## Hvordan CV-en tilpasser seg innholdet

- Forsiden har kontaktinformasjon, «Om» og teknisk kompetanse, helst i to kolonner. Er «Om» lang, stables kompetansen under. Er det god plass igjen, starter «Erfaring» allerede på forsiden. Ellers lukkes forsiden med seismografbåndet.
- Prosjekter brytes over sideskift med den grønne venstrekanten intakt. Det er minst to linjer på hver side av et skift, og en prosjekttittel blir aldri stående alene nederst på en side. Kompetansen deles aldri inne i en gruppe.
- Kolonnene i «Generelt» måles ut fra innholdet og står på linje gjennom alle listene. Korte lister deles ikke over sideskift.
- Bygget prøver flere varianter og velger den med færrest sider uten halvtomme sider. Brødteksten er alltid 9,5 pt. Lange CV-er får heller flere sider enn mindre skrift.
- Malen er testet med 20 ekte KodeWorks-CV-er og med kunstige tester: bare navn, 0–13 prosjekter, spesialtegn, overlange ord og URL-er, og engelsk tekst.

## Skriveråd

- **Om deg:** fagprofil først (tyngdepunkt, erfaring, hvordan du jobber), deretter noe som skiller deg ut. Tredje person, konkret, uten superlativer.
- **Prosjektbeskrivelse:** start med problemet eller målet kunden hadde, og hva systemet er for noe. Beskriv deretter din rolle og ditt ansvar, og avslutt med resultatet. Tre til åtte linjer pluss kulepunkter for konkrete bidrag, med verb i fortid.
- **Nøkkelord:** de viktigste teknologiene i prosjektet, helst fire til åtte. Nevn dem også i teksten der de ble brukt.
- Eldre eller mindre prosjekter kan ha én til to setninger.

## Sjekkliste før CV-en sendes

1. Navn, tittel, telefon og e-post er riktige.
2. Prosjektene står med nyeste først, og alle perioder har samme format.
3. Kundenavn og prosjektnavn er skrevet likt som i tidligere CV-er og tilbud.
4. Ingen kundelogo brukes uten at kunden selv publiserer den.
5. Ingen advarsler fra byggeskriptet om manglende bilder, lav oppløsning eller fjernede tegn, og kontrollen (`check_cv_md.py`) gir ingen avvik.
6. Fonten er innebygd: i PDF-leseren, under Egenskaper → Skrifter, skal det bare stå NON Natural Grotesk.
7. Fotoet viser ansiktet godt i rammen.
8. Filnavnet er beskrivende, f.eks. `CV Ola Nordmann KodeWorks.pdf`.
