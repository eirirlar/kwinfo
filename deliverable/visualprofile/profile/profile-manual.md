---
title: KodeWorks profilmanual
---

::: {.cover title="Designmanual" subtitle="Visuell identitet for KodeWorks. Verktøykassen for riktig bruk av logo, farger, typografi og grafiske elementer." meta="Versjon 2026"}
:::

::: {.page section="Innhold" title="Innhold" lead=""}

```{=latex}
\kwatw{16}{44}{92}{\kwsize{11}{15.5}\kwregular Manualen samler reglene for hvordan KodeWorks ser ut. Hver regel vises med et eksempel.}
\kwtoc
```

:::


::: {.divider number="01" title="Introduksjon" text="Hva identiteten består av, hva den bygger på, og hva som er endret siden 2021."}
:::

::: {.page section="Introduksjon" title="Ideen" lead="Identiteten er verktøykassen til en teknologipartner som muliggjør ideer."}

```{=latex}
\providecommand{\kwph}[8]{\kwdraw{\begin{scope}
  \clip \kwo{#1}{#2} rectangle ++(#3mm,-#4mm);
  \pgfmathsetmacro{\kwiw}{max(#3,#4/#6)}
  \pgfmathsetmacro{\kwix}{#1-(\kwiw-#3)*#7}
  \pgfmathsetmacro{\kwiy}{#2-(\kwiw*#6-#4)*#8}
  \node[anchor=north west,inner sep=0pt] at \kwo{\kwix}{\kwiy} {\includegraphics[width=\kwiw mm]{photos/#5}};
  \end{scope}}}
\kwatw{16}{47}{140}{\kwsize{11.5}{17}\kwlight
KodeWorks sin identitet er verktøykassen til en teknologipartner som muliggjør ideer. Formen er nøktern og teknisk, detaljene er levende.
Lysegrønn og lys grå gir gjenkjennelsen. De mørke grønntonene gir ro og god lesbarhet i grensesnitt og på flater.
Non Natural Grotesk i lett vekt gir luft. KW-symbolet og det femte elementet er laget av samarbeid i KodeWorks sine egne kanaler.
Fotografiene viser ekte mennesker i ekte rom.
Helheten skal oppleves som industrielt tilsnitt uten å bli corporate: enkel, med mye luft og uten pynt som ikke betyr noe.}
% Strategisk grunnlag
\kwrect{16}{106}{140}{0.4}{kwhair}
\kwatw{16}{110}{44}{\kwsize{7.5}{9}\kwregular\color{kwmuted}VISJON\par\vspace{1mm}\kwsize{10}{13.5}\kwlight Vi muliggjør ideer.}
\kwatw{64}{110}{44}{\kwsize{7.5}{9}\kwregular\color{kwmuted}PERSONLIGHET\par\vspace{1mm}\kwsize{10}{13.5}\kwlight Frempå, nysgjerrig, dedikert og kunnskapsrik.}
\kwatw{112}{110}{44}{\kwsize{7.5}{9}\kwregular\color{kwmuted}LØFTER\par\vspace{1mm}\kwsize{10}{13.5}\kwlight Faglig sterk, åpen, delingskultur, samskapende.}
\kwatw{16}{131}{140}{\kwsize{8}{11}\kwregular\color{kwmuted}Grunnlaget er den strategiske plattformen fra 2021. Den gjelder fortsatt.}
% Fire byggesteiner
\kwtile{165}{47}{56}{44}{kwgrey}{none}{kw-wordmark-black.pdf}{38}{\color{kwmuted}Navnetrekk og symbol}
\kwrect{225}{47}{8}{44}{kwgreen}
\kwrect{233}{47}{8}{44}{kwgrey}
\kwrect{241}{47}{8}{44}{kwblack}
\kwrect{249}{47}{8}{44}{kwwhite}
\kwrect{257}{47}{8}{44}{kwdarkgreen}
\kwrect{265}{47}{8}{44}{kwdeepgreen}
\kwrect{273}{47}{8}{44}{kwpink}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{225}{47} rectangle ++(56mm,-44mm);}
\kwat{228}{83}{\colorbox{kwwhite}{\kwsize{6.5}{8}\kwregular\color{kwblack}\,Sju farger\,}}
\kwdraw{\fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{165}{95} rectangle ++(56mm,-44mm);}
\kwat{170}{98}{\kwsize{44}{44}\kwlight Aa}
\kwat{168}{132}{\kwsize{6.5}{8}\kwregular\color{kwmuted}Non Natural Grotesk}
\kwph{225}{95}{56}{44}{photo_team2.jpg}{0.6664}{0.5}{0.3}
\kwat{228}{132}{\colorbox{kwwhite}{\kwsize{6.5}{8}\kwregular\color{kwblack}\,Egne bilder\,}}
```

:::

::: {.page section="Introduksjon" title="Hva er nytt" lead="Det som er endret siden 2021-manualen, og hvorfor. Resten av identiteten er beholdt."}

```{=latex}
\kwat{16}{47}{\kwsize{9}{12}\kwlight\setlength{\tabcolsep}{0pt}\renewcommand{\arraystretch}{1}%
\providecommand{\kwhl}{\noalign{{\color{kwhair}\hrule height 0.4pt}}}%
\begin{tabular}{@{}>{\kwmedium}p{27mm}@{\hspace{4mm}}>{\kwregular}p{66mm}@{\hspace{4mm}}>{\kwregular}p{84mm}@{\hspace{4mm}}>{\kwregular}p{80mm}@{}}
\kwsize{7}{9}\kwregular\color{kwmuted}ELEMENT & \kwsize{7}{9}\kwregular\color{kwmuted}2021 & \kwsize{7}{9}\kwregular\color{kwmuted}2026 & \kwsize{7}{9}\kwregular\color{kwmuted}HVORFOR\\[1.5mm]\kwhl\noalign{\vspace{2.6mm}}
Farger & Grønn og grå som hovedfarger, hvit og svart som støtte & Samme farger, med mørkegrønn \#35664C, dypgrønn \#254333 og rosa \#FAD5D5 & Mørkegrønn og rosa er i bruk på nettsiden. Knapper og lenker trenger en farge med god kontrast\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Grå & Dominerende flate & Igjen standard sekundærflate, også på nett & Nettsiden bruker nesten bare hvit\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Kontrast & Ikke beskrevet & Beregnede tall for alle fargepar & Lysegrønt på hvitt er uleselig og skal ikke forekomme\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Typografi & Regular vist, Arial som fallback, ingen størrelsesregler & Light til titler og ingress, Regular til brødtekst, Medium til utheving. Fast størrelseshierarki & Light i liten størrelse taper på lesbarhet. Nettsiden bruker Light i titler\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Logo & Symbol svart eller grønt på grått, ingen mål & Flere tillatte bakgrunner, frisone og minstestørrelse & 2021-manualen mangler mål og svart bakgrunn\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Femte element & Sentral bakgrunnsflate på alle flater & Støtteelement med regler for plassering og mengde & Brukes ikke på nettsiden og trenger en tydelig rolle\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Grid & Tre justeringer, avrundede hjørner i mockups & Venstrejustert, rektangulære hjørner, mål fra nettsiden og trykk & Nettsidens mål er testet i drift\\[2.6mm]\kwhl\noalign{\vspace{2.6mm}}
Foto & Referansebilder som ikke tilhørte KodeWorks & KodeWorks' egne bilder av ansatte og kontor & Egne bilder gir tillit og kan brukes fritt
\end{tabular}}
```

:::


::: {.divider number="02" title="Logo" text="Navnetrekket og symbolet er KodeWorks' viktigste gjenkjennelsesmerke. Her finner du varianter, frisone, minstestørrelse og hva som er tillatt."}
:::

::: {.page section="Logo" title="Navnetrekk og symbol" lead="Logoen finnes som navnetrekk og som symbol. Begge leveres som tegnet vektorfil, ikke som tekst i fonten."}

```{=latex}
\kwtile{16}{50}{62.5}{34}{kwwhite}{kwhair}{kw-wordmark-black.pdf}{42}{\color{kwmuted}Navnetrekk, svart}
\kwtile{83.5}{50}{62.5}{34}{kwblack}{none}{kw-wordmark-white.pdf}{42}{\color{kwgrey}Navnetrekk, hvit}
\kwtile{151}{50}{62.5}{34}{kwblack}{none}{kw-wordmark-green.pdf}{42}{\color{kwgrey}Navnetrekk, grønn}
\kwatw{222}{50}{59}{\kwsize{9.5}{12}\kwmedium Navnetrekket er hovedlogo\par\vspace{1.5mm}\kwsize{8.5}{12}\kwregular Symbolet kan stå alene eller sammen med navnetrekket, men aldri overlappe det. I løpende tekst skrives navnet \mbox{KodeWorks} med stor K og stor W.}%
\kwtile{16}{89}{62.5}{54}{kwwhite}{kwhair}{kw-symbol-black.pdf}{18}{\color{kwmuted}Symbol, svart}
\kwtile{83.5}{89}{62.5}{54}{kwwhite}{kwhair}{kw-symbol-black-with-green-stroke.pdf}{18}{\color{kwmuted}Symbol, svart med grønn strek}
\kwtile{151}{89}{62.5}{54}{kwblack}{none}{kw-symbol-white-with-green-stroke.pdf}{18}{\color{kwgrey}Symbol, hvit med grønn strek}
\kwtile{218.5}{89}{62.5}{54}{kwblack}{none}{kw-symbol-green.pdf}{18}{\color{kwgrey}Symbol, grønn}
```

:::

::: {.page section="Logo" title="Frisone og minstestørrelse" lead="Frisonen er fri for tekst, kanter, bilder og andre logoer. Målene følger logoens egne proporsjoner, slik at de gjelder i alle størrelser."}

```{=latex}
% ---- Navnetrekk: width 72 mm; x = K height = 10.35 mm; frisone 0.5x = 5.17 mm
\kwat{16}{47.5}{\kwsize{11}{13}\kwmedium Navnetrekk}
\kwrect{16}{58}{82.34}{20.96}{kwgrey}
\kwdraw{\fill[fill=kwwhite,draw=kwdarkgreen,dash pattern=on 1.2mm off 0.8mm,line width=0.4pt] \kwo{21.17}{63.17} rectangle ++(72mm,-10.62mm);
  \kwdimh{16}{21.17}{56.2}{0,5x}\kwdimh{93.17}{98.34}{56.2}{0,5x}
  \kwdimv{58}{63.17}{13.5}{0,5x}\kwdimv{63.17}{73.79}{13.5}{x}\kwdimv{73.79}{78.96}{13.5}{0,5x}}
\kwimg{21.17}{63.17}{72}{kw-wordmark-black.pdf}
\kwatw{16}{84}{132}{\kwsize{8.5}{12}\kwregular x er høyden på K. Frisonen er 0,5x på alle sider, omtrent 7 prosent av bredden. Grå flate viser frisonen. Bakgrunnsfarge og seismograf bak er ikke brudd, så lenge logoen har minst 3:1 kontrast og seismografen ikke krysser bokstavene.}
\kwatw{16}{103}{132}{\kwsize{9}{12}\kwmedium Minstestørrelse\par\kwsize{8.5}{12}\kwregular 24 mm bredde på trykk, 100 px bredde på skjerm.}
\kwdraw{\kwdimh{16}{40}{127.5}{24 mm}}
\kwimg{16}{129}{24}{kw-wordmark-black.pdf}
\kwatw{50}{127}{95}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Under 100 px bredde (for eksempel e-postsignatur): bruk 120 til 160 px og lever 2x-fil for høyoppløselige skjermer.}

% ---- Symbol: height 50 mm; s = width = 28.82 mm; frisone 0.25s = 7.21 mm
\kwat{165}{47.5}{\kwsize{11}{13}\kwmedium Symbol}
\kwrect{165}{58}{43.24}{64.42}{kwgrey}
\kwdraw{\fill[fill=kwwhite,draw=kwdarkgreen,dash pattern=on 1.2mm off 0.8mm,line width=0.4pt] \kwo{172.21}{65.21} rectangle ++(28.82mm,-50mm);
  \kwdimh{165}{172.21}{56.2}{0,25s}\kwdimh{201.03}{208.24}{56.2}{0,25s}\kwdimh{172.21}{201.03}{123.9}{s}
  \kwdimv{58}{65.21}{162.5}{0,25s}\kwdimv{115.21}{122.42}{162.5}{0,25s}}
\kwimg{172.21}{65.21}{28.82}{kw-symbol-black.pdf}
\kwatw{222}{58}{59}{\kwsize{8.5}{12}\kwregular s er symbolets bredde. Frisonen er 0,25s på alle sider, omtrent 14 prosent av høyden. Grå flate viser frisonen.}
\kwatw{222}{86}{59}{\kwsize{9}{12}\kwmedium Minstestørrelse\par\kwsize{8.5}{12}\kwregular 20 mm høyde på trykk, 80 px høyde på skjerm.}
\kwimg{222}{103}{11.5}{kw-symbol-black.pdf}
\kwdraw{\kwdimv{103}{123.0}{245}{20 mm}}
\kwatw{249}{103}{32}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Under 80 px høyde forsvinner den tynne diagonalen. Der trengs et forenklet symbol (åpent punkt).}
```

:::

::: {.page section="Logo" title="Bakgrunner: navnetrekk" lead="Navnetrekket skal ha minst 3:1 kontrast mot bakgrunnen. Tallene er beregnet etter WCAG 2.x."}

