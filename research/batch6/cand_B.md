# Kandidatai B (gyvunu, sportas/turizmas, baldai, namai, elektronika, apsvietimas, santechnika)

(Pildoma eigoje. Patikrinimų laikai UTC, 2026-10-06. Pastaba: HTTPS eina per proxy, todėl tikro sertifikato galiojimo datos nematyti — įrodymas yra curl klaidos tekstas.)

## pyramis.lt
- Įmonė / ką parduoda: UAB "Dovita" — oficialus Pyramis atstovas LT; akmens masės ir nerūdijančio plieno plautuvės, maišytuvai, gartraukiai, mini virtuvės (aktyvus katalogas, kainos pvz. €219, €299).
- Platforma: OpenCart 1.5.x — `catalog/view/javascript/jquery/jquery-1.7.1.min.js` + `jquery-ui-1.8.16`, colorbox, tema `lexus_mobile` (OC 1.5 tema); jquery-1.7.1 failo `Last-Modified: Tue, 18 Mar 2014`.
- Kategorija: **big**
- El. paštas: info@pyramis.lt (footer pagrindiniame + `http://pyramis.lt/index.php?route=information/contact`)
- Įrodymai:
  - HTTPS sugedęs: `curl https://pyramis.lt/` ir `https://www.pyramis.lt/` → `curl: (60) SSL certificate problem: certificate has expired` (ssl_verify_result=10). 07:41 ir 07:47.
  - http neperadresuoja: `http://pyramis.lt/` → 200 (lieka http). 07:41 ir 07:47.
  - Prisijungimo forma per nešifruotą ryšį: `http://pyramis.lt/index.php?route=account/login` → `<form action="http://pyramis.lt/index.php?route=account/login"` (slaptažodis siunčiamas be šifravimo). 07:47.
  - Sena platforma: jQuery 1.7.1 (2011 m.), OpenCart 1.5; footer `© 2014 Visos teisės saugomos. UAB "Dovita"`. 07:41 ir 07:47.
- Detalė laiškui: atidarius https://pyramis.lt naršyklė rodo įspėjimą apie pasibaigusį sertifikatą; pvz. prekė „Akmens masės plautuvė Alazia (100x50)“ (`http://pyramis.lt/plautuves/akmens-mases-plautuve-alazia-100x50-1-1-2b-1d`) atsidaro tik per nesaugų http, o paskyros prisijungimas siunčia slaptažodį be šifravimo.
- Patarimas patiems: paprašyti hostingo įjungti nemokamą Let's Encrypt sertifikatą su automatiniu atnaujinimu.
- Siūloma kaina: SSL + http→https peradresavimas + mixed content tvarkymas 80–120 €; platformos perkėlimas iš OC 1.5 į OC 3/4 — preliminariai nuo 500 € (+ PVM).
- Siūlomas darbas ir trukmė: SSL 1 d.; migracija į naują OpenCart su produktų/kategorijų perkėlimu 2–3 sav.

## raisantas.lt
- Įmonė / ką parduoda: R. Stanaičio įmonė „Raisantas“ — šildymo/šaldymo įranga: katilai, vandens šildytuvai, šilumos siurbliai, radiatoriai, kondicionieriai (aktyvus katalogas, pvz. „Elektriniai radiatoriai“ 229 prekės, „Dujiniai katilai“ 112).
- Platforma: OpenCart 1.5.x — `jquery-1.7.1.min.js`, `jquery-ui-1.8.16`, colorbox, OC 1.5 footer komentaras „Please donate via PayPal to donate@opencart.com“; tema `pav_clothes` (drabužių parduotuvės tema).
- Kategorija: **big**
- El. paštas: raisantas@gmail.com (footer + `https://www.raisantas.lt/index.php?route=information/contact`)
- Įrodymai:
  - Sena platforma: OpenCart 1.5 su jQuery 1.7.1 (2011 m.), footer `© 2017 R.Stanaičio įmonė Raisantas`. 07:41 ir 07:47.
  - Sugedę meniu punktai: meniu nuorodos „Anglies pluošto šildymo kilimėliai“ ir „Kieto kuro katilai“ veda į `https://www.raisantas.lt/index.php?route=product/category&path=0` → HTTP 404, puslapyje „Kategorija nerasta!“. 07:42 ir 07:47.
  - Pagrindiniame puslapyje nuoroda į `index.php?route=product/product&product_id=` (tuščias ID) → HTTP 404 „Prekė nerasta!“. 07:42 ir 07:47.
  - HTTPS veikia, http→https peradresuoja (ne problema).
- Detalė laiškui: viršutiniame meniu paspaudus „Kieto kuro katilai“ arba „Anglies pluošto šildymo kilimėliai“ atsidaro „Kategorija nerasta!“, nors tokios kategorijos svetainėje yra (pvz. /kieto-kuro-katilai veikia).
- Patarimas patiems: meniu nustatymuose pakeisti tų dviejų punktų nuorodas į teisingas kategorijas.
- Siūloma kaina: meniu nuorodų sutvarkymas 50–80 €; perkėlimas iš OC 1.5 į OC 3/4 su ~1000+ prekių — preliminariai nuo 600 € (+ PVM).
- Siūlomas darbas ir trukmė: nuorodos — 1 val.; migracija 3–4 sav.

