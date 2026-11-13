# Dokumentmal for KodeWorks

Denne veiledningen er for deg som skal lage et A4-dokument i KodeWorks' profil. Du skriver teksten som vanlig Markdown og bygger den til en PDF. Malen har to varianter: **brev** og **dokument**. Brevet brukes til salgsbrev og henvendelser til kunder. Dokumentvarianten brukes til utlysning av konsulentoppdrag, notater og tilbud. Begge bruker profilfonten NON Natural Grotesk, KodeWorks' navnetrekk og en bunntekst med selskapsopplysninger.

## Filene

| Fil | Hva den er |
|---|---|
| `brevmal.md` | Malen for brev. Hvert felt har en forklarende plassholder. Kopier filen og fyll ut. |
| `dokumentmal.md` | Malen for dokument. Hvert element står med en kort instruks. Kopier filen og fyll ut. |
| `eksempel-brev.md` | Et ferdig salgsbrev på to sider. Bruk det som forbilde for tone og oppbygging. |
| `eksempel-utlysning.md` | En utlysning av et konsulentoppdrag på to sider. |

PDF- og PNG-filene er ikke i git. De bygges fra Markdown-filene med `uv run python src/build_all.py` fra prosjektroten (se «Bygge alt» i prosjektets README).

## Bygge PDF

Fra prosjektroten:

```
uv run src/build_document.py mitt-dokument.md
```

PDF-en havner ved siden av Markdown-filen, med samme navn (`mitt-dokument.pdf`). Bruk `-o` for et annet filnavn. Du trenger pandoc, LuaLaTeX (TeX Live) og uv. Et bygg tar vanligvis under et halvt minutt. Byggescriptet sier fra med vanlig norsk tekst hvis et felt mangler, hvis en linje går utenfor margen, hvis et avsnitt ender med ett ord alene på siste linje, eller hvis et tegn ikke finnes i fonten (for eksempel «✓»; tegnet blir da utelatt). Les varslene før du sender PDF-en. I brev holdes siste avsnitt sammen med hilsenen og signaturen, så signaturen aldri står alene øverst på en side.

## YAML-feltene

Alle felt er valgfrie. De står øverst i filen, mellom to linjer med `---`.

| Felt | Gjelder | Hva det gjør |
|---|---|---|
| `variant` | begge | `letter` (brev) eller `document` (dokument). Uten feltet bygges et dokument. De eldre verdiene `brev` og `dokument` virker fortsatt, men gir en advarsel. |
| `title` | begge | I brev: emnelinjen. I dokument: tittelen. Uten feltet brukes første overskrift på nivå én. |
| `subtitle` | dokument | Undertittel under tittelen. |
| `company` | begge | Avsenderselskapet i bunnteksten (se under). |
| `date` | begge | Dato på formen `2026-11-11`, som settes som «11. november 2026». Brev uten dato får dagens dato. Dokument uten dato får ingen dato. |
| `recipient` | brev | Mottakerblokken, én linje per rad. |
| `their-ref` | brev | «Deres ref.» |
| `our-ref` | brev | «Vår ref.» |
| `closing` | brev | Avslutningshilsen. Standard er «Vennlig hilsen». |
| `sender` | brev | Signaturen: `name`, `title`, `email`, `phone`. Én person, eller en liste. |
| `contact` | dokument | Kontaktblokken sist i dokumentet, med samme felt som `sender`. Én person, eller en liste. |

Et felt over flere linjer, som mottakeren i et brev, skrives med `|` og én linje per rad.

## Slik skriver du

Vanlig pandoc-Markdown. Malen tar seg av skrift, farger og plassering.

