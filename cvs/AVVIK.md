# Avvik og valg ved konverteringen av CV-ene

CV-ene i denne mappen er konvertert én gang fra Word-originalene (én PDF) til KodeWorks' CV-format i Markdown. Innholdet er beholdt som i originalen, og bare formen er gjort lik. Under står, per person, det konsulenten selv bør rette eller ta stilling til: feil i originalen, innhold som ikke fikk plass, felt som mangler, og valg som ble tatt under konverteringen.

Alle filene består kontrollen (`uv run python src/check_cv_md.py cvs/*/*.md`) og bygges til PDF uten feil.

**Felles for flere:**

- **Logoer med lav oppløsning** (byggeskriptet advarer): Sunlit Sea (200 × 200 piksler, 149 dpi) hos Jan-Marius Vatle, Simen Moen Storvik, Sindre Stephansen og Vegard Stengrundet; NTNU (126 dpi) hos Sindre Stephansen; Lilbit (157 dpi) hos Ørjan Bostad Vesterlid; AppearTV (199 dpi) hos Aleksander Skraastad. En felles logo i bedre oppløsning (helst SVG) bør skaffes og brukes av alle.
- **Kunder som er utledet** fra logo, tittel eller tekst fordi originalen ikke hadde kundefelt, bør bekreftes av konsulenten (se den enkelte).
- **Utelatte logoer:** når kunden er KodeWorks, og der originalen hadde feil logo (Thomas Ax Gulbrandsrød: Sunami med EyaSys-logo; Ørjan Bostad Vesterlid: 3T Treningssenter med WTW-logo).
- **Uten ekte portrett:** Lasse Holanger. PDF-en viser da en grå plassholder.
- **Formatet støtter ikke** lenker eller kursiv. Der originalen hadde det, er lenken eller stjernene fjernet og notert.

## Aleksander Skraastad

- Bygg-advarsel: logoen til AppearTV er 200 × 200 piksler (199 dpi ved 19 mm). Bygget melder også 2 «overfull boxes» (smal tekst som stikker litt utenfor, trolig lange nøkkelord-/URL-linjer). Ser ikke feil ut i PDF-en, men bør sjekkes.
- Kunde mangler i originalen for flere prosjekter. Utledet fra logo og tekst: DNB (RDM/EDM, teksten nevner DNB og logoen er DNB), Statkraft (Fusion og Algorithmic Trading, Statkraft-logo og tekst), AppearTV (Gateway, logoen er Appear; arbeidsgiver heter «AppearTV» i Arbeidserfaring). Bør bekreftes.
- Prosjektet Algorithmic Trading har ingen egen rolle i originalen. Det følger rett etter Fusion og har fått Fusions rolle («Utvikler / Tech lead / Team lead»).
- Nøkkelord: «Elhub» to ganger i EnerSky, «Tailwind v5» (trolig v4), «TypeScript 5» uten «v». Beholdt.
- EnerSky-teksten har lenken enersky.no og Fusion-teksten beacon.io som lenker i originalen. De står nå som ren tekst.
- Valg: «(deltid)» på to rader i Arbeidserfaring (Telenor Digital, MyWorkout AS) stod i arbeidsgiverfeltet; flyttet til parentes etter perioden.
- Valg: arbeidsgiverne «KodeWorks Oslo» og «AppearTV» beholdt som i originalen.
- Rolle for EnerSky-prosjektet har tre titler («Arkitekt / Utvikler / SRE»); beholdt.
- «Publikasjoner» (2017) lagt i «Foredrag og publikasjoner».

## Brage Wichstrøm

- Originalens «Prosjekt»-felt inneholdt kundenavn for CK Consult og Enersky. De er brukt som `Kunde` uten `Prosjekt`. For «Masteroppgave» (logo NTNU) og «Sommerjobb» (logo KSAT, og Arbeidserfaring sier Kongsberg Satellite Services) er kunden utledet fra logoen og arbeidserfaringen, og originalens prosjektnavn står som `Prosjekt`. Bør bekreftes.
- Alle fire prosjektene har rollen «Programvareutvikler», også masteroppgaven og sommerjobben. Beholdt.
- Enersky (07.2024 – 08.2024) sto sist i originalen men er nyest, og er sortert først.
- CK Consult og Enersky har ingen logo i originalen.
- Skrivefeil beholdt: «i AW» (AWS), «hosting av i AWS», «Sckit-learn», «manuell mottak», «authentiseringstjeneste», «kontainere». Masteroppgave-beskrivelsen mangler punktum.
- Originalens «Artikler, foredrag og verv» inneholdt bare to verv (TIHLDE, Itemize), uten perioder. Lagt i «Verv og engasjement» med tom periode. TIHLDE-teksten er lang og beholdt hel.
- Side 3 i PDF-en er halvtom, fordi bygget velger å starte «Generelt» på ny side fremfor å splitte det.

