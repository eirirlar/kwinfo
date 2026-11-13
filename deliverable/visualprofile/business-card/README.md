# Visittkort – slik lager og bestiller du et nytt kort

KodeWorks-visittkortet har en grå forside med navnetrekket og kontaktinformasjonen din, og en grønn bakside med KW-symbolet. Alt som skiller ett kort fra et annet, står i fem linjer i en Markdown-fil.

## Filene i mappen

| Fil | Innhold |
|---|---|
| `visittkort-mal.md` / `.pdf` / `.png` | Malen med plassholdere (Navn Navnesen) |
| `visittkort-eksempel.md` / `.pdf` / `.png` | Eksempelkort for Eirik Larsen |
| `README.md` | Denne veiledningen |

PDF- og PNG-filene er ikke i git. De bygges fra Markdown-filene med `uv run python src/build_all.py` fra prosjektroten (se «Bygge alt» i prosjektets README).

PDF-en er trykkfila. PNG-en er en skjermversjon, for eksempel til e-post eller intranett.

## Lag et nytt kort

1. Kopier malen og gi kopien ditt navn, for eksempel `visittkort-kari-nordmann.md`.
2. Endre verdiene i hodet øverst i fila:

   ```yaml
   ---
   name: Kari Nordmann
   title: Seniorkonsulent
   phone: +47 912 34 567
   email: kari.nordmann@kodeworks.no
   web: kodeworks.no
   ---
   ```

   - `name` er påkrevd. Alle de andre feltene kan utelates, og da forsvinner linjen uten at resten av kortet flytter seg.
   - Skriv telefonnummeret med landskode og mellomrom: `+47 912 34 567`.
   - Skriv nettadressen uten `https://` og `www.`.

3. Bygg kortet fra prosjektroten:

   ```bash
   uv run src/build_business_card.py deliverable/visualprofile/business-card/visittkort-kari-nordmann.md
   ```

   Bygget tar noen sekunder. Det lager `visittkort-kari-nordmann.pdf` (trykk) og `visittkort-kari-nordmann.png` (skjerm) ved siden av Markdown-fila.

4. Se på PNG-en. Bygget kontrollerer også kortet selv og skriver `VARSEL:` hvis noe er galt, for eksempel at en lang tittel vokser opp mot navnetrekket eller at teksten havner for nær kuttkanten. Lange titler brytes over flere linjer. Hvis du får et varsel, kort ned teksten.

## Trykkfila

| Egenskap | Verdi |
|---|---|
| Ferdig format | 85 × 55 mm, liggende, tosidig (side 1 forside, side 2 bakside) |
| Utfallende kant | 3 mm på alle sider. Arket er 105 × 75 mm med skjæremerker utenfor den utfallende kanten. TrimBox og BleedBox er satt i PDF-en. |
| Sikker sone | All tekst står minst 5,5 mm innenfor kuttkanten. Kravet er 3 mm. |
| Font | NON Natural Grotesk Regular og Medium, innebygd i PDF-en. Lisensen tillater innbygging. |
| Grafikk | Bare vektor: navnetrekk, symbol og flater. Ingen rasterbilder. |
| Farger | Bare CMYK. Verdiene er hentet fra profilens fargepalett. |

| Farge | Brukes til | CMYK | PMS |
|---|---|---|---|
| Grå `#E8E7E6` | Forsidens flate | 8 / 6 / 7 / 0 | 179-2 C/U (fra 2021, må kontrolleres) |
| Grønn `#B6FF9E` | Baksidens flate | 31 / 0 / 40 / 0 | 2267 C / 2267 U (neon) |
| Svart `#000000` | Tekst, navnetrekk og symbol | 0 / 0 / 0 / 100 | Black C (forslag) |
| Registreringsfarge | Bare skjæremerkene | 100 / 100 / 100 / 100 | – |

Profilgrønnen er en neonfarge. Den kan ikke gjengis i CMYK, så i firefargetrykk blir baksiden mattere enn på skjerm. Skjermversjonen (PNG) bygges derfor separat med profilens RGB-farger. Vil du ha den riktige grønnfargen på trykk, be trykkeriet om å trykke baksidens flate i Pantone 2267 som spotfarge.

## Bestill kortet

Send trykk-PDF-en til trykkeriet med denne bestillingen:

- format 85 × 55 mm, tosidig, 3 mm utfallende kant (inkludert i fila);
- papir etter avtale, gjerne ubestrøket 350–400 g;
- farger: CMYK som i fila, eller baksiden i Pantone 2267 C/U som spotfarge for riktig grønn;
- be om korrektur før trykk, og kontroller at svart er ren svart (100 % K) og ikke en firefargesvart.

CMYK-verdiene for svart og PMS-navnet for grått er forslag som trykkeriet bør bekrefte før første opplag.

## QR-kode

Kortet har ingen QR-kode. Profilmanualen viser kortet uten, og navnetrekket og nettadressen dekker det samme behovet.

## Bygget

Bygget bruker pandoc og lualatex, som de andre KodeWorks-malene. Fonten pakkes ut fra den lisensierte font-fila i repoet til en midlertidig mappe og installeres aldri. Fontkontrollen stopper bygget hvis en font fra operativsystemet blir brukt. Kortet blir derfor likt på Windows, WSL2 og Linux.
