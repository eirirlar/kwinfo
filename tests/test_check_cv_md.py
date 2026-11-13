"""Conventions checked by src/check_cv_md.py."""
from pathlib import Path

from check_cv_md import check_file, check_text

ROOT = Path(__file__).resolve().parent.parent

GOOD = """\
# Åse Nordmann

Senior utvikler

- Telefon: +47 930 85 452
- E-post: ase@kodeworks.no
- Erfaring: 9 år
- Språk: norsk, engelsk

## Om Åse

Tekst.

## Teknisk kompetanse

### Språk og rammeverk

TypeScript, React

## Erfaring

### Lead-utvikler

- Kunde: Equinor
- Prosjekt: Echo 3D
- Periode: 03.2022 – nå

Beskrivelse.

- Bidrag

Nøkkelord: React

### Utvikler

- Kunde: Cisco
- Periode: 2019 – 2021 (40 % stilling)

Beskrivelse.

## Arbeidserfaring

- 03.2022 – nå | KodeWorks | Senior utvikler

## Utdanning

- 2015 – 2016 | M.Sc. | NTNU

## Verv og engasjement

- 2019 | Styremedlem | TIHLDE
"""


def test_good_cv_has_no_deviations() -> None:
    assert check_text(GOOD) == []


def test_delivered_example_has_no_deviations() -> None:
    assert check_file(ROOT / "deliverable" / "visualprofile" / "cv" / "cv-example.md") == []


def issues_for(old: str, new: str) -> list[str]:
    assert old in GOOD
    return check_text(GOOD.replace(old, new, 1))


def test_period_form() -> None:
    assert any("period in the wrong form" in i for i in issues_for("03.2022 – nå", "mars 2022 - d.d."))


def test_projects_newest_first() -> None:
    assert any("newest first" in i for i in issues_for("2019 – 2021", "2023 – 2024"))


def test_project_equal_to_customer() -> None:
    assert any("equals Kunde" in i for i in issues_for("- Prosjekt: Echo 3D", "- Prosjekt: Equinor"))


def test_metadata_order() -> None:
    issues = issues_for("- Kunde: Equinor\n- Prosjekt: Echo 3D", "- Prosjekt: Echo 3D\n- Kunde: Equinor")
    assert any("order Kunde" in i for i in issues)


def test_phone_form() -> None:
    assert any("phone" in i for i in issues_for("+47 930 85 452", "93085452"))


def test_about_heading_uses_first_name() -> None:
    assert any("should be «Om Åse»" in i for i in issues_for("## Om Åse", "## Om meg"))


def test_section_order() -> None:
    issues = issues_for("## Utdanning\n\n- 2015 – 2016 | M.Sc. | NTNU\n",
                        "")
    assert issues == []
    moved = GOOD.replace("## Utdanning\n\n- 2015 – 2016 | M.Sc. | NTNU\n\n", "")
    moved = moved.replace("## Arbeidserfaring", "## Utdanning\n\n- 2015 – 2016 | M.Sc. | NTNU\n\n## Arbeidserfaring")
    assert any("out of order" in i for i in check_text(moved))


def test_unknown_list_title() -> None:
    assert any("unknown section" in i for i in issues_for("## Verv og engasjement", "## Annet"))


def test_capital_group_and_duplicates() -> None:
    issues = issues_for("### Språk og rammeverk\n\nTypeScript, React",
                        "### SPRÅK OG RAMMEVERK\n\nTypeScript, React, react")
    assert any("sentence case" in i for i in issues)
    assert any("duplicates" in i for i in issues)


def test_text_bullets() -> None:
    assert any("bullet written as text" in i for i in issues_for("- Bidrag", "\\- Bidrag"))


def test_image_naming_and_existence(tmp_path: Path) -> None:
    text = GOOD.replace("- Språk: norsk, engelsk", "- Språk: norsk, engelsk\n- Foto: bilder/ase.jpg")
    issues = check_text(text, base=tmp_path)
    assert any("images/photo.jpg" in i for i in issues)
    assert any("does not exist" in i for i in issues)
