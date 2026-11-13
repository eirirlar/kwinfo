# Presentasjonsmal for KodeWorks

Denne veiledningen er for deg som skal lage en presentasjon i KodeWorks' profil. Du skriver presentasjonen som vanlig tekst i Markdown og bygger den til en PDF. Malen følger profilmanualen: hvit innholdsflate, dypgrønn åpning og seksjonsskille, grønn sitatflate, grå flate for nøkkeltall, svart avslutning og profilfonten NON Natural Grotesk. Formatet er 16:9.

## Filene

| Fil | Hva den er |
|---|---|
| `presentasjonsmal.md` og `presentasjonsmal.pdf` | Malen. En presentasjon som forklarer seg selv: ett lysbilde per lysbildetype, med en kort instruks på lysbildet og Markdown-syntaksen i talernotatene. Kopier filen og fyll ut. |
| `eksempel.md` og `eksempel.pdf` | Et ferdig eksempel på 14 lysbilder som bruker alle lysbildetypene. Bruk det som forbilde for tone og oppbygging. |
| `images/` | KodeWorks' egne foto som brukes i malen og eksempelet. |

PDF- og PNG-filene er ikke i git. De bygges fra Markdown-filene med `uv run python src/build_all.py` fra prosjektroten (se «Bygge alt» i prosjektets README).

## Bygge PDF

Fra prosjektroten:

```
uv run src/build_presentation.py min-presentasjon.md
```

PDF-en havner ved siden av Markdown-filen, med samme navn (`min-presentasjon.pdf`). Bruk `-o` for et annet filnavn.

Du trenger pandoc, LuaLaTeX (TeX Live) og uv. Profilfonten og grafikken hentes av byggescriptet. Et bygg tar vanligvis 5–40 sekunder.

Byggescriptet sier fra hvis noe er galt: bilder som ikke finnes (med linjenummer), og lysbilder med for mye tekst (med lysbildets tittel). Les varslene før du sender PDF-en.

## Slik skriver du

Vanlig pandoc-Markdown. Et nytt lysbilde starter med en overskrift på nivå 2 (`##`). Klassen i krøllparentes bak overskriften velger lysbildetype. Uten klasse får du et vanlig tekstlysbilde.

| Lysbildetype | Slik skriver du den | Grense |
|---|---|---|
| Åpning | Lages automatisk fra YAML-blokken øverst: `title`, `subtitle`, `author`, `date`. | Én tittel, valgfri undertittel |
| Seksjonsskille | `# Tittel {number="01"}`, med en valgfri setning under. Uten `number` nummereres skillene automatisk. | Én kort setning |
| Tekst | `## Tittel`, valgfritt avsnitt og punktliste. Med `{.lead}` blir første avsnitt en ingress. | Høyst fire punkter |
| Tekst og bilde | `## Tittel {.image}`, tekst, og `![](images/foto_team1.jpg)`. Bildet fyller høyre del av lysbildet. | Ett bilde, høyst tre punkter |
| To kolonner | En `columns`-blokk med to `column`-blokker (se under). | Høyst tre punkter per kolonne |
| Sammenligning | Som to kolonner, men hver kolonne starter med `### Overskrift`. | Høyst tre punkter per kolonne |
| Sitat | `## {.quote}`, sitatet som blokksitat (`>`), og en linje `Kilde: …`. | Én til to setninger |
| Nøkkeltall | `## Tittel {.figures}`, hvert tall som definisjonsliste (se under). Sett enheten i forklaringen, ikke i tallet. | To til fire tall |
| Kundelogoer | `## Tittel {.logos}`, kundenavn som punktliste, eller logoer som bilder i PDF-format. | Høyst åtte |
| Avslutning | `## Takk {.closing}`. Kontaktpersonene hentes fra `contacts` i YAML. Uten `contacts` vises KodeWorks' felles kontaktinformasjon. | Én til to kontakter |

Eksempler:

````
## To kolonner

:::: columns
::: column
Venstre kolonne
:::
::: column
Høyre kolonne
:::
::::

## KodeWorks i *tall* {.figures}

27
: utviklere

39,7
: MNOK i omsetning, 2023

## Takk {.closing}

::: notes
Talernotater skrives slik.
:::
````