```{=latex}
\kwtileok{16}{50}{40.83}{38}{kwwhite}{kwhair}{kw-wordmark-black.pdf}{28}{\color{kwmuted}\shortstack[l]{Svart på hvit\\21,00:1}}
\kwtileok{60.83}{50}{40.83}{38}{kwgrey}{none}{kw-wordmark-black.pdf}{28}{\color{kwmuted}\shortstack[l]{Svart på grå\\17,00:1}}
\kwtileok{105.67}{50}{40.83}{38}{kwgreen}{none}{kw-wordmark-black.pdf}{28}{\color{kwblack}\shortstack[l]{Svart på grønn\\17,79:1}}
\kwtileok{150.5}{50}{40.83}{38}{kwblack}{none}{kw-wordmark-white.pdf}{28}{\color{kwgrey}\shortstack[l]{Hvit på svart\\21,00:1}}
\kwtileok{195.33}{50}{40.83}{38}{kwdarkgreen}{none}{kw-wordmark-white.pdf}{28}{\color{kwwhite}\shortstack[l]{Hvit på mørkegrønn\\6,65:1}}
\kwtileok{240.17}{50}{40.83}{38}{kwpink}{none}{kw-wordmark-black.pdf}{28}{\color{kwblack}\shortstack[l]{Svart på rosa\\15,54:1}}
\kwtileno{16}{93}{40.83}{38}{kwwhite}{kwhair}{kw-wordmark-green.pdf}{28}{\color{kwmuted}\shortstack[l]{Grønn på hvit\\1,18:1}}
\kwtileno{60.83}{93}{40.83}{38}{kwgrey}{none}{kw-wordmark-green.pdf}{28}{\color{kwmuted}\shortstack[l]{Grønn på grå\\1,05:1}}
\kwtileno{105.67}{93}{40.83}{38}{kwgrey}{none}{kw-wordmark-white.pdf}{28}{\color{kwmuted}\shortstack[l]{Hvit på grå\\1,23:1}}
\kwtileno{150.5}{93}{40.83}{38}{kwgreen}{none}{kw-wordmark-white.pdf}{28}{\color{kwblack}\shortstack[l]{Hvit på grønn\\1,18:1}}
\kwtileno{195.33}{93}{40.83}{38}{kwpink}{none}{kw-wordmark-white.pdf}{28}{\color{kwblack}\shortstack[l]{Hvit på rosa\\1,35:1}}
\kwtileno{240.17}{93}{40.83}{38}{kwdeepgreen}{none}{kw-wordmark-black.pdf}{28}{\color{kwgrey}\shortstack[l]{Svart på dypgrønn\\1,93:1}}
\kwatw{16}{134}{265}{\kwsize{8}{11}\kwregular\color{kwmuted}Grønt navnetrekk brukes bare på svart, dypgrønn eller mørkegrønn flate. På foto: svart eller hvitt navnetrekk, bare over rolig og jevn flate.}
```

:::

::: {.page section="Logo" title="Bakgrunner: symbol" lead="Symbolet bærer informasjon i den tynne diagonalen. Det skal ha minst 3:1 kontrast mot bakgrunnen, også i den grønne streken."}

```{=latex}
\kwtileok{16}{50}{40.83}{38}{kwwhite}{kwhair}{kw-symbol-black.pdf}{11}{\color{kwmuted}\shortstack[l]{Svart på hvit\\21,00:1}}
\kwtileok{60.83}{50}{40.83}{38}{kwgrey}{none}{kw-symbol-black.pdf}{11}{\color{kwmuted}\shortstack[l]{Svart på grå\\17,00:1}}
\kwtileok{105.67}{50}{40.83}{38}{kwgreen}{none}{kw-symbol-black.pdf}{11}{\color{kwblack}\shortstack[l]{Svart på grønn\\17,79:1}}
\kwtileok{150.5}{50}{40.83}{38}{kwblack}{none}{kw-symbol-green.pdf}{11}{\color{kwgrey}\shortstack[l]{Grønn på svart\\17,79:1}}
\kwtileok{195.33}{50}{40.83}{38}{kwblack}{none}{kw-symbol-white-with-green-stroke.pdf}{11}{\color{kwgrey}\shortstack[l]{Hvit, grønn strek\\på svart, 21,00:1}}
\kwtileok{240.17}{50}{40.83}{38}{kwdeepgreen}{none}{kw-symbol-white.pdf}{11}{\color{kwwhite}\shortstack[l]{Hvit på dypgrønn\\10,88:1}}
\kwtileno{16}{93}{40.83}{38}{kwwhite}{kwhair}{kw-symbol-green.pdf}{11}{\color{kwmuted}\shortstack[l]{Grønn på hvit\\1,18:1}}
\kwtileno{60.83}{93}{40.83}{38}{kwgrey}{none}{kw-symbol-green.pdf}{11}{\color{kwmuted}\shortstack[l]{Grønn på grå\\1,05:1}}
\kwtileno{105.67}{93}{40.83}{38}{kwgrey}{none}{kw-symbol-white.pdf}{11}{\color{kwmuted}\shortstack[l]{Hvit på grå\\1,23:1}}
\kwtileno{150.5}{93}{40.83}{38}{kwgreen}{none}{kw-symbol-white.pdf}{11}{\color{kwblack}\shortstack[l]{Hvit på grønn\\1,18:1}}
\kwtileno{195.33}{93}{40.83}{38}{kwpink}{none}{kw-symbol-white.pdf}{11}{\color{kwblack}\shortstack[l]{Hvit på rosa\\1,35:1}}
\kwtileno{240.17}{93}{40.83}{38}{kwdeepgreen}{none}{kw-symbol-black.pdf}{11}{\color{kwgrey}\shortstack[l]{Svart på dypgrønn\\1,93:1}}
\kwatw{16}{134}{265}{\kwsize{8}{11}\kwregular\color{kwmuted}Det grønne symbolet brukes bare på svart, dypgrønn eller mørkegrønn flate. Åpent punkt: under 80 px høyde (favicon, app-ikon) trengs et forenklet symbol uten tynne streker.}
```

:::

::: {.page section="Logo" title="Feil bruk" lead="Logoen tegnes aldri om og settes aldri selv. Bruk alltid de ferdige filene."}

```{=latex}
% tiles: x = 16, 83.5, 151, 218.5 ; rows y = 50, 94 ; size 62.5 x 40
\kwcell{16}{50}{62.5}{40}{kwwhite}{kwhair}{\color{kwmuted}Strekking eller press}
\kwatc{47.25}{68}{\includegraphics[width=40mm,height=10mm]{\kwimgdir/kw-wordmark-black.pdf}}
\kwmark{no}{16}{50}
\kwcell{83.5}{50}{62.5}{40}{kwwhite}{kwhair}{\color{kwmuted}Skråstilling}
\kwatco{114.75}{68}{xslant=0.45,transform shape}{\includegraphics[width=36mm]{\kwimgdir/kw-wordmark-black.pdf}}
\kwmark{no}{83.5}{50}
\kwcell{151}{50}{62.5}{40}{kwgrey}{none}{\color{kwmuted}Kontur}
\kwdraw{\foreach \a in {0,30,...,330}{\node[inner sep=0pt] at \kwoo{182.25}{68}{0.05*cos(\a)}{0.05*sin(\a)} {\includegraphics[width=36mm]{\kwimgdir/kw-wordmark-black.pdf}};}
  \node[inner sep=0pt] at \kwo{182.25}{68} {\includegraphics[width=36mm]{\kwimgdir/kw-wordmark-white.pdf}};}
\kwmark{no}{151}{50}
\kwcell{218.5}{50}{62.5}{40}{kwwhite}{kwhair}{\color{kwmuted}Skygge}
\kwatc{250.4}{68.9}{\includegraphics[width=36mm]{\kwimgdir/x-wordmark-shadow.pdf}}
\kwatc{249.75}{68}{\includegraphics[width=36mm]{\kwimgdir/kw-wordmark-black.pdf}}
\kwmark{no}{218.5}{50}
\kwcell{16}{94}{62.5}{40}{kwwhite}{kwhair}{\color{kwmuted}Annen farge enn svart, hvit eller grønn}
\kwatc{47.25}{112}{\includegraphics[width=36mm]{\kwimgdir/x-wordmark-darkgreen.pdf}}
\kwmark{no}{16}{94}
\kwpanel{83.5}{94}{62.5}{40}{kwblack}{fifth-element-green.pdf}{93.5}{86}{42}
\kwcell{83.5}{94}{62.5}{40}{none}{none}{\colorbox{kwblack}{\color{kwgrey}Seismograf gjennom navnetrekket}}
\kwatc{114.75}{112}{\includegraphics[width=36mm]{\kwimgdir/kw-wordmark-white.pdf}}
\kwmark{no}{83.5}{94}
\kwcell{151}{94}{62.5}{40}{kwwhite}{kwhair}{\color{kwmuted}Satt som tekst i fonten}
\kwatc{182.25}{112}{\kwsize{26}{28}\kwbold KodeWorks}
\kwmark{no}{151}{94}
\kwcell{218.5}{94}{62.5}{40}{kwgrey}{none}{\color{kwmuted}Symbolet som dekormønster}
\kwdraw{\foreach \i in {0,...,5}{\foreach \j in {0,1}{\node[inner sep=0pt] at \kwoo{228}{104}{1.0*\i}{-1.35*\j} {\includegraphics[width=5mm]{\kwimgdir/kw-symbol-black.pdf}};}}}
\kwmark{no}{218.5}{94}
```

:::


::: {.divider number="03" title="Farger" text="Grønn og grå er hovedfarger. Svart og hvit gir ro. De mørke grønntonene og rosa støtter. Her er verdiene, rollene og reglene for kontrast."}
:::

::: {.page section="Farger" title="Paletten" lead="Sju farger. Grønn og grå er hovedfarger, svart og hvit gir ro. Mørkegrønn, dypgrønn og rosa er støttefarger."}

```{=latex}
% Local component: swatch with role text. \kwswr{x}{y}{w}{colour}{name}{HEX}{RGB}{CMYK}{PMS}{role}
\providecommand{\kwswr}[8]{%
  \kwdraw{\fill[fill=#2,draw=kwhair,line width=0.4pt] \kwo{#1}{47} rectangle ++(33mm,-34mm);}%
  \kwatw{#1}{84}{33}{{\kwsize{9.5}{12}\kwmedium \vphantom{Åg}#3}\par\vspace{1.2mm}%
    {\kwsize{7}{9.5}\kwlight\setlength{\tabcolsep}{0pt}\renewcommand{\arraystretch}{1.2}%
    \begin{tabular}{@{}>{\kwregular\color{kwmuted}}l@{\hspace{3mm}}l@{}}%
      HEX & \##4\\ RGB & #5\\ CMYK & #6\\ PMS & #7\end{tabular}}}%
  \kwatw{#1}{111}{33}{\kwsize{7.5}{10}\kwregular #8}}
\kwswr{16}{kwgreen}{Grønn}{B6FF9E}{182, 255, 158}{31, 0, 40, 0}{2267 C / U}{Aksent og profilflate. Hovedfarge.}
\kwswr{54.67}{kwgrey}{Grå}{E8E7E6}{232, 231, 230}{8, 6, 7, 0}{179-2 C / U\,\textsuperscript{a}}{Standard sekundærflate. Hovedfarge.}
\kwswr{93.33}{kwblack}{Svart}{000000}{0, 0, 0}{0, 0, 0, 100\,*}{Black C\,*}{Tekst, logo og mørk flate.}
\kwswr{132}{kwwhite}{Hvit}{FFFFFF}{255, 255, 255}{0, 0, 0, 0}{Papir}{Grunnflate og tekst på mørkt.}
\kwswr{170.67}{kwdarkgreen}{Mørkegrønn}{35664C}{53, 102, 76}{80, 30, 70, 40\,*}{ca. 7729 C\,*}{Interaktive elementer og utheving i titler.}
\kwswr{209.33}{kwdeepgreen}{Dypgrønn}{254333}{37, 67, 51}{85, 45, 75, 65\,*}{ca. 3435 C\,*}{Mørk flate: skillesider og mørke seksjoner. Ikke tekstfarge.}
\kwswr{248}{kwpink}{Rosa}{FAD5D5}{250, 213, 213}{0, 15, 10, 0\,*}{ca. 706 C\,*}{Støtteflate i liten dose.}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{16}{128} -- ++(265mm,0);}
\kwatw{16}{131}{150}{\kwsize{7.5}{10.5}\kwmedium * Forslag.\kwregular\ CMYK og PMS er ikke verifisert og må kontrolleres av trykkeri før bruk i trykk.\par
  \kwsize{7.5}{10.5}\kwregular \textsuperscript{a} PMS-navnet er hentet fra 2021-manualen og må kontrolleres.}
\kwatw{175}{131}{106}{\kwsize{7.5}{10.5}\kwmedium Mørkegrå \#666666\kwregular\ (RGB 102, 102, 102) brukes til sekundærtekst. Teknisk farge, ikke del av profilpaletten.}
```

:::

::: {.page section="Farger" title="Roller og fordeling" lead="Hver farge har én rolle. Fordelingen under er veiledende."}

