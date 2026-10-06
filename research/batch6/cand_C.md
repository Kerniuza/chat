# Kandidatai C (kosmetika, vaikams, maistas, drabužiai, rankdarbiai, kanceliarija, gėlės/dovanos) — 2026-10-06

Pastaba: tikrinta tik curl/python3 (be Browser). 1-as patikrinimas ~07:35–07:55 UTC, 2-as — žr. kiekvieno įrašo laiką. Atradimo šaltinis: 1551.lt katalogo kategorijos (WebSearch rezultatai buvo beverčiai).

Patikrinimų laikai UTC, 2026-10-06.

## mocca.lt
- Įmonė / ką parduoda: moteriški drabužiai ir aksesuarai (suknelės, paltai, skarelės, linas), pvz. skarelės po 35.00€.
- Platforma: OpenCart 2.x (HTML: `catalog/view/javascript/jquery/jquery-2.1.1.min.js` + `bootstrap.min.css` + `index.php?route=common/home`; TemplateMonster tema `catalog/view/theme/theme638`).
- Kategorija: big
- El. paštas: info@mocca.lt (https://mocca.lt kontaktų puslapis `http://mocca.lt/index.php?route=information/contact` ir pagrindinio puslapio HTML)
- Įrodymai:
  - Nėra veikiančio HTTPS: `curl -sS "https://mocca.lt/"` -> `curl: (60) SSL certificate problem: unable to get local issuer certificate` (ssl_verify_result=20); `openssl s_client -connect mocca.lt:443 -servername mocca.lt` -> `subject=CN = *.serveriai.lt` (hostingo bendras sertifikatas, NETINKA mocca.lt domenui, naršyklė rodys "Not secure/Jūsų ryšys nėra privatus"). Tikrinta 07:50 ir 07:57 UTC.
  - http neperadresuoja į https: `curl -o /dev/null -w "%{http_code} %{redirect_url}" "http://mocca.lt/"` -> `200` be redirect (07:50, 07:57 UTC). Visa svetainė veikia per paprastą http.
  - Prisijungimo forma su slaptažodžiu siunčiama nešifruotu http: `http://mocca.lt/index.php?route=account/login` -> 200, `<form action="http://mocca.lt/index.php?route=account/login"` + `<input type="password" name="password" ...>` (07:53 UTC).
  - Sena platforma: OpenCart 2.x su jQuery 2.1.1 (OC 2.0–2.3 laikotarpis, ~2015–2017).
  - Prekės ir kainos yra (kategorija `index.php?route=product/category&path=61` – 6 prekės po 35.00€), nuotraukos visos kraunasi (8/8 patikrintų 200).
- Viena konkreti detalė laiškui: atsidarius `https://mocca.lt` naršyklė rodo saugumo įspėjimą, nes sertifikatas išduotas `*.serveriai.lt`, o ne mocca.lt; o per http prisijungimo puslapis siunčia slaptažodį nešifruotai.
- Patarimas patiems: hostinge (serveriai.lt) įjungti nemokamą Let's Encrypt sertifikatą mocca.lt domenui ir OpenCart nustatymuose įjungti "Use SSL" + 301 redirect .htaccess.
- Siūloma kaina: HTTPS/SSL + redirect + mišraus turinio sutvarkymas 80–120 € (+ PVM); jei kartu OpenCart atnaujinimas į 3.x/4.x — preliminariai nuo 400 € (+ PVM).
- Siūlomas darbas ir trukmė: SSL sutvarkymas 0,5–1 d.; platformos migracija 1–2 sav.

## kosmetikavisiems.lt
- Įmonė / ką parduoda: kosmetika, higienos prekės, vaikiška kosmetika, kojinės/pėdkelnės (pvz. "Apsauginis kremas vaikams Bibi Dream", kainos 2,40€–4,75€).
- Platforma: OpenCart 1.5.x (HTML: `catalog/view/javascript/jquery/jquery-1.7.1.min.js` + `jquery/ui/jquery-ui-1.8.16.custom.min.js` + `nivo-slider` — tipinis OC 1.5 rinkinys; tema `catalog/view/theme/elegium`).
- Kategorija: big
- El. paštas: info@kosmetikavisiems.lt (`https://www.kosmetikavisiems.lt/index.php?route=information/contact`)
- Įrodymai:
  - OpenCart 1.5.x: `curl -sS "https://www.kosmetikavisiems.lt/" | grep -oE 'jquery-1\.7\.1\.min\.js|jquery-ui-1\.8\.16'` -> abu randami (07:38 ir 07:57 UTC). Failo `catalog/view/javascript/jquery/jquery-1.7.1.min.js` `last-modified: Sat, 13 Dec 2014`.
  - Puslapyje vienu metu įkeliamos dvi jQuery versijos (`//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js` ir `jquery-1.7.1.min.js`).
  - Neveikiantis išorinis skriptas: `<script src="http://html5shim.googlecode.com/svn/trunk/html5.js">` -> `curl` 404 (googlecode uždarytas) + tai http resursas https puslapyje.
  - Serveris kartais nutraukia ryšį: keli `curl: (35) Recv failure: Connection reset by peer` / `ConnectionResetError` kraunant prekių/kontaktų puslapius (07:39–07:41 UTC, 3 iš ~15 užklausų) — gali būti apsaugos/rate limit, laiške NEMINĖTI be papildomo patikrinimo.
  - Gyva: kainos kategorijose (`index.php?route=product/category&path=94`: 2,40€, 2,50€, 4,75€), © 2026, ESTO vartojimo paskolos modulis; nuotraukos 8/8 kraunasi.
- Viena konkreti detalė laiškui: parduotuvė veikia ant OpenCart 1.5 (jQuery 1.7.1 failas datuotas 2014 m.), kurios saugumo atnaujinimai seniai nebeleidžiami ir kuri nesuderinama su naujomis PHP versijomis.
- Patarimas patiems: bent pašalinti neveikiantį `html5shim.googlecode.com` skriptą iš temos header.tpl.
- Siūloma kaina: didelis darbas — migracija į OpenCart 3/4 su prekių/klientų perkėlimu, preliminariai nuo 500 € (+ PVM).
- Siūlomas darbas ir trukmė: 2–3 sav. (duomenų migracija, tema, mokėjimų/ESTO moduliai).

## korleja.lt
- Įmonė / ką parduoda: kūdikių tekstilė ir aksesuarai (seilinukai, prijuostėlės, kuprinės, 4.50–18.00 €), namų tekstilė, siuvimo paslaugos.
- Platforma: WooCommerce 3.4.8 / WordPress 4.9.26 (`<meta name="generator" content="WordPress 4.9.26">`, `content="WooCommerce 3.4.8"`), tema Savoy, Slider Revolution 5.4.8.
- Kategorija: big
- El. paštas: info@korleja.lt (https://korleja.lt/kontaktai/; taip pat Rita@korleja.lt)
- Įrodymai:
  - Sena platforma: generator meta `WordPress 4.9.26` (4.9 šaka – 2017–2018), `WooCommerce 3.4.8` (2018), `Slider Revolution 5.4.8`, `jquery.js?ver=1.12.4` (07:44 ir 07:57 UTC). Dabartinė WordPress 7.x, WooCommerce 11.x.
  - Tuščia kategorija navigacijoje: `https://korleja.lt/parduotuve/kudikiu-tekstile/ciuziniai/` -> 200, bet puslapyje "Produktų nerasta", 0 prekių (07:46 UTC), nors subkategorija rodoma kategorijų sąraše.
  - Kainos formatuojamos su tašku `4.50 €`, `18.00 €` (LT standartas – kablelis) — smulkmena.
  - Gyva: kainos yra, naujausi įkėlimai `wp-content/uploads/2022`.
- Viena konkreti detalė laiškui: kūdikių tekstilės kategorijoje "Čiužiniai" (https://korleja.lt/parduotuve/kudikiu-tekstile/ciuziniai/) pirkėjas mato tik "Produktų nerasta".
- Patarimas patiems: paslėpti tuščias kategorijas (WooCommerce > kategorija be prekių) arba sudėti prekes.
- Siūloma kaina: WP/WooCommerce/temos atnaujinimas su testavimu — preliminariai nuo 250 € (+ PVM); smulkūs pataisymai 50–100 €.
- Siūlomas darbas ir trukmė: 3–5 d. (atsarginė kopija, staging, atnaujinimas, temos suderinamumas).

## floravitas.lt
- Įmonė / ką parduoda: gėlių pristatymas (puokštės, kompozicijos, vainikai, dovanos), kainos 4.99–299.00 €.
- Platforma: WooCommerce 2.4.13 / WordPress 4.9.26 (generator meta), Visual Composer, Slider Revolution 5.2.5.
- Kategorija: big
- El. paštas: floravitas@floravitas.lt (https://www.floravitas.lt/kontaktai/ ir footer)
- Įrodymai:
  - Labai sena platforma: `content="WooCommerce 2.4.13"` (2015 m.!), `content="WordPress 4.9.26"`, `Slider Revolution 5.2.5` (07:51 ir 07:57 UTC).
  - Atskira "mobili versija" (`?responsive=off`, footer'yje "Mobili Versija") — senas sprendimas vietoj vieno prisitaikančio dizaino.
  - Negyva nuoroda iš pagrindinio puslapio: raudonas blokas "TIK VILNIUJE" ir "Spalvotos Hydrangėjos VILNIUJE" veda į `https://www.floravitas.lt/geles/tik-vilniuje/` -> HTTP 404 (07:53 ir 07:57 UTC).
  - Gyva: kainos pagrindiniame puslapyje (35.00, 49.00, 299.00), įkėlimai iki 2021, © 2004-2026.
- Viena konkreti detalė laiškui: pagrindiniame puslapyje paspaudus "TIK VILNIUJE" / "Spalvotos Hydrangėjos VILNIUJE" atsidaro 404 puslapis.
- Patarimas patiems: pataisyti nuorodą į esamą kategoriją (pvz. /geles/geles-vilniuje/).
- Siūloma kaina: WooCommerce 2.4 → dabartinė versija + tema, preliminariai nuo 400 € (+ PVM); vien nuorodos pataisymas 50 €.
- Siūlomas darbas ir trukmė: 1–2 sav. (didelis versijų šuolis, reikia staging).

## geliulanka.lt
- Įmonė / ką parduoda: UAB "Gėlių lanka" — gėlių puokštės, vestuvinė floristika, gėlių prekyba.
- Platforma: WooCommerce 3.8.3 / WordPress 5.4.23 (generator meta), WPBakery, Slider Revolution 6.0.8, tema Fiorello.
- Kategorija: big
- El. paštas: info@geliulanka.lt (https://geliulanka.lt/kontaktai/; taip pat lanka@, laumene@)
- Įrodymai:
  - http neperadresuoja į https: `curl -o /dev/null -w "%{http_code} %{redirect_url}" "http://geliulanka.lt/"` -> `200` be redirect (07:51 ir 07:57 UTC) — visa parduotuvė pasiekiama nešifruota versija, Google gali indeksuoti abi.
  - Sena platforma: `WordPress 5.4.23` (2020 šaka), `WooCommerce 3.8.3` (2019) (07:51 ir 07:57 UTC).
  - Gyva: įkėlimai 2024–2026.
- Viena konkreti detalė laiškui: įvedus http://geliulanka.lt svetainė atsidaro be spynos ir nenukreipia į saugią versiją.
- Patarimas patiems: įjungti 301 redirect http→https (.htaccess arba hostingo nustatymas).
- Siūloma kaina: redirect + mišraus turinio patikra 50–80 €; WP/WC atnaujinimas preliminariai nuo 250 € (+ PVM).
- Siūlomas darbas ir trukmė: redirect 1 val.; atnaujinimas 3–5 d.

## spila.lt
- Įmonė / ką parduoda: Spila UAB — spirulina ir funkcinio maisto produktai.
- Platforma: WooCommerce 3.3.6 / WordPress 5.4.23 (generator meta), Divi tema, WPML 3.9.4.
- Kategorija: big
- El. paštas: info@spila.lt (https://www.spila.lt/kontaktai/)
- Įrodymai:
  - Sena platforma: `content="WooCommerce 3.3.6"` (2018), `content="WordPress 5.4.23"`, footer `© 2019` (07:51 ir 07:57 UTC).
  - "Dienos pasiūlymo" (su atgaline laiko atskaita) nuotrauka pagrindiniame puslapyje veda į `https://www.spila.lt/spirulina/spirulina-visiems-meduje-tabletemis-ir-supermaisto-misinyje/` -> HTTP 404 (07:53 ir 07:57 UTC); nuotrauka `uploads/2025/06/Tabletes-2025-06-23.jpeg`.
  - Gyva: įkėlimai iki 2026.
- Viena konkreti detalė laiškui: pagrindinio puslapio akcijos su laikmačiu nuotrauka (spirulina tabletėmis/meduje) atidaro 404 puslapį.
- Patarimas patiems: pakeisti nuorodą akcijos bloke į esamą prekę; footer metus pakeisti į automatiškai atsinaujinančius.
- Siūloma kaina: nuorodos pataisymas 50 €; WooCommerce 3.3 → dabartinė + Divi atnaujinimas preliminariai nuo 300 € (+ PVM).
- Siūlomas darbas ir trukmė: 3–5 d.

## wilara.lt
- Įmonė / ką parduoda: UAB Wilara (Prienai) — bitininkystės reikmenys: aviliai, apranga, pirštinės (12.50–18.50 €).
- Platforma: WooCommerce 3.1.1 / WordPress 4.9.33 (generator meta), WPML 3.7.1, tema forthecause.
- Kategorija: big
- El. paštas: info@wilara.lt (footer pagrindiniame puslapyje; taip pat parduotuve@wilara.lt, wilara@wilara.lt)
- Įrodymai:
  - Labai sena platforma: `content="WordPress 4.9.33"`, `content="WooCommerce 3.1.1"` (2017), `jquery.js?ver=1.12.4` (07:44 ir 07:57 UTC).
  - Header mygtukas "Prisijungimas" (`<a class="button" href="/paskyra/">`) -> `https://wilara.lt/paskyra/` HTTP 404 (07:53 ir 07:57 UTC) — klientai negali prisijungti per šį mygtuką.
  - Agentūros kreditas footer'yje (Foxi AD), bet dizainas/platforma seni (įkėlimai 2016) — ne naujas dizainas.
  - Gyva: kainos kategorijose (`/bitininkyste/apranga/pirstines/`: 16.50, 12.50, 16.00 €), © 2026.
- Viena konkreti detalė laiškui: viršuje esantis mygtukas "Prisijungimas" atidaro 404 puslapį.
- Patarimas patiems: WooCommerce > Nustatymai > Išplėstiniai patikrinti "Mano paskyra" puslapį ir pataisyti mygtuko nuorodą.
- Siūloma kaina: mygtuko pataisymas 50 €; WP 4.9/WC 3.1 → dabartinės versijos su WPML, preliminariai nuo 400 € (+ PVM).
- Siūlomas darbas ir trukmė: 1–2 sav. (daug kategorijų, WPML, reikia staging).

## senora.lt
- Įmonė / ką parduoda: raštinės reikmenys, biuro įranga, kasetės, kopijavimo/spausdinimo paslaugos (Vilnius).
- Platforma: OpenCart 2.x (HTML `catalog/view/theme/luxshop`, `jquery-2.1.1`, bootstrap).
- Kategorija: quick
- El. paštas: uzsakymai@senora.lt (pagrindinio puslapio header'is)
- Įrodymai (https://www.senora.lt/home/, tikrinta 07:55 ir 07:57 UTC — grep rezultatai):
  - Neišversti angliški temos tekstai lietuviškame puslapyje: "Wishlist", "Compare", "Everywhere" (paieškos laukas, 2×), "Products, total 0.00€", "It's never too late to fix it :)" (tuščio krepšelio tekstas), naujienlaiškio blokas "Want to stay updated on all promotions and discounts?" / "Subscribe to our newsletter" / "Subscribe".
  - OpenCart 2.x (jQuery 2.1.1).
- Viena konkreti detalė laiškui: tuščiame krepšelyje rodomas angliškas "It's never too late to fix it :)", o apačioje naujienlaiškio blokas tik angliškai ("Subscribe to our newsletter").
- Patarimas patiems: OpenCart admin > Design > Language editor (arba temos lt kalbos failai) — išversti likusias frazes.
- Siūloma kaina: vertimų/temos tekstų sutvarkymas 50–100 € (+ PVM).
- Siūlomas darbas ir trukmė: 0,5–1 d.

## natureselement.lt
- Įmonė / ką parduoda: UAB "Mėlynė" — liofilizuotos uogos, džemai, medus, sultys, sirupai, dovanų rinkiniai (pvz. rinkinys 21.00 €, "InStock").
- Platforma: WooCommerce 10.7.0 / WordPress 6.8.10 (generator meta) — platforma nauja.
- Kategorija: big (lengvesnis — vien HTTPS peradresavimas; platforma nauja)
- El. paštas: info@natureselement.lt (pagrindinio puslapio HTML)
- Įrodymai:
  - http neperadresuoja į https: `curl -o /dev/null -w "%{http_code} %{redirect_url}" "http://natureselement.lt/"` -> `301 -> http://www.natureselement.lt/` (vėl http!), o `"http://www.natureselement.lt/"` -> `200` be redirect (07:58 ir 08:02 UTC). Visa parduotuvė (su krepšeliu) pasiekiama nešifruota versija.
  - Footer'yje `UAB "Mėlyne" 2018` (pasenę metai, ir pavadinime trūksta "ė") (07:58, 08:02 UTC).
  - Lėtokas atsakas: TTFB https 6.2 s ir 4.7 s (07:58), bet 3.0 s ir 3.0 s (08:02) — NEPASTOVU, laiške neminėti kaip ">4 s".
- Viena konkreti detalė laiškui: įvedus natureselement.lt be "https" naršyklė nukreipia į http://www.natureselement.lt ir parduotuvė atsidaro be spynos (nesaugi).
- Patarimas patiems: .htaccess / hostinge įjungti 301 http→https ir WordPress nustatymuose patikrinti, kad Site URL būtų https://www.
- Siūloma kaina: HTTPS redirect + mišraus turinio patikra 50–80 € (+ PVM); greičio optimizavimas 100–200 €.
- Siūlomas darbas ir trukmė: redirect 1–2 val.; greitis 1–2 d.

---

## Atmesti
- merkada.lt (kaukes.lt) — kostiumai/kaukės; WP 4.9.26 / WC 2.5.5, "Showing 1-6 of 179 products", "Read More", kaukes.lt sertifikatas `*.serveriai.lt` netinka; BET atrodo apleista (naujausi įkėlimai 2016, © 2017) — neatitinka "gyvos veiklos" kriterijaus. Galima grįžti, jei patvirtintų, kad prekiauja.
- 888dovanos.lt — WP 4.1.41, nėra viewport, SSL grandinės klaida, bet NĖRA el. parduotuvės (tik galerija, be kainų/krepšelio).
- talda.lt — OpenCart 1.5 (jquery-1.7.1, colorbox), bet tik katalogas be kainų/krepšelio (audiniai, darbo drabužiai).
- editosvirtuve.lt — title "Just another WordPress site", WP 5.4.23, bet maitinimo paslaugos be el. parduotuvės.
- copy1.lt — WP 4.9.26, bet ne parduotuvė (el. parduotuvė atskirame e-copy1.lt, kuris naujas, WP 6.7.9).
- daos.lt — WP 5.4.23 informacinis puslapis, el. parduotuvė atskirai; nėra prekių su kainomis.
- pintine.lt — WP 4.6.29, pintiniai gaminiai, bet be kainų/krepšelio.
- herbatint.lt, artidea.lt, bitija.lt — sena WP/WC (5.2/5.4/5.6), bet viešai nerastas el. paštas.
- geles.lt — WP 5.4.23 / WC 4.0.1, © 2020, bet beveik tuščias (8 nuorodos), kitų patikrintų trūkumų nėra; silpnas.
- mezgimomanija.lt, casalana.lt, nikis.lt, babor-spa.lt — "Add to cart" tik aria-label (nematoma), kitų tikrų trūkumų nerasta.
- sabalin.lt (avalynė) — TTFB ~3.4 s (<4), "Uncategorized" tik JS vertimų lentelėje — ne trūkumas.
- dilada.lt — WP 5.9.2 / WC 6.4.1 (~2022), nuorodos visos veikia; per mažai įrodymų.
- kemikvesta.lt — WP 4.9.3 / WC 3.8.4, lėta (8.35 s), bet švaros chemija — ne mano nišos.
- patalai.lt — sertifikatas pasibaigęs, bet nukreipia į kilimastau.lt (kilimai) — ne nišos.
- kalendoriai.lt, pajuriomelyne.lt, sigutesgeles.lt, suvalkijosaliejus.lt, zirniokrautuvele.lt — naujesnė platforma arba ne parduotuvė, tikrų trūkumų nerasta.
- trepsiukas.lt, staipaplius.lt, medicata.lt, tiande-produktai.lt, kamkam.lt — eshoprent (nuomojama SaaS OpenCart platforma, savininkas negali keisti branduolio).

Iš viso: 9 (big 8, quick 1)