## elmega.lt
- Įmonė / ką parduoda: ELMEGA — elektros prekės (kabeliai, termosusitraukiantys vamzdeliai, gofruoti vamzdžiai, kabelių kanalai), kainos pvz. €10.50, €7.60.
- Platforma: OpenCart 2.x — `jquery-2.1.1.min.js`, tema `catalog/view/theme/lexus_megashop` (Pavothemes, OC2).
- Kategorija: **quick**
- El. paštas: info@elmega.lt (footer + `https://www.elmega.lt/index.php?route=information/contact`)
- Įrodymai:
  - Paliktas temos demo „Panel Tool“: kiekviename puslapyje `<div id="pav-paneltool" class="hidden-sm hidden-xs">` su `<h4>Panel Tool</h4>` ir pasirinkimais „Theme: default / aqua / christmas / orange / purple“, „Layout: Full Width…“; `paneltool.css`: `.paneltool{position: fixed; … z-index: 9999}` — kompiuteryje šone matomas krumpliaratis, pirkėjas gali perjungti parduotuvės spalvas. 07:43 ir 07:48.
  - Tuščios kategorijos meniu: `index.php?route=product/category&path=106` („Termosusitraukiantys vamzdeliai su klijais“), `path=107` („Termosusitraukiančios pirštinės“), `path=102` („Strypiniai antgaliai“) → „Šioje kategorijoje prekių nėra“. 07:49 ir 07:51.
  - Redirect grandinė: `https://elmega.lt/` → 301 `http://www.elmega.lt/` → 301 `https://www.elmega.lt/` (https→http šuolis). 07:43 ir 07:48.
  - Footer `© 2017-2023`. 
- Detalė laiškui: kompiuteriu atidarius elmega.lt šone kabo temos „Panel Tool“ krumpliaratis, per kurį bet kuris lankytojas gali perjungti dizainą į „christmas“ ar „purple“ spalvas.
- Patarimas patiems: temos (Pav Megashop) nustatymuose išjungti „Panel Tool“ / pašalinti paneltool modulį.
- Siūloma kaina: panelės pašalinimas + tuščių kategorijų paslėpimas + redirect sutvarkymas 60–120 € (+ PVM).
- Siūlomas darbas ir trukmė: 0,5–1 d.

## viskaszoo.lt
- Įmonė / ką parduoda: VisKasZoo — gyvūnų prekės (maistas, konservai, skanėstai šunims, katėms, graužikams, paukščiams, žuvims), kainos pvz. 12,90 €, 17,90 €.
- Platforma: OpenCart 3.x — tema `catalog/view/theme/journal3`, `index.php?route=`.
- Kategorija: **quick**
- El. paštas: info@viskaszoo.lt (footer + `https://www.viskaszoo.lt/index.php?route=information/contact`)
- Įrodymai:
  - http neperadresuoja į https: `http://viskaszoo.lt/` → 200 ir `http://www.viskaszoo.lt/` → 200 (be redirect); http versijoje `<base href="http://www.viskaszoo.lt/">` → naršyklė rodo „Nesaugu“. 07:35 ir 07:51.
  - Tuščios kategorijos meniu (meniu skaitliukas „0“, puslapyje „Šioje kategorijoje nėra prekių“): /egzotiniams-gyvunams/iranga/apsvietimas, /iranga/sildymas, /iranga/dekoracijos-iranga, /egzotiniams-gyvunams/maistas-egzotiniams-gyvunams, /egzotiniams-gyvunams/vitaminai-ir-mineralai, Terariumai (path=264_265), /zuvims/vandens-prieziuros-priemones, /pauksciams/skanestai-pauksciams — 9 tušti punktai; visa „Egzotiniams gyvūnams“ šaka turi tik 1 prekę. 07:38 ir 07:51.
  - Meniu nuorodos su tarpais/neužkoduotais simboliais (pvz. `/Konservuotas-visavertis-edalas-sunims-su-jautiena-gabaleliais-svelniame-padaze-1250 g`, `/image/catalog/foto instai.png`) ir pusė meniu nuorodų kietai įrašytos su `http://`. 07:35.
- Detalė laiškui: meniu „Egzotiniams gyvūnams“ → „Įranga“ → „Apšvietimas“/„Šildymas“ ir „Maistas“ atsidaro tušti („Šioje kategorijoje nėra prekių“); įvedus viskaszoo.lt be https lieka „Nesaugu“.
- Patarimas patiems: Journal3/OpenCart nustatymuose paslėpti tuščias kategorijas; .htaccess pridėti http→https 301.
- Siūloma kaina: http→https + nuorodų sutvarkymas + tuščių kategorijų tvarka 60–120 € (+ PVM).
- Siūlomas darbas ir trukmė: 0,5–1 d.