```{=latex}
% Local component: role demo tile. \kwrole{x}{colour}{title}{rule}
\providecommand{\kwrole}[4]{\kwatw{#1}{47}{41}{\kwsize{9}{11}\kwmedium #3}%
  \kwatw{#1}{78}{41}{\kwsize{7.5}{10}\kwregular #4}}
\kwrole{16}{}{Tekst}{Svart på hvit, grå, grønn og rosa. Mørkegrå til sekundærtekst.}
\kwdraw{\fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{16}{53} rectangle ++(41mm,-22mm);}
\kwat{19}{55}{\kwsize{20}{22}\kwlight Aa}
\kwat{19}{70}{\kwsize{7.5}{9}\kwregular\color{kwmuted}Sekundærtekst \#666}
\kwrole{60.8}{}{Bakgrunn}{Hvit er grunnflate. Grå er sekundærflate for kort og felt.}
\kwdraw{\fill[kwgrey] \kwo{60.8}{53} rectangle ++(41mm,-22mm);}
\kwat{64}{56}{\kwsize{11}{13}\kwlight Kort på grå flate}
\kwrole{105.6}{}{Aksent}{Grønn som understrek, markering og symbol på mørk flate. Aldri som tekst på lys bakgrunn.}
\kwdraw{\fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{105.6}{53} rectangle ++(41mm,-22mm);}
\kwat{109}{58}{\kwsize{11}{13}\kwlight Les mer}
\kwrect{109}{65}{17.5}{1.4}{kwgreen}
\kwrole{150.4}{}{Interaktiv}{Mørkegrønn til knapper og tekstutheving. Hvit tekst i knapp.}
\kwdraw{\fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{150.4}{53} rectangle ++(41mm,-22mm);}
\kwrect{154}{58}{33}{9}{kwdarkgreen}
\kwat{157}{60.3}{\kwsize{9.5}{11}\kwregular\color{kwwhite}Kontakt oss}
\kwat{154}{70}{\kwsize{11}{13}\kwlight\color{kwdarkgreen}Våre \color{kwblack}utviklere}
\kwrole{195.2}{}{Mørk flate}{Dypgrønn for skillesider og mørke seksjoner. Hvit eller grønn tekst.}
\kwdraw{\fill[kwdeepgreen] \kwo{195.2}{53} rectangle ++(41mm,-22mm);}
\kwat{198}{57}{\kwsize{11}{13}\kwlight\color{kwwhite}Skilleside}
\kwrect{198}{66}{10}{1.2}{kwgreen}
\kwrole{240}{}{Støtte}{Rosa som bakgrunn for enkeltflater. Høyst én per side.}
\kwdraw{\fill[kwpink] \kwo{240}{53} rectangle ++(41mm,-22mm);}
\kwat{243}{56}{\kwsize{11}{13}\kwlight Kunder}
% Proportion bars
\kwatw{16}{101}{265}{\kwsize{9}{11}\kwmedium Veiledende fordeling\kwregular\ (forslag, justeres ved første trykksak)}
% digital bar y=108, x=16, total width 265 mm: 55/15/10/8/5/4/3
\kwat{16}{111}{\kwsize{7.5}{9}\kwregular\color{kwmuted}DIGITALT}
\kwrect{16}{115}{145.75}{9}{kwwhite}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{16}{115} rectangle ++(265mm,-9mm);}
\kwrect{161.75}{115}{39.75}{9}{kwgrey}
\kwrect{201.5}{115}{26.5}{9}{kwblack}
\kwrect{228}{115}{21.2}{9}{kwgreen}
\kwrect{249.2}{115}{13.25}{9}{kwdarkgreen}
\kwrect{262.45}{115}{10.6}{9}{kwdeepgreen}
\kwrect{273.05}{115}{7.95}{9}{kwpink}
\kwat{18}{117.4}{\kwsize{7.5}{9}\kwregular Hvit 55}
\kwat{163.5}{117.4}{\kwsize{7.5}{9}\kwregular Grå 15}
\kwat{203}{117.4}{\kwsize{7.5}{9}\kwregular\color{kwwhite}Svart 10}
\kwat{230}{117.4}{\kwsize{7.5}{9}\kwregular Grønn 8}
\kwat{251}{117.4}{\kwsize{7.5}{9}\kwregular\color{kwwhite}5}
\kwat{265}{117.4}{\kwsize{7.5}{9}\kwregular\color{kwwhite}4}
\kwat{275}{117.4}{\kwsize{7.5}{9}\kwregular 3}
\kwatw{16}{140}{265}{\kwsize{7}{9}\kwregular\color{kwmuted}Digitalt: 5 = mørkegrønn, 4 = dypgrønn, 3 = rosa. Trykk: 5 = dypgrønn, 2 = mørkegrønn, 1 = rosa.}
% print bar y=131: grey 40 / white 25 / black 15 / green 12 / deep 5 / dark 2 / pink 1
\kwat{16}{125}{\kwsize{7.5}{9}\kwregular\color{kwmuted}TRYKK OG PROFILERTE FLATER}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{16}{129} rectangle ++(265mm,-9mm);}
\kwrect{16}{129}{106}{9}{kwgrey}
\kwrect{122}{129}{66.25}{9}{kwwhite}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{122}{129} rectangle ++(66.25mm,-9mm);}
\kwrect{188.25}{129}{39.75}{9}{kwblack}
\kwrect{228}{129}{31.8}{9}{kwgreen}
\kwrect{259.8}{129}{13.25}{9}{kwdeepgreen}
\kwrect{273.05}{129}{5.3}{9}{kwdarkgreen}
\kwrect{278.35}{129}{2.65}{9}{kwpink}
\kwat{18}{131.4}{\kwsize{7.5}{9}\kwregular Grå 40}
\kwat{124}{131.4}{\kwsize{7.5}{9}\kwregular Hvit 25}
\kwat{190}{131.4}{\kwsize{7.5}{9}\kwregular\color{kwwhite}Svart 15}
\kwat{230}{131.4}{\kwsize{7.5}{9}\kwregular Grønn 12}
\kwat{262}{131.4}{\kwsize{7.5}{9}\kwregular\color{kwwhite}5}
```

:::

::: {.page section="Farger" title="Kontrast" lead="Beregnet etter WCAG 2.x. Forholdet er det samme uansett hvilken farge som er tekst. Brødtekst krever minst 4,5:1, stor tekst minst 3:1."}

```{=latex}
% Local component: contrast chip. \kwchipM{x}{y}{background}{text colour}{ratio}{caption}
\providecommand{\kwchipM}[6]{\kwdraw{%
  \fill[fill=#3,draw=kwhair,line width=0.4pt] \kwo{#1}{#2} rectangle ++(40mm,-9mm);
  \node[anchor=north west,inner sep=0pt,text=#4] at ($(current page.north west)+(#1mm+2mm,-#2mm-1.5mm)$) {\kwsize{12}{14}\kwlight Aa};
  \node[anchor=north west,inner sep=0pt,text=#4] at ($(current page.north west)+(#1mm+14mm,-#2mm-3mm)$) {\kwsize{8}{10}\kwmedium #5:1};
  \node[anchor=north west,inner sep=0pt,text=kwmuted] at ($(current page.north west)+(#1mm,-#2mm-9.8mm)$) {\kwsize{6.5}{8}\kwregular #6};}}
\definecolor{kwmid}{HTML}{666666}
\kwat{16}{46}{\kwsize{9}{11}\kwmedium Tillatt til brødtekst\kwregular\ (minst 4,5:1)}
\kwchipM{16}{53}{kwwhite}{kwblack}{21,00}{Svart på hvit}
\kwchipM{58.7}{53}{kwgreen}{kwblack}{17,79}{Svart på grønn}
\kwchipM{101.4}{53}{kwgrey}{kwblack}{17,00}{Svart på grå}
\kwchipM{144.1}{53}{kwpink}{kwblack}{15,54}{Svart på rosa}
\kwchipM{16}{69}{kwdeepgreen}{kwwhite}{10,88}{Hvit på dypgrønn}
\kwchipM{58.7}{69}{kwdeepgreen}{kwgreen}{9,22}{Grønn på dypgrønn}
\kwchipM{101.4}{69}{kwdeepgreen}{kwgrey}{8,81}{Grå på dypgrønn}
\kwchipM{144.1}{69}{kwpink}{kwdeepgreen}{8,06}{Dypgrønn på rosa}
\kwchipM{16}{85}{kwdarkgreen}{kwwhite}{6,65}{Hvit på mørkegrønn}
\kwchipM{58.7}{85}{kwwhite}{kwmid}{5,74}{Mørkegrå på hvit}
\kwchipM{101.4}{85}{kwdarkgreen}{kwgreen}{5,64}{Grønn på mørkegrønn og omvendt}
\kwchipM{144.1}{85}{kwdarkgreen}{kwgrey}{5,39}{Grå på mørkegrønn}
\kwchipM{16}{101}{kwpink}{kwdarkgreen}{4,92}{Mørkegrønn på rosa}
\kwchipM{58.7}{101}{kwgreen}{kwmid}{4,86}{Mørkegrå på grønn}
\kwchipM{101.4}{101}{kwgrey}{kwmid}{4,65}{Mørkegrå på grå, ikke under 12 pt}
\kwat{204}{46}{\kwsize{9}{11}\kwmedium Kun stor tekst\kwregular\ (3 til 4,5:1)}
\kwchipM{204}{53}{kwpink}{kwmid}{4,25}{Mørkegrå på rosa}
\kwchipM{204}{69}{kwblack}{kwmid}{3,66}{Mørkegrå på svart}
\kwchipM{204}{85}{kwdarkgreen}{kwblack}{3,16}{Svart på mørkegrønn}
\kwatw{204}{100}{77}{\kwsize{7.5}{10}\kwregular Grønn brukes som flate bak svart tekst, ikke som tekst på lys bakgrunn. Mørkegrå brukes ikke under 12 pt på grå flate.}
\kwat{16}{116}{\kwsize{9}{11}\kwmedium Forbudt\kwregular\ (under 3:1)}
\kwchipM{16}{123}{kwwhite}{kwgreen}{1,18}{1,18:1 Grønn på hvit. Vanligste feil}
\kwchipM{60}{123}{kwgrey}{kwgreen}{1,05}{1,05:1 Grønn på grå}
\kwchipM{104}{123}{kwwhite}{kwgrey}{1,23}{1,23:1 Grå på hvit}
\kwchipM{148}{123}{kwpink}{kwwhite}{1,35}{1,35:1 Hvit på rosa}
\kwchipM{192}{123}{kwdeepgreen}{kwdarkgreen}{1,64}{1,64:1 Mørkegrønn på dypgrønn}
\kwchipM{236}{123}{kwdeepgreen}{kwblack}{1,93}{1,93:1 Svart på dypgrønn}
```

:::

::: {.page section="Farger" title="Farger i trykk og på skjerm" lead="Samme farge gjengis ulikt på skjerm, papir, tekstil og skilt. Bruk de oppgitte verdiene for hvert medium."}

```{=latex}
\kwat{16}{47}{\kwsize{9}{12}\kwlight\setlength{\tabcolsep}{0pt}\renewcommand{\arraystretch}{1}%
\providecommand{\kwhl}{\noalign{{\color{kwhair}\hrule height 0.4pt}}}%
\begin{tabular}{@{}>{\kwmedium}p{39mm}@{\hspace{3mm}}>{\kwregular}p{27mm}@{\hspace{3mm}}>{\kwregular}p{80mm}@{}}
\kwsize{7}{9}\kwregular\color{kwmuted}MEDIUM & \kwsize{7}{9}\kwregular\color{kwmuted}FARGEMODELL & \kwsize{7}{9}\kwregular\color{kwmuted}REGEL\\[1.5mm]\kwhl\noalign{\vspace{3.6mm}}
Skjerm, nett og Office & RGB / HEX & Bruk HEX-verdiene i paletten. Grønn er \#B6FF9E, ikke en nærliggende lysgrønn\\[3.6mm]\kwhl\noalign{\vspace{3.6mm}}
Trykk i fire farger & CMYK & Bruk CMYK-verdiene i paletten. Grønn er 31, 0, 40, 0. Ikke la tekstbehandleren regne om fra RGB\\[3.6mm]\kwhl\noalign{\vspace{3.6mm}}
Trykk med spesialfarge & PMS & Grønn trykkes med PMS 2267 (neon) på store flater, skilt og tekstil der den skal lyse\\[3.6mm]\kwhl\noalign{\vspace{3.6mm}}
Tekst i trykk & 100 \% svart (K) & Svart tekst settes i ren K, ikke i fire farger, så små tegn ikke får fargekanter\\[3.6mm]\kwhl\noalign{\vspace{3.6mm}}
Skilt, tekstil og interiør & Prøve på materialet & Lag prøve før produksjon. Grønnfargen varierer en del mellom flater
\end{tabular}}
% Same green, three models
\kwatw{175}{47}{106}{\kwsize{7}{9}\kwregular\color{kwmuted}SAMME GRØNN I TRE MODELLER}
\kwdraw{\fill[kwgreen] \kwo{175}{52} rectangle ++(33mm,-30mm);\fill[kwgreen] \kwo{211.5}{52} rectangle ++(33mm,-30mm);\fill[kwgreen] \kwo{248}{52} rectangle ++(33mm,-30mm);}
\kwatw{175}{83}{33}{\kwsize{8}{10.5}\kwmedium RGB\par\kwregular 182, 255, 158\par\kwregular\color{kwmuted}Skjerm}
\kwatw{211.5}{83}{33}{\kwsize{8}{10.5}\kwmedium CMYK\par\kwregular 31, 0, 40, 0\par\kwregular\color{kwmuted}Fire farger}
\kwatw{248}{83}{33}{\kwsize{8}{10.5}\kwmedium PMS\par\kwregular 2267 C / U\par\kwregular\color{kwmuted}Spesialfarge}
\kwatw{175}{104}{106}{\kwsize{7.5}{10.5}\kwregular Alle tre er gjengitt her på skjerm. På papir og tekstil blir resultatet mer eller mindre intenst. Det er derfor prøve er påkrevd.}
\kwatw{16}{128}{265}{\kwsize{7.5}{10.5}\kwregular\color{kwmuted}CMYK- og PMS-verdier for mørkegrønn, dypgrønn, rosa, svart og mørkegrå er forslag som må kontrolleres av trykkeri.}
```

:::


::: {.divider number="04" title="Typografi" text="Profilfonten er Non Natural Grotesk. Her står vektene, størrelsene og reglene for utheving og fallback."}
:::

```{=latex}
% Lokale komponenter (delt mellom seksjonsfilene; providecommand gjør dem trygge å definere flere ganger)
\providecommand{\kwchip}[5]{\kwdraw{\node[anchor=north west,inner xsep=1.6mm,inner ysep=0.9mm,fill=#4,text=#5] at \kwo{#1}{#2} {\kwsize{6.5}{8}\kwmedium #3};}}
\providecommand{\kwline}[4]{\kwrect{#1}{#2}{#3}{0.3}{#4}}
\providecommand{\kwlabel}[3]{\kwat{#1}{#2}{\kwsize{6.5}{8}\kwregular\color{kwmuted}#3}}
% Arial is neither in the repo nor in TeX Live. TeX Gyre Heros (TeX Live) has the same advance widths and stands in for it.
\newfontfamily\kwarial{texgyreheros-regular.otf}
```

::: {.page section="Typografi" title="Profilfonten og vektene" lead="Non Natural Grotesk er profilfonten. Tre vekter brukes: Light, Regular og Medium. Thin og Bold finnes i fontpakken, men brukes ikke."}

