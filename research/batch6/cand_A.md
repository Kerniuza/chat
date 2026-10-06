# Kandidatai A (statyba, auto/moto, sodas, zvejyba/medziokle, dviraciai, irankiai, gamyba)

Tyrimas pradetas 2026-10-06. Saltinis: 1551.lt katalogo kategorijos + automatinis skenavimas (curl/python), tada rankinis patikrinimas.

## raisantas.lt
- Įmonė / ką parduoda: R. Stanaičio įmonė „Raisantas“ – šildymo/šaldymo įranga (katilai, radiatoriai, šilumos siurbliai, kondicionieriai, vandens šildytuvai), su el. parduotuve.
- Platforma: OpenCart 1.5.x (catalog/view/javascript/jquery/jquery-1.7.1.min.js + jquery-ui-1.8.16.custom.min.js – 1.5.x rinkinys; tema catalog/view/theme/pav_clothes; HTML komentaras „OpenCart is open source software… donate@opencart.com“)
- Kategorija: big
- El. paštas: raisantas@gmail.com (pagrindinis puslapis https://www.raisantas.lt/, footer/kontaktų blokas)
- Įrodymai (patikrinta du kartus: 07:44 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Sena platforma: `curl https://www.raisantas.lt/ | grep jquery` → `catalog/view/javascript/jquery/jquery-1.7.1.min.js`, `jquery-ui-1.8.16.custom.min.js` (OpenCart 1.5 – ~2011–2013 m. kartos). Footer: „© 2017 R.Stanaičio įmonė Raisantas…“. [07:44 UTC, 07:48 UTC]
  - 7 pagrindinio meniu kategorijos veda į neegzistuojančius puslapius (HTTP 404, antraštė „Produktų kategorija nerasta!“): „Kieto kuro katilai“ ir „Anglies pluošto šildymo kilimėliai“ → `index.php?route=product/category&path=0`; „Skysto kuro katilai“ → path=501; „Vonios ir virtuvės įranga“ → path=190; „Šildymas dujų balionais“ → path=355; „Vogel&Noot plieniniai radiatoriai“ → path=444; „Infraraudonųjų spindulių šildytuvai“ → path=462. `curl -o /dev/null -w "%{http_code}"` → 404 visiems 6 URL (abu kartus 07:44 ir 07:48 UTC).
  - Kitos kategorijos veikia, yra prekių su kainomis (pvz. 81.00€ pagrindiniame), parduotuvė gyva.
- Viena detalė laiškui: meniu punktas „Kieto kuro katilai“ (sezoninė, šildymo sezono prekė!) atidaro „Produktų kategorija nerasta!“.
- Patarimas patiems: admin'e Dizainas → Meniu / Kategorijos – perrišti 7 meniu nuorodas į esamas kategorijas (path=0 reiškia ištrintą/neparinktą kategoriją).
- Siūloma kaina: meniu nuorodų sutvarkymas 50–100 €; OpenCart 1.5 → 3.x/4.x atnaujinimas su tema ir prekių perkėlimu – preliminariai nuo 600 € (+ PVM)
- Siūlomas darbas ir trukmė: nuorodos – 1 d.; platformos atnaujinimas – 2–4 sav.

## v-s.lt
- Įmonė / ką parduoda: UAB „Viskas sodininkams“ (Vilnius) – sodo technika: vejapjovės, robotai, traktoriukai, krūmapjovės, pjūklai, motoblokai.
- Platforma: WooCommerce 9.7.3 / WordPress 6.7.9 (meta generator), WPML 4.7.1, Visual Composer
- Kategorija: quick
- El. paštas: info@v-s.lt (footer, pvz. https://v-s.lt/produkto-kategorija/uncategorized-lt/)
- Įrodymai (patikrinta du kartus: 07:40 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Meniu „Kategorijos“ sąraše rodoma techninė kategorija „Uncategorized @lt“ (WPML artefaktas) → https://v-s.lt/produkto-kategorija/uncategorized-lt/ atidaro tuščią puslapį „Pagal Jūsų pasirinkimą prekių nėra.“ (`grep '>Uncategorized @lt'` pagrindiniame HTML) [07:40, 07:48 UTC]
  - http://v-s.lt/ neperadresuoja į https: `curl -w "%{http_code} %{redirect_url}" http://v-s.lt/` → `200` be redirect (abu kartus). Svetainė pasiekiama nešifruotai – naršyklė rodo „Nesaugu“, jei atėjo per http nuorodą.
  - Prekės kopijavimo artefaktas: https://v-s.lt/parduotuve/sodo-traktoriai/sodo-traktoriukas-bs-intek-20-ag-107-cm-kopijuoti/ – URL sako „BS Intek 20 Ag … kopijuoti“, o antraštė „Sodo traktoriukas SECO 16 Ag, 107 cm.“
  - Skirtingos prekės su ta pačia nuotrauka: „Grandininis pjūklas 54.0 cm³“ ir „54.5 cm³“ abu KJ5400Z-349x400.jpg; krūmapjovės 40.1 cm³ ir 50.1 cm³ abi JMBC5021HRS-400x400.jpg. Prekė „Krūmapjovė 22.5 cm³“ turi URL …/19-8-cm-kw-0-8-49-kg/ (nesutampa).
- Viena detalė laiškui: kategorijų sąraše matosi „Uncategorized @lt“, kurį paspaudus – „prekių nėra“.
- Patarimas patiems: WooCommerce → Prekės → Kategorijos: pervadinti/paslėpti „Uncategorized @lt“ (ar nustatyti kitą numatytąją kategoriją); įjungti http→https 301 peradresavimą .htaccess.
- Siūloma kaina: kelios smulkios klaidos 100–200 € (+ PVM)
- Siūlomas darbas ir trukmė: kategorija, https redirect, prekių URL/nuotraukų sutvarkymas – 1–2 d.

## darbobatai.lt
- Įmonė / ką parduoda: UAB „Ravioli“ – darbo drabužiai, darbo batai, apsaugos priemonės, pirštinės, gesintuvai (statybininkams/įmonėms).
- Platforma: WooCommerce 3.3.6 / WordPress 4.9.26 (meta generator), jQuery 1.12.4, Slider Revolution 5.4.6.4, WPBakery
- Kategorija: big
- El. paštas: pardavimai@darbobatai.lt (pagrindinis puslapis https://darbobatai.lt/, footer; kontaktai https://darbobatai.lt/kontaktai/ → 200)
- Įrodymai (patikrinta du kartus: 07:47 ir 07:51 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Sena platforma: `curl https://darbobatai.lt/ | grep generator` → `WordPress 4.9.26`, `WooCommerce 3.3.6`, `Slider Revolution 5.4.6.4`; `wp-includes/js/jquery/jquery.js?ver=1.12.4`. WP 4.9 šaka – 2017–2018 m., WooCommerce 3.3 – 2018 m. pradžia (dabartinės: WP 6.x/7.x, Woo 10.x). [07:47 UTC, 07:51 UTC – identiška]
  - Kategorijų puslapių pavadinimai su angl. „Archives“: https://darbobatai.lt/pruduktai/darbo-batai/ → `<title>Darbo batai Archives | Darbo Batai</title>` (taip rodoma Google paieškoje).
  - Kategorijų URL bazėje rašybos klaida „pruduktai“ (https://darbobatai.lt/pruduktai/darbo-drabuziai/ ir kt.); meniu viršuje angl. „Account“.
  - Parduotuvė gyva: prekės su kainomis „475.00 € / 440.00 € su PVM“, „380.00 € 360.00 €“ pagrindiniame.
- Viena detalė laiškui: Google'e kategorija rodoma kaip „Darbo batai Archives“; o variklis po apačia – WooCommerce 3.3.6 iš 2018 m., kuris saugumo atnaujinimų nebegauna.
- Patarimas patiems: bent jau atnaujinti WordPress branduolį/įskiepius (su atsargine kopija) ir Yoast/SEO nustatymuose pakeisti archyvų pavadinimo šabloną.
- Siūloma kaina: platformos (WP+Woo+tema+Slider Revolution) atnaujinimas ir patikra – preliminariai nuo 300 € (+ PVM); jei tema nesuderinama – dizaino atnaujinimas 250–600 €
- Siūlomas darbas ir trukmė: kopija → staging → atnaujinimas → testas (krepšelis, mokėjimai) – 3–7 d.

## stabdziudalys.lt
- Įmonė / ką parduoda: stabdžių dalys automobiliams (armuotos žarnelės, diskų apsaugos, stabdžių skysčiai, Microcar/Ligier dalys) + stabdžių sistemų gamyba/servisas.
- Platforma: WooCommerce 10.3.8 / WordPress 7.1.2 (generator), WPBakery 7.9
- Kategorija: quick
- El. paštas: info@stabdziudalys.lt (header „SKAMBINKITE: +37067148044 info@stabdziudalys.lt“, https://stabdziudalys.lt/); taip pat stabdziai44@gmail.com
- Įrodymai (pagrindinis https://stabdziudalys.lt/, matomas tekstas per bs4, 07:49 UTC) (patikrinta du kartus: 07:49 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Prisijungimo langas visas angliškai: „Sign in … Username or email * Password * Please enter an answer in digits: 7 + ten = Log in Lost your password? Remember me No account yet? Create an Account“; paieška „Search for: Search“; krepšelis „Cart ( o ) 0 / 0,00 €“.
  - Parduotuvės puslapio pavadinimas angliškai: https://stabdziudalys.lt/shop/ → `<title>Shop – Stabdžių dalys</title>`.
  - Pagrindiniame rodomi seni blogo įrašai „Read More … 23 Bal Uncategorized Cypia stabdžiai? 23 balandžio, 2015 By admin“ (https://stabdziudalys.lt/category/uncategorized/).
  - Prekės URL nesutampa su kodu: „Disko apsauga Hyundai / Kia 582512P500 left“ → URL …/disko-apsauga-hyundai-kia-282512p500/.
  - Parduotuvė gyva: 2026/09 įkeltos nuotraukos, kainos 11,00 € – 138,00 €.
- Viena detalė laiškui: lietuviškame puslapyje prisijungimo langas „Sign in / Lost your password? / Create an Account“ ir antispam klausimas „7 + ten =“ angliškai.
- Patarimas patiems: įdiegti/atnaujinti lietuvišką vertimą (Nustatymai → Kalba = Lietuvių, Atnaujinimai → Vertimai) ir temos vertimą per Loco Translate.
- Siūloma kaina: kelios smulkios klaidos 100–150 € (+ PVM)
- Siūlomas darbas ir trukmė: vertimai, „Uncategorized“ pervadinimas, puslapių title – 1 d.

## dviratininkams.lt
- Įmonė / ką parduoda: UAB „Dviratininkas“ (Kaunas) – dviračiai (Cube ir kt.), dalys, aksesuarai, servisas.
- Platforma: WooCommerce 10.8.1 (plugins/woocommerce/...?ver=10.8.1), WordPress (wp-content)
- Kategorija: quick
- El. paštas: info@dviratininkams.lt (Cloudflare data-cfemail header'yje https://dviratininkams.lt/, dekoduota XOR)
- Įrodymai (patikrinta du kartus: 07:49 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Pagrindinio puslapio `<title>` tuščias: `curl https://dviratininkams.lt/ | grep '<title'` → `<title> </title>` (Google rodo tik adresą/atsitiktinį tekstą). [07:49 UTC]
  - Visi kiti puslapių pavadinimai baigiasi tuščiu „ : “ (trūksta svetainės pavadinimo): `<title> Kontaktai : </title>`, `<title> Apie Mus : </title>`, `<title> Produkto kategorijos Aksesuarai : </title>`, `<title> Cube Nuroad Pro mysticpurple’n’black 2027-M : </title>`.
  - Meta description visai svetainei tik „UAB Dviratininkas“.
  - Kiekvienas dydis – atskira prekė (cube-nuroad-pro-…-2027-xs / -s / -m / -l / -xl / -xxl – 6 atskiros prekės vietoj vienos su dydžio pasirinkimu) → katalogas išsipučia, dubliuojasi turinys.
- Viena detalė laiškui: pagrindinio puslapio pavadinimas tuščias, o kituose puslapiuose pavadinimas baigiasi „Kontaktai : “ – Google rezultatuose neatrodo gerai.
- Patarimas patiems: SEO įskiepyje (Yoast/Rank Math) nustatyti title šabloną „%%title%% | Dviratininkams.lt“ ir pagrindinio puslapio pavadinimą.
- Siūloma kaina: SEO title/meta sutvarkymas 80–150 €; dydžių sujungimas į variacines prekes – 150–300 € (+ PVM)
- Siūlomas darbas ir trukmė: title/meta – 1 d.; variacijos – 2–4 d.

## dazas.lt
- Įmonė / ką parduoda: „Tikrasis dažas“ – amerikietiški Coronado Paint / Benjamin Moore dažai, lakai, apdailos ir elektriniai įrankiai (Festool ir kt.), įrankių nuoma.
- Platforma: WooCommerce (woocommerce-blocks ?ver=2.5.14) / WordPress 5.1.26 (wp-includes …?ver=5.1.26), jQuery 1.12.4, Revolution Slider „rev=4.6.0“
- Kategorija: big
- El. paštas: info@dazas.lt (https://www.dazas.lt/ footer)
- Įrodymai (patikrinta du kartus: 07:50 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Sena platforma: `curl https://www.dazas.lt/ | grep -o "ver=5\.[0-9.]*"` → `wp-includes/css/dist/block-library/style.min.css?ver=5.1.26` (WordPress 5.1 šaka – 2019 m.), `wp-includes/js/jquery/jquery.js?ver=1.12.4`, `revslider/rs-plugin/css/settings.css?rev=4.6.0` (Revolution Slider 4.x – ~2014 m., žinomos saugumo spragos). [07:50 UTC]
  - Rašybos klaida parduotuvės puslapio pavadinime (rodomas Google): https://www.dazas.lt/parduotuve/ → `<title>Elekroninė amerikietiškų Coronado Paint dažų parduotuvė | Tikrasis dažas</title>` („Elekroninė“ be „t“).
  - Filtro antraštė angliškai „Brands“ tarp lietuviškų „Kategorija“, „Kaina“.
  - Gyva: kainos 89,00 €, 69,00 €, 5,95 € ir kt., © 2026.
- Viena detalė laiškui: parduotuvės puslapio pavadinime „Elekroninė“ – taip ir rodoma Google paieškoje.
- Patarimas patiems: pataisyti puslapio „Parduotuvė“ SEO pavadinimą; pervadinti valdiklį „Brands“ → „Gamintojai“.
- Siūloma kaina: WP 5.1 → 6.x + Woo + slider'io pakeitimas – preliminariai nuo 300 € (+ PVM); smulkmenos 50 €
- Siūlomas darbas ir trukmė: 3–5 d. (su staging ir testu)

## motogama.lt
- Įmonė / ką parduoda: „Motogama“ (Meistrų g. 16, Vilnius) – motociklai ir moto dalys („Respect the classics. Ride the legend.“).
- Platforma: WooCommerce / WordPress 7.0.6 (meta generator), WooCommerce tema „Autusin“ (demo turinys)
- Kategorija: big
- El. paštas: info@motogama.lt (footer „Email: info@motogama.lt“, http://www.motogama.lt/)
- Įrodymai (patikrinta du kartus: 07:54 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - HTTPS neveikia: `curl https://www.motogama.lt/` → `curl: (60) SSL certificate problem: unable to get local issuer certificate` (ssl_verify_result=20; tas pats be www); http://motogama.lt/ → 301 į **http**://www.motogama.lt/ (ne https). check_site: https="ssl_error", http_redirects_to_https=false. [07:54 UTC]
  - Parduotuvėje vietoj tikrų prekių – temos demo turinys su lotynišku „lorem ipsum“: prekės „beatae vitae dicta $ 72.00“, „totam rem aperiam $ 79.00“, „numquam eius modi $ 90.00“, „Nisi ut aliqu $ 60.00 – $ 70.00“; URL pvz. http://www.motogama.lt/?product=beatae-vitae-dicta, http://www.motogama.lt/?product=iste-natus-error-copy. Kainos doleriais (valiutos jungiklis „USD USD EUR“).
  - Antraštė „The best products of Autusin“ (temos pavadinimas), visas meniu angliškai: „Home Shop About Us All Category Uncategorized Automotive Body Parts … Smart Devices Dash Cam …“, „Shopping Cart … No products in the cart.“, „Sign in Or Register Forgot your password?“.
  - Sugadinta koduotė footer'yje: „©2024 ┬® 2026 Motogama. All rights reserved.“
- Viena detalė laiškui: atsidarius svetainę, „Featured Products“ rodo prekes „beatae vitae dicta“ ir „totam rem aperiam“ su kainomis doleriais – tai temos pavyzdinis turinys, ne jūsų prekės; o https adresas meta saugumo klaidą.
- Patarimas patiems: bent jau paslėpti/ištrinti demo prekes (Prekės → Visos → filtruoti pagal datą) ir perjungti valiutą į EUR; hostinge įjungti nemokamą Let's Encrypt sertifikatą.
- Siūloma kaina: SSL + http→https 50–120 €; demo turinio išvalymas, vertimas, EUR – 150–250 €; tikrų prekių kėlimas su aprašymais – pagal kiekį; viso „preliminariai nuo 400 €“ (+ PVM)
- Siūlomas darbas ir trukmė: SSL – 1 d.; parduotuvės paruošimas su prekėmis – 1–3 sav.
- Pastaba: tikrų prekių kol kas nėra (kriterijus „prekės su kainomis“ formaliai tenkinamas tik demo prekėmis) – bet verslas realus, svetainė akivaizdžiai nebaigta.

## enbaterija.lt
- Įmonė / ką parduoda: „Eurobaterija“ – baterijų, akumuliatorių, įkroviklių, apšvietimo, duomenų laikmenų didmeninė ir mažmeninė prekyba internetu.
- Platforma: OpenCart 1.5.x (catalog/view/javascript/jquery/jquery-1.7.1.min.js, jquery-ui-1.8.16, image/data/ katalogas, tema catalog/view/theme/omf2; HTML komentaras su donate@opencart.com)
- Kategorija: big
- El. paštas: info@eurobaterija.lt (pagrindinio puslapio viršutinis blokas https://enbaterija.lt/, eilutė 54)
- Įrodymai (patikrinta du kartus: 07:56 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Nėra viewport meta: `curl https://enbaterija.lt/ | grep -c 'name="viewport"'` → 0. Temoje YRA mobilios versijos CSS (catalog/view/theme/omf2/s.php?p=mobile2.scss su `@media (max-width:768px)`), bet be viewport žymės telefonas puslapį atvaizduoja kaip ~980 px darbalaukio versiją ir ši mobili CSS niekada neįsijungia – telefone svetainė mažytė, reikia didinti pirštais. [07:56 UTC]
  - Sena platforma: jquery-1.7.1.min.js, jquery-ui-1.8.16 (OpenCart 1.5 – ~2012–2013 m.).
  - Gyva: kainos 23.96€, 23.84€, 1.03€, 38.95€ pagrindiniame, Omniva paštomatų integracija, © 2026.
- Viena detalė laiškui: telefone atsidarius enbaterija.lt rodoma pilna kompiuterio versija sumažinta – nors mobilus stilius temoje jau yra, jis neįsijungia dėl vienos trūkstamos eilutės.
- Patarimas patiems: į catalog/view/theme/omf2/template/common/header.tpl <head> įdėti `<meta name="viewport" content="width=device-width, initial-scale=1">` ir patikrinti telefone.
- Siūloma kaina: viewport + mobilios versijos patikra/pataisymai 100–250 €; OpenCart 1.5 → 3.x/4.x migracija – preliminariai nuo 700 € (+ PVM)
- Siūlomas darbas ir trukmė: mobilumas – 1–2 d.; migracija – 3–5 sav.

## ofnis.lt
- Įmonė / ką parduoda: „Ofnis“ – pramoninė valymo technika ir įranga (HAKO, Kränzle, Cleanfix, Christ plovyklos, Buzil priemonės, Butzbach vartai).
- Platforma: WooCommerce / WordPress 5.5.22 (generator), jQuery 1.12.4, Revolution Slider
- Kategorija: quick (kelios klaidos kartu; su WP 5.5 atnaujinimu galėtų būti didesnis darbas)
- El. paštas: info@ofnis.lt (https://ofnis.lt/ footer)
- Įrodymai (patikrinta du kartus: 07:57 ir 08:03 UTC, 2026-10-06 – abu kartus rezultatas tas pats):
  - Pagrindiniame puslapyje matomas neveikiantis trumpasis kodas: tekstas „[aws_search_form]“ vietoj paieškos laukelio (`grep -c aws_search_form` → 3). [07:57 UTC]
  - Pagrindinio slider'io skaidrė „BUZIL VALYMO PRIEMONĖS“ ir mygtukas „PLAČIAU“ veda į https://ofnis.lt/product-category/buzil-valymo-priemones/ekologines-valymo-priemones/ → HTTP 404 „Puslapis nerastas – Ofnis“ (kitos 12 kategorijų nuorodų → 200).
  - Meniu dubliuotas punktas: „PAGRINDINIS, APIE MUS, PRODUKTAI, PASLAUGOS, PASLAUGOS, NAUJIENOS…“.
  - Kainos angl. formatu: https://ofnis.lt/product-category/akcijos/ → „€ 5,548.00 € 4,599…“, „€ 956.00 € 759.00“ (vietoj „5 548,00 €“); angl. „Sale“, „Quick View“, kelias „Home / Produktai“.
- Viena detalė laiškui: pagrindiniame puslapyje vietoj paieškos rodomas tekstas „[aws_search_form]“, o slider'io „Buzil valymo priemonės → Plačiau“ veda į „Puslapis nerastas“.
- Patarimas patiems: įjungti (arba pašalinti) „Advanced Woo Search“ įskiepį; WooCommerce → Nustatymai → Bendri: tūkstančių skirtukas „ “, dešimtainis „,“, valiutos pozicija „dešinėje su tarpu“.
- Siūloma kaina: kelios klaidos 100–200 € (+ PVM); WP 5.5 → 6.x atnaujinimas papildomai nuo 200 €
- Siūlomas darbas ir trukmė: 1–2 d.

## Atmesti
- balimpeksas.lt – visa svetainė (pagrindinis ir ?s=) grąžina HTTP 500 „Fatal error: Uncaught Error: Call to undefined function Automattic\Jetpack\Assets\wp_is_serving_rest_request()… woocommerce-payments“, sertifikatas pasibaigęs (ssl=10); kiti puslapiai 404 → el. pašto svetainėje rasti neįmanoma. KARŠTAS leadas, jei el. paštą rastų kitur (statybinių įrankių didmena).
- automera.lt – visa svetainė „Fatal error: Allowed memory size of 268435456 bytes exhausted… elementor“, net /kontaktai/ ir wp-json; el. pašto svetainėje nėra. Taip pat karštas, jei kontaktą rastų kitur.
- ravika.lt – auto kilimėliai/purvasaugiai, OpenCart 1.5 (jq 1.7.1), SSL klaida, © 2015; bet 15 iš 15 atsitiktinių subkategorijų (iš 208) „Šioje kategorijoje nėra prekių“, prekės „Kaina: 0.00€“, URL „dgdgs-35“ → neaktyvi, nėra realių kainų.
- autrota.lt – traktoriukai/vejapjovės (Tauragė), SSL hostname mismatch, WP 5.4.16, 4 iš 5 meniu kategorijų „Nothing Found“; bet prekės – blogo įrašai, paskutinis 2020-12 → abejotina gyva veikla. Rezervas.
- horomechanika.lt – traktoriai; demo prekė „Et harum quidem rerum facili“, „Specialūs pasliūlymai“, „0 out of 5“, „Quick View“, serverio kelias generator meta; BET kainų nėra nei kategorijose, nei prekėse (kriterijus 3). Rezervas (geras quick, jei kainos nebūtinos).
- garbaltic.lt – sunkiosios technikos dalys, WP 4.9.26, SSL blogas, © 2016, el. paštas šablono „contac@yourcompany.com“ šalia tikro; bet kainų nėra, visos nuotraukos 2017 → apleista.
- technosta.lt – tvirtinimo detalės, OpenCart 1.5 (jq 1.7.1, ie6.css), be viewport; bet katalogas be kainų/krepšelio.
- sanmonta.lt – santechnika, WooCommerce 2.6.14 / WP 5.1.19; kainų nėra, turinys 2016.
- citreum.lt – ne OpenCart (Tėja-commerce).
- autosima.lt – agentūros kreditas „El. parduotuvės sprendimas: ParduotuvesNuoma.lt“.
- agrovartai.lt – parduotuvė .com domene (agrovartai.com).
- rolma.lt, stotras.lt, knortas.lt, kvarcas.lt, kega.lt, techpart.lt, slshydraulics.lt, autoprizme.lt, gysarda.lt, kinivarpa.lt, lavitas.lt – be el. parduotuvės/kainų (tik vizitinė ar katalogas).
- medzioklekaunas.lt – medžiotojų sąjunga, ne parduotuvė; druskininkust.lt – šilumos tiekėjas (įstaiga); ddf.lt – gamykla be parduotuvės, EN turinys.
- elektrospec.lt – „Sale!“/„Uncategorized“ tik JS vertimų eilutėse, ne matomame tekste.
- sildymasjums.lt – tik http→https neperadresuoja, visos nuorodos 200 – per mažai.
- weeride.lt – OpenCart be viewport, bet ne parduotuvė („Kur įsigyti“).
- jusmeda.lt – OpenCart su PHP „Deprecated: mysql_connect()“ ir SSL klaida, bet higienos prekės (ne mano nišos) – perduoti kitam agentui.
- zvejokultas.lt, angleris.lt, zvejybosreikmenys.lt – 403 (blokuoja), platforma nepatvirtinta.

Iš viso: 9 (big 5, quick 4)
- big: raisantas.lt, darbobatai.lt, dazas.lt, motogama.lt, enbaterija.lt
- quick: v-s.lt, stabdziudalys.lt, dviratininkams.lt, ofnis.lt
