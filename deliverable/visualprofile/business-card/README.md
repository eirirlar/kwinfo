# Business card – how to make and order a new card

The KodeWorks business card has a grey front with the wordmark and your contact information, and a green back with the KW symbol. Everything that differs from one card to another is in five lines of a Markdown file.

Employees with a CV in `cvs/` get their card automatically when the CV is built (`uv run python src/build_employee_cvs.py <my-folder>`, see the CV guide). This guide is for making a card on its own, and for ordering it.

## The files in the folder

| File | Content |
|---|---|
| `business-card-template.md` / `.pdf` / `.png` | The template with placeholders (Navn Navnesen) |
| `business-card-example.md` / `.pdf` / `.png` | Example card for Eirik Larsen |
| `README.md` | This guide |

The PDF and PNG files are not in git. They are built from the Markdown files with `uv run python src/build_all.py` from the project root (see «Building everything» in the project README).

The PDF is the print file. The PNG is a screen version, for example for email or the intranet.

## Make a new card

1. Copy the template and give the copy your name, for example `business-card-kari-nordmann.md`.
2. Change the values in the header at the top of the file:

   ```yaml
   ---
   name: Kari Nordmann
   title: Seniorkonsulent
   phone: +47 912 34 567
   email: kari.nordmann@kodeworks.no
   web: kodeworks.no
   ---
   ```

   - `name` is required. All the other fields can be left out, and then the line disappears without the rest of the card moving.
   - Write the phone number with the country code and spaces: `+47 912 34 567`.
   - Write the web address without `https://` and `www.`.

3. Build the card from the project root:

   ```bash
   uv run src/build_business_card.py deliverable/visualprofile/business-card/business-card-kari-nordmann.md
   ```

   The build takes a few seconds and needs pandoc, LuaLaTeX (TeX Live) and uv (see «Quick start» in the project README). It makes `business-card-kari-nordmann.pdf` (print) and `business-card-kari-nordmann.png` (screen) next to the Markdown file.

4. Look at the PNG. The build also checks the card itself and prints `WARNING:` if something is wrong, for example that a long title grows up towards the wordmark or that the text ends up too close to the cut edge. Long titles wrap over several lines. If you get a warning, shorten the text.

## The print file

| Property | Value |
|---|---|
| Finished format | 85 × 55 mm, landscape, two-sided (page 1 front, page 2 back) |
| Bleed | 3 mm on all sides. The sheet is 105 × 75 mm with crop marks outside the bleed. TrimBox and BleedBox are set in the PDF. |
| Safe zone | All text is at least 5.5 mm inside the cut edge. The requirement is 3 mm. |
| Font | NON Natural Grotesk Regular and Medium, embedded in the PDF. The licence allows embedding. |
| Graphics | Vector only: wordmark, symbol and surfaces. No raster images. |
| Colours | CMYK only. The values come from the profile's colour palette. |

| Colour | Used for | CMYK | PMS |
|---|---|---|---|
| Grey `#E8E7E6` | The front surface | 8 / 6 / 7 / 0 | 179-2 C/U (from 2021, must be checked) |
| Green `#B6FF9E` | The back surface | 31 / 0 / 40 / 0 | 2267 C / 2267 U (neon) |
| Black `#000000` | Text, wordmark and symbol | 0 / 0 / 0 / 100 | Black C (proposal) |
| Registration colour | Only the crop marks | 100 / 100 / 100 / 100 | – |

The profile green is a neon colour. It cannot be reproduced in CMYK, so in four-colour printing the back comes out duller than on screen. The screen version (PNG) is therefore built separately with the profile's RGB colours. If you want the right green in print, ask the printer to print the back surface in Pantone 2267 as a spot colour.

## Order the card

Send the print PDF to the printer with this order:

- format 85 × 55 mm, two-sided, 3 mm bleed (included in the file);
- paper by agreement, preferably uncoated 350–400 g;
- colours: CMYK as in the file, or the back in Pantone 2267 C/U as a spot colour for the right green;
- ask for a proof before printing, and check that black is pure black (100 % K) and not a four-colour black.

The CMYK values for black and the PMS name for grey are proposals the printer should confirm before the first print run.

## QR code

The card has no QR code. The profile manual shows the card without one, and the wordmark and the web address cover the same need.

## The build

The build uses pandoc and lualatex, like the other KodeWorks templates. The font is unpacked from the licensed font file in the repo to a temporary folder and is never installed. The font check stops the build if a font from the operating system is used. The card therefore comes out the same on Windows, WSL2 and Linux.