```{=latex}
\kwat{16}{46}{\kwsize{120}{120}\kwlight Aa}
\kwatw{16}{99}{108}{\kwsize{10.5}{15}\kwlight ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ\\abcdefghijklmnopqrstuvwxyzæøå\\0123456789 (.,:;!?«»–)}
\kwatw{16}{123}{108}{\kwsize{8.5}{12}\kwregular Fontfamilien heter Non Natural Grotesk (Non Foundry). Nettsiden og enkelte systemer viser den som «Natural Grotesk». Det er samme font.}
% weight table
\kwline{135}{47.5}{146}{kwhair}
\kwat{135}{51}{\kwsize{20}{22}\kwlight Light}
\kwchip{185}{51}{BRUKES}{kwgreen}{kwblack}
\kwatw{185}{57}{96}{\kwsize{8.5}{11}\kwregular Titler, ingress og store tekster (14 pt / 20 px og større).}
\kwline{135}{64.5}{146}{kwhair}
\kwat{135}{68}{\kwsize{20}{22}\kwregular Regular}
\kwchip{185}{68}{BRUKES}{kwgreen}{kwblack}
\kwatw{185}{74}{96}{\kwsize{8.5}{11}\kwregular Brødtekst og liten tekst (bildetekst, tabeller, juridisk tekst).}
\kwline{135}{81.5}{146}{kwhair}
\kwat{135}{85}{\kwsize{20}{22}\kwmedium Medium}
\kwchip{185}{85}{BRUKES}{kwgreen}{kwblack}
\kwatw{185}{91}{96}{\kwsize{8.5}{11}\kwregular Utheving i løpende tekst og mellomtitler i liten størrelse.}
\kwline{135}{98.5}{146}{kwhair}
\kwat{135}{102}{\kwsize{20}{22}\kwthin\color{kwmuted}Thin}
\kwchip{185}{102}{BRUKES IKKE}{kwgrey}{kwblack}
\kwatw{185}{108}{96}{\kwsize{8.5}{11}\kwregular Finnes i fontpakken. Bare lesbar i svært store størrelser.}
\kwline{135}{115.5}{146}{kwhair}
\kwat{135}{119}{\kwsize{20}{22}\kwbold\color{kwmuted}Bold}
\kwchip{185}{119}{BRUKES IKKE}{kwgrey}{kwblack}
\kwatw{185}{125}{96}{\kwsize{8.5}{11}\kwregular Finnes i fontpakken. Passer ikke til et uttrykk bygget på lette titler.}
\kwline{135}{132.5}{146}{kwhair}
\kwatw{135}{135}{146}{\kwsize{10.5}{14}\kwregular Eksempel på utheving i løpende tekst: Frist for innsending er {\kwmedium 15. mars}.}
```

:::

::: {.page section="Typografi" title="Hierarki" lead="Samme struktur på skjerm og på trykk. Eksemplene står i faktisk størrelse: digitalt er 1 px vist som 0,75 pt, trykk er i punkt."}

```{=latex}
\kwat{16}{46}{\kwsize{9.5}{12}\kwmedium Digitalt (px)}
\kwat{151}{46}{\kwsize{9.5}{12}\kwmedium Trykk, A4 (pt)}
\kwline{16}{51}{130}{kwhair}
\kwline{151}{51}{130}{kwhair}
% Row 1: titles
\kwlabel{16}{53}{TITTEL (H1, H2) | LIGHT | 48 PX, LINJEAVSTAND 1,0}
\kwat{16}{57}{\kwsize{36}{36}\kwlight Digitale løsninger}
\kwlabel{151}{53}{H1 32–40 PT | H2 24–28 PT | LIGHT | LINJEAVSTAND 1,0–1,15}
\kwat{151}{57}{\kwsize{32}{34}\kwlight Digitale løsninger}
% Row 2: H3
\kwlabel{16}{73}{UNDERTITTEL (H3) | LIGHT | 30 PX, LINJEAVSTAND 1,15}
\kwat{16}{77}{\kwsize{22.5}{26}\kwlight Utvikling, team og AI}
\kwlabel{151}{73}{H3 | LIGHT | 16–18 PT}
\kwat{151}{77}{\kwsize{17}{20}\kwlight Utvikling, team og AI}
% Row 3: lead
\kwlabel{16}{88}{INGRESS | LIGHT | 20 PX, LINJEAVSTAND 1,6}
\kwat{16}{92}{\kwsize{15}{24}\kwlight Vi bygger systemer som varer.}
\kwlabel{151}{88}{INGRESS | LIGHT | 12–14 PT, LINJEAVSTAND 1,6}
\kwat{151}{92}{\kwsize{13}{20.8}\kwlight Vi bygger systemer som varer.}
% Row 4: body
\kwlabel{16}{103}{BRØDTEKST | REGULAR | 16–18 PX, LINJEAVSTAND 1,4}
\kwat{16}{107}{\kwsize{13.5}{18.9}\kwregular Teksten settes venstrejustert, med god luft.}
\kwlabel{151}{103}{BRØDTEKST | REGULAR | 9,5–10,5 PT, LINJEAVSTAND 1,4}
\kwat{151}{107}{\kwsize{10.5}{14.7}\kwregular Teksten settes venstrejustert, med god luft.}
% Row 5: small
\kwlabel{16}{116}{LITEN TEKST | REGULAR | 14 PX}
\kwat{16}{120}{\kwsize{10.5}{14.7}\kwregular Bildetekst, tabell, juridisk tekst og metadata}
\kwlabel{151}{116}{LITEN TEKST | REGULAR | 8–9 PT}
\kwat{151}{120}{\kwsize{8.5}{12}\kwregular Bildetekst, tabell, juridisk tekst og metadata}
% Row 6: buttons / labels
\kwlabel{16}{129}{KNAPP, ETIKETT, NAVIGASJON | REGULAR ELLER MEDIUM | 16–20 PX}
\kwdraw{\fill[fill=kwdarkgreen] \kwo{16}{133} rectangle ++(40mm,-9mm);}
\kwat{20}{135.7}{\kwsize{12}{14}\kwregular\color{kwwhite}Kontakt oss}
\kwlabel{151}{129}{ETIKETT, NAVIGASJON | REGULAR ELLER MEDIUM | 9–10 PT}
\kwat{151}{133.5}{\kwsize{9.5}{12}\kwmedium Seksjon 04}
\kwat{185}{133.5}{\kwsize{9.5}{12}\kwregular Typografi}
```

:::

::: {.page section="Typografi" title="Fallback og lisens" lead="Fonten kan bare bygges inn i PDF, PS og EPS. Derfor lages KodeWorks' materiale som PDF med fonten innebygd."}

```{=latex}
\kwat{16}{46}{\kwsize{9.5}{12}\kwmedium Samme tekst i profilfont og fallback}
\kwline{16}{51}{125}{kwhair}
\kwlabel{16}{53}{NON NATURAL GROTESK LIGHT | MALENE, BYGGET TIL PDF}
\kwat{16}{57}{\kwsize{24}{28}\kwlight Dine ideer, våre utviklere}
\kwlabel{16}{71}{ARIAL | OFFICE OG GOOGLE UTEN PROFILFONTEN | VIST MED TEX GYRE HEROS, SAMME TEGNBREDDER}
\kwat{16}{75}{\kwsize{24}{28}\kwarial Dine ideer, våre utviklere}
\kwatw{16}{91}{125}{\kwsize{10.5}{14.5}\kwregular{\kwmedium Regel for materiale.} CV, presentasjon, dokument og brev skrives i Markdown og bygges til PDF med KodeWorks' byggeverktøy. Det henter fonten fra den lisensierte fontfila, så resultatet blir likt på alle maskiner, uten installert font.}
\kwatw{16}{113}{125}{\kwsize{10.5}{14.5}\kwregular{\kwmedium Office og Google.} Uten profilfonten vises Arial, som er riktig reserve. Det som sendes ut i KodeWorks' navn, lages fra malene.}
% right side: licence
\kwat{151}{46}{\kwsize{9.5}{12}\kwmedium Lisensen i korte trekk}
\kwline{151}{51}{130}{kwhair}
\kwlabel{151}{53}{FONTEN KAN BYGGES INN I}
\kwchip{151}{57.5}{PDF}{kwgreen}{kwblack}
\kwchip{164}{57.5}{EPS}{kwgreen}{kwblack}
\kwchip{177}{57.5}{PS}{kwgreen}{kwblack}
\kwlabel{151}{69}{FONTEN KAN IKKE BYGGES INN I}
\kwchip{151}{73.5}{DOCX}{kwgrey}{kwblack}
\kwchip{167}{73.5}{PPTX}{kwgrey}{kwblack}
\kwchip{183}{73.5}{XLSX}{kwgrey}{kwblack}
\kwchip{199}{73.5}{MALER OG LOGOFILER}{kwgrey}{kwblack}
\kwlabel{151}{85}{FONTEN KAN IKKE}
\kwatw{151}{89}{130}{\kwsize{9.5}{13}\kwregular
 {\kwmedium Tegne logo.} Navnetrekket leveres som ferdig tegnet vektorfil, ikke som tekst i fonten.\par\vspace{1.5mm}
 {\kwmedium Gjøres om til webfont.} Ingen WOFF, WOFF2, EOT eller TTF-konvertering.\par\vspace{1.5mm}
 {\kwmedium Deles videre.} Lisensen er personlig for selskapet som har kjøpt den.}
\kwimg{151}{125}{40}{kw-wordmark-black.pdf}
\kwat{196}{125.5}{\kwsize{7}{9}\kwregular\color{kwmuted}Ferdig tegnet navnetrekk (vektor)}
```

:::

::: {.page section="Typografi" title="Utheving i titler" lead="Ord i titler uthevet med farge, ikke med vekt. Fargen er mørkegrønn #35664C."}

```{=latex}
\kwat{16}{46}{\kwsize{9.5}{12}\kwmedium Slik gjør vi det}
\kwline{16}{51}{140}{kwhair}
\kwat{16}{54}{\kwsize{48}{48}\kwlight Dine \color{kwdarkgreen}ideer}
\kwat{16}{68}{\kwsize{48}{48}\kwlight \color{kwdarkgreen}Våre \color{kwblack}utviklere}
\kwat{16}{93}{\kwsize{7}{9}\kwregular\color{kwmuted}LIGHT 48 PX (36 PT) | UTHEVING I \#35664C | KONTRAST MOT HVIT 6,65:1}
\kwatw{16}{100}{140}{\kwsize{10.5}{14.5}\kwregular Ett eller to ord per tittel. Resten av tittelen står i svart. Vekten er den samme i hele tittelen.}
% dark surface
\kwrect{16}{115}{140}{30}{kwdeepgreen}
\kwat{21}{119}{\kwsize{24}{26}\kwlight\color{kwwhite} Dine \color{kwgreen}ideer\color{kwwhite}, våre utviklere}
\kwatw{21}{134}{130}{\kwsize{7}{9}\kwregular\color{kwgreen}PÅ MØRK FLATE (\#254333): UTHEVING I LYSEGRØNN \#B6FF9E, KONTRAST 9,22:1}
% don'ts
\kwat{171}{46}{\kwsize{9.5}{12}\kwmedium Slik gjør vi det ikke}
\kwline{171}{51}{110}{kwhair}
\kwrect{171}{55}{110}{26}{kwgrey}
\kwat{176}{58}{\kwsize{18}{22}\kwlight Dine {\kwbold ideer}, våre utviklere}
\kwatw{176}{71}{100}{\kwsize{7}{9}\kwregular\color{kwmuted}FEIL: FET SKRIFT. UTHEVING GJØRES MED FARGE.}
\kwrect{171}{86}{110}{26}{kwgrey}
\kwat{176}{89}{\kwsize{18}{22}\kwlight Dine \color{kwgreen}ideer\color{kwblack}, våre utviklere}
\kwatw{176}{102}{100}{\kwsize{7}{9}\kwregular\color{kwmuted}FEIL: LYSEGRØNN TEKST PÅ GRÅTT (1,05:1). IKKE LESBAR.}
\kwrect{171}{117}{110}{26}{kwgrey}
\kwat{176}{120}{\kwsize{18}{22}\kwlight Dine ideer, \color{kwdarkgreen}våre utviklere}
\kwatw{176}{133}{100}{\kwsize{7}{9}\kwregular\color{kwmuted}FEIL: HELE TITTELEN I FARGE. DA FORSVINNER UTHEVINGEN.}
```

:::


::: {.divider number="05" title="Grafiske elementer" text="Seismografen, rutenettet og komponentene fra nettsiden. Få elementer, brukt med måte og med mye luft."}
:::

::: {.page section="Grafiske elementer" title="Det femte elementet" lead=""}

```{=latex}
\kwpanel{128}{46}{70}{97}{kwblack}{fifth-element-green.pdf}{131}{51}{64}
\kwrect{206}{46}{75}{97}{kwgrey}
\kwdraw{%
  \foreach \c in {0,...,5}{\draw[kwhair,line width=0.4pt] \kwoo{214}{50}{1.12*\c}{0} -- \kwoo{214}{122}{1.12*\c}{0};}
  \draw[line width=0.8pt] \kwo{214}{54} -- \kwo{247.6}{60};
  \draw[line width=3.4pt] \kwo{247.6}{60} -- \kwo{225.2}{66};
  \draw[line width=0.8pt] \kwo{225.2}{66} -- \kwo{258.8}{72};
  \draw[line width=0.8pt] \kwo{258.8}{72} -- \kwo{236.4}{78};
  \draw[line width=3.4pt] \kwo{236.4}{78} -- \kwo{270}{84};
  \draw[line width=3.4pt] \kwo{270}{84} -- \kwo{214}{90};
  \draw[line width=0.8pt] \kwo{214}{90} -- \kwo{258.8}{96};
  \draw[line width=3.4pt] \kwo{258.8}{96} -- \kwo{225.2}{102};
  \draw[line width=0.8pt] \kwo{225.2}{102} -- \kwo{270}{108};
  \draw[line width=0.8pt] \kwo{270}{108} -- \kwo{236.4}{114};
  \draw[line width=3.4pt] \kwo{236.4}{114} -- \kwo{247.6}{120};
  \kwdotat{214}{54}\kwdotat{247.6}{60}\kwdotat{225.2}{66}\kwdotat{258.8}{72}\kwdotat{236.4}{78}\kwdotat{270}{84}
  \kwdotat{214}{90}\kwdotat{258.8}{96}\kwdotat{225.2}{102}\kwdotat{270}{108}\kwdotat{236.4}{114}\kwdotat{247.6}{120}
  \draw[line width=3.4pt] \kwo{214}{128.5} -- \kwo{222}{128.5};
  \draw[line width=0.8pt] \kwo{214}{134.5} -- \kwo{222}{134.5};}
\kwatw{225}{126.3}{54}{\kwsize{7.5}{10}\kwregular Mye aktivitet: tykk strek (13 px)}
\kwatw{225}{133.3}{54}{\kwsize{7.5}{10}\kwregular Lite aktivitet: tynn strek (3 px)}
\kwatw{16}{135}{104}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Åpent punkt: det er ikke bekreftet at generatoren fortsatt er i drift. Uten den leveres motivene som ferdig eksporterte filer.}
\noindent\begin{minipage}{104mm}\kwsize{10}{14}
```

