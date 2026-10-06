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

## sildymasjums.lt
- Įmonė / ką parduoda: UAB „ŠildymasJums“ (Klaipėda, Minijos g. 49) — šilumos siurbliai, dujiniai katilai, rekuperatoriai, radiatoriai, dūmtraukiai, vonios įranga (didelis katalogas: pvz. „Šilumos siurbliai“ 2191 prekė; kainos 799,00 €, 445,45 €).
- Platforma: OpenCart 2.x — `catalog/view/theme/default`, `jquery-2.1.1.min.js`, OpenCart footer komentaras „Please donate via PayPal to donate@opencart.com“.
- Kategorija: **quick**
- El. paštas: info@sildymasjums.lt (header + `https://www.sildymasjums.lt/index.php?route=information/contact`)
- Įrodymai:
  - http neperadresuoja į https: `http://sildymasjums.lt/` → 200 ir `http://www.sildymasjums.lt/` → 200 (be redirect) → naršyklė rodo „Nesaugu“. 08:04 ir 08:23.
  - Tuščios kategorijos meniu (tik antraštė + mygtukas „Tęsti“, 0 prekių): /sildymo-iranga/izoliacines-plokts, /sildymo-iranga/vamzdziai-sildymui-vandentiekiui, /sildymo-iranga/vamzdziu-fasonines-detales, /granuliniai-katilai/Granuliniai-degikliai-NBE, /granuliniai-katilai/nbe-black-star- (5 vnt.). 08:06 ir 08:23.
  - Sugadinti SEO adresai — lietuviškos raidės tiesiog išmestos: /vonios-ranga („Vonios įranga“), /montavimo-priedai-ilumos-siurbliams („šilumos“), /nerudijancio-plieno-dmtraukiai, /dmtraukiai-dujiniams-katilams („dūmtraukiai“), /izoliacines-plokts („plokštės“), /oro-valytuvai--drkintuvai. 08:06.
- Detalė laiškui: meniu „Šildymo įranga“ → „Izoliacinės plokštės“ ar „Vamzdžiai (šildymui-vandentiekiui)“ atsidaro tušti; nuorodos tipo sildymasjums.lt/vonios-ranga ir /montavimo-priedai-ilumos-siurbliams praranda raides (blogai Google paieškai).
- Patarimas patiems: paslėpti tuščias kategorijas admin'e (Status: Off); .htaccess pridėti http→https 301.
- Siūloma kaina: https peradresavimas + tuščių kategorijų tvarka 50–100 €; SEO URL perrašymas su 301 peradresavimais 100–200 € (+ PVM).
- Siūlomas darbas ir trukmė: 1–2 d.

