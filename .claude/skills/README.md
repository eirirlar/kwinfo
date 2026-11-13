# Prosjekt-skills for kwinfo

Hver skill ligger i egen undermappe med `SKILL.md` (navn, beskrivelse og prosedyre). Claude Code aktiverer en skill når brukeren skriver `/<navn>`, eller når forespørselen matcher beskrivelsen. Innholdet leses først når skill-en invokeres.

| Skill | Formål |
|---|---|
| [`fetch-from-drive/`](fetch-from-drive/SKILL.md) | Hent filer eller mapper fra Google Drive (fildato = sist endret på Drive) med `src/fetch_from_drive.py`. Ikke for CV-ene, som er i git i `cvs/`. |