## Hva det er

Seismografen er profilens femte element. Den er bygget av samarbeid: hvor mye det skrives i KodeWorks' Slack-kanaler, over tid. Symbolet har samme opphav.

## Slik lages det

- Seks kolonner, én prikk per tidsenhet, forbundet med streker
- Mye aktivitet gir tykk strek, lite gir tynn
- Tidsperiode: 20 minutter, dagen, 24 timer eller året (365 dager i årsrapporten)
- Bare mengden teller, aldri innholdet: ingen meldinger, ingen navn
- Svart eller grønn. Leveres som SVG, EPS, PNG eller MP4

```{=latex}
\end{minipage}
```

:::

::: {.page section="Grafiske elementer" title="Bruk av seismografen" lead="Ett motiv per flate. Svart på grå eller hvit, grønn på svart eller dypgrønn."}

```{=latex}
% row 1 (ok) y=47, row 2 (no) y=92, tiles 62.5 x 40
\kwpanel{16}{47}{62.5}{40}{kwwhite}{fifth-element-black.pdf}{24}{34}{46}
\kwcell{16}{47}{62.5}{40}{none}{kwhair}{\color{kwmuted}\shortstack[l]{Svart på hvit\\21,00:1}}
\kwmark{ok}{16}{47}
\kwpanel{83.5}{47}{62.5}{40}{kwgrey}{fifth-element-black.pdf}{91.5}{34}{46}
\kwcell{83.5}{47}{62.5}{40}{none}{none}{\color{kwmuted}\shortstack[l]{Svart på grå\\17,00:1}}
\kwmark{ok}{83.5}{47}
\kwpanel{151}{47}{62.5}{40}{kwblack}{fifth-element-green.pdf}{159}{34}{46}
\kwcell{151}{47}{62.5}{40}{none}{none}{\color{kwgrey}\shortstack[l]{Grønn på svart\\17,79:1}}
\kwmark{ok}{151}{47}
\kwpanel{218.5}{47}{62.5}{40}{kwdeepgreen}{fifth-element-green.pdf}{226.5}{34}{46}
\kwcell{218.5}{47}{62.5}{40}{none}{none}{\color{kwgrey}\shortstack[l]{Grønn på dypgrønn\\9,22:1}}
\kwmark{ok}{218.5}{47}
\kwpanel{16}{92}{62.5}{40}{kwwhite}{fifth-element-green.pdf}{24}{79}{46}
\kwcell{16}{92}{62.5}{40}{none}{kwhair}{\color{kwmuted}\shortstack[l]{Grønn på hvit, stort motiv\\1,18:1}}
\kwmark{no}{16}{92}
\kwpanel{83.5}{92}{62.5}{40}{kwgreen}{fifth-element-black.pdf}{91.5}{79}{46}
\kwcell{83.5}{92}{62.5}{40}{none}{none}{\color{kwblack}Svart på grønn flate}
\kwmark{no}{83.5}{92}
\kwpanel{151}{92}{62.5}{40}{kwblack}{fifth-element-green.pdf}{159}{79}{46}
\kwatc{182.25}{112}{\color{kwwhite}\kwsize{20}{22}\kwlight Tekst over streker}
\kwcell{151}{92}{62.5}{40}{none}{none}{\color{kwgrey}Tekst over tykke streker}
\kwmark{no}{151}{92}
\kwpanel{218.5}{92}{62.5}{40}{kwgrey}{fifth-element-black.pdf}{214}{68}{40}
\kwpanel{250}{92}{31}{40}{kwgrey}{fifth-element-black.pdf}{240}{72}{40}
\kwcell{218.5}{92}{62.5}{40}{none}{none}{\color{kwmuted}Flere motiver på samme flate}
\kwmark{no}{218.5}{92}
\kwatw{16}{135}{265}{\kwsize{8}{11}\kwregular\color{kwmuted}Høyst omtrent en tredel av en tekstflate. På tekstrike dokumenter (CV, brev, rapport) brukes den som ramme i kanten og ved seksjonsstart, aldri bak eller gjennom tekst; som slik ramme kan den være grønn også på hvit og grå, fordi de tykke strekene bærer formen (se Visittkort og brevark). Ikke i skjemaer eller verktøysider. Motivet bygger bare på aktivitetsmengde, aldri på innhold.}
```

:::

::: {.page section="Grafiske elementer" title="Grid og layout" lead="Digitalt følger vi nettsidens mål. På trykk er A4 utgangspunktet. Rektangulære former og venstrejustert tekst."}

```{=latex}
% ---- Digital: 1400 px = 112 mm (0.08 mm per px); column 7.13 mm, gutter 2.4 mm
\kwat{16}{43.5}{\kwsize{9}{11}\kwmedium Digitalt}
\kwdraw{%
  \draw[kwhair,line width=0.4pt] \kwo{16}{52} rectangle ++(112mm,-64mm);
  \foreach \i in {0,...,11}{\fill[kwgrey] \kwoo{16}{52}{0.953*\i}{0} rectangle ++(7.13mm,-64mm);}
  \fill[kwblack] \kwo{16}{57} rectangle ++(35.72mm,-3.2mm);
  \fill[kwblack] \kwo{16}{61.4} rectangle ++(28mm,-3.2mm);
  \foreach \j in {0,1,2}{\fill[kwmuted] \kwoo{73.18}{57}{0}{-0.26*\j} rectangle ++(54.8mm,-1.4mm);}
  \fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{16}{69.4} rectangle ++(54.78mm,-22.6mm);
  \foreach \j in {0,...,4}{\fill[kwmuted] \kwoo{73.18}{70}{0}{-0.4*\j} rectangle ++(54.8mm,-1.2mm);}
  \fill[kwblack] \kwo{16}{101.6} rectangle ++(28mm,-3.2mm);
  \foreach \j in {0,1,2}{\fill[kwmuted] \kwoo{73.18}{102}{0}{-0.3*\j} rectangle ++(54.8mm,-1.2mm);}
  \draw[kwdarkgreen,dotted,line width=0.4pt] \kwo{128}{64.6} -- \kwo{141}{64.6} \kwo{128}{69.4} -- \kwo{141}{69.4} \kwo{128}{92} -- \kwo{141}{92} \kwo{128}{101.6} -- \kwo{141}{101.6};
  \kwdimh{16}{128}{48.5}{maks bredde 1400 px}
  \kwdimh{28}{116}{122}{smal 1100 px}
  \kwdimv{64.6}{69.4}{141}{60 px}
  \kwdimv{92}{101.6}{141}{120 px}}
\kwatw{16}{126}{112}{\kwsize{8}{11}\kwregular 12 kolonner à 89 px, gutter 30 px (20 px på mobil). Innhold venstrejustert, ingress kan forskyves mot høyre. Hjørner med 0 radius. Luft prioriteres foran fylling.}
% ---- Print: A4 at 0.28 (58.8 x 83.2 mm); margin 20 mm = 5.6 mm; 12 columns, gutter 5 mm = 1.4 mm
\kwat{156}{43.5}{\kwsize{9}{11}\kwmedium Trykk, A4}
\kwdraw{%
  \draw[kwhair,line width=0.4pt] \kwo{156}{52} rectangle ++(58.8mm,-83.16mm);
  \foreach \i in {0,...,11}{\fill[kwgrey] \kwoo{161.6}{57.6}{0.408*\i}{0} rectangle ++(2.68mm,-72mm);}
  \fill[kwblack] \kwo{161.6}{62} rectangle ++(30mm,-2.5mm);
  \foreach \j in {0,...,8}{\fill[kwmuted] \kwoo{161.6}{74}{0}{-0.3*\j} rectangle ++(23.08mm,-0.7mm);}
  \foreach \j in {0,...,8}{\fill[kwmuted] \kwoo{186.08}{74}{0}{-0.3*\j} rectangle ++(23.08mm,-0.7mm);}
  \kwdimh{156}{214.8}{48.5}{210 mm}
  \kwdimv{52}{57.6}{152}{20 mm}}
\kwatw{224}{47}{57}{\kwsize{7.5}{10}%
\begin{kwtable}{@{}p{15mm}@{\hspace{2mm}}p{25mm}@{\hspace{2mm}}p{15mm}@{}}
\kwth{Mål} & \kwth{Digitalt} & \kwth{Trykk}\\ \hline
Format & maks 1400 px, smal 1100 px & A4, 210 × 297 mm\\ \hline
Kolonner & 12 à 89 px & 12\\ \hline
Gutter & 30 px, 20 px mobil & 5 mm\\ \hline
Marg & – & 20 mm\\ \hline
Loddrett luft & 60 og 120 px & – \\ \hline
\end{kwtable}\par\vspace{2mm}{\kwsize{7.5}{10}\kwmutedtext{Trykkmålene er forslag og justeres ved første trykksak. Brevark: avsender øverst til venstre, referanselinje under, tekst i én spalte.}}}
```

:::

::: {.page section="Grafiske elementer" title="Komponenter" lead="Komponentene er hentet fra nettsiden og gjelder alle digitale flater. Rektangulære former, tynne linjer, grønt som aksent."}

```{=latex}
\kwat{16}{46}{\kwsize{11}{13}\kwmedium Knapp}
\kwat{83.5}{46}{\kwsize{11}{13}\kwmedium Lenke}
\kwat{151}{46}{\kwsize{11}{13}\kwmedium Sitat}
\kwat{218.5}{46}{\kwsize{11}{13}\kwmedium Boks}
\kwcell{16}{54}{62.5}{42}{kwwhite}{kwhair}{}
\kwcell{83.5}{54}{62.5}{42}{kwwhite}{kwhair}{}
\kwcell{151}{54}{62.5}{42}{kwwhite}{kwhair}{}
\kwcell{218.5}{54}{62.5}{42}{kwwhite}{kwhair}{}
\kwatc{47.25}{68}{\kwbutton{kwdarkgreen}{Ta kontakt}}
\kwatc{47.25}{84}{\kwbutton{kwdeepgreen}{Ta kontakt}}
\kwatc{114.75}{75}{\kwlink{Les mer om oss}}
\kwatc{182.25}{75}{\kwquote{44mm}{Teknologi er et samarbeid.}}
\kwatc{249.75}{75}{\kwbox{44mm}{\kwmedium Teknologi\par\kwregular Kort tekst i en boks med tynn ramme.}}
\kwatw{16}{99}{62.5}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Rektangulær, 0 radius. Fyll mørkegrønn, hvit tekst (6,65:1). Hover og trykket: dypgrønn.}
\kwatw{83.5}{99}{62.5}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Svart tekst med grønn understrek. Understreken er pynt og bærer ikke lenken alene.}
\kwatw{151}{99}{62.5}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Grønn venstrekant på 10 px, tekst i Light. Midtstilt bare for enkeltsitater.}
\kwatw{218.5}{99}{62.5}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Tynn svart ramme, 1 til 1,25 px, 0 radius. Brukes på teknologibokser og skjemafelt.}
\kwat{16}{111.5}{\kwsize{11}{13}\kwmedium Bunntekst}
\kwrect{16}{118}{265}{22}{kwblack}
\kwimg{267}{122}{7.8}{kw-symbol-green.pdf}
\kwatw{24}{123}{60}{\color{kwwhite}\kwsize{8.5}{11.5}\kwmedium KodeWorks AS\par\kwregular Fjordgata 30\\7010 Trondheim}
\kwatw{92}{123}{60}{\color{kwwhite}\kwsize{8.5}{11.5}\kwmedium KodeWorks Oslo AS\par\kwregular Grønnegata 10\\0350 Oslo}
\kwat{16}{141.5}{\kwsize{7.5}{10}\kwregular\color{kwmuted}Svart flate, hvit tekst, KW-symbolet i grønt øverst til høyre. Eksempelinnhold.}
```

:::


::: {.divider number="06" title="Foto" text="KodeWorks viser seg med egne bilder: ekte mennesker, ekte rom og varmt lys."}
:::

::: {.page section="Foto" title="Prinsipper for foto" lead="Mennesket er hovedmotivet. Bildene tas av og med KodeWorks, i dagslys og varme toner."}

