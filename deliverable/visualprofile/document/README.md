# Document template for KodeWorks

This guide is for you if you are making an A4 document in the KodeWorks profile. You write the text as plain Markdown and build it into a PDF. The template has two variants: **letter** and **document**. The letter is used for sales letters and enquiries to customers. The document variant is used for consultant assignment postings, notes and offers. Both use the profile font NON Natural Grotesk, the KodeWorks wordmark and a footer with company details. The documents themselves are usually written in Norwegian.

## The files

| File | What it is |
|---|---|
| `letter-template.md` | The letter template. Every field has an explanatory placeholder. Copy the file and fill it in. |
| `document-template.md` | The document template. Every element comes with a short instruction. Copy the file and fill it in. |
| `example-letter.md` | A finished two-page sales letter. Use it as the model for tone and structure. |
| `example-job-posting.md` | A two-page posting of a consultant assignment. |

The PDF and PNG files are not in git. They are built from the Markdown files with `uv run python src/build_all.py` from the project root (see «Building everything» in the project README).

## Building the PDF

From the project root:

```
uv run src/build_document.py my-document.md
```

The PDF ends up next to the Markdown file, with the same name (`my-document.pdf`). Use `-o` for a different file name. You need pandoc, LuaLaTeX (TeX Live) and uv (see «Quick start» in the project README). A build usually takes less than half a minute. The build script warns if a field is missing, if a line runs outside the margin, if a paragraph ends with a single word alone on the last line, or if a character does not exist in the font (for example «✓»; the character is then left out). Read the warnings before you send the PDF. In letters the last paragraph is kept together with the closing and the signature, so the signature is never alone at the top of a page.

## The YAML fields

All fields are optional. They go at the top of the file, between two lines of `---`.

| Field | Applies to | What it does |
|---|---|---|
| `variant` | both | `letter` or `document`. Without the field a document is built. The older values `brev` and `dokument` still work, but give a warning. |
| `title` | both | In a letter: the subject line. In a document: the title. Without the field the first level 1 heading is used. |
| `subtitle` | document | Subtitle below the title. |
| `company` | both | The sending company in the footer (see below). |
| `date` | both | Date in the form `2026-11-11`, which is set as «11. november 2026». A letter without a date gets today's date. A document without a date gets no date. |
| `recipient` | letter | The recipient block, one line per row. |
| `their-ref` | letter | «Deres ref.» |
| `our-ref` | letter | «Vår ref.» |
| `closing` | letter | The closing greeting. The default is «Vennlig hilsen». |
| `sender` | letter | The signature: `name`, `title`, `email`, `phone`. One person, or a list. |
| `contact` | document | The contact block at the end of the document, with the same fields as `sender`. One person, or a list. |

A field over several lines, such as the recipient of a letter, is written with `|` and one line per row.

## How to write

Plain pandoc Markdown. The template takes care of type, colours and placement.

| Element | How to write it |
|---|---|
| Title | The field `title` in the YAML. Without it the first `#` heading becomes the title. If the title contains a colon, for example «Konsulentoppdrag: Android-utvikler», the part before the colon becomes a small label above the title. If the file has both `title` and a `#` heading, `title` wins and the heading becomes a section. |
| Section | `## Heading` |
| Subsection | `### Heading` |
| Facts box | Lines of the form `**Label:** value` right after the title, each line except the last ending with `\`. They become a box automatically, but only when all the lines have that form and the labels are short (up to about 25 characters, without a full stop). Otherwise the paragraph becomes ordinary text. A facts box elsewhere in the document: `::: {.facts}` around the lines. |
| Two columns | `:::: {.columns}` around two `::: {.column}` blocks. Suits «må ha» and «fint å ha». |
| Contact block | The field `contact` in the YAML, or `::: {.contact}` around lines with the name first and the title on the second line. A last paragraph that starts with a name in bold and contains an email address also becomes a contact block. |
| Quote | `> Quote` |
| Lists | `- item` or `1. item`, with up to two levels. |
| Table | A simple pipe table with `\|` between the columns. |
| Bold | `**bold**` gives Medium weight. |
| Italic | `*italic*` gives slanted Regular. Use sparingly. |

## The company in the footer

The footer shows the sending company's name and organisation number, the office addresses and kodeworks.no. Choose the sender with the field `company`:

| Value | Org. no. |
|---|---|
| `KodeWorks AS` | 820 478 452 |
| `KodeWorks Trondheim AS` | 920 478 492 |
| `KodeWorks Eiendom AS` | 920 478 506 |
| `KodeWorks Oslo AS` | 922 070 709 |

These are four different companies. Choose the one that actually sends the document. Without `company`, KodeWorks AS is used.

## Writing well

**Tone.** Concrete and factual. Write whole sentences, and let documented facts speak for themselves. Avoid superlatives such as «verdensledende» and «best i klassen». We are a partner that stays as long as we contribute, and the language should show it: calm, direct and without sales talk.

**Length.** A posting should stay at one or two pages. A letter should not be longer than two pages. If you have more to say, it is usually a sign that the content should be split into two documents.

**Letters.** Start with why you are writing and what you are asking for or offering, and refer to earlier contact with a date. End with what happens next and who takes the next step.

**Postings.** The facts box at the top gives the location, start, deadline and duration. Then follow the assignment, the tasks, «må ha» and «fint å ha», a short presentation of KodeWorks and how to get in touch. Only write «må ha» about what really is a requirement.

**Numbers.** Only use numbers you can document, and always give the year («omsetning i 2023»).

## Before you send

1. The build script has given no warnings.
2. The facts are checked against the source: dates, deadlines, addresses and names.
3. Numbers have a year and can be documented.
4. Customer names, logos and images are mentioned or used only where we are allowed to and where consent exists.
5. The company in the footer is the right sender.
6. You have paged through the whole PDF: no single words on a line of their own, no empty pages and no heading at the bottom of a page.
7. The contact information is correct.
8. You send the PDF. Never send the Markdown file, and never the font files.

## When the template lacks what you need

If you need something the template does not have, for example a new kind of box, a table style or another page type, do not make a local solution with extra LaTeX or manual adjustments in the single document. Such solutions disappear the next time the template is updated, and two documents end up with two different expressions. New needs should instead become elements in the shared template, so everyone gets them.

How to ask for it: send a short description to the person who maintains the templates at KodeWorks, with an example of what you would write in Markdown and how you want the result to look. Attach the document you are working on. Until the element exists, build the document without it and send the PDF as usual.

## About the font

NON Natural Grotesk is a licensed font. The build script unpacks it to a temporary folder during the build, embeds it in the PDF and deletes it again, so the document looks right for the recipient. The font files must not be copied, forwarded or installed.
