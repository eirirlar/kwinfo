# Thomas Ax Gulbrandsrød

Konsulent

- Telefon: +47 986 83 010
- E-post: thomas@kodeworks.no
- Erfaring: 5 år
- Språk: norsk, engelsk
- Foto: images/photo.jpg
## Om Thomas

Thomas er en embedded- og backend-utvikler med fem års erfaring i C++ og Python. Han har spesialisert seg på utvikling av robuste og ytelseskritiske systemer innen robotikk, sensorikk og embedded Linux. Med en bachelor i informatikk og påbegynt grad i elektronikk har han arbeidet på tvers av hele stacken – fra lavnivå mikrokontrollerkode og bootloadere til systemdesign og infrastruktur.

Han har erfaring fra medisinsk teknologi (Abbott Rapid Diagnostics, QNX-migrering), robotikk og sensorteknologi (Kilter Systems), samt HIL-infrastruktur og droneteknologi (Six Robotics). Felles for prosjektene er et fokus på stabilitet, pålitelighet og effektiv implementasjon i krevende miljøer.

Utenom arbeid bygger Thomas egne prosjekter innen droner og embedded systemer, CAD design med 3D printing og han trives både i tett samarbeid med andre utviklere og i selvstendig, teknisk fordypning.

## Teknisk kompetanse

### Språk og rammeverk

Python, SQL, Flask, Bash, ROS2, Java, C++, Django, ASIO, Pandas, JavaScript

### Plattform, tech og verktøy

Linux, Docker, Pytest, CMake, Visual Studio, CubeIDE, STM32, Git, GitHub Actions, CTest / gcovr, Poetry, Android Studio, MPLABX, PIC

### Metode

Agile, Kanban, Scrum

## Erfaring

### Cisco microsoft teams

- Kunde: Cisco
- Periode: 01.2026 – nå
- Logo: ../logos/cisco.png
**Cisco** er et teknologiselskap som utvikler møteromsteknologi. Her har han vært med i teamet som er ansvarlige for Microsoft Teams Rooms integrasjon inn til Cisco sine møteromsplatformer. Dette innebærer utvikling og vedlikehold av Cisco's Android og Java programmer for å støtte Microsoft Teams Rooms. I tillegg har han vært med på å videreutvikle Cisco’s interne tester og testsystem.

Noen av kjerneområdene for prosjektet var:

- **Android Java:** Network interface service for å støtte Teams nettverkskrav.
- **Test vedlikehold:** Vedlikehold og utvikling av nye ende til ende tester for nytt hardware for å ha godt overblikk over at nytt hardware fungerer som forventet.
- **Utvikling i testrammeverk:** Egetinitiativ på videreutvikling av Applitools bibliotek for bedre visuell regresjonssjekk

Nøkkelord: Python, Java, testing, testsystemer

### Infrastruktur og HIL testing

- Kunde: Six Robotics
- Periode: 03.2025 – 01.2026
- Logo: ../logos/six-robotics.png
**Six Robotics** er et teknologiselskap som utvikler svermdroner for militært bruk. Thomas har vært ansvarlig for kjerneinfrastrukturen til Six Robotics for HIL (Hardware In the Loop) samt jobbet i team som har fokus på intern tooling. Dette innebærer servere, hardware setup og tooling i Python for å gjøre bruken av HIL enkelt for utviklere og robust i CI. Ved siden av har han også vært med på oppdateringslogikken til Nvidia Jetson som er en del av hovedproduktet til Six Robotics.

Noen av kjerneområdene for prosjektet var:

- **HIL testing:** Enable HIL for utviklere gjennom pytest og tooling for autogenerering av github workflows basert på HIL brukere ønsker.
- **Nvidia Jetson updates:** AB oppdateringer og update logikk for Nvidia Jetson for å sikre trygg og pålitelig oppdatering av systemet.
- **Pytest integrasjon:** Tett integrasjon av pytest i tooling for å holde brukere vant til det de har brukt fra før.
- **Robuste systemer:** Tooling og HIL for utviklere har høy kostnad ved nedetid, så all utvikling på tooling og HIL har hatt høyt fokus på robusthet.

Nøkkelord: Python, Linux, testing, pytest, Nvidia Jetson, HIL, networking

### Embedded og robotikk utvikler

- Kunde: Kilter Systems
- Periode: 12.2023 – 03.2025
- Logo: ../logos/kilter.png
**Kilter** er et teknologiselskap som utvikler robotikk- og sensorløsninger med fokus på ROS2, embedded Linux og mikrokontrollere. Et av Thomas’ prosjekter var å designe en skreddersydd vindsensor med tilhørende CAN-bus-basert bootloader. Denne løsningen muliggjør multi-node-oppdateringer uten å forstyrre andre noder i nettverket. I tillegg utviklet han et Python-basert testbibliotek for å validere PCB-funksjonalitet før montering, med full integrasjon mot WATS for logging og kvalitetskontroll.

Noen av kjerneområdene for prosjektet var:

- **ROS2 på Linux (Nvidia Jetson):** Setups for robuste robotikkapplikasjoner med sanntidskrav.
- **Custom bootloader for CAN-bus:** Sørger for sikker flashing av firmware i et multi-node-miljø, uten å forstyrre annen trafikk.
- **HAL-bibliotek og flash-håndtering:** Implementering av lavnivåfunksjonalitet for å starte og styre applikasjoner på mikrokontrollere.
- **Python-basert testløsning med Pytest:** Bygget for å kjøre automatiserte tester som sikrer at kretskort og elektronikk fungerer etter spesifikasjon.
- **Rapportering og integrasjon mot WATS:** Automatisk generering av testrapporter og sømløs kobling til systemet for produksjonslogistikk og kvalitetskontroll.
- **Pålitelighet og robusthet i robotikk:** Utvikling av løsninger med vekt på sanntidsytelse og stabilitet, sentralt for Kilters robotikkplattformer.
- **GPS Systemer:** Utvikling og integrering av forskjellige GPS(rtk) systemer(Swiftnav, Septentrio og Marvelmind) samt utvikling av tester for slike systemer.

Nøkkelord: c++17, c, ros2, embedded, Linux, stm32, PIC18, canbus, bootloader, Python3.10, testing, pytest, Nvidia Jetson, GPS RTK

### Systemutvikler

- Kunde: KodeWorks
- Prosjekt: KW-TV (internprosjekt)
- Periode: 09.2023 – 12.2023

KW-TV er et Python-rammeverk for å sende datagenererte videostrømmer til YouTube eller andre plattformer som støtter RTMP. Sammen med rammeverket er det laget en videogenerator i både Python og C++. Python-versjonen bruker Pillow Image Library for generering av bilder. C++ delen benytter SFML for GPU-basert generering av bilder. Den C++ baserte modulen for videogenerering er eksponert til Python via bindings. Rammeverket er modulbasert og muliggjør utvidelse med egne bildegeneratorer.

Noen av kjerneområdene for prosjektet var:

- Skreddersydd Python-rammeverk for streaming av datagenerert video
- Prosjektoppsett i Python med Poetry, MyPy, Pytest og Black
- Prosjektoppsett i C++ med CMake, CTest, gcovr og ClangFormat
- Eksponering av C++ bibliotek til Python gjennom Pybind11
- CPU-genererte bilder i Python gjennom PIL
- GPU-genererte bilder i C++20 gjennom SFML
- Komplett CI/CD pipeline for bygg/pakking, linting, testing og coverage-analyse i GitHub Actions
- Videokoding gjennom ffmpeg med enkel konfigurasjon av stream sink (IP-adresse + nøkkel)
- Integrasjons- og unittester med mål om 100% testdekning

Nøkkelord: Python, C++20, SFML, Pybind11, CMake, Poetry, Pillow, ffmpeg, Github Actions, CTest, gcovr, MyPy, Pytest, Black, ClangFormat

### Konsulent

- Kunde: Elporten
- Periode: 04.2023 – 09.2023
- Logo: ../logos/elporten.png
Elporten tilbyr et KIS SAAS-system for salg av strøm, spesielt designet for mindre aktører. Thomas har bidratt betydelig i å utvikle systemet, samt deler av systemets design. Systemet er todelt:

- Et KIS-system utviklet med Python og Django
- En Elhub-kontroller som kommuniserer direkte med Elhub. Denne opprettholder en oversikt (ledger) over alle hendelser, slik at brukere til enhver tid kan få en fullstendig forståelse av sanntidsdata. Dette er også utviklet i Python, men med Flask.

Noen av oppgavene Thomas var ansvarlig for var:

- Implementering av inn- og utloggingsflyt
- Design og implementasjon av en modul for innhenting og mellomlagring av valutakurser med støtte for prioriterte kilder.
- Design og implementasjon av en modul for innhenting og mellomlagring av spotpriser for strøm, med støtte for prioriterte kilder og priskorrigeringer.
- Design og implementasjon av fakturagrunnlag-modul som kombinerer kundeforbruk med spotpriser og vekslingskurser.
- Eksportering av spotpriser, valutakurser og forbruksrapport som Excel-dokumenter.
- Feil og avviksfaner i de ulike rapportene
- Implementere støtte for målepunkttype “kombinert” for plusskunder, og støtte for endring underveis i leveranseperioden.
- Implementere støtte for Elhub-meldinger om “winback” av tidligere kundeforhold.
- Unit og integrasjonstesting
- Debugging og feilretting

Nøkkelord: Python, Django, Flask, Ledger, API, Elhub, Pandas

### Systemutvikler

- Kunde: KodeWorks
- Prosjekt: SOCKS4 (internprosjekt)
- Periode: 01.2023 – 03.2023

Som internprosjekt har Thomas utviklet en SOCKS4 proxy med egenutviklet versjon av shared_ptr fra standardbiblioteket.

Dette var et prosjekt for å videreutvikle moderne C++(>17) kunnskap og async nettverksprogrammering gjennom biblioteket boost asio.

Nøkkelord: C++(>17), nettverk, sockets, asio, async programmering

### Konsulent

