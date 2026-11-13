"""Fetch files or whole folders from Google Drive to a local folder.

What to fetch is given as Drive links or file/folder IDs, or as a CSV list with a Link column. Google Docs
are exported in the chosen format (default docx); Sheets and Slides as xlsx/pptx (or pdf with --format pdf);
uploaded files (docx, pdf, images, ...) are downloaded unchanged. A folder is fetched with its files;
with --recursive its subfolders too, mirrored as subfolders.

Each file's modification time is set to the Drive file's modifiedTime, so the local date shows when it
was last changed on Drive. A file is fetched again only when it is missing or its date differs from Drive
(--force: always). Read-only OAuth (secrets/credentials.json, secrets/token.json).

The default output folder, data/drive/, is ignored by git. The employees' CVs are maintained in git in
cvs/ and are not fetched from Drive.

Usage (from the project root):
    uv run python src/fetch_from_drive.py <link or ID> [...] [--out data/drive] [--format docx|pdf|md|txt|odt]
                                          [--recursive] [--force] [--dry-run]
    uv run python src/fetch_from_drive.py --list data/cv_sources.csv --out data/drive/cv
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
DEFAULT_OUT = Path("data/drive")

GOOGLE_APPS_PREFIX = "application/vnd.google-apps."
FOLDER_MIME = "application/vnd.google-apps.folder"
DOC_MIME = "application/vnd.google-apps.document"
SHEET_MIME = "application/vnd.google-apps.spreadsheet"
SLIDES_MIME = "application/vnd.google-apps.presentation"

PDF = "application/pdf"
DOC_EXPORT = {
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "pdf": PDF,
    "md": "text/markdown",
    "txt": "text/plain",
    "odt": "application/vnd.oasis.opendocument.text",
}
SHEET_EXPORT = ("xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
SLIDES_EXPORT = ("pptx", "application/vnd.openxmlformats-officedocument.presentationml.presentation")

_ID_PATTERNS = [
    re.compile(r"/(?:document|spreadsheets|presentation|drawings|forms|file)/(?:u/\d+/)?d/([^/]+)(?:/|$)", re.I),
    re.compile(r"/folders/([^/?#]+)", re.I),
]
_BARE_ID = re.compile(r"^[A-Za-z0-9_-]{10,}$")
_INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


@dataclass(frozen=True)
class Item:
    """One Drive file to fetch, and where it goes, relative to the output folder."""
    file_id: str
    name: str
    mime: str
    modified: str
    subdir: str = ""


def extract_id(ref: str) -> str | None:
    """The Drive file or folder ID from a Docs/Sheets/Slides/Drive link, or a bare ID; else None."""
    ref = ref.strip()
    if _BARE_ID.match(ref):
        return ref
    parsed = urlparse(ref)
    if not parsed.netloc:
        return None
    for pattern in _ID_PATTERNS:
        m = pattern.search(parsed.path or "")
        if m:
            return m.group(1)
    ids = parse_qs(parsed.query or "").get("id")
    return ids[0] if ids else None


def is_folder_link(ref: str) -> bool:
    """True if a link points at a Drive folder (the ID alone does not tell)."""
    return "/folders/" in urlparse(ref.strip()).path


def safe_filename(name: str) -> str:
    """Make a Drive name safe as a file or folder name on Windows and Linux."""
    cleaned = _INVALID_FILENAME_CHARS.sub("_", name).strip().rstrip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "unnamed"


def export_choice(mime: str, fmt: str) -> tuple[str, str] | None:
    """(extension, export MIME type) for a Google Apps file, or None if it is downloaded as-is.

    Raises ValueError for Google Apps types that cannot be exported (forms, shortcuts, ...)."""
    if not mime.startswith(GOOGLE_APPS_PREFIX):
        return None
    if mime == DOC_MIME:
        return fmt, DOC_EXPORT[fmt]
    if mime == SHEET_MIME:
        return ("pdf", PDF) if fmt == "pdf" else SHEET_EXPORT
    if mime == SLIDES_MIME:
        return ("pdf", PDF) if fmt == "pdf" else SLIDES_EXPORT
    if mime == "application/vnd.google-apps.drawing":
        return "pdf", PDF
    raise ValueError(f"cannot export Google Apps type {mime.removeprefix(GOOGLE_APPS_PREFIX)}")


def target_filename(drive_name: str, mime: str, fmt: str) -> str:
    """Filename for a fetched file: the Drive name, plus the export extension for Google Apps files."""
    base = safe_filename(drive_name)
    choice = export_choice(mime, fmt)
    if choice is None:
        return base  # uploaded files keep their own name and extension
    ext = "." + choice[0]
    return base if base.lower().endswith(ext) else base + ext


def drive_timestamp(modified_time: str) -> float:
    """Convert a Drive RFC 3339 modifiedTime (e.g. 2026-10-01T08:15:30.123Z) to a POSIX timestamp."""
    return datetime.fromisoformat(modified_time.replace("Z", "+00:00")).timestamp()


def is_up_to_date(path: Path, timestamp: float) -> bool:
    """True if the file exists and its mtime matches the Drive timestamp (within 1 s)."""
    return path.exists() and abs(path.stat().st_mtime - timestamp) < 1.0


def read_link_list(path: Path) -> list[str]:
    """The links in a CSV file with a Link column (separator ; or ,). Rows without a link are skipped."""
    text = path.read_text(encoding="utf-8-sig")
    delimiter = ";" if text.splitlines()[0].count(";") >= text.splitlines()[0].count(",") else ","
    rows = csv.DictReader(io.StringIO(text), delimiter=delimiter)
    if "Link" not in (rows.fieldnames or []):
        raise SystemExit(f"{path}: no Link column (found: {', '.join(rows.fieldnames or [])})")
    return [(r.get("Link") or "").strip() for r in rows if (r.get("Link") or "").strip()]


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fetch files or folders from Google Drive.")
    p.add_argument("refs", nargs="*", help="Drive links or file/folder IDs")
    p.add_argument("--list", type=Path, help="CSV file with a Link column, fetched in addition to the arguments")
    p.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output folder (default: {DEFAULT_OUT.as_posix()})")
    p.add_argument("--format", choices=sorted(DOC_EXPORT), default="docx",
                   help="export format for Google Docs (default: docx); Sheets/Slides become xlsx/pptx, or pdf")
    p.add_argument("--recursive", action="store_true", help="also fetch the subfolders of a folder")
    p.add_argument("--force", action="store_true", help="fetch even if the local file is up to date with Drive")
    p.add_argument("--dry-run", action="store_true", help="show what would be fetched and where, without fetching")
    p.add_argument("--credentials", type=Path, default=Path("secrets/credentials.json"))
    p.add_argument("--token", type=Path, default=Path("secrets/token.json"))
    args = p.parse_args(argv)
    if args.list:
        args.refs = list(args.refs) + read_link_list(args.list)
    if not args.refs:
        p.error("give at least one Drive link or ID, or --list")
    return args


def load_credentials(credentials_file: Path, token_file: Path):
    """Load OAuth user credentials; opens a browser for consent on first run."""
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if token_file.exists():
        # No scopes argument: keep whatever scopes the stored token was granted.
        creds = Credentials.from_authorized_user_file(str(token_file))
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not credentials_file.exists():
            sys.exit(f"Missing OAuth client file: {credentials_file}")
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_file), SCOPES)
        creds = flow.run_local_server(port=0)
    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(creds.to_json(), encoding="utf-8")
    return creds


FIELDS = "id,name,mimeType,modifiedTime"


def list_folder(drive, folder_id: str) -> list[dict]:
    """The files and subfolders directly in a Drive folder (not trashed), sorted by name."""
    out, token = [], None
    while True:
        res = drive.files().list(q=f"'{folder_id}' in parents and trashed = false",
                                 fields=f"nextPageToken, files({FIELDS})", pageToken=token, pageSize=200,
                                 supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        out += res.get("files", [])
        token = res.get("nextPageToken")
        if not token:
            return sorted(out, key=lambda f: f["name"].lower())


def expand(drive, meta: dict, recursive: bool, subdir: str = "", notes: list[str] | None = None) -> list[Item]:
    """The files to fetch for one Drive entry: the file itself, or a folder's files (and subfolders)."""
    if meta["mimeType"] != FOLDER_MIME:
        return [Item(meta["id"], meta["name"], meta["mimeType"], meta["modifiedTime"], subdir)]
    folder = f"{subdir}/{safe_filename(meta['name'])}".lstrip("/")
    items: list[Item] = []
    for child in list_folder(drive, meta["id"]):
        if child["mimeType"] == FOLDER_MIME and not recursive:
            if notes is not None:
                notes.append(f"subfolder {folder}/{child['name']} skipped (use --recursive)")
            continue
        items += expand(drive, child, recursive, folder, notes)
    return items


