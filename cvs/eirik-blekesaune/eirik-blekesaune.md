# Eirik Blekesaune

Ekspert Konsulent

- Telefon: +47 415 00 966
- E-post: eirik.blekesaune@kodeworks.no
- Erfaring: 10+ år
- Språk: norsk, engelsk
- Foto: images/foto.jpg
- Fotofokus: 0.5, 0.3

## Om Eirik

Eirik er en dyktig fullstack utvikler med over 10 års erfaring. Han har bred erfaring med programmeringsspråk som Java, SuperCollider, C++, Rust, JavaScript/TypeScript, CSS, Python, og arbeidet med rammeverk som Spring, React og Angular. Eirik har jobbet på tverrfaglige prosjekter, noe som har gitt ham en unik evne til å forstå problemstillinger fra forskjellige perspektiver og fremme felles forståelse i samarbeid.

Som en lyttende og fleksibel samarbeidspartner, er Eirik engasjert i å støtte kolleger og dele kunnskap. Han er en av arrangørene bak Rust Trondheim Meetup-gruppen, hvor han arrangerer månedlige workshops, og han har hostet en internasjonal online-meetup for SuperCollider-programmering.

Eiriks erfaring inkluderer design, implementering og feilsøking av programvare for komplekse, sammenkoblede og distribuerte digitale systemer. Han har jobbet med kommunikasjon mellom datamaskiner, roboter og mikrokontrollere, og har designet kretskort for motorstyring, lys og sensorinnhenting. For design og konstruksjonsarbeid bruker han CAD-programvare som Eagle, FreeCAD, Vcarve og SketchUp, og har erfaring med CNC-maskin, 3D-printer og laserskjærer.

## Teknisk kompetanse

### Språk og rammeverk

Java, C++, Bash, Javascript, Typescript, React, Rust, Arduino, SuperCollider, Node.js/Deno, Python, CSS/HTML

### Plattform, tech og verktøy

Git, MacOS, MongoDB, Maven, Zigbee, Postman, VS Code, Json, Linux, Vim/NeoVim, NPM, SQL, FreeCAD, Eagle, Eclipse

### Metode

Agile, Scrum, Kanban, DevOps

## Erfaring

### Utvikler

- Kunde: inatur.no
- Periode: 06.2023 – nå
- Logo: images/logo-inatur.png

Inatur sine systemer består av blant annet en applikasjon skrevet i Java/Spring, med en front-end bestående av nyere TypeScript/React-kode of eldre legacy kode skrevet i backbone.js.

Oppgavene mine er hovedsakelig utvikling av nye tjenester for Inatur, både på frontend og backend, samt forvaltning av den eksisterende kodebasen gjennom optimalisering, refaktorering og feilretting.

En av oppgavene min var å utvikle et system for logging av endringer brukere gjør. Dette har gitt Inatur et nyttig verktøy for å bedre dialog og support for kundene sine. Systemet registrerer forandringer som blir gjort på tilbudene som tilbydere setter opp og lager differenslogginger av de, slik at feilsøking for både bruker- og systemfeil har blitt enklere og mer effektivt.

Jeg har bidratt til en større integrasjonsprosess av en karttjeneste, levert av et eksternt konsulentfirma, som har krevd mye samhandling på tvers av utviklerteam. Her har en del av oppgaven gått ut på ytelsesoptimalisering gjennom analyse av ytelesmonitorering og komme anbefalinger til måter å øke ytelsen på. Det har også vært viktig at vi har fått til en bra samarbeidskultur på tvers av teamene, med tett kommunikasjon, proaktiv holdning til å avklare uklarheter i leveringsspesifikasjoner, samt en vennlig og løsningsorientert formidling av behov for forbedringer.

I dette integrasjonsarbeidet har jeg også laget brukerdesign og implementert et brukerverktøy for sanntids-aktivering av jaktkort. Dette verktøyet er et av de mest tids- og belastningkritiske delene av Inatur sine systemer, da det skal understøtte mange påloggede brukere som konkurrerer om å gjennomføre aktiveringer innen kort tid. De største utfordringene her var å tilrettelegge for en god brukeropplevelse i frontend gjennom optimaliseringer i hele stacken, samt fokus på testing, universell utforming, og støtte for både mobil-, lesebrett-, og desktopbrukere. På backend har jeg gjort flere framtidsrettede omstruktureringer av datamodellene, samtidig som vi opprettholder god forvaltning av legacy kode, som det ikke er budsjettert med å refaktorere per nå.

