---
name: fetch-from-drive
description: Hent filer eller hele mapper fra Google Drive med src/fetch_from_drive.py, for eksempel originaler som skal inn i innboksen background/new/. Google-dokumenter eksporteres (docx, pdf, md, txt, odt), opplastede filer hentes uendret, fildatoen settes lik «sist endret» på Drive, og bare endrede filer hentes på nytt. Ikke for de ansattes CV-er, som vedlikeholdes i git i cvs/. Trigger-fraser: «hent fra Drive», «last ned fra driven», «hent denne fila/mappa fra Google Drive», «last ned dokumentet <lenke>».
---

# Hente filer fra Google Drive

## Når skill-en skal brukes

Når brukeren vil ha en fil eller en mappe fra Google Drive inn i prosjektet: en original til innboksen, et regneark, en leveranse fra en partner. Skill-en dekker hentingen. Konvertering til Markdown følger innboksprosedyren i CLAUDE.md og gjøres bare når brukeren ber om det.

De ansattes CV-er hentes **ikke** herfra. De vedlikeholdes i Markdown i `cvs/`, og utviklerne oppdaterer dem med commits.

## Forutsetninger

- Python-miljøet er satt opp (`uv sync`, se README «Python-oppsett»).
- `secrets/credentials.json` (OAuth-klient, «Desktop app») finnes. `secrets/` er git-ignorert og må legges inn per maskin.
- `secrets/token.json` finnes, eller brukeren kjører scriptet selv første gang og godkjenner tilgangen i nettleseren. Claude skal ikke starte godkjenningen i nettleseren. Ber scriptet om godkjenning: stopp, og be brukeren kjøre `! uv run python src/fetch_from_drive.py <lenke> --dry-run`.

## Trinn for trinn

1. **Finn lenken eller ID-en.** Brukeren gir den. Ikke gjett lenker.
2. **Velg målmappe.** Standard er `data/drive/` (utenfor git). Originaler som skal behandles, kan hentes rett til `background/new/` (`--out background/new`). Skriv aldri til `cvs/`.
3. **Tørrkjøring:**

   ```bash
   uv run python src/fetch_from_drive.py <lenke eller ID> --dry-run [--recursive] [--out <mappe>]
   ```

   Viser filene og målstiene. En mappe hentes med filene sine. Undermapper hoppes over uten `--recursive` og nevnes med `NOTE`.
4. **Hent:**

   ```bash
   uv run python src/fetch_from_drive.py <lenke eller ID> [...] [--out <mappe>] [--format docx|pdf|md|txt|odt] [--recursive]
   ```

   Google-dokumenter eksporteres i valgt format (standard `docx`). Regneark blir `xlsx` og presentasjoner `pptx`, eller `pdf` med `--format pdf`. Opplastede filer hentes uendret. En fil som finnes lokalt med samme tidspunkt som på Drive, hoppes over (`SKIP … up to date`). `--force` henter alt på nytt. En liste med lenker kan gis med `--list <fil.csv>` (kolonnen `Link`).
5. **Rapportér** antall `OK` / `SKIP` / `FAIL` til brukeren. `FAIL` med HTTP 403 eller 404 betyr at kontoen ikke har tilgang, eller at lenken er feil. Rapportér lenken, og ikke gjett en ny.

## Ikke gjør

- Ikke legg inn hentet innhold i memory, og ikke gjengi det i chat ut over det oppgaven krever. Filer fra Drive kan inneholde personopplysninger.
- Ikke flytt eller kopier hentede filer på en måte som nullstiller fildatoen (bruk `cp -p`).
- Ikke slett lokale filer som ikke lenger finnes på Drive uten eksplisitt tillatelse.
- Ikke sjekk inn `secrets/` eller `data/`.
