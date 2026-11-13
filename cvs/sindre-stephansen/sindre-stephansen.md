# Sindre Stephansen

Konsulent

- Telefon: +47 958 67 003
- E-post: sindre@kodeworks.no
- Erfaring: 6 år
- Språk: norsk, engelsk
- Foto: images/foto.jpg

## Om Sindre

Sindre er en allsidig systemutvikler med spesialisering i skjæringspunktet mellom maskinvare og programvare. Han har en mastergrad i datateknologi og bred erfaring som spenner fra lavnivå utvikling til moderne applikasjonsutvikling og arkitektur.

Han trives best med teknisk utfordrende oppgaver, gjerne som involverer sensorer, signalbehandling eller sanntidskrav. Sindre har det siste året fokusert på backend-utvikling i C#/.NET, men har også erfaring med frontend, og har lagd flere mindre servicer og scripts i Python.

Han er sikkerhetsklarert Hemmelig, vant til å jobbe i graderte miljøer, og setter seg raskt inn i komplekse kodebaser.

## Teknisk kompetanse

### Sikkerhetsklarering

Hemmelig / NATO Secret

### Språk og rammeverk

C, C++, C#, Rust, Java, Kotlin, Python, Scala, Chisel, PHP, Verilog, Javascript

### Plattform, tech og verktøy

Windows, Linux, Embedded, Docker, Android, Mac OS, Git, IntelliJ, Pycharm

### Metode

Scrum, Kanban, Agile, Lean

## Erfaring

### Utvikler

- Kunde: EnerSky
- Periode: 02.2026 – nå
- Logo: images/logo-enersky.png

EnerSky er et selskap som leverer forenklet tilgang til energidata. Hovedproduktet er EnerSky Insight API, som lar kunder enkelt be om tredjepartstilgang til energidata for sluttbrukere. Insight API er et veldokumentert REST API basert på OpenAPI v3, og gjør det enkelt å integrere, fremfor å måtte selv integrere med Elhub sitt SOAP XML grensesnitt.

Sindre jobber med å utvide EnerSky med et API for å hente nettleiepriser for målepunkter, uansett hvilket nettselskap de tilhører. Dette innebærer å kartlegge prismodellene for alle nettselskaper i Norge, definere en modell som kan representere alle de mulige variasjonene, og å lage et API for sluttbrukere.

Nøkkelord: Python, FastAPI, Pydantic, Elhub, asyncio

### Konsulent

- Kunde: Kongsberg
- Prosjekt: Ship Noise Monitoring
- Periode: 05.2025 – 01.2026
- Logo: images/logo-kongsberg.png

Sindre utvikler en applikasjon som tar imot lyd fra hydrofoner og viser spektrogrammer i sanntid. Dette kan brukes til å monitorere lyder fra dyr i vann, eller å følge med på ulyder fra båter. Applikasjonen prosesserer store mengder data (150GB per dag per hydrofon). Den tar også imot data fra andre sensorer, som GPS, som korreleres med lyddataene.

Applikasjonen består av en backend skrevet i C# ASP.NET, med en frontend skrevet i Angular, og distribueres til Windows, Debian, RHEL og Docker.

Sindre skrev backend og første versjon av frontend, og jobbet med pakking av applikasjonen til de forskjellige plattformene. Han skrev en prosesserings-pipeline som sørger for at applikasjonen bare prosesserer data som brukerne trenger, og unngår dobbel prosessering når flere brukere trenger det samme. Han har også funnet løsninger på diverse nettverksproblemer hos hydrofonene.

Nøkkelord: C#, .NET, Angular, WiX Toolset, Docker, Windows, Linux

### Hobbyprosjekt

- Prosjekt: Operativsystem
- Periode: 2025 – nå

Sindre har et hobbyprosjekt der han skriver sitt eget operativsystem. Det blir skrevet for både x86_64 og RISC-V, med en egen bootloader. Operativsystemet bruker en microkernel-arkitektur der kernel gjør så lite som mulig, og overlater ansvaret til privilegerte user-space prosesser.

Bootloader, kernel, drivere og applikasjoner i user-space er skrevet i Rust, med litt assembly der det er nødvendig. Det testes foreløpig i en virtuell maskin gjennom QEMU, men det skal testes på ekte maskinvare når det er stabilt nok.

Nøkkelord: Rust, Qemu, RISC-V, x86, Assembly

### Konsulent

- Kunde: Thales Norway
- Prosjekt: Gradert
- Periode: 03.2022 – nå
- Logo: images/logo-thales-norway.png