## Dee Roberts

- Originalen blander «Dee» og «han» i Om-teksten, og «Jeg» i prosjektbeskrivelser (Inatur). Beholdt uendret.
- «Nåværende» i Inatur-perioden er skrevet som «nå».
- Inatur-logoen i originalen er svært liten (119 × 40 px). Byttet til den større Inatur-filen (255 × 85 px) fra Simen Moen Storvik sin CV, siden det er samme logo. Bør byttes mot en ordentlig fil.
- Periodene «01.2024» (KodeWorks) og «02.2024» (Inatur) og Asolvi (Arbeidserfaring 08.2019 – 07.2020, prosjekt til 08.2020) er ulike i originalen. Beholdt.
- To studentprosjekter (Brettspill utviklingsplattform, eLæringsmodul for e-helse), fra seksjonen «Artikler, foredrag og verv», står under Foredrag og publikasjoner med Keele University og UCL som sted. Det er egentlig studentprosjekter, ikke publikasjoner. Konsulenten bør ta stilling til plasseringen. Tittelen har punktum («Brettspill utviklingsplattform.»), beholdt.
- Skrivefeil beholdt: «ut ifra», «rettningsfinnendevnene», «Et grafisk editor», «Et GDPR-kompatibel», «oppholdt», «Arkitekte», «OAuth2-flytter».
- Bygget: «Generelt»-overskriften blir stående alene nederst på side 4 med listene på side 5 (se svakheter i rapporten).
- Fotoet er PNG (521 × 568), og er brukt som images/foto.png.

## Eirik Blekesaune

- Fotoet er et helfigursbilde (stående i en gate, 1536 × 2048). Jeg har lagt til `Fotofokus: 0.5, 0.3` for at ansiktet skal havne i rammen. Bør byttes mot et ekte portrett.
- Kun én logo (inatur.no). A Thoth Work (egen kunstinstallasjon) og Verdensteateret har ingen logo i originalen, og logoer er ikke funnet.
- A Thoth Work har ingen kunde (egen produksjon). «Kunde» er utelatt, ikke diktet opp.
- Verdensteatret-prosjektet har ingen egen rolle i originalen; det følger rett etter A Thoth Work og har fått samme rolle («Prosjekteier / utvikler»). Kunde er satt til «Verdensteateret» som i originalen (skrivefeil for «Verdensteatret» som brukes i teksten).
- Perioden for Inatur var «Juni 2023 – nå» (månedsnavn gjort om til 06.2023).
- Teksten veksler mellom første og tredje person («Oppgavene mine», «Eirik har», «jeg»). Beholdt, men bør jevnes ut.
- Skrivefeil beholdt: «of eldre» (Inatur), «En av oppgavene min», «ytelesmonitorering», «Kravvspesifikasjonene», «tilrettela for å arbeide», «Verdensteateret», «ibl.a.»
- Valg: «Undervisninger / Veiledning / Sensur» (16 emner, 2006 – 2020) passer ikke i noen av de faste listene. Lagt i «Verv og engasjement» som én rad med emnene som underpunkter (originalens fete titler er gjort om til «Tittel: beskrivelse»). Bør vurderes om det skal få egen fast tittel.
- «Kurs og sertifiseringer» delt: ISTQB CTFL under Sertifiseringer, «Epic React: React Fundamentals Workshop» under Kurs. Raden for Epic React står to ganger (2022) i originalen; beholdt begge.
- «Foredrag» (8 rader) lagt i «Foredrag og publikasjoner». Radene har bare periode og beskrivelse (ingen sted).
- Valg: lister med dobbel nivå (krav i A Thoth Work) er beholdt som nøstede punktlister.
- «Erfaring: 10+ år» beholdt.

## Eirik Larsen

