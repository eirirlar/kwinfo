"""Code, flags, messages, folder names and documentation are in English; documents (PDFs and their sources) are Norwegian.

Checked here:
- help texts and descriptions of command-line flags in every script in src/;
- messages printed by the scripts (die/print/exit/warnings/issues) in the scripts listed in MESSAGE_SCRIPTS,
  where text quoted in «…» is content (a CV label, a slide title) and may be Norwegian;
- folder names in the repo, except the media folders of documents in background/ (they follow the
  Norwegian document name) and the folders listed in EXCLUDED_DIRS;
- file names in the repo, except the background documents in NORWEGIAN_FILES (the user's decision,
  2026-11-13). The content of documents stays Norwegian; only the names are English.
"""
import ast
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
NORWEGIAN = re.compile(r"[æøåÆØÅ]|\b(ikke|mangler|finnes|finner|fant|feil|kjøring|sider|linje|mappe|varsel|bygget|"
                       r"standard|ingen|skal|eller|og|ved|siden)\b", re.I)

MESSAGE_SCRIPTS = ["build_document.py", "build_presentation.py", "check_document_pdf.py", "check_presentation_pdf.py",
                   "check_cv_md.py", "build_cv_pdf.py", "build_profile_manual.py", "font_guard.py", "build_md_pdf.py",
                   "export_profile_assets.py", "build_business_card.py"]
MESSAGE_CALLS = {"die", "print", "exit", "SystemExit", "append", "add", "write"}
# temp/ and data/ hold working data, not part of the project's structure.
EXCLUDED_DIRS = {".git", ".venv", ".venv-linux", "__pycache__", ".pytest_cache", "node_modules", "temp", "tmp", "data",
                 "secrets", "worktrees"}
# Background documents that keep their Norwegian names.
NORWEGIAN_FILES = {f"background/{n}.md" for n in (
    "2026-09-22_ansatthaandbok", "2026-09-22_eiendom", "2026-09-22_itko_medlemskap", "2026-09-22_kodeworks_om_selskapet",
    "2026-09-22_kw_masterpresentasjon", "2026-09-22_prosjektoversikt", "2026-09-22_webside_tekst_grunnlag",
    "2026-09-24_itko_temp_rapportering", "2026-11-11_notat_konsulentoppdrag_android_kotlin")}
# Norwegian words that have been, or are likely to be, used in file names. Matched as whole parts of the name
# (split on - _ . and space), so person and customer names in cvs/ do not trigger it.
NORWEGIAN_WORDS = {
    "avvik", "visittkort", "foto", "forside", "topp", "ekte", "ansattliste", "rapport", "oversikt", "eksempel", "mal",
    "maler", "brevmal", "dokumentmal", "presentasjonsmal", "farger", "profilmanual", "ramme", "bunn", "femte",
    "navnetrekk", "gronn", "svart", "hvit", "bred", "logobakgrunn", "strek", "mork", "skygge", "brev", "dokument",
    "utheving", "konsulentoppdrag", "utlysning", "mottaker", "mangler", "sider", "elementer", "punkter", "uten",
    "kontoret", "portrett", "notat", "selskapet", "prosjektoversikt", "webside", "tekst", "grunnlag", "medlemskap",
    "eiendom", "ansatthaandbok", "masterpresentasjon", "rapportering", "bilde", "bilder", "kunde", "kunder",
    "prosjekt", "prosjekter", "ansatte", "presentasjon", "veiledning", "lesmeg", "mappe", "fil"}


def literal_text(node: ast.AST) -> str:
    """The literal parts of a string constant or f-string (the {…} expressions left out)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(v.value for v in node.values if isinstance(v, ast.Constant) and isinstance(v.value, str))
    return ""


def without_quoted(text: str) -> str:
    return re.sub(r"«[^»]*»", "", text)


def scripts() -> list[Path]:
    return sorted((ROOT / "src").glob("*.py"))


@pytest.mark.parametrize("path", scripts(), ids=lambda p: p.name)
def test_flag_help_is_english(path: Path) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") in ("add_argument", "ArgumentParser") \
                or isinstance(node, ast.Call) and getattr(node.func, "id", "") == "ArgumentParser":
            for kw in node.keywords:
                if kw.arg in ("help", "description") and NORWEGIAN.search(literal_text(kw.value)):
                    bad.append(literal_text(kw.value))
    assert bad == [], f"{path.name}: Norwegian help text: {bad}"


@pytest.mark.parametrize("name", MESSAGE_SCRIPTS)
def test_messages_are_english(name: str) -> None:
    tree = ast.parse((ROOT / "src" / name).read_text(encoding="utf-8"))
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fname = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
        if fname not in MESSAGE_CALLS:
            continue
        for arg in node.args:
            parts = [arg] if not isinstance(arg, ast.BinOp) else [arg.left, arg.right]
            for part in parts:
                text = without_quoted(literal_text(part))
                if text.startswith("\\") or text.lstrip().startswith(("|", "#", "%")):
                    continue   # LaTeX or Markdown written to a document, not a message
                if NORWEGIAN.search(text):
                    bad.append(text.strip()[:80])
    assert bad == [], f"{name}: Norwegian message text: {bad}"


def folders() -> list[Path]:
    out = []
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if not p.is_dir() or any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        out.append(rel)
    return out


def test_folder_names_are_english() -> None:
    bad = []
    for rel in folders():
        name = rel.name
        if rel.parts[0] == "background" and (name.endswith("_media") or any(x.endswith("_media") for x in rel.parts)):
            continue   # follows the (Norwegian) name of the document it belongs to
        if re.search(r"[æøåÆØÅ]", name) or name.lower() in {"cver", "mønster", "bilder", "kilde", "runde", "profil",
                                                             "presentasjon", "dokument", "visittkort", "mal", "maler"} \
                or "leveranse" in name.lower() or "last-ned" in name.lower():
            bad.append(str(rel))
    assert bad == [], f"Norwegian folder names: {bad}"


def repo_files() -> list[str]:
    out = []
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if p.is_file() and not any(part in EXCLUDED_DIRS for part in rel.parts) and rel.parts[:2] != ("background", "new"):
            out.append(rel.as_posix())
    return sorted(out)


def test_file_names_are_english() -> None:
    bad = []
    for rel in repo_files():
        if rel in NORWEGIAN_FILES:
            continue
        name = rel.rsplit("/", 1)[-1]
        parts = set(re.split(r"[-_.\s]+", name.lower()))
        if re.search(r"[æøåÆØÅ]", name) or parts & NORWEGIAN_WORDS:
            bad.append(rel)
    assert bad == [], f"Norwegian file names: {bad}"


@pytest.mark.parametrize("rel", sorted(NORWEGIAN_FILES))
def test_norwegian_file_exceptions_exist(rel: str) -> None:
    """An exception for a file that no longer exists is a stale entry: remove it."""
    assert (ROOT / rel).is_file()
