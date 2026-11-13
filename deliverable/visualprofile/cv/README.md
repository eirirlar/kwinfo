# CV template for KodeWorks consultants

**Start here if you are a consultant.** Your CV is written as an ordinary Markdown file and built automatically into a finished PDF in the KodeWorks visual profile. You write the content. Layout, typography, page breaks, logos, photo and the seismograph frame are handled by the build script. There is no Word version, because the profile font can only be embedded in PDF.

| File | What it is |
|---|---|
| `cv-template.md` | An empty template with guidance in comments. Start here. |
| `cv-template.pdf` | What the template looks like when typeset. |
| `cv-example.md` | A filled-in example with eight projects, a photo and customer logos. |
| `cv-example.pdf` | The finished example (four pages). |
| `images/` | Photo and logos used by the example. |

The PDF and PNG files are not in git. They are built from the Markdown files with `uv run python src/build_all.py` from the project root (see «Building everything» in the project README).

## What you need

The build works the same on Windows, Linux and macOS. It needs `uv`, TeX Live with `lualatex`, and Pandoc (the CV command also builds your business card, which uses Pandoc). The profile font is taken from the font file in the project and does not need to be installed on the machine. Installation and a quick check of the setup are in «Quick start» in the project README. If you do not have the tools, the person responsible for the profile can build the CV for you.

## How to make your CV

1. Create one folder for the CV under `cvs/`, named after you in lower case, where æ becomes ae, ø becomes oe, å becomes aa and spaces become hyphens. Copy `cv-template.md` into the folder with the same name, and put the photo in the subfolder `images/`. The customer logos are in the shared logo library `cvs/logos/`, which all the CVs share:

   ```
   cvs/
   ├── logos/
   │   ├── equinor.png
   │   └── ...
   └── ola-nordmann/
       ├── ola-nordmann.md
       └── images/
           └── photo.jpg
   ```

2. Fill it in. Use `cv-example.md` as the model for level and length. The file can be read and edited in any text editor, and previewed in e.g. VS Code.
3. Build the PDF and check the file from the project folder:

   ```bash
   uv run python src/build_employee_cvs.py ola-nordmann          # CV PDF and business card next to the CV
   uv run python src/check_cv_md.py cvs/ola-nordmann/ola-nordmann.md
   ```

   The check makes sure the CV follows the same rules as all the others (order, labels, date format and image names), and prints what needs fixing, if anything. The build takes 5–40 seconds.
4. Read the warnings from the build, open the PDF and go through the checklist at the bottom.
5. Commit the Markdown file and the photo. The PDF and the business card are not committed.

## The format

The CV itself can be in Norwegian or English. The example below is Norwegian; English labels are listed under the rules.

```markdown
# Ola Nordmann

Senior utvikler

- Telefon: +47 000 00 000
- E-post: ola@kodeworks.no
- Erfaring: 8 år
- Språk: norsk, engelsk
- Foto: images/photo.jpg

## Om Ola

Ett til tre avsnitt i tredje person.

## Teknisk kompetanse

### Språk og rammeverk

TypeScript, React, Kotlin

## Erfaring

### Lead-utvikler

- Kunde: Equinor
- Prosjekt: Echo 3D
- Periode: 03.2022 – nå
- Logo: images/logo-equinor.png

Beskrivelse i ett eller flere avsnitt.

- Konkret bidrag
- Konkret bidrag

Nøkkelord: React, TypeScript, Azure

## Arbeidserfaring

- 03.2022 – nå | KodeWorks | Senior utvikler

## Utdanning

- 2015 – 2016 | Business Economics, M.Sc. | Handelshøyskolen BI

## Sertifiseringer

- 2021 | Azure Fundamentals (AZ-900) | Microsoft
```

**Rules:**

- `#` is the name. The paragraph right below is the job title.
- The list below the title is the contact information, always in this order: Telefon (`+47 000 00 000`), E-post, Erfaring (`N år`), Språk (lower case, separated by commas) and Foto.
- The sections come in this order: `## Om <first name>`, `## Teknisk kompetanse`, `## Erfaring`, `## Arbeidserfaring`, `## Utdanning`, `## Sertifiseringer` and any extra lists. The «Om» text is on the front page, and bullet points are allowed.
- Under `## Teknisk kompetanse` each `###` is a group, with the group name in sentence case («Infrastruktur og DevOps», not capitals). The items are written on one line separated by commas. Whole sentences are written as a bullet list. Each item appears only once.
- Under `## Erfaring` each `###` is one project, with the role as the heading and the newest project first.
  - The list right below the heading holds fixed fields, in the order Kunde, Prosjekt, Periode and Logo.
  - Prosjekt is left out when it is the same as the customer.
  - Then comes the description, and finally one line that starts with `Nøkkelord:`.
