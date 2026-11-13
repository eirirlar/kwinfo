# Dee Roberts

Konsulent

- Telefon: +47 920 49 514
- E-post: dee@kodeworks.no
- Erfaring: 5 år
- Språk: norsk, engelsk
- Foto: images/foto.jpg
## Om Dee

Dee er en fullstack utvikler med fem års erfaring. Dee har bred erfaring i frontend-utvikling med TypeScript og React, inkludert biblioteker som Redux og Zustand, og har bygget både single page-applikasjoner og lokale applikasjoner via Electron.

Han er dyktig i å oversette komplekse domener til brukervennlig design ved hjelp av SCSS, SVG og three.js. På backend-siden, er Dee spesialisert i Elixir og Phoenix-rammeverket, forstår OTP-prinsipper for å bygge skalerbare og fault-tolerant systemer, og har erfaring med Node.js i flere kontekster, inkludert VS Code-utvidelser. Han har også jobbet med Python og Flask, og er dyktig i å designe komplekse APIer, både i REST og GraphQL, og sikring gjennom OAuth2.

Utenfor arbeidsplassen liker Dee å utdype sitt programmeringskunnskap til andre domener, som i et nylig prosjekt hvor han lagde en fungerende modell-CPU i Rust og WebAssembly.

## Teknisk kompetanse

### Språk og rammeverk

TypeScript, Node.js, Phoenix, Flask, CSS (inkl. Tailwind), React, Elixir, Rust, Playwright, Python

### Plattform, tech og verktøy

Git, PostgreSQL, MongoDB, GraphQL, Keycloak, Remix / React Router (framework), REST APIer, Jira, OAuth2, Azure, Ansible

### Metode

Agile, CI/CD, Kanban, Scrum

## Erfaring

### Programvareutvikler

- Kunde: Inatur
- Periode: 02.2024 – nå
- Logo: ../logos/inatur.png
Hovedoppgaven har gått ut på å vedlikeholde og videreutvikle en stor Java Spring-applikasjon, med nye features og bugfixes etter behov. En stor del av arbeidet har involvert å sikre interoperabilitet av flere eldre frontend-teknologier som kjører sammen på én side. Jeg bidro til modernisering av systemet ved å designe en strategi for gradvis migrering til TypeScript, samt innføre strengere rutiner rundt CI.

**Nytt API-prosjekt**

Inatur hadde behov for et nytt REST API som ville la eksterne applikasjoner koble til systemet på en trygg og sikker måte.

En “schema-first” designtilnærming ble brukt til APIet, hvor Microsoft sitt TypeSpec DSL ble brukt til å lage en enkelt sannhetskilde hvor API-endepunktene og responseobjekter kunne bli definert. Ut ifra dette ble det generert en OpenAPI schema, som ble brukt til både generering av både dokumentasjon samt Java interfaces og POJOs. Dette garanterte type safety gjennom hele implementasjonen, for både selve API-serveren og klientene som tok det i bruk.

Sikring av APIet innebar oppsett av og migrering til Keycloak, en ekstern identitetsprovider (auth server). Migreringen involverte å overføre ~300.000 brukere fra MongoDB til en Postgres-database. Diverse custom Keycloak-providere ble skrevet for å få til integrasjon med Spring-systemet gjennom en event-drevet arkitektur. Integrasjon med Spring Security gjennom diverse OAuth2-flytter.

**Modernisering av frontend**

Ledet omfattende moderniseringsinitiativ for frontend for å adressere systematiske flaskehalser som hindret funksjonsutvikling og markedsrespons:

- Arkitekte og gjennomførte gradvis migrering fra legacy-frontend til en ny React Router-plattform som bruker backend-for-frontend-mønsteret. Samspill med det eksisterende systemet ble opprettholdt gjennom overgangsprosessen.
- Implementerte sikker autentisering mot organisasjonens eksisterende Keycloak-server i henhold til beste praksis for backend-for-frontend-arkitektur, inkludert sikker håndtering av tokens og beskyttelse av sensitive autentiseringsdata.
- Anvendte UX-erfaring og designkompetanse for å utvikle et nytt navigasjonssystem som balanserer behovene til både sporadiske brukere og superbrukere som arbeider daglig i applikasjonen.
- Benyttet Tailwind CSS med statens designsystem for å akselerere utvikling samtidig som kvalitetsstandarder ble oppholdt.

I forbindelse med ny frontend forkjempet jeg en transformativ overgang til API-først utviklingsmetodikk, etablerte formelle tjenestekontrakter og implementerte strangler-mønsteret for å pakke inn legacy-tjenester bak veldefinerte APIer. Denne arkitektoniske tilnærmingen adresserte direkte organisatoriske flaskehalser ved å levere ende-til-ende typesikkerhet gjennom automatisert kodegenerering, forbedret testing gjennom automatisert testdatagenerering, og forbedret kodekvalitet gjennom tidlige API-designgjennomganger. Utviklet dokumentasjonsplattform ved bruk av MkDocs for interne team og eksterne leverandører. Dette forbedret plattformtilgjengelighet betydelig, noe som posisjonerte organisasjonen til raskere å kunne kapitalisere på nye markedsmuligheter.

Nøkkelord: Java, Spring, TypeScript, React, Backend-for-frontend, Tailwind, TypeSpec, REST APIer, OpenAPI, OAuth2, Keycloak, MongoDB

### Programvareutvikler

- Kunde: Nordic Semiconductor
- Periode: 08.2020 – 12.2023
- Logo: ../logos/nordic-semiconductor.png
Jobbet i avdelingen for programvareverktøy, med å designe, utvikle og vedlikeholde desktop-applikasjoner og relaterte systemer som gjør det enkelt for utviklere å skrive programvare for Nordics brikker.

**nRF Direction Viewer**

En interaktiv 3D-visualisering som demonstrerer de rettningsfinnendevnene til Nordics antennaoppstilling. Applikasjonen bruker three.js for å vise posisjonen til en tilkoblet beacon relativ til antennaoppstillinga. Grafer av øvrige lesninger er rendret med charts.js. Den kjører i et Electron-vindu og utfører avlesninger gjennom node-serial biblioteket. Redux brukes som state management-løsning.

**nRF Connect for VS Code**

En stor VS Code-utvidelse som gjør editoren til en IDE for Nordics enheter. Den har omfattende funksjonalitet som dekker hele build-flash-debug livssyklusen for embeddedprogramvareutvikling. Utvidelsen er hovedsakelig skrevet i TypeScript, med bred bruk av VS Code- og Node.js-APIene. Den inkluderer flere mindre applikasjoner, som et konfigurasjonsverktøy for Linux-kernelen og en minneutforsker; disse bruker primært React.

**nRF Devicetree**

Et grafisk editor for et kompleks hardwaredesignspråk. Istedenfor å måtte skrive språket for hånd, lar editoren brukere designe hardwaren sin gjennom et intuitivt brukergrensesnitt. Idet man gjør en endring i GUIen, skrives den tilsvarende koden automatisk. Den inkluderer en custom SVG layoutmotor som dynamisk rendrer kretsdiagrammer, og bruker D3 for å lage en pannable canvas. Zustand brukes til state management.

**nRF Connect SDK App Index**

Et nettsted som inneholder informasjon om sampleapplikasjoner som fungerer med nRF Connect SDKen. Brukerne kan søke etter og filtrere samplene basert på hva slags prosjekt de starter. Nettstedet er en Next.js-applikasjon som på byggetidspunktet bruker GitHub-SDKen for å hente informasjon om samplene, for så å generere en statisk nettside som enkelt kan hostes. Tailwind brukes til styling. Når indeksen blir oppdatert kjører en GitHub Actions-pipeline for å gjenoppbygge og distribuere nettstedet på nytt.