| Element | Slik skriver du det |
|---|---|
| Tittel | Feltet `title` i YAML. Uten det blir første `#`-overskrift tittelen. Står det et kolon i tittelen, for eksempel «Konsulentoppdrag: Android-utvikler», blir delen før kolonet en liten etikett over tittelen. Har filen både `title` og en `#`-overskrift, vinner `title`, og overskriften blir en seksjon. |
| Seksjon | `## Overskrift` |
| Underseksjon | `### Overskrift` |
| Faktaboks | Linjer på formen `**Etikett:** verdi` rett etter tittelen, hver linje unntatt den siste avsluttet med `\`. De blir automatisk en boks, men bare når alle linjene har den formen og etikettene er korte (inntil ca. 25 tegn, uten punktum). Ellers blir avsnittet vanlig tekst. Faktaboks andre steder i dokumentet: `::: {.facts}` rundt linjene. |
| To kolonner | `:::: {.columns}` rundt to `::: {.column}`-blokker. Passer for «må ha» og «fint å ha». |
| Kontaktblokk | Feltet `contact` i YAML, eller `::: {.contact}` rundt linjer med navnet først og tittelen på andre linje. Et siste avsnitt som begynner med et navn i fet skrift og inneholder en e-postadresse, blir også en kontaktblokk. |
| Sitat | `> Sitat` |
| Lister | `- punkt` eller `1. punkt`, med inntil to nivåer. |
| Tabell | Enkel pipe-tabell med `\|` mellom kolonnene. |
| Fet skrift | `**fet**` gir skrift i Medium-vekt. |
| Kursiv | `*kursiv*` gir skrå Regular. Bruk sparsomt. |

## Selskapet i bunnteksten

Bunnteksten viser avsenderselskapets navn og organisasjonsnummer, kontoradressene og kodeworks.no. Velg avsender med feltet `company`:

| Verdi | Org.nr. |
|---|---|
| `KodeWorks AS` | 820 478 452 |
| `KodeWorks Trondheim AS` | 920 478 492 |
| `KodeWorks Eiendom AS` | 920 478 506 |
| `KodeWorks Oslo AS` | 922 070 709 |

Dette er fire forskjellige selskaper. Velg det som faktisk er avsender av dokumentet. Uten `company` brukes KodeWorks AS.

## Slik skriver du godt

**Tone.** Konkret og saklig. Skriv hele setninger, og la dokumenterte fakta tale for seg. Unngå superlativer som «verdensledende» og «best i klassen». Vi er en partner som er med så lenge vi bidrar, og det skal merkes i språket: rolig, direkte og uten salgsprat.

**Lengde.** En utlysning bør holde seg på én til to sider. Et brev bør ikke bli lengre enn to sider. Har du mer å si, er det som regel et tegn på at du bør dele innholdet i to dokumenter.

**Brev.** Start med hvorfor du skriver og hva du ber om eller tilbyr, og henvis til tidligere kontakt med dato. Avslutt med hva som skjer videre og hvem som tar neste steg.

**Utlysning.** Faktaboksen øverst gir sted, oppstart, frist og varighet. Deretter følger oppdraget, oppgavene, «må ha» og «fint å ha», en kort presentasjon av KodeWorks og hvordan man tar kontakt. Skriv «må ha» bare om det som virkelig er et krav.

**Tall.** Bruk bare tall du kan dokumentere, og oppgi alltid årstall («omsetning i 2023»).

## Før du sender

1. Byggescriptet har ikke gitt varsler.
2. Fakta er kontrollert mot kilden: datoer, frister, adresser og navn.
3. Tall har årstall og kan dokumenteres.
4. Kundenavn, logoer og bilder er nevnt eller brukt bare der vi har lov til det og der samtykke finnes.
5. Selskapet i bunnteksten er riktig avsender.
6. Du har bladd gjennom hele PDF-en: ingen enslige ord på egen linje, ingen tomme sider og ingen overskrift nederst på siden.
7. Kontaktinformasjonen er riktig.
8. Du sender PDF-en. Send aldri Markdown-filen, og aldri fontfilene.

## Når malen ikke har det du trenger

Trenger du noe malen ikke har, for eksempel en ny type boks, en tabellstil eller en annen sidetype, skal du ikke lage en lokal løsning med ekstra LaTeX eller manuelle justeringer i det enkelte dokumentet. Slike løsninger blir borte neste gang malen oppdateres, og to dokumenter ender opp med to ulike uttrykk. Nye behov skal i stedet bli elementer i den felles malen, slik at alle får dem.

Slik ber du om det: Send en kort beskrivelse til den som forvalter malene i KodeWorks, med et eksempel på hva du ville skrevet i Markdown og hvordan du vil at resultatet skal se ut. Legg ved dokumentet du jobber med. Så lenge elementet ikke finnes, bygg dokumentet uten det og send PDF-en som vanlig.

## Om fonten

NON Natural Grotesk er en lisensiert font. Byggescriptet pakker den ut til en midlertidig mappe under bygget, bygger den inn i PDF-en og sletter den igjen, slik at dokumentet ser riktig ut for mottakeren. Fontfilene skal ikke kopieres, videresendes eller installeres.