Åpningen og avslutningen trenger ikke noe innhold utover YAML-blokken:

```
---
title: "Dine *ideer*, våre utviklere"
subtitle: "Hva presentasjonen handler om"
author: "Navn Navnesen"
date: "12. mars 2027"
contacts:
  - name: "Navn Navnesen"
    role: "Kontaktperson"
    email: "navn@kodeworks.no"
    phone: "+47 000 00 000"
---
```

Felt du utelater (for eksempel `subtitle`, kilden i et sitat eller telefonnummeret) utgår uten at siden får hull. Et felt over flere linjer, som en adresse, skrives med `|` og en omvendt skråstrek (`\`) på slutten av hver linje som ikke er den siste.

## Regler

**Fargeutheving i titler.** Sett stjerner rundt ett eller to ord i tittelen: `Vi muliggjør *ideer*`. Ordet får farge, ikke fet skrift: mørkegrønn på lys flate og lysegrønn på dypgrønn. Aldri uthev mer enn to ord, og aldri hele tittelen. I brødtekst gir `**dobbel stjerne**` skrift i Medium-vekt. Fonten har ingen ekte kursiv, så enkel stjerne i brødtekst bør unngås.

**Skrift.** Titler og store tall står i Light, brødtekst i Regular. Du velger ikke skrift selv, og fet skrift brukes ikke.

**Mengde tekst.** Inntil fire punkter per lysbilde, og korte punkter. Brødtekst er 20 pt. Får ikke teksten plass, setter malen den først i 18 pt. Er det fortsatt for mye, krymper malen teksten slik at den holder seg innenfor flaten, og byggescriptet varsler «For mye tekst på lysbildet …». Da skal du dele lysbildet i to, ikke sende det slik.

**Seismografen og navnetrekket.** Seismografen (strekgrafikken på åpningen og seksjonsskillene) og navnetrekket «KodeWorks» nederst på hvert innholdslysbilde ligger i temaet. Du skal ikke legge dem inn selv.

**Bilder og samtykke.** Bruk KodeWorks' egne foto av ansatte og lokaler, ikke stockfoto. Legg bildene i `images/` ved siden av Markdown-filen. Bildet bør være minst 2000 piksler bredt, ellers blir det grovt i PDF-en. Bruk bare bilder der de som er avbildet har samtykket til at bildet brukes til formålet.

**Kunder.** Nevn bare kunder vi har lov til å vise. Logoer legges inn som PDF (vektor), ikke som skjermbilde. Uten logofiler settes kundenavnene som tekst i fliser.

**Tall og sitater.** Bruk bare tall du kan dokumentere, og oppgi årstall (for eksempel «omsetning i 2023»). Et sitat skal være ekte og ha kilde.

**Tone.** Korte, direkte titler og konkret tekst. Ikke superlativer som «verdensledende» eller «best i klassen».

## Talernotater

Skriv notatene i en `::: notes`-blokk rett under lysbildet de hører til. De vises ikke i den vanlige PDF-en. Bygg med `--notes` for å få en egen versjon med notatsider (`min-presentasjon-notater.pdf`) til eget bruk:

```
uv run src/build_presentation.py min-presentasjon.md --notes
```

Send ikke notatversjonen til andre.

## Før du sender

1. Byggescriptet har ikke gitt varsler.
2. Titlene har høyst ett eller to uthevede ord.
3. Bla gjennom hele PDF-en: ingen tekst som er krympet, ingen enslige ord på egen linje.
4. Kontroller tall, årstall, kundenavn og sitater mot kilden.
5. Sjekk kontaktinformasjonen på siste lysbilde.
6. Sjekk at bildene er KodeWorks' egne, og at samtykke finnes.
7. Send den vanlige PDF-en, ikke notatversjonen.

## Om fonten

NON Natural Grotesk er en lisensiert font. Byggescriptet pakker den ut til en midlertidig mappe under bygget, bygger den inn i PDF-en og sletter den igjen, slik at dokumentet ser riktig ut for mottakeren. Fontfilene skal ikke kopieres, videresendes eller installeres. Flagget `--keep-build` beholder byggemappen (med fontfilene) for feilsøking; slett den etterpå.