```{=latex}
% Local components (also defined in the other section files with \providecommand)
% \kwph{x}{y}{w}{h}{file}{h/w of image}{focus x 0-1}{focus y 0-1}: image covering the box, clipped
\providecommand{\kwph}[8]{\kwdraw{\begin{scope}
  \clip \kwo{#1}{#2} rectangle ++(#3mm,-#4mm);
  \pgfmathsetmacro{\kwiw}{max(#3,#4/#6)}
  \pgfmathsetmacro{\kwix}{#1-(\kwiw-#3)*#7}
  \pgfmathsetmacro{\kwiy}{#2-(\kwiw*#6-#4)*#8}
  \node[anchor=north west,inner sep=0pt] at \kwo{\kwix}{\kwiy} {\includegraphics[width=\kwiw mm]{photos/#5}};
  \end{scope}}}
% \kwok{x}{y} / \kwno{x}{y}: round badge centred at x,y (mm)
\providecommand{\kwok}[2]{\kwdraw{\fill[kwgreen] ($(current page.north west)+(#1mm,-#2mm)$) circle (2.7mm);
  \draw[kwblack,line width=0.8pt,line cap=round,line join=round] ($(current page.north west)+(#1mm-1.2mm,-#2mm-0.1mm)$) -- ++(0.8mm,-0.9mm) -- ++(1.7mm,1.9mm);}}
\providecommand{\kwno}[2]{\kwdraw{\fill[kwblack] ($(current page.north west)+(#1mm,-#2mm)$) circle (2.7mm);
  \draw[kwwhite,line width=0.8pt,line cap=round] ($(current page.north west)+(#1mm-1mm,-#2mm-1mm)$) -- ++(2mm,2mm) ($(current page.north west)+(#1mm-1mm,-#2mm+1mm)$) -- ++(2mm,-2mm);}}
% \kwcapM{x}{y}{w}{title}{text}
\providecommand{\kwcapM}[5]{\kwatw{#1}{#2}{#3}{{\kwsize{9}{11}\kwmedium #4}\par\vspace{0.8mm}{\kwsize{7.5}{10}\kwregular #5}}}

% Portrait on a green panel
\kwrect{16}{46}{55}{99}{kwgreen}
\kwph{21}{51}{45}{56}{photo_portrait.jpg}{1.25}{0.5}{0.1}
\kwok{24}{54}
\kwcapM{21}{111}{45}{Portrett}{Rolig bakgrunn og øyekontakt. Portrett kan ligge på en grønn eller grå flate.}
% Row 1
\kwph{78}{46}{64}{32}{photo_oslo.jpg}{0.6664}{0.5}{0.5}
\kwok{82}{50}
\kwcapM{78}{81}{64}{Dagslys og varme toner}{Tre, planter og dagslys. Ingen kalde eller blålige bilder.}
\kwph{147.5}{46}{64}{32}{photo_team2.jpg}{0.6664}{0.5}{0.3}
\kwok{151.5}{50}
\kwcapM{147.5}{81}{64}{Mennesket er hovedmotivet}{Folk i samtale og arbeid. Utstyret er bakgrunn.}
\kwph{217}{46}{64}{32}{photo_team3.jpg}{0.6664}{0.5}{0.3}
\kwok{221}{50}
\kwcapM{217}{81}{64}{Ekte arbeid}{Ingen poseringer. Ansatte og kunder slik de jobber sammen.}
% Row 2
\kwph{78}{98}{64}{32}{photo_office.jpg}{1.3337}{0.5}{0.3}
\kwok{82}{102}
\kwcapM{78}{133}{64}{Rom og lokaler}{Kontorene i Oslo og Trondheim. Rolige flater gir plass til tittel.}
\kwph{147.5}{98}{64}{32}{photo_team1.jpg}{0.6664}{0.5}{0.4}
\kwok{151.5}{102}
\kwcapM{147.5}{133}{64}{Rektangulær beskjæring}{Mennesket i fokus, rette hjørner.}
\kwrect{217}{98}{64}{32}{kwgrey}
\kwat{221}{102}{\kwsize{7}{9}\kwregular\color{kwmuted}RETTIGHETER}
\kwatw{221}{107}{56}{\kwsize{9}{12}\kwlight Samtykke og lisens for hvert bilde av enkeltpersoner.}
\kwok{277}{102}
\kwcapM{217}{133}{64}{Rettigheter}{Samtykke for trykk, web og sosiale medier. Bruk bare KodeWorks' egne bilder.}
```

:::

::: {.page section="Foto" title="Ikke-gjør" lead="Slik brukes ikke bildene. Tre av eksemplene er laget av KodeWorks' egne bilder, tre er plassholdere."}

```{=latex}
\providecommand{\kwph}[8]{\kwdraw{\begin{scope}
  \clip \kwo{#1}{#2} rectangle ++(#3mm,-#4mm);
  \pgfmathsetmacro{\kwiw}{max(#3,#4/#6)}
  \pgfmathsetmacro{\kwix}{#1-(\kwiw-#3)*#7}
  \pgfmathsetmacro{\kwiy}{#2-(\kwiw*#6-#4)*#8}
  \node[anchor=north west,inner sep=0pt] at \kwo{\kwix}{\kwiy} {\includegraphics[width=\kwiw mm]{photos/#5}};
  \end{scope}}}
\providecommand{\kwno}[2]{\kwdraw{\fill[kwblack] ($(current page.north west)+(#1mm,-#2mm)$) circle (2.7mm);
  \draw[kwwhite,line width=0.8pt,line cap=round] ($(current page.north west)+(#1mm-1mm,-#2mm-1mm)$) -- ++(2mm,2mm) ($(current page.north west)+(#1mm-1mm,-#2mm+1mm)$) -- ++(2mm,-2mm);}}
\providecommand{\kwcapM}[5]{\kwatw{#1}{#2}{#3}{{\kwsize{9}{11}\kwmedium #4}\par\vspace{0.8mm}{\kwsize{7.5}{10}\kwregular #5}}}
% 1 circle crop
\kwrect{16}{46}{83}{32}{kwgrey}
\kwdraw{\begin{scope}\clip ($(current page.north west)+(57.5mm,-62mm)$) circle (15mm);
  \node[anchor=north west,inner sep=0pt] at ($(current page.north west)+(42.5mm,-47mm)$) {\includegraphics[width=30mm]{photos/photo_portrait.jpg}};\end{scope}}
\kwno{20}{50}
\kwcapM{16}{81}{83}{Sirkel og avrunding}{Beskjæres rektangulært, aldri som sirkel.}
% 2 overlay
\kwph{107}{46}{83}{32}{photo_team2.jpg}{0.6664}{0.5}{0.3}
\kwdraw{\fill[kwpink,opacity=0.6] \kwo{107}{46} rectangle ++(83mm,-32mm);}
\kwno{111}{50}
\kwcapM{107}{81}{83}{Fargeoverlegg og filter}{Bildene brukes som de er. Ingen duotone eller fargeflate over bildet.}
% 3 text over faces
\kwph{198}{46}{83}{32}{photo_team3.jpg}{0.6664}{0.5}{0.3}
\kwat{203}{55}{\kwsize{30}{30}\kwlight\color{kwwhite}Overskrift}
\kwno{202}{50}
\kwcapM{198}{81}{83}{Tekst over ansikter}{Titler legges på rolig flate utenfor motivet.}
% 4 stock
\kwrect{16}{96}{83}{32}{kwgrey}
\kwatw{20}{108}{75}{\kwsize{8}{10}\kwregular\color{kwmuted}\centering Plassholder\par Stockfoto: generiske poseringer, håndtrykk, dresskledde møter\par}
\kwno{20}{100}
\kwcapM{16}{131}{83}{Stockfoto}{Ikke generiske bilder av folk i dress eller håndtrykk.}
% 5 illustration / icon
\kwrect{107}{96}{83}{32}{kwgrey}
\kwdraw{\fill[kwdarkgreen] ($(current page.north west)+(131mm,-107mm)$) circle (5mm);
  \fill[kwgreen] ($(current page.north west)+(143mm,-102mm)$) rectangle ++(10mm,-10mm);
  \fill[kwblack] ($(current page.north west)+(160mm,-113mm)$) -- ++(5mm,9mm) -- ++(5mm,-9mm) -- cycle;}
\kwatw{111}{119}{75}{\kwsize{8}{10}\kwregular\color{kwmuted}\centering Plassholder: illustrasjon eller ikon\par}
\kwno{111}{100}
\kwcapM{107}{131}{83}{Illustrasjon og ikon}{Ikke som erstatning for foto av mennesker.}
% 6 2021 references
\kwrect{198}{96}{83}{32}{kwgrey}
\kwatw{202}{108}{75}{\kwsize{8}{10}\kwregular\color{kwmuted}\centering Plassholder\par Referansebilder fra 2021-manualen\par}
\kwno{202}{100}
\kwcapM{198}{131}{83}{Bildene fra 2021-manualen}{De tilhører ikke KodeWorks og kan ikke brukes.}
```

:::


::: {.page section="Tone" title="Tone" lead="Visjonen er «Vi muliggjør ideer». Uttrykket er nøkternt og lekent. Hvert plattformord har en visuell regel."}

```{=latex}
\label{sec:07}%
\providecommand{\kwph}[8]{\kwdraw{\begin{scope}
  \clip \kwo{#1}{#2} rectangle ++(#3mm,-#4mm);
  \pgfmathsetmacro{\kwiw}{max(#3,#4/#6)}
  \pgfmathsetmacro{\kwix}{#1-(\kwiw-#3)*#7}
  \pgfmathsetmacro{\kwiy}{#2-(\kwiw*#6-#4)*#8}
  \node[anchor=north west,inner sep=0pt] at \kwo{\kwix}{\kwiy} {\includegraphics[width=\kwiw mm]{photos/#5}};
  \end{scope}}}
\providecommand{\kwok}[2]{\kwdraw{\fill[kwgreen] ($(current page.north west)+(#1mm,-#2mm)$) circle (2.7mm);
  \draw[kwblack,line width=0.8pt,line cap=round,line join=round] ($(current page.north west)+(#1mm-1.2mm,-#2mm-0.1mm)$) -- ++(0.8mm,-0.9mm) -- ++(1.7mm,1.9mm);}}
\providecommand{\kwno}[2]{\kwdraw{\fill[kwblack] ($(current page.north west)+(#1mm,-#2mm)$) circle (2.7mm);
  \draw[kwwhite,line width=0.8pt,line cap=round] ($(current page.north west)+(#1mm-1mm,-#2mm-1mm)$) -- ++(2mm,2mm) ($(current page.north west)+(#1mm-1mm,-#2mm+1mm)$) -- ++(2mm,-2mm);}}
\kwat{16}{45}{\kwsize{7}{9}\kwregular\color{kwmuted}PLATTFORMORD}
\kwat{68}{45}{\kwsize{7}{9}\kwregular\color{kwmuted}VISUELL REGEL}
\kwat{192}{45}{\kwsize{7}{9}\kwregular\color{kwmuted}EKSEMPEL}
% row helper: \kwrow{y}{word}{rule}
\providecommand{\kwrow}[3]{%
  \kwdraw{\draw[kwhair,line width=0.4pt] \kwo{16}{\the\numexpr#1-2\relax} -- ++(265mm,0);}%
  \kwatw{16}{#1}{50}{\kwsize{9.5}{11.5}\kwmedium #2}%
  \kwatw{68}{#1}{118}{\kwsize{8.5}{11}\kwregular #3}}
% 1
\kwrow{51}{Solid, faglig sterk}{Svart tekst, rektangulære former, lite farge, ingen effekter.}
\kwrect{192}{50}{30}{7.5}{kwdarkgreen}
\kwat{195}{52}{\kwsize{8.5}{10}\kwregular\color{kwwhite}Kontakt oss}
\kwat{226}{51.5}{\kwsize{8.5}{10}\kwlight Rette hjørner}
% 2
\kwrow{62}{High tech, industrielt}{Grotesk, grå flater og tekniske linjer, som i det femte elementet.}
\kwpanel{192}{61}{45}{8}{kwgrey}{fifth-element-black.pdf}{188}{44}{50}
% 3
\kwrow{73}{Lekenhet, nysgjerrig}{Lysegrønn aksent, rosa i liten dose, ordvis fargeutheving i titler.}
\kwat{192}{72}{\kwsize{12}{14}\kwlight Dine \color{kwdarkgreen}ideer}
\kwrect{237}{72.3}{7}{6}{kwgreen}
\kwrect{245}{72.3}{4}{6}{kwpink}
% 4
\kwrow{84}{Samskapende, samhold}{Ekte mennesker, og symbol og seismograf som er laget av felles aktivitet.}
\kwph{192}{83}{45}{8}{photo_team3.jpg}{0.6664}{0.5}{0.3}
% 5
\kwrow{95}{Åpenhet}{Mye luft og høy kontrast. Ingen dekor som skjuler innholdet.}
\kwdraw{\fill[kwwhite,draw=kwhair,line width=0.4pt] \kwo{192}{94} rectangle ++(45mm,-8mm);}
\kwat{194}{95}{\kwsize{11}{13}\kwlight Aa}
\kwat{206}{96.5}{\kwsize{8}{10}\kwmedium 21,00:1}
% 6
\kwrow{106}{Frempå}{Store, direkte titler og korte setninger.}
\kwat{192}{105}{\kwsize{14}{16}\kwlight Dine \color{kwdarkgreen}ideer. Våre \color{kwblack}utviklere.}
% 7
\kwrow{117}{Kunnskapsrik, dedikert}{Konkret og faktabasert tekst. Ingen superlativer.}
\kwok{194}{119.7}
\kwat{199}{118.2}{\kwsize{8}{10}\kwregular Vi bygger det dere trenger.}
\kwno{244}{119.7}
\kwat{249}{118.2}{\kwsize{8}{10}\kwregular Verdensledende løsninger.}
% 8
\kwrow{128}{Nei-listen}{Unngå corporate, kjedelig og overload: ingen stockfoto, gradient eller skygge, og høyst tre farger i en komposisjon.}
\kwrect{192}{129}{14}{5}{kwgreen}
\kwrect{206}{129}{14}{5}{kwblack}
\kwrect{220}{129}{14}{5}{kwgrey}
\kwdraw{\draw[kwhair,line width=0.4pt] \kwo{220}{129} rectangle ++(14mm,-5mm);}
```

:::


::: {.divider number="08" title="Anvendelse" text="Fire eksempler på hvordan reglene brukes: visittkort, brevark, presentasjon og nettside. Eksemplene er illustrasjoner av prinsippene, ikke ferdige maler."}
:::

```{=latex}
\providecommand{\kwchip}[5]{\kwdraw{\node[anchor=north west,inner xsep=1.6mm,inner ysep=0.9mm,fill=#4,text=#5] at \kwo{#1}{#2} {\kwsize{6.5}{8}\kwmedium #3};}}
\providecommand{\kwline}[4]{\kwrect{#1}{#2}{#3}{0.3}{#4}}
\providecommand{\kwlabel}[3]{\kwat{#1}{#2}{\kwsize{6.5}{8}\kwregular\color{kwmuted}#3}}
\providecommand{\kwbar}[4]{\kwrect{#1}{#2}{#3}{0.9}{#4}}
```

