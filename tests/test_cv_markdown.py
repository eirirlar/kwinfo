"""The Markdown CV format (src/cv_markdown.py) maps to the build script's data model and back."""
import cv_markdown as cm

SAMPLE = """\
<!-- guidance for the consultant: ignored -->
# Åse Nordmann

Senior utvikler | Arkitekt

- Telefon: +47 000 00 000
- **E-post:** ase@kodeworks.no
- Erfaring: 10+ år
- Språk: norsk, engelsk
- Foto: images/ase.jpg
- Fotofokus: 0.5, 0.3

## Om Åse

Første avsnitt som går
over to linjer.

- Et kulepunkt i om-teksten

## Teknisk kompetanse

### Språk og rammeverk

TypeScript, NextJS (App router, Pages router), C#/.NET

### Ledelse

- Fullt regnskapsansvar for konsern med flere selskaper, inkludert årsoppgjør

## Erfaring

### Lead-utvikler

- Kunde: Equinor
- Prosjekt: Echo 3D
- Periode: 03.2022 – nå
- Logo: logoer/equinor.svg

Beskrivelse: med kolon.

**Leveranser**

- Første bidrag
- Andre bidrag med **fet** tekst

Nøkkelord: React, Three.js

### Eget prosjekt

- Prosjekt: Eget prosjekt
- Periode: 2020

## Arbeidserfaring

- 2016 – 2023 | Tillertorget Legesenter | Fastlege, medeier
  - Klinisk arbeid
  - HMS-ansvar
- 2011 – 2018 (40 % stilling) | NTNU | Lektor

## Utdanning

- 2003 – 2009 | Cand.med. | Medical University of Warsaw

## Sertifiseringer

-  | Kurs uten år | Utsteder \\| med strek

## Verv og engasjement

- 2006 – 2008 | Leder | ANSA Polen
"""


def test_parse_sample() -> None:
    cv = cm.parse_text(SAMPLE)
    assert cv["name"] == "Åse Nordmann"
    assert cv["title"] == "Senior utvikler | Arkitekt"
    assert cv["email"] == "ase@kodeworks.no"
    assert cv["experience_years"] == "10+"
    assert cv["languages"] == ["norsk", "engelsk"]
    assert cv["photo_focus"] == [0.5, 0.3]
    assert cv["about"] == ["Første avsnitt som går over to linjer.", "- Et kulepunkt i om-teksten"]
    assert cv["skills"][0] == {"group": "Språk og rammeverk",
                               "items": ["TypeScript", "NextJS (App router, Pages router)", "C#/.NET"]}
    assert len(cv["skills"][1]["items"]) == 1
    p = cv["projects"][0]
    assert (p["role"], p["customer"], p["project"], p["period"], p["logo"]) == \
        ("Lead-utvikler", "Equinor", "Echo 3D", "03.2022 – nå", "logoer/equinor.svg")
    assert p["description"] == ["Beskrivelse: med kolon.", "**Leveranser**", "- Første bidrag",
                                "- Andre bidrag med **fet** tekst"]
    assert p["keywords"] == ["React", "Three.js"]
    assert "role" not in cv["projects"][1]          # heading equals the project name
    assert cv["experience"][0]["description"] == ["- Klinisk arbeid", "- HMS-ansvar"]
    assert cv["experience"][1]["period"] == "2011 – 2018 (40 % stilling)"
    assert cv["certifications"] == [{"name": "Kurs uten år", "issuer": "Utsteder | med strek"}]
    assert cv["lists"] == [{"title": "Verv og engasjement",
                            "items": [{"period": "2006 – 2008", "name": "Leder", "issuer": "ANSA Polen"}]}]
    assert "language" not in cv


def test_round_trip() -> None:
    cv = cm.parse_text(SAMPLE)
    assert cm.parse_text(cm.render(cv)) == cv


def test_english_cv() -> None:
    cv = cm.parse_text("# Dee\n\n## About Dee\n\nText.\n\n## Experience\n\n### Developer\n\n"
                       "- Customer: Nordic\n- Period: 2020\n\nKeywords: Rust, C\n")
    assert cv["language"] == "en"
    assert cv["projects"][0] == {"role": "Developer", "customer": "Nordic", "period": "2020",
                                 "keywords": ["Rust", "C"]}
    assert cm.parse_text(cm.render(cv)) == cv


def test_escaped_leading_markers_survive() -> None:
    cv = {"name": "X", "about": ["# not a heading", "- a bullet", "+ plus sign first"]}
    assert cm.parse_text(cm.render(cv))["about"] == cv["about"]


def test_row_with_paragraph_description_and_period_only_row() -> None:
    cv = {"name": "X",
          "experience": [{"period": "2018 – nå", "employer": "Firma", "role": "Rådgiver",
                          "description": ["Et avsnitt om jobben.", "**Mellomtittel**", "- Et kulepunkt"]},
                         {"period": "2010"}],
          "certifications": [{"name": "Uten periode"}]}
    assert cm.parse_text(cm.render(cv)) == cv