def _download(request) -> bytes:
    from googleapiclient.http import MediaIoBaseDownload

    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buf.getvalue()


def main(argv: list[str] | None = None) -> int:
    # Windows consoles default to a legacy code page; keep æøå readable.
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args(argv)

    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

    drive = build("drive", "v3", credentials=load_credentials(args.credentials, args.token), cache_discovery=False)
    fetched = skipped = failed = 0
    notes: list[str] = []
    items: list[Item] = []
    for ref in args.refs:
        file_id = extract_id(ref)
        if not file_id:
            print(f"FAIL  no Drive ID in {ref}")
            failed += 1
            continue
        try:
            meta = drive.files().get(fileId=file_id, fields=FIELDS, supportsAllDrives=True).execute()
            items += expand(drive, meta, args.recursive, notes=notes)
        except HttpError as e:
            print(f"FAIL  {ref}: HTTP {e.resp.status} {e.reason}")
            failed += 1

    for it in items:
        try:
            name = target_filename(it.name, it.mime, args.format)
        except ValueError as e:
            print(f"SKIP  {it.subdir + '/' if it.subdir else ''}{it.name}: {e}")
            skipped += 1
            continue
        target = args.out / it.subdir / name
        timestamp = drive_timestamp(it.modified)
        if not args.force and is_up_to_date(target, timestamp):
            print(f"SKIP  {target.as_posix()} up to date ({it.modified[:10]})")
            skipped += 1
            continue
        if args.dry_run:
            print(f"would fetch: {target.as_posix()}  (changed {it.modified[:10]})")
            continue
        try:
            choice = export_choice(it.mime, args.format)
            if choice:
                req = drive.files().export_media(fileId=it.file_id, mimeType=choice[1])
            else:
                req = drive.files().get_media(fileId=it.file_id, supportsAllDrives=True)
            content = _download(req)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            os.utime(target, (timestamp, timestamp))
            print(f"OK    {target.as_posix()} ({len(content) // 1024} KB, changed {it.modified[:10]})")
            fetched += 1
        except HttpError as e:
            print(f"FAIL  {it.name}: HTTP {e.resp.status} {e.reason}")
            failed += 1

    for n in notes:
        print(f"NOTE  {n}")
    verb = "would be fetched" if args.dry_run else "fetched"
    count = len(items) - skipped if args.dry_run else fetched
    print(f"\n{count} {verb}, {skipped} skipped, {failed} failed -> {args.out.as_posix()}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