- Originalen har ikke Erfaring-år, så feltet er utelatt. «Født 1979» har ikke noe felt og er ikke tatt med. Språknivå («Norsk Morsmål», «Engelsk Muntlig og skriftlig meget godt») ble til «norsk, engelsk» i kontaktlista, og nivåene mangler.
- Telefon er normalisert til «+47 416 70 269» (originalen «416 70 269»), og e-posten er beholdt.
- «Annen erfaring» (2014 – 2018: «Webrammeverk, maskinlæring, spillprogrammering») har ingen riktig plass i formatet. Lagt under Kurs som skjønnsvalg. Konsulenten bør ta stilling til dette.
- Foredrag er omformatert fra «Foredrag, JavaZone, JSF2 med Seam og Hibernate» til «JSF2 med Seam og Hibernate (foredrag) | JavaZone». Ingen logoer finnes (originalen har bare KodeWorks-logo), så alle prosjekter mangler Logo-linje.
- Prosjektene hadde rolle som egen rad («Rolle»). Første setning(er) av rollen er brukt som overskrift og resten av rolleteksten står som avsnitt etter beskrivelsen. Det gir noen overskrifter som er lister over roller (f.eks. «Kravspesifisering, Arkitekt, Utvikler, Tech-lead, Webdesign, Brukerinteraksjon»).
- Kundeintroduksjonen («Sunlit Sea utvikler …») ligger som første avsnitt i beskrivelsen. Politiet-prosjektene etter det første har ingen kundeintroduksjon i originalen.
- «Sikker Mobilplattform» og «Sentry» har begge periode «Mar 2017 – Nov 2017» i originalen, mens beskrivelsen av Sikker Mobilplattform sier 2010 – 2017. Sannsynlig kopifeil. Beholdt.
- Hako (01.2016 – 10.2017) overlapper flere andre prosjekter. Beholdt.
- Politiet MOVA har tre perioder i originalen (Jan 2009 – Aug 2015, Jan 2016 – Sep 2016, Jun 2017 – Sep 2017). Skrevet som «01.2009 – 08.2015 (også 01.2016 – 09.2016 og 06.2017 – 09.2017)».
- Prosjektet står sortert etter startdato, så MOVA (2009) ligger etter Apps for polititjenestemenn (2013). Navnet «Kodeworks» er skrevet «KodeWorks» i Kunde- og Arbeidserfaring-feltene, men «Kodeworks» er beholdt i løpende tekst.
- Skrivefeil beholdt: «prototyp», «kvalitetsikring», «feks», «ifm», «Avinor … kvalitet..», «et samfunnsoppdrag er å sørge», «låse- hardware», «Socket.io» osv. Kursiv rundt «Sentry» og «DIFAS,» er fjernet (formatet støtter ikke kursiv).
- «Forsvaret» (06.1999 – 06.2010) overlapper med alt annet, og står som i originalen.
- «Thomson Reuters»-prosjektnavnet «Web service og streaming av sanntids prognosedata.» har punktum, beholdt.
- Rolleinformasjonen i Arbeidserfaring-tabellen har punktum til slutt i originalen. Fjernet.

## Elias Kristoffer Bruvik

- IT3105-prosjektet har nøkkelordene «Django, AWS, SQL, Scrum, Git» kopiert fra TDT4290-prosjektet (stemmer ikke med innholdet, som er AI-spill). Beholdt, må rettes.
- Tutle- og IT3105-prosjektene har samme periode (03.2020 – 06.2020).
- TDT4290 og IT3105 er skrevet i førsteperson («Jeg», «vi») mens resten er tredjeperson. Beholdt. TDT4290-teksten mangler punktum etter «med kunde».
- Studentprosjektene (Masteroppgave, TDT4290, IT3105, Tutle) har Kunde: NTNU (logo fra originalen). Kunde for TDT4290 var egentlig en ekstern kunde som ikke er navngitt.
- Java sto to ganger i «Språk og rammeverk», og er fjernet i den andre. Django står både i Språk og rammeverk og i Plattform (ulike grupper, beholdt).
- Kurs-listen har tomme stedsfelt. «Sikkerhetsklarert av NSM» (2021) er ikke et kurs, men står i Kurs fordi originalen hadde den der. Bør flyttes til Om-teksten eller Utmerkelser.
- Epic React-kursene er sortert alfabetisk (original var omvendt alfabetisk, alle 2023).
- Erfaring står som «3 år», men Equinor-prosjektet begynte 05.2023 og KodeWorks 04.2023. Sommerjobber gir mer. Konsulenten bør bekrefte.
- Uninett-rolleoverskriften er «Utvikler», mens Arbeidserfaring sier «Sommerjobb». Samme for Thales.

## Filip Henrik Larsen