I prosjektet har jeg også gjennomført en større oppgave med å oppgradere og standardisere testkoden til Inatur, slik at tilliten til testene og har økt og kjøretiden for hele testsuiten har blitt redusert til halvparten. Jeg er opptatt av at utviklerne har god flyt i arbeidet sitt, og automatisering av kvalitetssjekking mener jeg skaper en bedre utvikleropplevelse.

Nøkkelord: Java, React, Spring, Gradle, JavaScript, TypeScript, REST APIer, MongoDB, backbone.js

### Prosjekteier / utvikler

- Prosjekt: A Thoth Work
- Periode: 2020 – 2022

A Thoth Work er en kunstinstallasjon av Eirik Blekesaune, hvor trepinner heises ned fra taket til absolutte posisjoner foran en videoprojektor. Systemet består av en hardwarenivå med robotikk og styringsbokser, en grafikkserver, og et sentralisert styringssystem. Alle enhetene kommuniserer over nettverk. Systemet har vært stilt ut som en selvgående installasjon i 2 måneder på galleriet Studio.TEKS i Trondheim i 2022. Video av utdrag fra arbeidet kan ses her: https://www.eirikblekesaune.com/a-thoth-work

Eirik har designet, implementert og bygd alle de teknologiske enhetene i dette prosjektet. Det er fire nivåer i stacken: hardware med 8 stk. Teensy (ARM Cortex M7) mikrokontrollere, 4 stk. Wifi-joystickbokser, én grafikkserver, og ett sentralisert styringsprogram. Komponentene i systemet kommuniserer over nettverk, hovedsaklig gjennom UDP/OSC.

Kravvspesifikasjonene kom fra de kunstneriske visjonene, de tekniske rammene for avvikling, og den faglige interessen for utviklerfaget. Disse kan oppsummeres kort slik:

- Fleksibilitet i bruk og konfigurasjon:
  - Systemet skal kunne settes opp på kort tid, til ulike typer rom og visningssteder.
  - Det skal kunne kontrolleres både i sanntid og gjennom forhåndsprogrammerte rutiner og sekvenser.
- Åpen for utvidelse av implementasjon:
  - Nye moduler skal enkelt kunne integreres med eksisterende rammeverk.
- Forutsigbarhet og driftssikkerhet:
  - Visningssituasjonen opererer innen små tids- og budsjettrammer. Det er lite tid til montering, kalibrering og vedlikehold.
- Selv-monitorering og fjern-support av elektromekanikk, sensorer og kjøring av programvare.
  - Systemer vil oftest kjøre uten kompetent teknisk personale tilstede, og må derfor kunne enkelt vedlikeholdes og fjernovervåkes.

De 8 robotene som heiser pinnene fra taket er basert på en Teensy mikrokontroller med Ethernet grensesnitt. Disse styres over UDP/OSC for å få høy hastighet i kommunikasjonen mellom styringsprogrammet. Hver robot har to DC-motorer med encodere som signaliserer hvert trinn de går, og i hvilken retning. Dette bruker jeg til å gjøre om DC motoren til en servo, som gir mulighet til absolutt posisjonering og dobbelsikring av ytterposisjonene. Dvs. både mekanisk stoppbryter og software-grense for posisjoner for topp og bunnposisjon. Pinnene kan kontrolleres i sanntid med 4 joystickkontrollere som kommuniseres via WiFi. Koden for robotikken og de trådløse joystickkontrollerene er skrevet i C++.

Styringssystemet sender posisjons-requests til robotene med mulighet for å deklarere bevegelsesdynamikk og hastighet. PID-kontroller på MCU sørger for å posisjoneringen skjer presist og med kontroll over jevn endring i akselerasjon. MCU sender kontinuerlig tilstandsrapport for hver "flytt" tilbake til både styringsprogram og grafikkserver. Siden transportlaget ikke implementerer overføringsbekreftelse er hver "flytt" tagget med en pakke-ID som gjør at styringsprogram kan ta stilling til hvorvidt kritiske beskjeder har kommet over til robot.

