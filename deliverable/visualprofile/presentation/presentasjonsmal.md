---
title: "[Tittel med ett *uthevet* ord]"
subtitle: "[Undertittel: hva presentasjonen handler om og for hvem]"
author: "[Ditt navn]"
date: "[Dato, f.eks. 12. mars 2027]"
contacts:
  - name: "[Navn på kontaktperson]"
    role: "[Rolle]"
    email: "[navn@kodeworks.no]"
    phone: "[+47 000 00 000]"
---

::: notes
ÅPNING. Dette lysbildet lages automatisk fra YAML-blokken øverst i filen: title, subtitle, author og date. Sett stjerner rundt ett eller to ord i tittelen for fargeutheving. Slett subtitle-linjen hvis du ikke trenger den. Talernotater skrives i en blokk som denne, rett under lysbildet de hører til: en linje med tre kolon og ordet notes, teksten, og en linje med tre kolon.
:::

# [Seksjonstittel med ett *uthevet* ord] {number="01"}

[Seksjonsskille: starter en ny del. Nummer, tittel og én kort setning.]

::: notes
SEKSJONSSKILLE. Lages med en overskrift på nivå 1 (en enkelt #). Tallet settes med {number="01"}; utelater du det, nummereres seksjonene automatisk. Teksten rett under overskriften blir skillets korte tekst og er valgfri. Bruk skiller når presentasjonen har mer enn omtrent ti lysbilder.
:::

## [Tittel med ett *uthevet* ord]

[Tekst: et kort avsnitt og høyst fire korte punkter.]

- **[Nøkkelord]:** [kort forklaring, én linje]
- **[Nøkkelord]:** [kort forklaring, én linje]
- **[Nøkkelord]:** [kort forklaring, én linje]

::: notes
TEKST. Overskrift på nivå 2 (##) lager et nytt lysbilde. Bruk inntil fire punkter, og hvert punkt skal få plass på en eller to linjer. Skriv dobbel stjerne rundt et nøkkelord for Medium-vekt. Et ekstra innrykk (fire mellomrom) gir et nivå 2-punkt, men bruk det sjelden. Starter lysbildet med klassen {.lead}, blir første avsnitt en ingress i større Light-skrift. Passer ikke teksten, del opp lysbildet i stedet for å minske skriften.
:::

## [Tittel med ett *uthevet* ord] {.image}

[Tekst og bilde: høyst tre punkter til venstre, ett foto fra KodeWorks til høyre.]

![](images/foto_team1.jpg)

::: notes
TEKST OG BILDE. Legg til klassen {.image} på overskriften. Teksten står til venstre, og det første bildet blir en stor flate til høyre, beskåret til å fylle. Bruk KodeWorks' egne foto av ansatte og lokaler, ikke stockfoto. Bildet må ligge i mappen images/ ved siden av Markdown-filen. Har du ikke samtykke fra de som er avbildet, bruker du et annet bilde.
:::

## [Tittel med ett *uthevet* ord]

:::: columns
::: column
[To kolonner: to likestilte tekster, høyst tre punkter i hver.]
:::
::: column
[Bruk den når to ting hører sammen uten å stå mot hverandre.]
:::
::::

::: notes
TO KOLONNER. Brukes til to likestilte tekster. Bygg den med en columns-blokk (fire kolon) som inneholder to column-blokker (tre kolon). Hold kolonnene omtrent like lange.
:::

## [Sammenligning med ett *uthevet* ord]

:::: columns
::: column
### [Overskrift A]

- [Punkt]
- [Punkt]
- [Punkt]
:::
::: column
### [Overskrift B]

- [Punkt]
- [Punkt]
- [Punkt]
:::
::::

::: notes
SAMMENLIGNING. Samme oppbygging som to kolonner, men hver kolonne starter med en overskrift på nivå 3 (###). Bruk den til før og etter, to alternativer eller to faser. Høyst tre punkter i hver kolonne.
:::

## {.quote}

> [Sitat: ett til to setninger, ordrett og ekte.]

Kilde: [Hvem som sa det, og hvor]

::: notes
SITAT. Lysbildet har ingen tittel: overskriften er tom og har klassen {.quote}. Blokksitatet (starter med >) er sitatet. Et avsnitt som starter med «Kilde:» blir kilden i liten skrift. Utelater du kilden, utgår linjen. Sitatet må være ekte og gjengitt ordrett; strategiplattformens ønskede inntrykk er ikke et kundesitat.
:::

## [Tittel med ett *uthevet* ord] {.figures}

[Tall 1]
: [Nøkkeltall: to til fire tall, med årstall og kilde]

[Tall 2]
: [Nøkkeltall: to til fire tall, med årstall og kilde]

[Tall 3]
: [Nøkkeltall: to til fire tall, med årstall og kilde]

::: notes
NØKKELTALL. Klassen {.figures}. Hvert tall er en definisjonsliste: tallet på én linje, og under den en linje som starter med kolon og forklaringen. Bruk to til fire tall. Oppgi årstall (for eksempel «omsetning i 2023») og ha en kilde du kan vise til. Skriv tall med mellomrom som tusenskille og komma som desimaltegn. Sett enheten (MNOK, %) i forklaringen, ikke i tallet, så tallene blir like store.
:::

## [Tittel med ett *uthevet* ord] {.logos}

[Kundelogoer: høyst åtte kunder, bare de vi har lov til å vise.]

- [Kunde 1]
- [Kunde 2]
- [Kunde 3]
- [Kunde 4]

::: notes
KUNDELOGOER. Klassen {.logos}. Punktlisten er kundenavn, som settes i fonten i et rutenett (opptil åtte). Har du klarerte logoer, bytter du punktene med bilder, for eksempel `![](logoer/kunde.pdf)`. Bruk vektorfiler i PDF-format, ikke skjermbilder. Vis bare kunder du har lov til å nevne.
:::

## [Takk] {.closing}

::: notes
AVSLUTNING. Klassen {.closing}. Tittelen er overskriften, og kontaktpersonene hentes fra contacts i YAML-blokken øverst. Navn, rolle, e-post og telefon vises; felt du utelater, utgår. Har du ikke contacts i YAML, kan du skrive kontaktinformasjonen som innhold på lysbildet.
:::