- Foto er hentet fra originalen (PNG med gjennomsiktig bakgrunn, lagt på hvit bakgrunn og lagret som JPEG; uten dette ble bakgrunnen svart i PDF-en). Ingen kundelogoer i originalen, bare kundenavn i fet skrift («PISCADA», «Optoscale»). «Piscada» er skrevet med vanlig stor forbokstav, slik det står i Arbeidserfaring.
- Originalen har feltet «Prosjekt» tomt for Piscada. Prosjektet står derfor uten `Prosjekt`. Bioscope er prosjektnavn for Optoscale.
- Kurs: originalen har to årstall (2022, 2021) og tre kurstitler i samme celle uten kobling. Koblet etter rekkefølge: 2022 for Practical AI …, 2021 for Leadership …, og Docker and Kubernetes uten år. Filip bør rette årstallene.
- Skrivefeil beholdt: «stereobiler» (stereobilder), «forøvrig», «… Google Cloud; Dette var …» med stor D, «oppdretsanlegg».
- Tomme rader og tomme overskrifter i originalen er utelatt. «Master - Computational Physics» er beholdt slik originalen skriver det.

## Jan-Marius Vatle

- Bygg-advarsel: logoen til Sunlit Sea (`logo-sunlit-sea.png`) er bare 200 × 200 piksler og gir 149 dpi i PDF-en. Originalen har ikke bedre. Bør byttes mot SVG eller større PNG.
- Nøkkelord i Echo3D-prosjektet har «Scrum» to ganger. Beholdt som i originalen.
- Prosjektet hos Brattvaag Electro AS (06.2009 – 04.2016) står som ett prosjekt, mens Arbeidserfaring har tre rader hos samme arbeidsgiver. Periodene stemmer ikke helt (Arbeidserfaring-raden «Deltidsansatt» starter 06.2008). Ikke endret.
- Skrivefeil beholdt: «Elekrtiker» (Arbeidserfaring), «Kodeworks» i prosjektteksten, «teknologien» (SpareBank 1), «IFE’s».
- Prosjektet Brattvaag Electro AS har rollen «Elektriker» og lange nøkkelord (14 stk.) som ikke er teknologier.
- Prosjektet SpareBank 1 er et sommerprosjekt (praktikant); «Prosjekt» er den lange tittelen fra originalen.
- Valg: «Publiseringer» er lagt i «Foredrag og publikasjoner». Kolonnene «Språk og rammeverk» er lest kolonne for kolonne (venstre, så høyre).
- Valg: «Plattform, tech & verktøy» er skrevet «Plattform, tech og verktøy» som i forbildet.

## Joachim Spange

- Utkastrest i originalen: punktet «Mer?» under Ansvarsoppgaver i Blue Insight. Beholdt, må fjernes eller fylles ut av konsulenten.
- Kunde for Blue Insight er ikke oppgitt i originalen. Satt Kunde: Kongsberg Discovery (fra Om-teksten og Kongsberg-logoen). Konsulenten bør bekrefte.
- Eldste prosjekt har kunde «Kongsberg Seatex» (nå Kongsberg Discovery) med samme Kongsberg-logo, delt fil logo-kongsberg.png.
- Rollene «Datakryptering» (Ocean Access) er egentlig en oppgave, ikke en rolle. Brukt som overskrift fordi originalen ikke har rolle.
- Perioden «03.2024 - 03.2024» ble skrevet som «03.2024».
- Bioscope-beskrivelsen er én lang tekst med kolon-introduserte punkter. Gjort om til punktlister. Setningen «I tillegg til alt dette var også Joachim de ansattes tillitsvalgte…» hørte til siste punkt i originalen og står nå som eget avsnitt. Den siste punktlista (Programvareutvikler, Drift, Hardware osv.) sto som en egen rad uten tittel i originalen og står nå som punktliste før Nøkkelord.
- Lenken til masteroppgaven (nva.sikt.no/registration/0198cc55c8c7-a1ef35a7-15ec-4b54-8e9c-aaad92c08644) mistet formatet fordi formatet ikke støtter lenker i listeradene. Teksten står uten lenke; lenken må legges inn på annen måte om den skal beholdes.
- «Masters's thesis» (feil apostrof i originalen) er beholdt.
- Studentassistent og TEKNA-kurs er plassert under Verv og engasjement og Foredrag og publikasjoner (originalens «Artikler, foredrag og verv»). Valget er skjønn.
- Kurs-raden (Docker Mastery) har tomt stedsfelt i originalen.
- «I²C»/«I2C» skrives ulikt i kompetanse og nøkkelord. «C ++» står med mellomrom i nøkkelord.
- Skrivefeil beholdt: «samme opp» (sette opp), «Mest Python», «kolleger har», «gjøv fatt».

## John Hagen