Grafikkserveren er skrevet i Rust, med bruk av grafikkbiblioteket Nannou. Det har et deklarativt, typesikkert API man bruker over UDP/OSC/JSON. Geometriske enheter deklareres fra styringsprogrammet, og disse vises på videoprojeksjon på bakvegg. Geometrien oppdateres i sanntid basert på pinnenes fysiske posisjoner i rommet, og gjennom utregning av pinnenes skyggeprojeksjon på veggen kan jeg tegne kunstige skygger som følger de ekte skyggene.

Styringsprogrammet er skrevet i SuperCollider. Dette programmet kommuniserer med robotikk, mottar signaler fra joysticker, styrer lyd, lys og grafikk. Programmet har en grafisk grensesnitt som monitorer og styrer systemet. Systemet kan også styres gjennom joystickene, eller en REPL. Koden er skrevet i rammeverket VTM som jeg har laget.

**Utviklingsprosjekter oppsummert**

- Trådløs joystick kontroller, for styring av robotikk
- Grafikkserver styrt gjennom OSC/UDP
- Robotikk-, lyd- og grafikkstyringssystem
- GUI
- Mikrokontroller for elektromekanisk skulptur
- Utvikling av nettverks API for fjernstyring, monitorering og debugging
- PID-kontroller for regulering av hastighet og absolutt posisjonering
- Implementasjon redundant styringslogikk for driftssikkerhet

Nøkkelord: C++, Arduino, Rust, SuperCollider, Teensy, FreeCAD, 3D printing, CNC

### Prosjekteier / utvikler

- Kunde: Verdensteateret
- Prosjekt: Broen over Gjørme
- Periode: 2012 – 2015

Verdensteatret er en norsk kunstgruppe som arbeider med store multimediale prosjekter. Broen over Gjørme var den mest komplekse teknologiske produksjonen Verdensteatret har laget så langt. Min hovedrolle i dette prosjektet var design og implementasjon av systemer som skulle gjøre det mulig å styre og sammenkoble alle mediene i scenerommet. Verket turnerte internasjonalt og fikk flere nasjonale priser, ibl.a. Heddaprisen for beste audiovisuelle design.

Som utvikler i dette prosjektet var Eirik systemarkitekt og programmerer av et distribuert modulsystem, samt utvikler av surroundlydsystem, flertallige roboter, elektronikk, LED-lys systemer, videotrackingsystem, og et system for modelltogbane som fraktet lys, høyttalere og skulpturer.

Surroundlydsystemet var designet som en sentralisert server som fordelte lyden i de 80 forskjellige høyttalerne vi hadde satt opp i scenerommet. Klientene styrte serveren gjennom proxy-objekter eller et JSON API. Systemet kunne gjøre de fleste kjente spatialiseringsteknikker for et arbitrært utvalg av høyttalere. Systemet konfigurerte all nødvendig forsinkelsestid basert på posisjonen til hver enkel høyttaler. Det inkluderte en sanntids-lydanalyse tjeneste hvor klienter kunne subscribe til f.eks. pitch for vilkårlige lyder som spilte på serveren. For sin tid var dette systemet noe helt nyskapende, særlig siden det tilrettela for å arbeide med lydspatialisering innen flere ulike paradigmer på en fleksibel måte.

Av robotikk lagde jeg

- 20 takhengte roboter som heiste objekter og høyttalere opp og ned fra taket.
- 5 roboter som styrte fugleskjellettskulpturer.
- 16 trådløse Wifi-lokomotiver med fartsregulering, posisjonerings- og videotrackingsystem, og I2C-grensesnitt for utvidelse med peripherals som f.eks. ekstra LED-dimmere. For sanntids-tracking av posisjon bygde jeg inn en encoder og en IR diode. I mellom svillene i togbanen la jeg små egendesignede kretskort som sendte ut IR lyssignaler som gav lokomotivet beskjed om absolutt posisjon. Encode gav relativ bevegelse mellom kalibreringspunktene som kunne fortelle absolutt posisjon til videotrackingen.

Til alt dette brukte Eirik Arduino, Raspberry Pi, ATTiny14, som styrte DC-, servo- og stegmotorer. Kretsutlegg ble gjort med Eagle.