::: {.page section="Anvendelse" title="Visittkort og brevark" lead="Grå og hvit flate, svart navnetrekk, grønt som liten aksent. På brevark ligger seismografen bare som ramme i kanten, så teksten har ro."}

```{=latex}
% business card front
\kwdraw{\fill[fill=kwgrey,draw=kwhair,line width=0.4pt] \kwo{16}{50} rectangle ++(85mm,-55mm);}
\kwimg{22}{56}{40}{kw-wordmark-black.pdf}
\kwat{22}{81}{\kwsize{9}{11}\kwmedium\color{kwblack}Navn Navnesen}
\kwat{22}{85.5}{\kwsize{8}{10}\kwregular\color{kwblack}Konsulent}
\kwat{22}{91.5}{\kwsize{8}{10}\kwregular\color{kwblack}+47 000 00 000}
\kwat{22}{95.5}{\kwsize{8}{10}\kwregular\color{kwblack}navn@kodeworks.no}
% business card back
\kwdraw{\fill[fill=kwgreen] \kwo{106}{50} rectangle ++(85mm,-55mm);}
\kwimg{140.4}{63.5}{16.2}{kw-symbol-black.pdf}
% letterhead (scale 0.26)
\kwdraw{\fill[fill=kwwhite,draw=kwhair,line width=0.4pt] \kwo{226}{50} rectangle ++(54.6mm,-77.2mm);}
\kwbar{231.2}{70}{18}{kwblack!70}
\kwbar{231.2}{72.4}{13}{kwblack!70}
\kwrect{231.2}{81}{24}{1.1}{kwblack}
\kwbar{231.2}{86}{43}{kwblack!25}
\kwbar{231.2}{88.4}{43}{kwblack!25}
\kwbar{231.2}{90.8}{43}{kwblack!25}
\kwbar{231.2}{93.2}{43}{kwblack!25}
\kwbar{231.2}{95.6}{29}{kwblack!25}
\kwbar{231.2}{100.4}{43}{kwblack!25}
\kwbar{231.2}{102.8}{43}{kwblack!25}
\kwbar{231.2}{105.2}{36}{kwblack!25}
% seismograph frame in the footer: closing figure with the wordmark, address line below
\kwdraw{\node[anchor=north west,inner sep=0pt] at \kwo{231.2}{117.6} {\includegraphics[width=44.2mm]{photos/frame-bottom.png}};}
\kwbar{231.2}{122.6}{14}{kwblack!40}
\kwbar{250}{122.6}{14}{kwblack!40}
% captions
\kwlabel{16}{108}{FRAMSIDE | 85 × 55 MM}
\kwatw{16}{112}{85}{\kwsize{9}{12.5}\kwregular Grå flate. Navnetrekket er svart og 40 mm bredt, med frisone på minst 2,9 mm (halve K-høyden). Navn i Medium 9 pt, resten i Regular 8 pt.}
\kwlabel{106}{108}{BAKSIDE | 85 × 55 MM}
\kwatw{106}{112}{85}{\kwsize{9}{12.5}\kwregular Grønn flate med svart symbol, 28 mm høyt (minst 20 mm). Symbolet står alene, fordi avsenderen allerede er klar fra framsiden.}
\kwlabel{226}{129.5}{BREVARK | A4, VIST I 26 \%}
\kwatw{226}{133}{55}{\kwsize{8}{10.5}\kwregular Seismograf og navnetrekk som ramme i bunnteksten. Brødtekst 10 pt Regular.}
```

:::

::: {.page section="Anvendelse" title="Presentasjon" lead="Formatet er 16:9. Tre sidetyper dekker det meste: åpning, innhold og avslutning."}

```{=latex}
% slide 1: opening, deep green
\kwrect{16}{50}{84.33}{47.4}{kwdeepgreen}
\kwimg{21}{54}{22}{kw-wordmark-white.pdf}
\kwat{21}{70}{\kwsize{15}{15.5}\kwlight\color{kwwhite}Dine \color{kwgreen}ideer\color{kwwhite},}
\kwat{21}{76.5}{\kwsize{15}{15.5}\kwlight\color{kwwhite}våre utviklere}
\kwat{21}{89}{\kwsize{5.5}{7}\kwregular\color{kwwhite}Navn Navnesen | 12. mars 2027}
% slide 2: content, white
\kwdraw{\fill[fill=kwwhite,draw=kwhair,line width=0.4pt] \kwo{106.33}{50} rectangle ++(84.33mm,-47.4mm);}
\kwat{111.3}{54}{\kwsize{12}{13}\kwlight\color{kwblack}Teknologi med \color{kwdarkgreen}retning}
\kwatw{111.3}{63}{50}{\kwsize{6}{8.4}\kwregular\color{kwblack}Brødtekst i Regular. Venstrejustert, god luft mellom linjene.\par\vspace{1mm}Maks tre punkter per side.}
\kwrect{111.3}{78}{20}{11}{kwgrey}
\kwrect{134}{78}{20}{11}{kwgrey}
\kwrect{156.7}{78}{20}{11}{kwgrey}
\kwimg{111.3}{91.5}{14}{kw-wordmark-black.pdf}
\kwat{182}{91.3}{\kwsize{5}{6}\kwregular\color{kwblack}02}
% slide 3: closing, black
\kwrect{196.67}{50}{84.33}{47.4}{kwblack}
\kwimg{204}{58}{11.5}{kw-symbol-green.pdf}
\kwat{225}{58}{\kwsize{13}{15}\kwlight\color{kwwhite}Takk}
\kwat{225}{66}{\kwsize{6}{8}\kwregular\color{kwwhite}navn@kodeworks.no}
\kwat{225}{70}{\kwsize{6}{8}\kwregular\color{kwwhite}+47 000 00 000}
% captions
\kwlabel{16}{101}{ÅPNING}
\kwatw{16}{105}{80}{\kwsize{9}{12.5}\kwregular Dyp grønn flate (\#254333) med hvitt navnetrekk. Tittel i Light, utheving i lysegrønn (9,22:1).}
\kwlabel{106.33}{101}{INNHOLD}
\kwatw{106.33}{105}{80}{\kwsize{9}{12.5}\kwregular Hvit flate. Tittel i Light med ett ord i \#35664C. Brødtekst i Regular, minst 18 pt i en presentasjon.}
\kwlabel{196.67}{101}{AVSLUTNING}
\kwatw{196.67}{105}{80}{\kwsize{9}{12.5}\kwregular Svart flate med grønt symbol (17,8:1). Kontaktperson med navn, e-post og telefon.}
\kwline{16}{127}{265}{kwhair}
\kwatw{16}{130}{265}{\kwsize{9}{12.5}\kwregular{\kwmedium Skrift.} Presentasjonen skrives i Markdown og bygges til PDF med profilfonten innebygd. {\kwmedium Navnetrekk} nederst til venstre og sidetall nederst til høyre, med frisone. {\kwmedium Seismograf} bare på åpningsbildet, aldri bak brødtekst.}
```

:::

::: {.page section="Anvendelse" title="Nettside" lead="Hvit grunnflate, svart tekst, mørkegrønn for det som kan trykkes. Lysegrønn brukes som aksent og på svart bunntekst."}

```{=latex}
% browser frame
\kwdraw{\fill[fill=kwwhite,draw=kwblack!30,line width=0.5pt] \kwo{16}{48} rectangle ++(165mm,-93mm);}
% top nav
\kwimg{21}{51.5}{24}{kw-wordmark-black.pdf}
\kwat{85}{52}{\kwsize{5.5}{7}\kwregular\color{kwblack}Våre eksperter \hspace{3mm} Våre prosjekter \hspace{3mm} Håndboka}
\kwrect{150}{50}{26}{7.5}{kwdarkgreen}
\kwat{154.5}{52.3}{\kwsize{5.5}{7}\kwregular\color{kwwhite}Kontakt oss}
% hero
\kwat{21}{65}{\kwsize{26}{26}\kwlight\color{kwblack}Dine \color{kwdarkgreen}ideer}
\kwat{21}{74}{\kwsize{26}{26}\kwlight\color{kwdarkgreen}Våre \color{kwblack}utviklere}
\kwatw{115}{70}{58}{\kwsize{7.5}{12}\kwlight\color{kwblack}Vi hjelper deg fra idé til løsning, og blir med hele veien.}
\kwat{115}{86}{\kwsize{6}{7}\kwregular\color{kwblack}Les mer}
\kwrect{115}{89}{11}{0.7}{kwgreen}
% grey section with cards
\kwrect{17}{98}{163}{24}{kwgrey}
\kwat{21}{100}{\kwsize{10}{12}\kwlight\color{kwblack}Våre tjenester}
\kwdraw{\draw[kwblack,line width=0.4pt] \kwo{21}{108} rectangle ++(48mm,-11mm);}
\kwdraw{\draw[kwblack,line width=0.4pt] \kwo{73}{108} rectangle ++(48mm,-11mm);}
\kwdraw{\draw[kwblack,line width=0.4pt] \kwo{125}{108} rectangle ++(51mm,-11mm);}
\kwat{23}{110}{\kwsize{7}{8}\kwlight\color{kwblack}Utvikling}
\kwat{75}{110}{\kwsize{7}{8}\kwlight\color{kwblack}Team}
\kwat{127}{110}{\kwsize{7}{8}\kwlight\color{kwblack}AI}
% footer
\kwrect{17}{123}{163}{17.5}{kwblack}
\kwimg{166}{125}{8}{kw-symbol-green.pdf}
\kwat{22}{127}{\kwsize{5.5}{7}\kwregular\color{kwgreen}Kontakt oss}
\kwat{22}{131}{\kwsize{5.5}{7.5}\kwregular\color{kwwhite}navn@kodeworks.no}
\kwat{70}{127}{\kwsize{5.5}{7}\kwregular\color{kwgreen}Oslo}
\kwat{70}{131}{\kwsize{5.5}{7.5}\kwregular\color{kwwhite}Grønnegata 10}
\kwat{115}{127}{\kwsize{5.5}{7}\kwregular\color{kwgreen}Trondheim}
\kwat{115}{131}{\kwsize{5.5}{7.5}\kwregular\color{kwwhite}Fjordgata 30}
% annotations
\kwline{190}{47.5}{91}{kwhair}
\kwatw{190}{50}{91}{\kwsize{8.5}{11.5}\kwregular
 {\kwmedium Toppmeny.} Navnetrekket i svart, minst 100 px bredt. Knappen er \#35664C med hvit tekst (6,65:1).\par\vspace{2.2mm}
 {\kwmedium Tittel.} Light, 48 px. Utheving med farge, ikke vekt.\par\vspace{2.2mm}
 {\kwmedium Lenke.} Svart tekst med lysegrønn understrek. Understreken er pynt og kan ikke være eneste markering.\par\vspace{2.2mm}
 {\kwmedium Seksjonsskille.} Grå flate \#E8E7E6 mellom hvite seksjoner. Boksene har tynn svart ramme og ingen fyll.\par\vspace{2.2mm}
 {\kwmedium Bunntekst.} Svart flate, hvit tekst og lysegrønne etiketter. Symbolet står i grønt.}
```

:::


::: {.divider number="09" title="Produksjon" text="Hvilke filer som brukes hvor, hva fontlisensen betyr i praksis, og hva du sjekker før et dokument sendes."}
:::

```{=latex}
\providecommand{\kwchip}[5]{\kwdraw{\node[anchor=north west,inner xsep=1.6mm,inner ysep=0.9mm,fill=#4,text=#5] at \kwo{#1}{#2} {\kwsize{6.5}{8}\kwmedium #3};}}
\providecommand{\kwm}[1]{{\kwmedium #1}}
\providecommand{\kwline}[4]{\kwrect{#1}{#2}{#3}{0.3}{#4}}
\providecommand{\kwlabel}[3]{\kwat{#1}{#2}{\kwsize{6.5}{8}\kwregular\color{kwmuted}#3}}
% caption under a file tile: \kwcap{x}{y}{w}{file name}{use}
\providecommand{\kwcap}[5]{\kwatw{#1}{#2}{#3}{{\kwsize{7.5}{10}\kwmedium #4}\par\vspace{0.8mm}{\kwsize{7.5}{10}\kwregular #5}}}
```

::: {.page section="Produksjon" title="Filformater" lead="Bruk vektor der det går, og PNG i Office. Velg alltid fil etter bakgrunn, ikke etter smak."}