- Originalens overskrifter hadde formen «Kunde – Rolle». Delt opp i `Kunde` og rolle. For reMarkable (Store), TechnipFMC (Vision) og Equinor (Well Design) er originalens prosjektnavn beholdt som `Prosjekt`. KLP og Sunlit Sea hadde prosjektnavn lik kunden og er derfor utelatt. For KodeWorks står prosjektnavnet «Hako, Sentry, Fjordgata 30 Minilager».
- Nøkkelordene for KodeWorks-prosjektet (2015 – 2017) er kopiert fra Equinor-prosjektet (TypeScript, Angular, React, C#, .NET Core, Azure, RxJS) med Ember, Scala, Akka lagt til. Er sannsynligvis feil. Beholdt, John bør rette.
- TechnipFMC har bare nøkkelordet «Javascript». Sunlit Sea har «React, Redux, 3D».
- Utdanning sto som «2011-2016 | Master i Datateknikk, NTNU – 2016» med tom tredje kolonne. Skrevet som `2011 – 2016 | Master i Datateknikk | NTNU`.
- Prosjektet for KodeWorks har ingen logo (utelatt etter regelen). Originalen har ingen Arbeidserfaring eller Sertifiseringer.

## Lars Ødegaard

- Tre prosjekter har prosjektnavnet «Gradert» (Thales ×2, Kongsberg Defence & Aerospace). Kundene er hentet fra tekst og logo (Thales Norway → Thales).
- Rolleoverskriften «Senior konsulent» / «Senior Konsulent» har ulik stor bokstav i originalen. Beholdt.
- Nøkkelord for KDA hadde punktum på slutten («SDL.»), fjernet.
- Skrivefeil beholdt: «Som en del av software-teamet har jobbet han», «utviklingsprosjekt med som tester», «med med ansvaret», «GBD» (sannsynligvis GDB), «Cmake»/«CMake».
- «Appear TV»/«AppearTV» skrives ulikt i teksten. Kunde satt til «Appear TV».
- Appear TV-prosjektene overlapper i tid: Coders (08.2014 – 01.2019) omfatter Transcoder og HLS Server. Beholdt som i originalen.
- «CMS-system i PHP» (2011–2014, frivillig webutvikling ved siden av studiene) er lagt under Verv og engasjement uten sted. Masteroppgaven ligger under Foredrag og publikasjoner med NTNU som sted. Begge er skjønnsvalg.
- «Lars har sikkerhetsklarering Hemmelig» står som siste avsnitt i Om-teksten (ikke eget felt).
- Foto er et helfigursportrett (1335 × 2000). Bygget beskjærer automatisk. Kan trenge Fotofokus.

## Lasse Holanger

- Lege-CV uten prosjekter. Stillingene står under «Arbeidserfaring» med kulepunktene fra originalen som beskrivelse (ikke som prosjekter, siden «Kunde» er feil etikett for en arbeidsgiver). Ingen logoer.
- Telefon manglet landkode i originalen (405 45 500). Skrevet som +47 405 45 500. E-posten er en privat Gmail-adresse (holanger@gmail.com). Bør bekreftes før CV-en sendes.
- «Erfaring» (antall år) mangler som felt, selv om teksten sier «over 15 år». Ikke lagt til. «Språk» er avledet fra «Flytende norsk og engelsk» (norsk, engelsk). Bosted «Trondheim» og den gjentatte «Kontaktinformasjon» nederst er utelatt, fordi malen ikke har felt for dem.
- Originalens «Profil» er skrevet i første person («Med over 15 års erfaring … har jeg …»). Beholdt som den står. Malen forutsetter tredje person, så teksten bør skrives om av Lasse.
- «Kjernekompetanse» er lagt under «Teknisk kompetanse» (malen godtar ikke annen kompetanseseksjon). «Språk og ferdigheter» og «Teknologisk interesse og hobbyer» er lagt inn som egne grupper der, fordi de ikke har noen annen plass.
- «Lege i spesialisering, St. Olavs Hospital» har to perioder i originalen: «2008 (Hjerte) & 2016–2017 (Hud)». Periodeformatet godtar bare én, så den står som `2016 – 2017 (Hud; 2008: Hjerte)`. Bør vurderes delt i to rader.
- «Annet & Engasjement» er lagt under «Verv og engasjement». «Tidligere profesjonell fotballspiller» og «Kursleder» (uten periode) står som rader uten periode.
- «1 år fotball i England (1998–1999)» sto under Utdanning i originalen. Beholdt der som rad uten sted.
- Utdanningsrader er omformet til `periode | grad | sted`: for «Trondheim Katedralskole (IB-linje)» og «Adolf Øien videregående, Allmennfag» står linja/faget som grad og skolen som sted.
- Ingen foto i originalen.

## Ørjan Bostad Vesterlid

- Fotoet er i liggende format (800 × 533) med personen til venstre. Lagt til `Fotofokus: 0.32, 0.3`. Bør sjekkes.
- Bygg-advarsel: logoen til Lilbit er 173 × 65 piksler (157 dpi ved 26 mm). Bør byttes.
- Prosjektet «3T Treningssenter iOS app» (01.2021 – 05.2021) har en kopiert beskrivelse fra Elkompis/SkandiaEnergi (beskriver ElKompis, SkandiaEnergi og Eggs Design) og nøkkelord for iOS. Beholdt som i originalen. Logoen i originalen er WTW (ikke 3T), så den er utelatt. Kunde er utledet fra tittelen. Beskrivelsen må skrives for riktig prosjekt.
- Prosjektet «Hverdagshelt» (01.2019) har nøkkelord fra et helt annet prosjekt («FoU, Maskinvare, RK3188, ARM, Android, Programvare, Produksjon, Prosjektledelse, Entreprenørskap»). Beholdt, men må rettes. Logoen er NTNU (skolefag TDAT2003); kunde satt til NTNU.
- Rekkefølge endret: Hverdagshelt (01.2019) står nå foran Mplify (06.2018); originalen hadde dem motsatt.
- Originalen har en tom «Fullstack utvikler»-blokk (ingen prosjekt, periode, beskrivelse eller nøkkelord). Utelatt.
- Prosjektet Pexip har et tomt kulepunkt i originalen; utelatt.
- Prosjektet 3T har to avsnitt som tydelig hører til siste kulepunkt («hvor han:»). Gjort om til underpunkter.
- Prosjektet Tail it slutter med et løst avsnitt «.»; utelatt.
- Kunde utledet fra tittel eller tekst der originalen ikke har kunde: Lilbit, Nomono, SkandiaEnergi, 3T Treningssenter, Tail it, SALT, EnerSky/Equinor (var oppgitt). «Prosjekt» har originalens tittel (f.eks. «Pilot- app for Nomono», «Elkompis app for SkandiaEnergi»).
- Rollen i SALT-prosjektet er «Back-end utvikler og kravdokument-ansvarlig, SALT» (inkluderer kundenavn). Beholdt.
- Skrivefeil beholdt: «Pilot- app», «kontrolllapplikasjon», «uten å krever», «bedriftsutviklig» (TIHLDE).
- Valg: «Annen verv og erfaring» (TIHLDE-Drift, 08.2017) lagt i «Verv og engasjement». Originalens lange fete tittel er delt i navn («TIHLDE-Drift») og sted («Linjeforeningen for …»). Beskrivelsen er underpunkt.
- Valg: Utdanning har en beskrivelse (Dataingeniør); lagt som underpunkt.
- Språk skrevet «Norsk og engelsk» i originalen; endret til «norsk, engelsk».
- «Test-Driven-Development» var delt over to linjer i originalen; satt sammen.

## Pål Nødseth

- Originalen er konvertert uten endringer i språk. Prosjektnavn der kundenavnet sto først er forkortet ved å flytte kunden til Kunde-feltet: «Equinor Echo 3D» → Echo 3D, «Cisco Webex Home og Cisco Photo Frame» → Webex Home og Cisco Photo Frame, «Scanreach ConnectPOB» → ConnectPOB, «Grønt Punkt gjenvinningskalkulator» → Gjenvinningskalkulator, «Piscada PMP / OAP» → PMP / OAP. GKCloud.no beholdt.
- «Teknologier:» sto tomt til slutt i Echo 3D-beskrivelsen og er fjernet. I Cisco-prosjektet sto «Teknologier: …» på samme linje som siste punkt. Skilt ut som eget avsnitt.
- Beskrivelsene brukte «- » som tekst. Gjort om til punktlister. I Grønt Punkt var to punkter skrevet på samme linje, og er delt i to.
- Om-teksten nevner «seniorutvikler hos Equinor og Kongsberg», men det finnes ikke noe Kongsberg-prosjekt i CV-en.
- Piscada-beskrivelsen (første avsnitt) er kopiert identisk i GKCloud.no og PMP / OAP. Beholdt.
- Skrivefeil beholdt: «Socket.iot», «Gul» (nøkkelord i PMP / OAP, uklart), «forstyring», «f.eks», «dybder..», «testbed/lab-miljø», «Devops».
- Tatimer har ingen prosjektnavn i originalen (bare tittelen «Tatimer.no» i beskrivelsen). Kunde: Tatimer, uten Prosjekt. Logoen (ugle, 309 × 309) er hentet fra originalen og antas å være Tatimer, må bekreftes.
- Nortek-kunde er hentet fra beskrivelsen. Rollen på Nortek- og Grønt Punkt-prosjektene er «Frontend utvikler»/«Lead Frontend utvikler» uten bindestrek, som originalen.
- «Prosjektmetodikk: Scrum, Kanban» i kompetanse har mistet ledeteksten «Prosjektmetodikk:», fordi elementene står som liste.
- Utdanning er sortert nyest først (originalen var 2008, 2015, 2006).
- «Kurs / Sertifisering»-tabellen er delt. Bare AZ-900 står som Sertifisering (utsteder ikke oppgitt i originalen; satt blank). Kursene fra LinkedIn og «Full stack Javascript (Team Treehouse)» står under Kurs, selv om originalen kalte det siste «Sertifisering». Tabellen hadde en tom rad til slutt, fjernet.
- Eggs Design, Trondheim Private Musikkskole og Tatimer står i Arbeidserfaring, men bare Tatimer og Piscada har prosjektrad.
- Erfaring-feltet «9 år» er beholdt, selv om første prosjekt starter 2015.

## Simen Moen Storvik

- Bygget advarer: logoen til Sunlit Sea har lav oppløsning (200 × 200 px, 149 dpi). Inatur-logoen (255 × 85 px) er også liten, men gir ingen advarsel. Bør byttes mot bedre filer.
- Ingen kunde er oppgitt for prosjektet «Nettapp som erstatter fysiske nøkler» (originalen har bare KodeWorks-logo). Satt Kunde: KodeWorks, så logo utelates.
- Prosjektet 2018–2019 har NTNU-logo og nevner SAP Norge AS i teksten. Satt Kunde: NTNU, og SAP Norge AS står i beskrivelsen og nøkkelordene. Sunlit Sea er hentet fra teksten og logoen som kunde for FPV-prosjektet.
- Seksjonen «Artikler, foredrag og verv» inneholdt bare Professional Scrum Master I (2022) med to beskrivelsesavsnitt. Flyttet til Sertifiseringer (utsteder satt til Scrum.org etter PSM-merket i originalen), og beskrivelsen ligger som underpunkter. PSM-merket (bilde) er ikke tatt med.
- Skrivefeil beholdt: «videreutviklig», «driftoptimalisering», «Github CI/CD». Perioden «2020 - 2022» i Om-teksten er beholdt uendret med bindestrek.

## Sindre Stephansen

- Originalen har ingen «Kunde»-felt: kunden går bare fram av logoen. Kunden er utledet fra logoen (EnerSky, Kongsberg, Skandia Energi, Sunlit Sea, NTNU, Lilbit, Eyasys, Vaskehjelp, KodeWorks) og for Gradert fra beskrivelsen («Thales Norway»). Logoen for «Ship Noise Monitoring» viser bare «Kongsberg», uten hvilken Kongsberg-enhet. Bør presiseres.
- Tre prosjekter har ingen kunde og ingen logo: Hobbyprosjekt (Operativsystem), Studentprosjekt (Nettside for MAKE NTNU) og Personlig prosjekt (Nettsiden for Bispehaugen Ungdomskorps). De står uten `Kunde`. Rollene «Hobbyprosjekt», «Studentprosjekt» og «Personlig prosjekt» er originalens overskrifter, ikke egentlige roller.
- For EnerSky var «Prosjekt» lik kunden i originalen, så `Prosjekt` er utelatt.
- «Sikkerhetsklarering: Hemmelig / NATO Secret» hadde ingen plass i malen. Lagt som egen kompetansegruppe.
- Sorteringen: hobbyprosjektet (2025 – nå) ligger rett etter Ship Noise Monitoring (05.2025). Originalen hadde det nesten sist.
- Bygget advarer om lav oppløsning på `logo-ntnu.png` (126 dpi) og `logo-sunlit-sea.png` (149 dpi). Sunlit Sea-logoen er et 200 x 200 piksler stort bilde med gul stripe. Bedre kilder bør hentes (John Hagens CV har en bredere Sunlit Sea-logo).
- Innholdsfeil beholdt: «Hovedsaklig», «IOS», «bla.», «Nøkkelord: C++, Arduino, Mbed OS.» (punktum til slutt), Lilbit-avsnittet uten punktum, «Kodeworks» med liten w i brødtekst. «Sindre utvikler/jobber med» i presens for avsluttede prosjekter (Ship Noise, 01.2026). «Erfaring: 6 år» stemmer ikke med Arbeidserfaring fra 05.2017.
- «Foredrag og publikasjoner»: 2018-oppføringen har bare en URL (medium.com) som underpunkt. Kursene i 2022 og 2023 er holdt for KodeWorks, men «sted» er ikke fylt ut fordi det står i beskrivelsen.
- Foto er et helfigurbilde som bygget beskjærer automatisk. Ansiktet kom ut riktig.
- «03.2019- 06.2020» i originalen er rettet til «03.2019 – 06.2020».

## Thomas Ax Gulbrandsrød

- Fotoet er en PNG (812 × 774, 1 MB) og heter derfor `foto.png`. Kan med fordel lagres som JPG.
- Logoen i Sunami-prosjektet (07.2016 – 07.2021) er EyaSys, ikke Sunami. Jeg har utelatt logoen i stedet for å bruke feil logo. Sunami har ingen egen logo i originalen. Kunde er satt til «Sunami» (arbeidsgiver er EyaSys). Bør avklares om kunden skal være EyaSys.
- KW-TV (internprosjekt) og SOCKS4 (internprosjekt) har KodeWorks-logo i originalen; kunde satt til KodeWorks og logo utelatt.
- Prosjektene «Cisco microsoft teams» og «Infrastruktur og HIL testing» har ikke en rolle som overskrift i originalen (det er tema-/prosjekttittel). Beholdt som overskrift. Bør byttes mot ekte rolle.
- Kunde for «Realtime OS migrering» er ikke oppgitt; utledet fra teksten og logoen: Abbott Rapid Diagnostics (originalteksten staver «Abbot»). Beholdt skrivefeilen i teksten.
- Perioder med enkeltsifret måned er normalisert: «1.2026 – nå» til «01.2026 – nå», «3.2025 – 1.2026» til «03.2025 – 01.2026».
- «Hobbyprosjekter» er i originalen et eget prosjektkort uten periode og kunde. Det passer ikke i Erfaring (kontrollskriptet krever periode). Lagt som rad uten periode i «Verv og engasjement», med de fire punktene og nøkkelordene som underpunkter. Bør vurderes.
- «Artikler, foredrag og verv» hadde én rad (Frivillig i Ten Sing, 2013 – 2017), lagt i «Verv og engasjement».
- Rader i Arbeidserfaring har «40% deltid» i rollen; beholdt slik (ikke flyttet til periode).
- Skrivefeil/uheldig språk beholdt: «Egetinitiativ», «Cisco's», «autogenerering av github workflows», «Enable HIL for utviklere», «Abbot».
- Kompetanselister: «Python, SQL, Flask, …» lest kolonne for kolonne.
- «Om Thomas» sier «påbegynt grad i elektronikk» mens Utdanning har to fullførte bachelorer; ikke endret.

## Vegard Stengrundet

- Bygg-advarsel: logoen til Sunlit Sea er 200 × 200 piksler (149 dpi). Bør byttes.
- Prosjektet «Visualisering av Fjordbyen og Sunlit Sea / Visualisering av skipssimulator / Administrere sensordata fra balansebrett / Likviditetskontrollsystem» (11.2018 – 11.2020) samler fire delprosjekter i ett. Kunde er satt til KodeWorks (logoen i originalen er KodeWorks) og logo er utelatt. Delprosjektene er mellomtitler. Bør vurderes delt i fire prosjekter med egne perioder og kunder (Sunlit Sea er kunde for Fjordbyen).
- HoloLens-prosjektet har KodeWorks som logo i originalen, så kunde er satt til KodeWorks og logo utelatt.
- Prosjektet «Sunlit Sea, Visualisering» er satt til kunde Sunlit Sea og prosjekt «Visualisering» (originalen skiller med komma). Samme for «Echo, Digital Tvilling» (kunde Equinor ut fra logo og tekst) og «K-Sim, Maritim Simulering» (kunde Kongsberg Digital).
- Prosjektet «Proof of concept» hos WTW har et lite beskrivende prosjektnavn. Beholdt.
- Rekkefølge endret: originalen har Echo (02.2019 – nå) først. Prosjektene er nå sortert på startdato, så Echo står etter Sunlit Sea-visualiseringen (04.2020) og før Fjordbyen/HoloLens.
- Valg: «Kurs og Sertifiseringer» delt. Microsoft Certified Professional (C#) og Oracle Certified Associate (Java SE 8) ligger under Sertifiseringer. De fem øvrige (nettkurs) ligger under Kurs. Utsteder mangler i originalen for alle.
- «MySQL» stod to ganger i «Plattform, tech og verktøy»; duplikatet er fjernet (regel for kompetansegrupper).
- Skrivefeil beholdt: «Simulatorien», «Vegard implementere også», «lagd», «bruker i flere norske byer» (mangler «brukes»), «api’er», «Kodeworks».
- Lenker i teksten (Equinor-artikkel, YouTube) står som ren tekst.
- «Om Vegard» sier «6 års erfaring», mens første ansettelse er 03.2018 (om lag 8 år i dag). Bør oppdateres.
