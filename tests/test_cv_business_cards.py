"""Business card fields read from a CV in Markdown (src/build_cv_business_cards.py)."""
import cv_markdown as cm
from build_cv_business_cards import WEB, card_fields, card_markdown

CV = """\
# Åse Nordmann

Senior utvikler | Arkitekt: sky

- Telefon: +47 930 85 452
- E-post: ase@kodeworks.no
- Erfaring: 9 år

## Om Åse

Tekst.
"""


def test_fields_from_cv() -> None:
    assert card_fields(cm.parse_text(CV)) == {"name": "Åse Nordmann", "title": "Senior utvikler | Arkitekt: sky",
                                              "phone": "+47 930 85 452", "email": "ase@kodeworks.no", "web": WEB}


def test_missing_fields_are_left_out() -> None:
    assert card_fields(cm.parse_text("# Nina Nordmann\n")) == {"name": "Nina Nordmann", "web": WEB}


def test_card_file_quotes_every_value() -> None:
    text = card_markdown(card_fields(cm.parse_text(CV)))
    assert text.splitlines() == ["---", 'name: "Åse Nordmann"', 'title: "Senior utvikler | Arkitekt: sky"',
                                 'phone: "+47 930 85 452"', 'email: "ase@kodeworks.no"', f'web: "{WEB}"', "---"]


def test_double_quotes_in_a_title_use_single_quotes() -> None:
    assert card_markdown({"name": "Ola", "title": 'Leder for "data"'}).splitlines()[2] == "title: 'Leder for \"data\"'"