**Analysesystem**

Et GDPR-kompatibel analysesystem som henter bruksdata fra Nordics desktop-applikasjoner. Dataene er lagret i Azure App Insights, og blir hentet ut med KQL queries som visualiserer viktige informasjonspunkter.

Nøkkelord: React, TypeScript, Node.js, Redux, Python, Zustand, three.js, D3, SVG, Next.js, Tailwind, SCSS, Electron, VS Code, Selenium, Azure Pipelines, Azure App Insights, GitHub Actions

### Programvareutvikler

- Kunde: Asolvi
- Periode: 08.2019 – 08.2020
- Logo: ../logos/asolvi.png
Jobbet som fullstack-utvikler i et self-managed team som var ansvarlig for å gjøre om komponenter i legacy-systemer til gjenbrukbare mikrotjenester. Alle tjenestene ble skrevet i Elixir, med bruk av Phoenix-webrammeverket. Fikk erfaring med Large Scale Scrum-metodologien, og jobbet i tett samarbeid med stakeholdere i flere land.

Spesifikke oppdrag:

**Sjekklistetjeneste**

En mikrotjeneste for å lage og fylle ut komplekse sjekklister og sjekklistemaler, noe mange av Asolvis kundevendte applikasjoner driver med. Dataene lagres i en PostgreSQL database. Kommunikasjon med tjenesten skjer gjennom en GraphQL API, som ble skapt med Absinthe-biblioteket. Tjenesten integrerer med Azure Blob Storage for lagring av bilder og signaturer som er inkludert i sjekklistene. I tillegg ble det bygd en sample React-frontend, som demonstrerer hvordan APIen kan tas i bruk.

**Tillatelsestjeneste**

En GraphQL API som sitter foran andre Asolvi-applikasjoner og sikrer at brukeren har gitt de nødvendige tillatelsene for å bruke applikasjonen. Autorisasjon skjer gjennom Auth0, med bruk av maskin-til-maskin tokener for å sikre kommunikasjon mellom applikasjonen og tjenesten.

**Evatic Next**

Et nytt skybasert service management-system som erstatter den eksisterende desktopapplikasjonen. Det inkluderer et stort datatransformasjonslag som henter dataene fra kundens on-premise legacy MSSQL database og normaliserer dem til en mer modern PostgreSQL-schema. Frontenden bruker Phoenix LiveView, og E2E-testing ble utført med Cypress.

Nøkkelord: Elixir, Phoenix, LiveView, React, PostgreSQL, MSSQL, GraphQL, Docker, Cypress, Domain Driven Design, Auth0

## Arbeidserfaring

- 01.2024 – nå | KodeWorks | Konsulent
- 08.2020 – 12.2023 | Nordic Semiconductor | Programvareutvikler
- 08.2019 – 07.2020 | Asolvi | Programvareutvikler

## Utdanning

- 2016 – 2019 | Computer Science. Bsc. | Keele University (UK)

## Foredrag og publikasjoner

- 2018 – 2019 | Brettspill utviklingsplattform. | Keele University
  - Utviklet en plattform som lar brukere utvikle sine egne brettspill og spille dem online mot andre mennesker i sanntid.
  - Inkludert et Lisp-basert programmeringsspråk for å skrive spillene, med en parser, interpreter, spillserver, protokoll og tilhørende API skrevet i Elixir.
  - Et redigeringsmiljø og eksempelwebklient ble programmert i TypeScript og ClojureScript.
- 2018 – 2019 | eLæringsmodul for e-helse | UCL
  - Utviklet et monolitisk system i samråd med en medisinsk startup for å evaluere kompetansen til anestesileger i å gjenkjenne preoperativ angst hos barn.
  - Sammensatt av en Elixir-backend som gir autentisering, serverer JSON til en ReasonML / React SPA og utfører statistiske beregninger i sanntid.
