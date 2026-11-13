# Project skills

Each skill has its own subfolder with a `SKILL.md` (name, description and procedure). Claude Code activates a skill when the user types `/<name>`, or when the request matches the description. The content is read only when the skill is invoked.

| Skill | Purpose |
|---|---|
| [`fetch-from-drive/`](fetch-from-drive/SKILL.md) | Fetch files or folders from Google Drive (file date = last modified on Drive) with `src/fetch_from_drive.py`. Not for the CVs, which are in git in `cvs/`. |