```{=latex}
\kwat{16}{46}{\kwsize{6.5}{8}\kwregular\color{kwmuted}BRUK}
\kwat{72}{46}{\kwsize{6.5}{8}\kwregular\color{kwmuted}FORMAT}
\kwat{150}{46}{\kwsize{6.5}{8}\kwregular\color{kwmuted}EKSEMPEL}
% row 1
\kwline{16}{50}{265}{kwhair}
\kwatw{16}{52.5}{52}{\kwsize{9.5}{12}\kwmedium Nettside og nett-e-post}
\kwatw{72}{52.5}{74}{\kwsize{9}{12}\kwregular SVG. PNG der e-postklienten ikke viser SVG.}
\kwimg{150}{54}{26}{kw-wordmark-black.pdf}
\kwat{182}{53.5}{\kwsize{8}{10}\kwregular kw-wordmark-black.svg}
% row 2
\kwline{16}{63}{265}{kwhair}
\kwatw{16}{65.5}{52}{\kwsize{9.5}{12}\kwmedium Trykk: rapport, brosjyre}
\kwatw{72}{65.5}{74}{\kwsize{9}{12}\kwregular PDF med vektorgrafikk, eller EPS. Oppgi farge: CMYK eller PMS.}
\kwimg{150}{67}{26}{kw-wordmark-black.pdf}
\kwat{182}{66.5}{\kwsize{8}{10}\kwregular kw-wordmark-black.pdf}
% row 3
\kwline{16}{76}{265}{kwhair}
\kwatw{16}{78.5}{52}{\kwsize{9.5}{12}\kwmedium Word, PowerPoint, Excel}
\kwatw{72}{78.5}{74}{\kwsize{9}{12}\kwregular PNG, minst dobbel størrelse og gjennomsiktig bakgrunn. Aldri en liten PNG skalert opp.}
\kwimg{150}{80}{26}{kw-wordmark-black.pdf}
\kwat{182}{79.5}{\kwsize{8}{10}\kwregular kw-wordmark-black.png}
% row 4
\kwline{16}{89}{265}{kwhair}
\kwatw{16}{91.5}{52}{\kwsize{9.5}{12}\kwmedium Google Dokumenter og Slides}
\kwatw{72}{91.5}{74}{\kwsize{9}{12}\kwregular PNG. Kontroller at fargen ikke blir svart etter opplasting.}
\kwdraw{\fill[fill=kwblack] \kwo{150}{92.5} rectangle ++(26mm,-7mm);}
\kwimg{152.5}{94.4}{21}{kw-wordmark-white.pdf}
\kwat{182}{92.5}{\kwsize{8}{10}\kwregular kw-wordmark-white.png}
% row 5
\kwline{16}{102}{265}{kwhair}
\kwatw{16}{104.5}{52}{\kwsize{9.5}{12}\kwmedium Skilt, tekstil, store flater}
\kwatw{72}{104.5}{74}{\kwsize{9}{12}\kwregular PDF eller EPS, vektor. Be leverandøren om prøve; grønnfargen varierer.}
\kwdraw{\fill[fill=kwblack] \kwo{150}{105.5} rectangle ++(26mm,-9mm);}
\kwimg{162.5}{106.4}{4.2}{kw-symbol-green.pdf}
\kwat{182}{105.5}{\kwsize{8}{10}\kwregular kw-symbol-green.pdf}
% row 6
\kwline{16}{115}{265}{kwhair}
\kwatw{16}{117.5}{52}{\kwsize{9.5}{12}\kwmedium Sosiale medier}
\kwatw{72}{117.5}{74}{\kwsize{9}{12}\kwregular PNG. Symbolet alene i profilbildet; hold symbolet på minst 80 px høyde.}
\kwdraw{\fill[fill=kwgreen] \kwo{150}{118.5} rectangle ++(26mm,-9mm);}
\kwimg{162.5}{119.4}{4.2}{kw-symbol-black.pdf}
\kwat{182}{118.5}{\kwsize{8}{10}\kwregular kw-symbol-black.png}
\kwline{16}{128}{265}{kwhair}
\kwatw{16}{131}{265}{\kwsize{9}{12.5}\kwregular{\kwmedium Ikke} strekk, roter, legg skygge på eller tegn om logoen. PNG-filene lages fra SVG-filene i filoversikten på neste side.}
```

:::

::: {.page section="Produksjon" title="Filoversikt: logo" lead="Åtte logofiler: navnetrekk og symbol i ulike farger. Navnet viser motiv og farge." }

```{=latex}
\kwtile{16}{47}{62.5}{32}{kwwhite}{kwhair}{kw-wordmark-black.pdf}{42}{\color{kwmuted}.svg}
\kwcap{16}{81}{62.5}{kw-wordmark-black}{Standard. På hvit, grå, lysegrønn og rosa flate.}
\kwtile{83.5}{47}{62.5}{32}{kwblack}{none}{kw-wordmark-white.pdf}{42}{\color{kwgrey}.svg}
\kwcap{83.5}{81}{62.5}{kw-wordmark-white}{På svart, dypgrønn og mørkegrønn flate.}
\kwtile{151}{47}{62.5}{32}{kwdeepgreen}{none}{kw-wordmark-green.pdf}{42}{\color{kwgrey}.svg}
\kwcap{151}{81}{62.5}{kw-wordmark-green}{Bare på svart, dypgrønn og mørkegrønn flate.}
\kwtile{218.5}{47}{62.5}{32}{kwwhite}{kwhair}{kw-symbol-black.pdf}{14}{\color{kwmuted}.svg}
\kwcap{218.5}{81}{62.5}{kw-symbol-black}{Standard. På hvit, grå, lysegrønn og rosa flate.}
\kwtile{16}{95}{62.5}{32}{kwblack}{none}{kw-symbol-green.pdf}{14}{\color{kwgrey}.svg}
\kwcap{16}{129}{62.5}{kw-symbol-green}{På svart, dypgrønn og mørkegrønn flate.}
\kwtile{83.5}{95}{62.5}{32}{kwdarkgreen}{none}{kw-symbol-white.pdf}{14}{\color{kwgrey}.svg}
\kwcap{83.5}{129}{62.5}{kw-symbol-white}{På svart og mørke flater når grønt ikke passer.}
\kwtile{151}{95}{62.5}{32}{kwwhite}{kwhair}{kw-symbol-black-with-green-stroke.pdf}{13.5}{\color{kwmuted}.svg}
\kwcap{151}{129}{62.5}{kw-symbol-black-with-green-stroke}{Svart bokstavform, grønn diagonal. Bare på hvit flate.}
\kwtile{218.5}{95}{62.5}{32}{kwblack}{none}{kw-symbol-white-with-green-stroke.pdf}{14}{\color{kwgrey}.svg}
\kwcap{218.5}{129}{62.5}{kw-symbol-white-with-green-stroke}{Hvit bokstavform, grønn diagonal. På svart og dypgrønn flate.}
```

:::

::: {.page section="Produksjon" title="Filoversikt: grafikk" lead="Det femte elementet og bakgrunnene til Google Slides. Alle filer har eksplisitte farger og tett viewBox." }

```{=latex}
\kwtile{16}{47}{49}{62}{kwgrey}{none}{fifth-element-black.pdf}{36}{\color{kwmuted}.svg}
\kwcap{16}{111}{49}{fifth-element-black}{Det femte elementet, svart. På hvit og grå flate.}
\kwtile{70}{47}{49}{62}{kwblack}{none}{fifth-element-green.pdf}{36}{\color{kwgrey}.svg}
\kwcap{70}{111}{49}{fifth-element-green}{Det femte elementet, grønt. På svart og dypgrønn flate. Aldri på hvit.}
\kwtile{124}{47}{49}{62}{kwgrey}{none}{fifth-element-slide-black-green.pdf}{26}{\color{kwmuted}.svg}
\kwcap{124}{111}{49}{fifth-element-slide-black-green}{Slidebakgrunn, svarte linjer med grønne fremhevinger. 521 × 1081.}
\kwtile{178}{47}{49}{62}{kwblack}{none}{fifth-element-slide-green-wide.pdf}{46}{\color{kwgrey}.svg}
\kwcap{178}{111}{49}{fifth-element-slide-green-wide}{Slidebakgrunn, grønne linjer midt på lerretet. 2048 × 1024. På svart flate.}
\kwtile{232}{47}{49}{62}{kwblack}{none}{fifth-element-slide-green-logo-background.pdf}{40}{\color{kwgrey}.svg}
\kwcap{232}{111}{49}{fifth-element-slide-green-logo-background}{Slidebakgrunn bak logo. 469 × 542. På svart flate.}
\kwline{16}{135}{265}{kwhair}
\kwatw{16}{137}{265}{\kwsize{8.5}{11.5}\kwregular Filnavn følger mønsteret motiv, farge og eventuelt tillegg. PNG- og PDF-filer lages fra SVG-ene, aldri omvendt.}
```

:::

::: {.page section="Produksjon" title="Fontlisens i praksis" lead="Fonten kan bygges inn i PDF, PS og EPS, men ikke i .docx, .pptx, nett eller logo. Slik gjør du det riktig."}

```{=latex}
\providecommand{\kwcheck}[2]{\kwdraw{\draw[kwblack,line width=0.4pt] \kwo{#1}{#2} rectangle ++(2.6mm,-2.6mm);}}
% left column: template makers
\kwat{16}{46}{\kwsize{11}{13}\kwmedium For malbyggere}
\kwline{16}{51}{125}{kwhair}
\kwat{16}{54}{\kwsize{9.5}{12}\kwmedium 1. Fonten hentes fra fontfila, aldri fra maskinen}
\kwatw{16}{59}{125}{\kwsize{9}{12}\kwregular Byggeverktøyet pakker ut fonten fra den lisensierte fila og bygger den inn i PDF-en. Installerte fonter brukes aldri.}
\kwrect{16}{68.5}{125}{8}{kwgrey}
\kwat{19}{70.8}{\kwsize{8}{10}\kwregular Bygget stopper hvis en font kommer fra operativsystemet}
\kwat{16}{81}{\kwsize{9.5}{12}\kwmedium 2. Ikke bygg inn skrifter i Office-filer}
\kwatw{16}{86}{125}{\kwsize{9}{12}\kwregular Lisensen tillater innebygging bare i PDF, PS og EPS.}
\kwrect{16}{91.5}{125}{8}{kwgrey}
\kwcheck{19}{94.2}
\kwat{24}{94}{\kwsize{8}{10}\kwregular Bygg inn skrifter i filen (må stå av)}
\kwat{16}{104}{\kwsize{9.5}{12}\kwmedium 3. Sett logoen inn som bilde}
\kwatw{16}{109}{125}{\kwsize{9}{12}\kwregular Navnetrekket er en tegnet vektorfil. Aldri skriv «KodeWorks» i fonten.}
\kwrect{16}{114.5}{125}{8}{kwgrey}
\kwimg{19}{116.4}{22}{kw-wordmark-black.pdf}
\kwat{46}{116}{\kwsize{8}{10}\kwregular Bilde, ikke tekst}
% right column: consultants
\kwat{156}{46}{\kwsize{11}{13}\kwmedium For konsulenter}
\kwline{156}{51}{125}{kwhair}
\kwat{156}{54}{\kwsize{9.5}{12}\kwmedium 1. Lag CV, presentasjon og brev fra malene}
\kwatw{156}{59}{125}{\kwsize{9}{12}\kwregular Skriv innholdet i Markdown og bygg PDF-en. Fonten trenger ikke være installert.}
\kwrect{156}{68.5}{125}{8}{kwgrey}
\kwat{159}{70.8}{\kwsize{8}{10}\kwregular cv-ola-nordmann.md \textrightarrow{} cv-ola-nordmann.pdf}
\kwat{156}{81}{\kwsize{9.5}{12}\kwmedium 2. Ferdige dokumenter sendes som PDF}
\kwatw{156}{86}{125}{\kwsize{9}{12}\kwregular Send PDF-en fra malen. Kontroller at skriften er innebygd.}
\kwrect{156}{94.5}{125}{8}{kwgrey}
\kwat{159}{96.8}{\kwsize{8}{10}\kwregular CV.pdf, Egenskaper, Skrifter: NON Natural Grotesk, innebygd}
\kwat{156}{107}{\kwsize{9.5}{12}\kwmedium 3. Del ikke fontfilen}
\kwatw{156}{112}{125}{\kwsize{9}{12}\kwregular Lisensen er personlig for selskapet som har kjøpt den.}
\kwrect{156}{117.5}{125}{8}{kwgrey}
\kwat{159}{119.8}{\kwsize{8}{10}\kwregular Ikke vedlegg .otf i e-post eller legg på åpen disk}
% open point
\kwrect{16}{131}{265}{14}{kwgrey}
\kwat{20}{133}{\kwsize{6.5}{8}\kwregular\color{kwmuted}ÅPENT PUNKT}
\kwatw{20}{137}{257}{\kwsize{8.5}{11}\kwregular Lisensen gjelder ett selskap på én adresse. Dekning for alle KodeWorks-selskaper og for webfonten på kodeworks.no avklares med fontleverandøren.}
```

:::

::: {.page section="Produksjon" title="Sjekkliste før utsending" lead="Gå gjennom punktene før noe forlater huset. Hvert punkt har et eksempel på hva du kontrollerer."}

```{=latex}
{\kwregular\kwsize{10}{13.5}\setlength{\parskip}{2.4mm}
```

1. \kwm{Mal.} Dokumentet bygger på siste versjon av malen, ikke på et gammelt dokument. \textcolor{kwmuted}{Eksempel: start fra letter-template.md, ikke fra en gammel PDF eller Word-fil.}

2. \kwm{Logo.} Varianten passer bakgrunnen: svart på lys flate, hvit eller grønn på mørk. \textcolor{kwmuted}{Eksempel: kw-wordmark-black på hvitt ark, aldri grønt navnetrekk.}

3. \kwm{Frisone og størrelse.} Navnetrekket er minst 24 mm (100 px) bredt, symbolet minst 20 mm (80 px) høyt, begge med frisone. \textcolor{kwmuted}{Eksempel: 40 mm navnetrekk gir 2,9 mm frisone.}

4. \kwm{Tekstfarge.} Svart på lys flate, hvit på mørk. Grønn eller grå tekst på hvitt er ikke tillatt. \textcolor{kwmuted}{Eksempel: svart på lysegrønn 17,8:1, lysegrønn på hvit 1,18:1.}

5. \kwm{Skrift.} Materialet er bygget fra malen til PDF, med profilfonten innebygd. Office- og Google-dokumenter viser Arial og sendes ikke ut i KodeWorks' navn. \textcolor{kwmuted}{Eksempel: Brev.pdf, Egenskaper, Skrifter: NON Natural Grotesk, innebygd.}

6. \kwm{Utheving.} Ord i titler utheves med \#35664C, ikke med fet skrift. \textcolor{kwmuted}{Eksempel: «Dine ideer», der «ideer» er mørkegrønt.}

7. \kwm{PDF-kontroll.} Åpne PDF-en og se at skrift og logo er riktige, bilder skarpe og ingen sider kuttet. \textcolor{kwmuted}{Eksempel: Egenskaper, Skrifter viser at alle fonter er innebygd.}

8. \kwm{Trykk.} Skal dokumentet trykkes, finnes det en prøve, og grønnfargen er godkjent. \textcolor{kwmuted}{Eksempel: prøveutskrift på samme papir før hele opplaget.}

9. \kwm{Metadata.} Forfatter, tittel og versjon er riktige, kommentarer og endringsspor er fjernet, og ingen interne filstier eller notater står igjen. \textcolor{kwmuted}{Eksempel: PDF-ens Egenskaper viser riktig tittel og forfatter.}

```{=latex}
}
```

:::


