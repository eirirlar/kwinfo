# Presentation template for KodeWorks

This guide is for you if you are making a presentation in the KodeWorks profile. You write the presentation as plain text in Markdown and build it into a PDF. The template follows the profile manual: a white content surface, a deep green opening and section dividers, a green quote surface, a grey surface for key figures, a black closing and the profile font NON Natural Grotesk. The format is 16:9. The slides themselves are usually written in Norwegian.

## The files

| File | What it is |
|---|---|
| `presentation-template.md` and `presentation-template.pdf` | The template. A presentation that explains itself: one slide per slide type, with a short instruction on the slide and the Markdown syntax in the speaker notes. Copy the file and fill it in. |
| `example.md` and `example.pdf` | A finished example of 14 slides that uses every slide type. Use it as the model for tone and structure. |
| `images/` | KodeWorks' own photos used in the template and the example. |

The PDF and PNG files are not in git. They are built from the Markdown files with `uv run python src/build_all.py` from the project root (see «Building everything» in the project README).

## Building the PDF

From the project root:

```
uv run src/build_presentation.py my-presentation.md
```

The PDF ends up next to the Markdown file, with the same name (`my-presentation.pdf`). Use `-o` for a different file name.

You need pandoc, LuaLaTeX (TeX Live) and uv (see «Quick start» in the project README). The profile font and the graphics are fetched by the build script. A build usually takes 5–40 seconds.

The build script reports problems: images that do not exist (with line number), and slides with too much text (with the slide title). Read the warnings before you send the PDF.

## How to write

Plain pandoc Markdown. A new slide starts with a level 2 heading (`##`). The class in curly brackets after the heading selects the slide type. Without a class you get an ordinary text slide.

| Slide type | How to write it | Limit |
|---|---|---|
| Opening | Made automatically from the YAML block at the top: `title`, `subtitle`, `author`, `date`. | One title, optional subtitle |
| Section divider | `# Title {number="01"}`, with an optional sentence below. Without `number` the dividers are numbered automatically. | One short sentence |
| Text | `## Title`, an optional paragraph and a bullet list. With `{.lead}` the first paragraph becomes a lead. | At most four bullets |
| Text and image | `## Title {.image}`, text, and `![](images/photo_team1.jpg)`. The image fills the right part of the slide. | One image, at most three bullets |
| Two columns | A `columns` block with two `column` blocks (see below). | At most three bullets per column |
| Comparison | Like two columns, but each column starts with `### Heading`. | At most three bullets per column |
| Quote | `## {.quote}`, the quote as a block quote (`>`), and a line `Kilde: …`. | One or two sentences |
| Key figures | `## Title {.figures}`, each figure as a definition list (see below). Put the unit in the explanation, not in the number. | Two to four figures |
| Customer logos | `## Title {.logos}`, customer names as a bullet list, or logos as images in PDF format. | At most eight |
| Closing | `## Takk {.closing}`. The contact people come from `contacts` in the YAML. Without `contacts` KodeWorks' shared contact information is shown. | One or two contacts |

Examples:

````
## To kolonner

:::: columns
::: column
Venstre kolonne
:::
::: column
Høyre kolonne
:::
::::

## KodeWorks i *tall* {.figures}

27
: utviklere

39,7
: MNOK i omsetning, 2023

## Takk {.closing}

::: notes
Talernotater skrives slik.
:::
````

The opening and the closing need no content beyond the YAML block:

```
---
title: "Dine *ideer*, våre utviklere"
subtitle: "Hva presentasjonen handler om"
author: "Navn Navnesen"
date: "12. mars 2027"
contacts:
  - name: "Navn Navnesen"
    role: "Kontaktperson"
    email: "navn@kodeworks.no"
    phone: "+47 000 00 000"
---
```

Fields you leave out (for example `subtitle`, the source of a quote or the phone number) are dropped without leaving a gap. A field over several lines, such as an address, is written with `|` and a backslash (`\`) at the end of every line except the last.

## Rules

**Colour highlighting in titles.** Put asterisks around one or two words in the title: `Vi muliggjør *ideer*`. The word gets colour, not bold: dark green on a light surface and light green on deep green. Never highlight more than two words, and never the whole title. In body text `**double asterisks**` gives Medium weight. The font has no true italic, so single asterisks in body text should be avoided.

**Type.** Titles and large numbers are in Light, body text in Regular. You do not choose the type yourself, and bold is not used.

**Amount of text.** Up to four bullets per slide, and short bullets. Body text is 20 pt. If the text does not fit, the template first sets it in 18 pt. If it is still too much, the template shrinks the text so it stays within the surface, and the build script warns «Too much text on slide …». Then split the slide in two; do not send it like that.

**The seismograph and the wordmark.** The seismograph (the stroke graphic on the opening and the section dividers) and the wordmark «KodeWorks» at the bottom of every content slide are part of the theme. Do not add them yourself.

**Images and consent.** Use KodeWorks' own photos of employees and premises, not stock photos. Put the images in `images/` next to the Markdown file. An image should be at least 2000 pixels wide, otherwise it looks coarse in the PDF. Only use images where the people shown have consented to the image being used for the purpose.

**Customers.** Only mention customers we are allowed to show. Logos are added as PDF (vector), not as screenshots. Without logo files the customer names are set as text in tiles.

**Numbers and quotes.** Only use numbers you can document, and give the year (for example «omsetning i 2023»). A quote must be real and have a source.

**Tone.** Short, direct titles and concrete text. No superlatives such as «verdensledende» or «best i klassen».

## Speaker notes

Write the notes in a `::: notes` block right below the slide they belong to. They are not shown in the normal PDF. Build with `--notes` to get a separate version with note pages (`my-presentation-notater.pdf`) for your own use:

```
uv run src/build_presentation.py my-presentation.md --notes
```

Do not send the notes version to others.

## Before you send

1. The build script has given no warnings.
2. The titles have at most one or two highlighted words.
3. Page through the whole PDF: no shrunk text, no single words on a line of their own.
4. Check numbers, years, customer names and quotes against the source.
5. Check the contact information on the last slide.
6. Check that the images are KodeWorks' own, and that consent exists.
7. Send the normal PDF, not the notes version.

## About the font

NON Natural Grotesk is a licensed font. The build script unpacks it to a temporary folder during the build, embeds it in the PDF and deletes it again, so the document looks right for the recipient. The font files must not be copied, forwarded or installed. The flag `--keep-build` keeps the build folder (with the font files) for debugging; delete it afterwards.