Sindre er en del av teamet hos Thales Norway som utvikler løsninger for et system for konfigurasjonsstyring og avvikshåndtering av maskiner på et gradert nettverk.

Sindre fikk hovedansvar for utvikling av en Kotlin backend som samler konfigurasjon og retter avvik, og et web-grensesnitt som presenterer konfigurasjon og avvik for en operatør.

Sindre utredet også mulighetene for å legge til video-streaming i en VoIP applikasjon skrevet i C++ og Qt. Dette krevde at han satte seg inn i en stor og gammel kodebase som var bygd rundt prosessering av lyd, og foreslå endringer i arkitekturen for å legge til støtte for video.

Nøkkelord: Kotlin, C++, Qt, SIP, SSH, SNMP, WMI, CIM, TLS, TCP, UDP, Windows, Linux

### Konsulent

- Kunde: Skandia Energi
- Prosjekt: Android app for oversikt over strømforbruk
- Periode: 09.2021 – 02.2022
- Logo: images/logo-skandia-energi.png

Skandia Energi utviklet en app for at kunder skulle kunne følge med på strømprisen og strømforbruket sitt enklere, og kunne tilpasse seg til når strømmen er billig. Under utviklingen ble designet av appen endret, og Sindre kom inn for å implementere det nye designet for Android.

Sindre identifiserte raskt svakheter i appens tilstandshåndtering. Han refaktorerte arkitekturen ved å innføre en reaktiv MVVM-modell. Han skrev om Repository- og ViewModel-laget til å bruke Kotlin Flows, slik at endringer i data (f.eks. bytte av visningsseksjon eller oppdatert brukerinfo) propagerte umiddelbart gjennom hele applikasjonen. Dette sikret en robust dataflyt og en sømløs brukeropplevelse uten behov for manuelle oppdateringer.

Nøkkelord: Android, Kotlin, MVVM, Reactive Programming, Coroutines, Flow

### Konsulent

- Kunde: Sunlit Sea
- Prosjekt: Bølgemåler
- Periode: 08.2021
- Logo: images/logo-sunlit-sea.png

Sunlit Sea er et nyoppstartet firma som utvikler flytende solcellepaneler for bruk på vann.

For å legge solceller på vann er det nødvendig med grundige undersøkelser av forholdene i området. En del av dette er bølgeforholdene og hvordan de påvirker panelene. Sindre jobbet med å videreutvikle et Open-Source program for en flytende bølgemåler som samler inn og analyserer data med Fast Fourier Transforms. Resultatet ble sendt over Iridium til et system som setter sammen en full analyse av forholdene for utplassering av en solcelle-installasjon.

Nøkkelord: C++, Arduino, Mbed OS.

### Masteroppgave

- Kunde: NTNU
- Prosjekt: Porting av Inferno til RISC-V
- Periode: 08.2020 – 08.2021
- Logo: images/logo-ntnu.png

Inferno er et operativsystem fra Bell Labs, som ble utviklet av de samme folkene som tidligere hadde lagd Unix. Det har en innebygd virtuell maskin slik at applikasjonene kan kjøre uavhengig av prosessorarkitektur.

Sindres oppgave var å porte Inferno til å kjøre på den nye RISC-V arkitekturen. Først måtte han integrere en kompatibel kompilator, fordi Inferno bruker sin egen dialekt av C. Denne kompilatoren produserte ikke debug-informasjon for verktøy som GDB, så all debugging måtte kjøres på assembly-nivå. Når kompilatoren var på plass måtte Sindre skrive et entrypoint for operativsystemet som konfigurerte prosessoren, klargjorde minneområder og satte opp timer og interrupts. Etter det skrev han drivere for tastatur og mus, og en grafikkdriver. Til slutt skrev han en Just-In-Time kompilator fra bytecode for den virtuelle maskinen til bytecode for RISC-V.

Nøkkelord: C, RISC-V, Assembly, QEMU, Inferno

### Lead Utvikler

- Kunde: Lilbit
- Prosjekt: Android App
- Periode: 06.2020 – 08.2021
- Logo: images/logo-lilbit.png

Lilbit AS (tidligere Tail it Technologies AS) produserer små GPS-enheter, hovedsakelig for kjæledyr

Lilbit har en mobil-app som kobler til GPS-enheter for å se hvor de er, og få varsler når de går utenfor et gitt område.