- Kunde: Abbott Rapid Diagnostics
- Prosjekt: Realtime OS migrering
- Periode: 10.2022 – 01.2023
- Logo: ../logos/abbott.png
Abbot Rapid Diagnostics leverer maskiner for rask blodtest. De har et system som trenger å migreres over til en nyere versjon. Det er et moderniseringsbehov, som gjør at de må se på/migrere kode som går gjennom hele systemet. Fra å sette opp CPU, MMU og andre peripherals til filsystem og applikasjonskode.

Eksperimentering, testing, dokumentering og planlegging av QNX real time OS versjons migrering. Abbott brukte en veldig gammel QNX versjon og trengte noen til å finne ut av hva som måtte gjøres og hvor lang tid migrering over til en ny versjon kom til å ta.

Nøkkelord: QNX RTOS, Makefile, C99 og 11, C++ 98 og 11

### Bacheloroppgave

- Kunde: Sunlit Sea
- Prosjekt: Realtime dashboard for solcelle-installasjon
- Periode: 01.2022 – 05.2022
- Logo: ../logos/sunlit-sea.png
Bacheloroppgaven ble skrevet for Sunlit Sea, et selskap som leverer norskproduserte flytende solcelleanlegg. Thomas har vært delaktig i utvikling av sensor-elektronikken i anleggene. Oppgaven gikk ut på å lage en web app hvor man kan se en digital tvilling av solcelleinstallasjonen representert i 3D sammen med relevant statistikk.

Designet og utviklet en fullstack web app-løsning som kunne streame data fra ulike sensorer i anlegget i realtime med Server Sent Events (SSE) fra backend. Dette ble visualisert i 3D via Three.js, sammen med annen tilhørende statistikk slik som produksjon, solinnstråling, bølge-aksellerasjon mm. Mye tid ble brukt på softwarearkitektur, 3D visualisering og backend utvikling for optimalisering av datastrøm. Python 3.10 med Flask som streaming/data backend. En initiell demo ble laget i React, mens resten ble skrevet i vanilla JavaScript.

Nøkkelord: Python, Flask, JavaScript, Three.js, Chart.js, InfluxDB, React

### Systemutvikler

- Kunde: Sunlit Sea
- Prosjekt: Elektronikk og sensorikk
- Periode: 06.2019 – 07.2022 (deltid 40%)
- Logo: ../logos/sunlit-sea.png
Sunlit Sea er et nyoppstartet firma som utvikler flytende solcellepaneler for bruk på vann. De har som salgspunkt at de samler data fra solcellepanelene så det blir mulig å se real time bevegelse, strømproduksjon, hva slags bølger det er og hva som er forventet return rate for strømproduksjon basert på disse dataene.

Fullstack utvikling av Sunlit Sea sin tekniske løsning. Dette inkluderer utformingen av kretskortet, etablering av en fysisk kommunikasjonsstandard for sensorene, og design av en mottakerenhet som tolker data fra denne kommunikasjonslinjen. Fysisk kravspesifisering for hele anlegg og hvordan de skal se ut elektrisk.

Nøkkelord: C++ 11, C, Python, Arduino, Raspberry PI, Autodesk Eagle, Kretsdesign

### Systemutvikler

- Kunde: Sunami
- Periode: 07.2016 – 07.2021 (deltid 40%)

Sunami er et selskap som ble inkubert og støttet av Eyasys. De er en utleier av solcellepaneler som bygger på en pay-as-you-go løsning hvor man kan leie et helt anlegg og betale per dag for å bruke det. Dette er for å senke paywallen for å leie og gjøre det enkelt å betale bare når man trenger å bruke anlegget.

Var med på kretsdesign og systemdesign for solcellekontrollere, samt å teste ut satellittkommunikasjon på en proof of concept modell ved bruk av Iridium satellittmoduler og Arduino for satellittkommunikasjon istedenfor GSM.

Nøkkelord: C/C++, Arduino, Autodesk Eagle, kretsdesign, satellittkommunikasjon, GSM, Iridium

## Arbeidserfaring

- 08.2022 – nå | KodeWorks | Konsulent
- 12.2021 – 07.2022 | KodeWorks | Systemutvikler (40% deltid)
- 07.2016 – 11.2021 | EyaSys | Systemutvikler (40% deltid)

## Utdanning

- 2019 – 2022 | Bachelor - Informatikk | Oslo MET
- 2017 – 2019 | Bachelor - Elektronikk, informatikk og teknologi | Oslo MET

## Verv og engasjement

- 2013 – 2017 | Frivillig i Ten Sing | Østenstad Ten Sing
- | Hobbyprosjekter
  - Bygget to FPV-racingdroner fra bunnen av, én med Cleanflight og én med Betaflight. Dette inkluderte hardware-oppsett, konfigurasjon og firmware-tilpasning.
  - Utviklet et FPV-streamingsystem for droner.
  - Embedded utvikling på ESP32-plattformen, inkludert utvikling av en hydroponisk styringsenhet med FreeRTOS og MQTT i C++.
  - Bygget et elektrisk skateboard med en open-source motor kontroller (VESC).
  - Nøkkelord: FPV, Cleanflight, Betaflight, droneteknologi, ESP32, FreeRTOS, MQTT, embedded systems, hardware-utvikling, C++