Eirik utviklet også en egen seriell protokoll og API for de mest komplekse robotene som gav mulighet for innhenting og monitorering av tilstand, samt typesikkerhet. Siden all kommunikasjon mellom enhetene var såpass domenespesifikk og at transport skjedde gjennom RS-232, ZigBee, eller UDP, så var det på den tiden enklere å implementere en egen avgrenset kommunikasjonsprotokoll, framfor å implementere noe ala MQTT-SN.

En kort video av dette verket kan ses her: https://vimeo.com/121460838

**Utviklingsprosjekter oppsummert**

- Trådløst kontrollert modelltogbane, med videotracking og absolutt posisjonering.
- Arkitektur og implementasjon av modulært rammeverk for et nettverk av digitale enheter som skal kontrollere hverandre.

Nøkkelord: SuperCollider, C++, Max/MSP, Arduino

## Arbeidserfaring

- 2023 – nå | KodeWorks | Konsulent
- 2010 – 2019 | Verdensteateret | Systemutvikler
- 2007 – 2010 | NTNU | Lektor innenfor elektronikk, programmering og lyddesign

## Utdanning

- 2005 – 2009 | Master i Musikkteknologi | NTNU Trondheim

## Sertifiseringer

- 2023 | ISTQB CTFL - Certified Tester Foundation Level

## Verv og engasjement

- 2006 – 2020 | Undervisning, veiledning og sensur | NTNU Trondheim
  - NTNU, MUST2059 Lydkunst: Forelesninger om avspillingsteknikker med bruk av multihøyttaleroppsett og surroundlyd, veiledning og sensur.
  - Høyskolen Kristiania, Lydprogrammering: Foreleser, veileder, og sensor. Lydprogrammering med Max/MSP og JavaScript
  - Kunsthøgskolen i Oslo, Master i Teater: Teknisk og kunstnerisk biveileder for masterstudent i regi.
  - NTNU, MUST1056, Musikkteknologi og kreativitet: Elektronikk og sensorteknologi. Foreleser, veiledning.
  - NTNU, MUST2057, Musikkteknologi i møte med publikum: undervisning og veiledning
  - NTNU, MUST1058, Musikkteknologi i historisk lys: Foreleser
  - NTNU, MUST2059, Lyd i offentlige rom: Forelesninger og workshops i elektronikk og sensorteknologi
  - NTNU, MUST2060, Lyd i offentlige rom II: Emneansvar, foreleser, veiledning. Grafikkprogrammering og lyd for dataspill
  - NTNU, MUST2059, Lyd i offentlige rom II: Forelesninger og veiledning. Elektronikk og lydkunstteori
  - NTNU, MUST1056: Forelesning og veiledning om sensorteknologi
  - NTNU, MUST2060: Forelesning og workshop i grunnleggende grafikkprogrammering med Pd/Gem
  - NTNU, MUST1052: Foreleser og veiledning. Programmering i Max/MSP
  - NTNU, MUST2059, Lyd i offentlige rom II: Underviser i sensorteknologi og elektronikk
  - NTNU, MUST3053, Digital signalprosessering: Emneansvar, underviser, veiledning, sensur. DSP teori og praksis for lydsignaler
  - NTNU, MUST1054, Musikkteknologi og kreativitet: Underviser, veiledning. Lydprogrammering med Csound
  - NTNU, MUST1054, Musikkteknologi og kreativitet: Underviser og studentassistent, programmering i Max/MSP

## Foredrag og publikasjoner

- 2023 | "Om: Algoritmer", foredrag om teater og algoritmer på Dramatikkens Hus
- 2020 | Oppdagelse av Pinnespråk, foredrag om robotikk og dans, Rimi/Imir scenekunst, Stavanger
- 2018 | Foredrag om egen kunstnerisk praksis, OsloMet, avd. For drama og teater.
- 2018 | Foredrag om egen kunstnerisk praksis, Høyskolen i Østfold, scenekunstakademiet
- 2018 | Foredrag om kunstnerisk forskning i Verdensteatret, Kunsthøgskulen i Oslo
- 2016 | Foredrag og Verdensteatrets "rom-instrument", Dramatikkens Hus, Oslo
- 2012 | Foredrag om Verdensteatrets kunstneriske praksis, NTNU, MUST2061
- 2011 | Foredrag om egen kunstnerisk praksis, Harvestworks, New York, USA

## Kurs

- 2022 | Epic React: React Fundamentals Workshop
- 2022 | Epic React: React Fundamentals Workshop