Sindre var lead developer for en ny versjon av Android-appen, som ble laget fra bunnen. Han hadde også ansvar for bluetooth-kommunikasjon med GPS-enhetene.

Nøkkelord: Android, Kotlin, Room, Bluetooth

### Studentprosjekt

- Kunde: NTNU
- Prosjekt: TDT4295 Datamaskinprosjektet / TDT4255 Datamaskinkonstruksjon
- Periode: 08.2019 – 12.2019
- Logo: images/logo-ntnu.png

I 4. klasse på NTNU tok Sindre to fag som fokuserte på FPGA og hardware.

I Datamaskinprosjektet skulle en gruppe studenter designe og programmere et kretskort fra bunnen av. Når Sindre tok faget skulle gruppen lage et lydbrett som tok inn lyd og la på effekter. Kortet skulle inneholde en FPGA for real-time lydprosessering og en MCU for kontrollering. Sindre hadde erfaring med kretskortdesign og FPGA-programmering, så han tok lederrollen for de delene av prosjektet. Han designet store deler av kretskortet, gjorde feilsøking når det var produksjonsfeil, og satte opp pipeline, struktur og lavnivågrensesnitt for FPGA-koden. Til slutt der man kunne legge på lydkompresjon, tremolo og ekko i real-time.

I Datamaskinkonstruksjon skulle studentene programmere hver sin RISC-V prosessor på en virtuell FPGA. Man startet med et enkelt design som håndterte én instruksjon av gangen, og la gradvis til funksjonalitet. Til slutt hadde Sindre en 5-stegs pipeline med flush ved branch miss, operand forwarding og branch prediction.

Nøkkelord: PCB, KiCAD, FPGA, Scala, Chisel, Verilog, Lydprosessering

### Konsulent

- Kunde: Eyasys
- Prosjekt: Battery Stick
- Periode: 03.2019 – 06.2020
- Logo: images/logo-eyasys.png

Eyasys tilbyr helhetlige løsninger i sjiktet mellom sikkerhet, pålitelighet, programvare og ved behov, tilpasset maskinvare.

Battery Stick er et mobilt batteri, rettet mot bønder i Afrika, som kan lades opp med solceller, og kan drive diverse elektriske apparater.

Produktet blir som regel utlånt til bøndene i noen måneder av gangen. Sindre hadde ansvar for å implementere en mekanisme som gjør at batteriet bare kan benyttes når kunden har betalt for det. Dette ble gjort gjennom krypterte koder som kunden måtte taste inn, siden det ikke alltid er tilgang på internett. Sindre designet et krypterings-regime som var tilpasset maskinvarens begrensede ressurser, som produserte koder som var korte nok til å taste inn for hånd og som ikke enkelt kunne knekkes.

Nøkkelord: C, ARM Cortex-M, Kryptering

### Konsulent

- Kunde: Vaskehjelp
- Prosjekt: Android App
- Periode: 01.2019 – 02.2019
- Logo: images/logo-vaskehjelp.png

Vaskehjelp AS er en markedsplass som knytter kunder opp mot vaskere i sitt geografiske område. De gjør det enkelt for kunder å finne renholdere i sitt område, og håndterer betaling og forsikring for å gjøre det trygt og enkelt for begge parter.

Mobilapplikasjonen er hovedplattformen til Vaskehjelp, og det er den både kunder og renholdere bruker for å legge ut og finne oppdrag. Det er separate apper for iOS og Android, og de utvikles parallelt.

Android-appen hadde en del problemer med brukervennlighet og funksjonalitet, og utviklingen hadde falt etter IOS-appen. Sindre ble da hyret inn for å redde Android-appen. Han jobbet mest med frontend og UX, men han var også involvert i en omstrukturering av appen.

Nøkkelord: Android, Kotlin, Room, Koin, Android Navigation, Retrofit

### Fullstack Utvikler

- Kunde: KodeWorks
- Prosjekt: Webapplikasjon for likviditetsberegning
- Periode: 01.2018 – 08.2018

Kodeworks har utviklet et internt system som gjør likviditetsberegning mer effektivt og mer anvendelig. Applikasjonen er utviklet av to team - et ansvarlig for å utvikle brukergrensesnittet, og et ansvarlig for å utvikle business-logikken i backend.

Sindre har designet grensesnittet mellom frontend og backend og implementert dette på backenden. Hovedsaklig jobbet med Java og databaser.

Nøkkelord: Java, SQL, CI/CD, Python, Django, Docker + docker-compose, Unit- og Integration Testing

