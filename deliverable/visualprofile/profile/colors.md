# KodeWorks fargepalett

Sju profilfarger og én teknisk farge. Grønn og grå er hovedfarger, svart og hvit gir ro, og mørkegrønn, dypgrønn og rosa er støttefarger med faste roller. Maskinlesbar utgave: `colors.json`.

| Farge | Rolle | HEX | RGB | CMYK | PMS |
|---|---|---|---|---|---|
| Grønn | Hovedfarge. Aksent og profilflate; symbol og seismograf på mørk flate. Aldri tekst på lys flate. | `#B6FF9E` | 182, 255, 158 | 31, 0, 40, 0 | 2267 C / 2267 U (neon) |
| Grå | Hovedfarge. Sekundærflate: kort, print, utvalgte nettseksjoner. | `#E8E7E6` | 232, 231, 230 | 8, 6, 7, 0 | 179-2 C / U ¹ |
| Svart | Tekst, logo, mørk flate (bunntekst). | `#000000` | 0, 0, 0 | 0, 0, 0, 100 \* | Black C \* |
| Hvit | Grunnflate og tekst på mørk flate. | `#FFFFFF` | 255, 255, 255 | 0, 0, 0, 0 | Papir |
| Mørkegrønn | Interaktiv farge: knapper, utheving av ord i titler. | `#35664C` | 53, 102, 76 | 80, 30, 70, 40 \* | ca. 7729 C \* |
| Dypgrønn | Mørk flate: skillesider, mørke seksjoner; hover på knapper. Ikke tekst. | `#254333` | 37, 67, 51 | 85, 45, 75, 65 \* | ca. 3435 C \* |
| Rosa | Støtteflate i liten dose, høyst én flate per side. Aldri tekst. | `#FAD5D5` | 250, 213, 213 | 0, 15, 10, 0 \* | ca. 706 C \* |
| Mørkegrå (teknisk) | Sekundærtekst. Ikke profilfarge. | `#666666` | 102, 102, 102 | 0, 0, 0, 60 \* | Cool Gray 10 C \* |

\* Forslag. Ikke verifisert; må kontrolleres av trykkeri før bruk i trykk.\
¹ PMS-navnet er hentet fra designmanualen fra 2021 og er ikke et standard Pantone-navn; må kontrolleres.

## Tekst og bakgrunn

Kravene følger WCAG 2.x: brødtekst minst 4,5:1, stor tekst (≥ 24 px, eller ≥ 18,7 px halvfet) minst 3:1. Tallene under er beregnet, ikke anslått.

- **Brødtekst tillatt:** svart på hvit, grå, grønn og rosa · hvit på mørkegrønn og dypgrønn · grønn og grå på mørkegrønn og dypgrønn · mørkegrønn på hvit, grå, grønn og rosa · dypgrønn på rosa · mørkegrå på hvit, grønn og grå (på grå bare fra 12 pt).
- **Bare stor tekst:** mørkegrå på rosa og på svart · svart på mørkegrønn.
- **Forbudt:** grønn på hvit, grå og rosa · grå på hvit · hvit på rosa · mørk farge på mørk farge (svart på dypgrønn, mørkegrønn på dypgrønn).

## Kontrastmatrise (beregnet etter WCAG 2.x)

Kontrast er symmetrisk: rad og kolonne kan byttes om.

| | Grønn #B6FF9E | Grå #E8E7E6 | Svart #000000 | Hvit #FFFFFF | Mørkegrønn #35664C | Dypgrønn #254333 | Rosa #FAD5D5 | Mørkegrå #666666 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Grønn** #B6FF9E | - | 1.05 | 17.79 | 1.18 | 5.64 | 9.22 | 1.14 | 4.86 |
| **Grå** #E8E7E6 | 1.05 | - | 17.00 | 1.23 | 5.39 | 8.81 | 1.09 | 4.65 |
| **Svart** #000000 | 17.79 | 17.00 | - | 21.00 | 3.16 | 1.93 | 15.54 | 3.66 |
| **Hvit** #FFFFFF | 1.18 | 1.23 | 21.00 | - | 6.65 | 10.88 | 1.35 | 5.74 |
| **Mørkegrønn** #35664C | 5.64 | 5.39 | 3.16 | 6.65 | - | 1.64 | 4.92 | 1.16 |
| **Dypgrønn** #254333 | 9.22 | 8.81 | 1.93 | 10.88 | 1.64 | - | 8.06 | 1.90 |
| **Rosa** #FAD5D5 | 1.14 | 1.09 | 15.54 | 1.35 | 4.92 | 8.06 | - | 4.25 |
| **Mørkegrå** #666666 | 4.86 | 4.65 | 3.66 | 5.74 | 1.16 | 1.90 | 4.25 | - |