- In descriptions `**bold**` gives emphasised text, and a paragraph that is only `**Text**` becomes a small subheading. Bullet points are written as a Markdown list (`- `), not as «\-» or «•».
- In `Arbeidserfaring`, `Utdanning` and `Sertifiseringer` each row is `period | name | place`. Without a period, write `- | name | place`. Sub-items (indented two spaces) become a short description of the row. Sertifiseringer are only formal certifications, such as AZ-900 and PSM I.
- Other lists get their own heading with one of the fixed titles `## Verv og engasjement`, `## Foredrag og publikasjoner`, `## Kurs` or `## Utmerkelser`, in the same form. Use them instead of putting such things under Sertifiseringer.
- Periods are written as `MM.ÅÅÅÅ – MM.ÅÅÅÅ`, `MM.ÅÅÅÅ – nå`, `ÅÅÅÅ – ÅÅÅÅ` or `ÅÅÅÅ`, with an en dash and spaces. Write «nå», not «d.d.». Additions go in brackets after the period and wrap neatly: `2011 – 2018 (40 % stilling)`.
- All fields are optional. What is missing is not shown and leaves no gap.
- Comments (`<!-- … -->`) are not shown in the PDF.
- **English CV:** use English headings and labels (`## About Ola`, `## Skills`, `## Experience`, `Customer:`, `Period:`, `Keywords:`, `## Work experience`, `## Education`, `## Certifications`). The CV then gets English hyphenation and English labels.

## Photo and customer logos

- **Photo:** a calm portrait. The image is cropped automatically to fill the frame, also when it is landscape or shows the whole person. If the face ends up in the wrong place, add `- Fotofokus: 0.5, 0.3` (horizontal and vertical point as a fraction of the image, where 0, 0 is the top left).
- **Photo format:** the photo is called `images/photo.jpg` and is a JPG without metadata (EXIF, colour profile), with at most 1200 pixels across the crop with the frame's aspect ratio (60:74), so at most 1200 × 1480 for a portrait photo. Add the photo as you have it, and run `uv run src/normalize_cv_images.py --apply`: it converts to JPG, removes metadata, scales down and fixes the reference in the CV. Run it without `--apply` first to see what will change.
- **Logos:** each customer has one logo in `cvs/logos/<customer>.svg` or `.png`, with the customer name in lower case with hyphens (e.g. `cvs/logos/sunlit-sea.png`). The CV refers to it as `- Logo: ../logos/sunlit-sea.png`. If the customer is already in the library, use that file. A new logo goes into the library. The normalisation script trims edges and scales a PNG down to at most 700 × 260 pixels. The CV check reports deviations for photos and logos that do not follow the format.
- **The template and the example** in this folder have their own images in `images/` (`images/photo.jpg`, `images/logo-<customer>.png`), so they can be used without the rest of the repo.
- **Logo:** the customer's logo is shown at the top right of the project block. SVG is best; a PNG should be at least 600 pixels wide. White and transparent edges are trimmed away, and the logo is scaled so all logos get about the same visual weight. The build script warns when a logo has too low a resolution. When the customer is KodeWorks, no logo is shown, because the wordmark is already at the bottom of the CV. Only use logos the customer publishes itself.

## How the CV adapts to the content

- The front page has the contact information, «Om» and the skills, preferably in two columns. If «Om» is long, the skills are stacked below. If there is plenty of room left, «Erfaring» starts on the front page already. Otherwise the front page is closed with the seismograph band.
- Projects break across pages with the green left edge intact. There are at least two lines on each side of a break, and a project title is never left alone at the bottom of a page. The skills are never split inside a group.
- The columns in «Generelt» are measured from the content and line up through all the lists. Short lists are not split across pages.
- The build tries several variants and picks the one with the fewest pages without half-empty pages. The body text is always 9.5 pt. Long CVs get more pages rather than smaller text.
- The template is tested with 20 real KodeWorks CVs and with artificial tests: name only, 0–13 projects, special characters, overlong words and URLs, and English text.

## Writing advice

- **About you:** professional profile first (focus, experience, how you work), then something that sets you apart. Third person, concrete, without superlatives.
- **Project description:** start with the problem or goal the customer had, and what kind of system it is. Then describe your role and responsibility, and end with the result. Three to eight lines plus bullet points for concrete contributions, with verbs in the past tense.
- **Keywords:** the most important technologies in the project, preferably four to eight. Also mention them in the text where they were used.
- Older or smaller projects can have one or two sentences.

## Checklist before the CV is sent

1. Name, title, phone and email are correct.
2. The projects are newest first, and all periods have the same format.
3. Customer and project names are written the same way as in earlier CVs and offers.
4. No customer logo is used unless the customer publishes it itself.
5. No warnings from the build script about missing images, low resolution or removed characters, and the check (`check_cv_md.py`) reports no deviations.
6. The font is embedded: in the PDF reader, under Properties → Fonts, only NON Natural Grotesk is listed.
7. The photo shows the face well in the frame.
8. The file name is descriptive, e.g. `CV Ola Nordmann KodeWorks.pdf`.