### Lead Utvikler

- Kunde: KodeWorks
- Prosjekt: Android app for balansebrett
- Periode: 01.2018 – 04.2019

Kodeworks fikk oppdrag om å lage en app og backend for et balansebrett, som måler bruk gjennom dagen. Brettet bruker en Thingy:52 fra Nordic Semiconductors for å måle akselerasjon, og appen skal analysere denne informasjonen og vise aktivitetsdata til brukeren. Man kan også konkurrere med hverandre innad i en bedrift, eller i mindre teams.

Sindre er hovedutvikler på prosjektet, og har ansvar for Android-appen, backend og hardware.

Nøkkelord: Android, Kotlin, Room, Dagger 2, Firebase, Gamification

### Lead Utvikler

- Kunde: KodeWorks
- Prosjekt: Vipps som myntinnkast
- Periode: 12.2017 – 08.2018

Kodeworks ønsket å utvikle en måte å bruke vipps som betalingsløsning for pinball- og andre arkademaskiner. Løsningen skulle være slik at en kunde raskt og enkelt kunne gå inn i vipps-appen, søke opp maskinen, og betale for et visst antall spill.

Sindre fikk ansvar for prosjektet, og han har kommet med en løsning som bruker en PyCom WiPy mikrokontroller som blir montert i maskinen. Denne er koblet opp mot en server, som igjen er koblet til vipps sin backend.

Nøkkelord: Micropython, Scala, Akka

### Lead Utvikler

- Kunde: KodeWorks
- Prosjekt: HAKO
- Periode: 07.2017 – 12.2017

Kodeworks ønsket å utvikle en egen hardware som kunne settes opp som en Secure Mobile Platform. Det ble designet og produsert kretskort med en Texas Instruments AM437x prosessor og komponenter for bla. wifi, 3G og satellittkommunikasjon. Denne maskinen skulle kjøre Android for å gjøre utvikling av programmer lettere.

Sindre jobbet med å tilpasse Android til å kjøre på denne maskinen. Først måtte Linux-kernel tilpasses til å fungere både med maskinvaren og Android. Så måtte det skrives grunnleggende konfigurasjon og drivere for å kunne starte Android på maskinvaren og få ut debug-informasjon. Til slutt måtte Sindre skrive drivere for å gjøre Android brukbart på maskinen.

Nøkkelord: Android, AOSP, Linux kernel, Java, C, C++

### Studentprosjekt

- Prosjekt: Nettside for MAKE NTNU
- Periode: 2017 – 2021

På NTNU var Sindre medlem av organisasjonen MAKE NTNU, som drev et makerverksted på campus.

Sindre var med i web-komiteen som lagde nettsidene for verkstedet. Nettsiden bestod av påmelding til kurs, booking av symaskin og 3D-printer, og videostrømming fra 3D-printere. Sindre var med i web-komiteen siden start, og jobbet med alle delene av nettsiden.

Nøkkelord: Python, Django, PostgreSQL, WebSockets

### Personlig prosjekt

- Prosjekt: Nettsiden for Bispehaugen Ungdomskorps
- Periode: 2016 – 2021

Under studiet var Sindre medlem av Bispehaugen Ungdomskorps, og drev nettsidene deres.

Nettsidene bestod av en offentlig del med informasjon og kalender, og en intern del med forum og filarkiv. Når Sindre startet var nettsiden skrevet i PHP, men han jobbet for å skrive om alt til Django.

Nøkkelord: Python, Django, PostgreSQL, PHP

## Arbeidserfaring

- 08.2021 – nå | KodeWorks | Konsulent
- 01.2021 – 05.2021 | NTNU | Vitenskapelig assistent
- 07.2017 – 07.2021 | KodeWorks | Konsulent (deltid)
- 05.2017 – 07.2017 | Eyasys AS | Sommerjobb

## Utdanning

- 2016 – 2021 | Mastergrad i Datateknologi | NTNU Trondheim

## Foredrag og publikasjoner

- 2023 | Hvordan lage et programmeringsspråk
  - Sindre holdt et kurs for Kodeworks, som gikk ut på å lage et eget programmeringsspråk med en interpreter skrevet i Rust.
- 2022 | Intro til Rust
  - Sindre holdt et introkurs til Rust for Kodeworks.
- 2018 | Pinball + Vipps. Bruk av automatisk Vipps betaling i en Pinball-maskin.
  - https://medium.com/kodeworkslabs/pinball-vipps-5c80c55054c1