## balduideja.lt
- Įmonė / ką parduoda: „Baldų idėja“ (Vilnius, Klaipėda) — svetainės, valgomojo, miegamojo, biuro, prieškambario baldai ir kolekcijos (pvz. „IŠPARDAVIMAI!“ 42 prekės, kainos 499.00 €, 1,890.00 €).
- Platforma: OpenCart 2.x — `catalog/view/theme/pav_furniture`, `jquery-2.1.1.min.js`, `index.php?route=product/category`.
- Kategorija: **quick**
- El. paštas: balduideja.vilnius@gmail.com, balduideja.klaipeda@gmail.com (footer pagrindiniame puslapyje https://balduideja.lt/)
- Įrodymai:
  - Meniu nuorodos į neegzistuojančias kategorijas (HTTP 404 „Kategorija nerasta!“): meniu punktas „Nature“ → `http://balduideja.lt/svetaines-baldu-kolekcijos/nature-stalai-valgomojo-baldai-masyvas-lukstas-krysiak-baldu-ideja`; „Mango“ → `http://balduideja.lt/svetaines-baldu-kolekcijos/svetaines-valgomojo-korpusiniu-kolekcija-baldu-ideja-mc-akcent-mango`. 08:42 ir 08:48.
  - Tuščios meniu kategorijos („Šioje kategorijoje prekių nėra“): „Atelie“ (/svetaines-baldu-kolekcijos/valgomojo-korpusiniai-svetaines-baldai-atelie-krysiak-baldu-ideja), „Čiužiniai“ (/miegamojo-baldai/ciuziniai), „Roma“ (path=276_278), „Mestre“ (path=276_281). 08:42 ir 08:48.
  - http neperadresuoja: `http://balduideja.lt/` → 200 ir `http://www.balduideja.lt/` → 200; meniu nuorodos kietai įrašytos su `http://`, todėl paspaudus meniu iš https versijos lankytojas numetamas į nesaugią „Nesaugu“ versiją. 08:44 ir 08:48.
  - Smulkiau: kainos rodomos angliškai formatuotos „1,890.00 €“ (LT turėtų būti „1 890,00 €“).
- Detalė laiškui: meniu „Korpusinių baldų kolekcijos“ paspaudus „Nature“ arba „Mango“ atsidaro „Kategorija nerasta!“, o „Čiužiniai“ ir „Atelie“ tušti.
- Patarimas patiems: admin'e išjungti (Status: Off) tuščias ir ištrintas kategorijas iš meniu; .htaccess http→https 301; temos meniu nuorodas pakeisti į santykines/https.
- Siūloma kaina: 80–150 € (+ PVM) — meniu ir kategorijų sutvarkymas, https peradresavimas, kainų formatas.
- Siūlomas darbas ir trukmė: 1 d.

## foleta.lt
- Įmonė / ką parduoda: UAB „Foleta“ — židiniai, ketinės krosnelės (HWAM, Romotop, Contura, Thorma, Jotul), dūmtraukiai, šilumos siurbliai; kainos pvz. 1,700 €, 2,408–3,240 €.
- Platforma: WordPress 5.1.1 + WooCommerce 3.5.6 — `<meta name="generator" content="WordPress 5.1.1">`, `<meta name="generator" content="WooCommerce 3.5.6">`, `wp-embed.min.js?ver=5.1.1`, `woocommerce.css?ver=3.5.6`.
- Kategorija: **big**
- El. paštas: info@foleta.lt (https://www.foleta.lt/kontaktai/)
- Įrodymai:
  - Labai pasenusi platforma: WordPress 5.1.1 (2019 m. kovas) ir WooCommerce 3.5.6 (2019 m. pradžia) — ~7 metai be atnaujinimų, su daugybe žinomų saugumo spragų (dabartinės versijos WP 6.x/7.x, WooCommerce 9–10+). 08:48 ir 08:49.
  - Footer `© 2018 UAB "Foleta"`. 08:48 ir 08:49.
  - Prekių kodai sugadinti dubliavimo: produkto puslapyje matoma „Produkto kodas: HU3LG 21-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-2-1-2-1-1-1-1-1-2-1-1-2-1-3-1-2-1-1-1-1-1“ (`https://www.foleta.lt/parduotuve/krosnele-romotop-laredo-t-04-5-2-kw/`); toks pats šiukšlinis SKU rastas 5 iš 24 patikrintų kategorijų prekių + 2 pagrindiniame (izoliuota, ne katalogo masto). 08:51.
  - Kainos formatuotos angliškai: „1,700 €“, „2,030 €“ (LT turėtų būti „1 700 €“). 08:47.
- Detalė laiškui: krosnelės ROMOTOP LAREDO T 04 puslapyje produkto kodas rodomas kaip „HU3LG 21-1-1-1-1-1-1-1-1…“ (kelios dešimtys „-1“), o svetainė veikia ant 2019 m. WordPress/WooCommerce versijų.
- Patarimas patiems: bent jau padaryti pilną atsarginę kopiją ir atnaujinti įskiepius; Woo nustatymuose pakeisti tūkstančių skyriklį į tarpą, dešimtainį į kablelį.
- Siūloma kaina: WP/WooCommerce/temos atnaujinimas su testavimu ir SKU sutvarkymu — preliminariai nuo 250 € (jei tema nesuderinama su nauja versija — dizaino atnaujinimas 400–600 €) (+ PVM).
- Siūlomas darbas ir trukmė: 3–5 d. (atnaujinimas staging'e, testai, perkėlimas).

## balticmobiles.lt
- Įmonė / ką parduoda: Balticmobiles.lt — mobilieji telefonai, planšetės, dėklai, apsauginiai stiklai ir priedai (labai aktyvus: naujausi Xiaomi Redmi Note 17, iPhone 16e; „Aksesuarai ir priedai“ 6166 prekės; kainos 319.00 €, 498.00 €).
- Platforma: OpenCart 1.5.x — `catalog/view/javascript/jquery/jquery-1.7.1.min.js` (`Last-Modified: Tue, 24 Jun 2014`), `jquery-ui-1.8.16.custom.min.js`, colorbox, tema `pav_citymart`.
- Kategorija: **big**
- El. paštas: info@balticmobiles.lt (header/footer https://www.balticmobiles.lt/)
- Įrodymai:
  - Sena platforma: OpenCart 1.5 su jQuery 1.7.1 (2011 m.) — senas kodas be saugumo atnaujinimų, nors parduotuvė prekiauja 2026 m. modeliais. 08:56 ir 08:59 (+09:03).
  - Kategorija „Blackview“ rodo ne tas prekes: `https://www.balticmobiles.lt/mobilieji-telefonai/blackview` → „Rodoma nuo 1 iki 102 iš 872“, visi 102 rodomi produktai yra „Apple iPhone …“ (0 Blackview telefonų). 09:00 ir 09:03.
  - Tuščios gamintojų kategorijos meniu „Mobilieji telefonai“: /mobilieji-telefonai/blackberry, /asus, /microsoft, /estar → „Šioje kategorijoje nėra prekių“ (4 vnt.). 08:57 ir 08:59.
  - HTTPS ir http→https veikia (ne problema).
- Detalė laiškui: meniu „Mobilieji telefonai“ → „Blackview“ atidaro 872 prekių sąrašą, kuriame vien Apple iPhone; Blackberry, Asus, Microsoft ir eStar — tušti.
- Patarimas patiems: admin'e išjungti tuščias gamintojų kategorijas ir patikrinti Blackview kategorijos priskyrimą/filtrą.
- Siūloma kaina: kategorijų sutvarkymas 50–100 €; perkėlimas iš OC 1.5 į OC 3/4 su ~8000 prekių — preliminariai nuo 700 € (+ PVM).
- Siūlomas darbas ir trukmė: kategorijos — 0,5 d.; migracija 3–5 sav.

## kamtojabaldai.lt  (SU IŠLYGA — kainų nematyti, nes katalogas neveikia)
- Įmonė / ką parduoda: „Kamtoja baldai“ — lauko / sodo baldai (poilsio komplektai, gultai, terasos stalai ir kėdės).
- Platforma: buvęs OpenCart (`catalog/view/theme/default`, `jquery-2.1.1.min.js`, `image/cache/catalog/...`, krepšelio blokas „Prekių krepšelis tuščias“), dabar pagrindinis puslapis atrodo kaip statinė HTML kopija (`Last-Modified: Tue, 23 Jun 2026`), `index.php?route=...` grąžina hostingo 404.
- Kategorija: **big**
- El. paštas: kamila.jankovska@kamtoja.lt (pagrindinis puslapis); Kamila.jankovska@kamtojabaldai.lt, Tomas.jankovski@kamtojabaldai.lt (https://www.kamtojabaldai.lt/kontaktai.html). MX įrašai abiem domenams yra (Outlook).
- Įrodymai:
  - Visas prekių meniu veda į 404: „Produktai“/„Poilsio baldai“ → `https://www.kamtojabaldai.lt/Poilsiniai lauko sodo baldai` (URL su tarpais) → 404; „Gultai“ → `/lauko sodo baldai Palermo Gultas` → 404; „Stalai ir kėdės“ → `/Terasos stalai ir kėdės` → 404; vienintelė prekės nuoroda `/poilsinis-komplektas-liguria` → 404. 08:58 ir 09:07.
  - Krepšelis neveikia: `index.php?route=checkout/cart` → 404 („Sorry, the page you’re looking for doesn’t exist. Hosted at Interneto vizija“). 08:59 ir 09:07.
  - Footer `© 2015 Visos teises saugomos Kamtoja baldai.lt`; sitemap.xml paskutinis `lastmod` 2016-05-02.
- Detalė laiškui: paspaudus bet kurį meniu punktą („Poilsio baldai“, „Gultai“, „Stalai ir kėdės“) atsidaro „404 – page doesn’t exist“, t.y. lankytojas nemato nė vienos prekės ir negali nieko užsisakyti.
- Patarimas patiems: susisiekti su hostingu (Interneto vizija) — atrodo, kad po perkėlimo liko tik statinis pradinis puslapis.
- Siūloma kaina: atkūrimas / nauja paprasta parduotuvė (OpenCart arba WooCommerce) su esamu turiniu — preliminariai nuo 400 € (+ PVM).
- Siūlomas darbas ir trukmė: 1–2 sav.
- IŠLYGA: kriterijus 3 („prekių su kainomis“) nepatikrinamas — kainų niekur nematyti, nes katalogas neveikia; gali būti, kad įmonė parduotuvės nebevysto. Siųsti tik jei vartotojas sutinka.

---

## Atmesti
- zookatalogas.lt — labai stiprus „big“ (OpenCart 1.5, jQuery 1.7.1, nėra viewport, fiksuotas 980px plotis, © 2017), BET vienintelis nurodytas el. paštas info@hiltonherbs.lt — domenas hiltonherbs.lt neegzistuoja (DNS NXDOMAIN, nėra MX) → laiškas nepasieks. Galima tik telefonu.
- etsistemos.lt — matomas PHP „Notice: Undefined variable: config_coyynfirm_cookies_button in /home/etsistemos/domains/.../header.tpl on line 111“ slapukų mygtuke + http be redirect, © 2015, BET kainų katalogas neskelbia (tik užklausa) → nekriterijus 3. Galima, jei kainos nebūtinos.
- mocca.lt — OpenCart 2 (theme638), https sertifikato grandinė nepatikima (curl 60 „unable to get local issuer certificate“), http be redirect; bet drabužiai — ne mano nišos (perduoti kitam agentui).
- kvarcas.lt — apšvietimas, jQuery 1.7.1, nėra viewport, © 2012, WP 4.9 — bet ne parduotuvė (be kainų), turinys 2011 m.
- ledlumina.lt — „About Us/Contact Us“ tik HTML komentare (nematomas); WP 6.9 atnaujintas → per maža.
- aquasharks.lt — WP/Woo atnaujinti, tik © 2018 → per maža.
- santechnikapigiau.lt — Journal2, bet veikia tvarkingai.
- argutus.lt, artaveniu.lt, krona-kitchen.lt, art-de-vivre.lt, persiski-kilimai.lt, techcoat.lt, cpbaldai.lt, patalai.lt, stikloplastis.lt, jwtrade.lt, miestoturgus.lt, 888dovanos.lt, navalda.lt, vannavanna.lt — SSL problemos, bet ne parduotuvės su kainomis / peradresuoja į kitą domeną / didmena / nėra el. pašto.
- uzuolaida.lt, baldustudija.lt, daistana.lt, santechprekyba.lt, silumeka.lt, budhaus.lt, piritas.lt, voniavonioje.lt, kamadoclub.lt, makso-baldai.lt — pasenęs WP ar © metai, bet be kainų / be el. pašto / tvarkingi.
- holo.lt (PHP Warning) — odontologija, ne niša.
- jojimoprekes.lt, akvareef.lt, ledlife.lt, ledima.lt, zuklys.lt, fitsport.lt, credo.lt, euroliux.lt — patikrinta, tikrų rimtų trūkumų nerasta (jojimoprekes „404“ buvo mano URL dekodavimo klaida — patikrinus 200).
- hi-power.lt — elementų/baterijų parduotuvė, numatytoji kalba anglų, daug tuščių kategorijų („There are no products to list in this category“), bet neaišku, ar LT įmonė (adresas nematomas) — nepakankamai patikrinta.
- h2o.lt — http be redirect + keli SEO URL su „-and-scaron-“ (pvz. /automatinis-mink-and-scaron-tinimo-filtras-pentair-a-5608-lt-html), bet per smulku; el. paštas kitame domene (info@akvatechnika.lt).
- foleta.lt SKU artefaktai — įtraukta į foleta įrašą kaip papildoma detalė, ne katalogo masto.

Iš viso: 9 (big 5, quick 4) — iš jų kamtojabaldai.lt su išlyga (be patikrinamų kainų); be jos 8 (big 4, quick 4).
