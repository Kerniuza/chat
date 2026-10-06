# Partija 6 — LT juodraščiai (NESIŲSTI be vartotojo „siųsk“)

Paruošta 2026-10-06. Įrodymai: `research/batch6/cand_A.md`, `cand_B.md`, `cand_C.md` (kiekvienas trūkumas patikrintas dukart agentų ~07:35–09:07 UTC; pagrindiniai URL patikrinti trečią kartą ~09:20 UTC).
Prieš siunčiant: importuoti pilną `outreach_tracking.csv` (DNC), nustatyti GMAIL_* aplinkos kintamuosius, trūkumus permatyti dar kartą, jei praėjo >2 d.

## pyramis.lt
- Platforma: OpenCart 1.5 (jQuery 1.7.1)
- Kategorija: big
- El. paštas: info@pyramis.lt
- Įrodymai: https://pyramis.lt → curl (60) „certificate has expired“; http://pyramis.lt → 200 be peradresavimo; prisijungimo forma `action="http://pyramis.lt/index.php?route=account/login"`; footer „© 2014“. Žr. cand_B.md.
- Trūkumas: pasibaigęs SSL sertifikatas, http be peradresavimo, prisijungimas per http, OpenCart 1.5
- Kaina laiške: 80–120 € + PVM
- Tema: pyramis.lt: naršyklė rodo, kad sertifikatas pasibaigęs
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Pastebėjau, kad pyramis.lt SSL sertifikatas pasibaigęs. Naršyklė rodo įspėjimą, kad svetainė nesaugi, todėl dalis pirkėjų išeina, o prisijungimo slaptažodžiai siunčiami nešifruoti.

Siūlau įdiegti naują sertifikatą ir nukreipti visą svetainę į saugų https. Darbas užtruktų dieną, kaina 80–120 € + PVM.

Esu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Darau ir SEO, prekių kėlimą, dizaino atnaujinimą.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## raisantas.lt
- Platforma: OpenCart 1.5 (jQuery 1.7.1)
- Kategorija: big
- El. paštas: raisantas@gmail.com
- Įrodymai: meniu „Kieto kuro katilai“ ir „Anglies pluošto šildymo kilimėliai“ → `index.php?route=product/category&path=0` 404 „Produktų kategorija nerasta!“; „Skysto kuro katilai“ path=501, „Infraraudonųjų spindulių šildytuvai“ path=462 → 404; footer „© 2017“. Žr. cand_A.md, cand_B.md.
- Trūkumas: keli pagrindinio meniu punktai veda į 404, OpenCart 1.5
- Kaina laiške: 50–100 € + PVM (dizainas 250–600 € + PVM)
- Tema: raisantas.lt: meniu „Kieto kuro katilai“ atidaro „Kategorija nerasta“
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau raisantas.lt ir pastebėjau, kad keli meniu punktai, pvz. „Kieto kuro katilai“, „Skysto kuro katilai“ ir „Anglies pluošto šildymo kilimėliai“, atidaro „Produktų kategorija nerasta!“. Šildymo sezono metu tai kaip tik tos prekės, kurių žmonės ieško.

Meniu sutvarkyčiau per dieną už 50–100 € + PVM. Jei norėtumėte, galiu ir atnaujinti dizainą, kad parduotuvė gerai atrodytų telefone, nekeičiant OpenCart sistemos, tai 250–600 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt, kuris irgi veikia ant OpenCart 1.5, padariau naują dizainą telefonams ir įdiegiau SSL, sistemos nekeisdamas.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## enbaterija.lt
- Platforma: OpenCart 1.5 (jQuery 1.7.1, tema omf2)
- Kategorija: big
- El. paštas: info@eurobaterija.lt
- Įrodymai: https://enbaterija.lt → `grep -c 'name="viewport"'` = 0; temoje yra `mobile2.scss` su `@media (max-width:768px)`, kuris be viewport neįsijungia. Žr. cand_A.md.
- Trūkumas: nėra viewport žymės — telefone rodoma sumažinta kompiuterio versija; OpenCart 1.5
- Kaina laiške: 100–250 € + PVM
- Tema: enbaterija.lt telefone rodoma kaip sumažinta kompiuterio versija
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau enbaterija.lt ir pastebėjau, kad telefone rodoma sumažinta kompiuterio versija, tekstą ir mygtukus tenka didinti pirštais. Mobili versija jūsų temoje yra, tik neįsijungia, nes puslapio kode trūksta vienos eilutės. Dabar dauguma pirkėjų ateina iš telefono.

Tai sutvarkyčiau ir patikrinčiau keliuose telefonuose per 1–2 dienas, kaina 100–250 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt, kuris irgi veikia ant OpenCart 1.5, padariau naują dizainą telefonams ir įdiegiau SSL, sistemos nekeisdamas.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## balticmobiles.lt
- Platforma: OpenCart 1.5 (jQuery 1.7.1, Last-Modified 2014-06-24)
- Kategorija: big
- El. paštas: info@balticmobiles.lt
- Įrodymai: https://www.balticmobiles.lt/mobilieji-telefonai/blackview → „Rodoma nuo 1 iki 102 iš 872“, rodomi tik „Apple iPhone …“; /mobilieji-telefonai/blackberry, /asus, /microsoft, /estar → „Šioje kategorijoje nėra prekių“. Žr. cand_B.md.
- Trūkumas: Blackview kategorijoje rodomi iPhone, 4 tuščios gamintojų kategorijos; OpenCart 1.5
- Kaina laiške: 50–100 € + PVM
- Tema: balticmobiles.lt: „Blackview“ kategorijoje rodomi vien iPhone
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau balticmobiles.lt ir pastebėjau, kad kategorijoje „Blackview“ rašo 872 prekės, bet rodomi vien Apple iPhone, nė vieno Blackview. Blackberry, Asus, Microsoft ir eStar kategorijos visai tuščios. Žmogus, ieškantis konkretaus gamintojo, tada eina kitur.

Kategorijas sutvarkyčiau per pusdienį, kaina 50–100 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt sukėliau virš 200 prekių su lietuviškais aprašymais ir nuotraukomis.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## kosmetikavisiems.lt
- Platforma: OpenCart 1.5 (jQuery 1.7.1 Last-Modified 2014-12-13, jquery-ui 1.8.16)
- Kategorija: big
- El. paštas: info@kosmetikavisiems.lt
- Įrodymai: pagrindiniame HTML `jquery-1.7.1.min.js` + `ajax.googleapis.com/.../jquery/1.8.2/jquery.min.js` (dvi jQuery versijos); `http://html5shim.googlecode.com/svn/trunk/html5.js` → 404. Žr. cand_C.md.
- Trūkumas: OpenCart 1.5 (2014 m. failai), dvi jQuery versijos, neveikiantis išorinis skriptas
- Kaina laiške: preliminariai nuo 300 € + PVM
- Tema: kosmetikavisiems.lt veikia ant OpenCart 1.5 – apie PHP atnaujinimą
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau kosmetikavisiems.lt ir pastebėjau, kad parduotuvė veikia ant OpenCart 1.5, failai datuoti 2014 m. Tokia versija nesuderinama su naujomis PHP versijomis, o hostingai senąsias anksčiau ar vėliau išjungia. Tada parduotuvė gali tiesiog nustoti veikti.

Galėčiau ją sutvarkyti taip, kad veiktų su nauja PHP ir gerai atrodytų telefone, nekeičiant visos sistemos ir neperkeliant prekių. Preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt, kuris irgi veikia ant OpenCart 1.5, padariau naują dizainą telefonams ir įdiegiau SSL, sistemos nekeisdamas.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## mocca.lt
- Platforma: OpenCart 2.x (jQuery 2.1.1, tema theme638)
- Kategorija: big
- El. paštas: info@mocca.lt
- Įrodymai: https://mocca.lt → curl (60); `openssl s_client` → `subject=CN = *.serveriai.lt` (netinka mocca.lt); http://mocca.lt → 200 be peradresavimo; prisijungimo forma `action="http://mocca.lt/index.php?route=account/login"`. Žr. cand_C.md.
- Trūkumas: SSL sertifikatas ne mocca.lt domenui, http be peradresavimo, prisijungimas per http
- Kaina laiške: 80–120 € + PVM
- Tema: mocca.lt: naršyklė rodo, kad ryšys nėra saugus
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau mocca.lt ir pastebėjau, kad atidarius svetainę per https naršyklė rodo įspėjimą, nes sertifikatas išduotas ne jūsų domenui, o hostingo *.serveriai.lt. Per paprastą http svetainė rodoma kaip „Nesaugi“, ir per ją siunčiamas prisijungimo slaptažodis. Toks užrašas daug pirkėjų atbaido.

Sutvarkyčiau sertifikatą ir nukreipčiau visą svetainę į https per dieną, kaina 80–120 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt neseniai įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## darbobatai.lt
- Platforma: WooCommerce 3.3.6 / WordPress 4.9.26 (generator), Slider Revolution 5.4.6.4
- Kategorija: big
- El. paštas: pardavimai@darbobatai.lt
- Įrodymai: generator `WordPress 4.9.26`, `WooCommerce 3.3.6`; https://darbobatai.lt/pruduktai/darbo-batai/ → `<title>Darbo batai Archives | Darbo Batai</title>`. Žr. cand_A.md.
- Trūkumas: WP 4.9 / WooCommerce 3.3 (2018), kategorijų pavadinimai „Archives“
- Kaina laiške: preliminariai nuo 300 € + PVM
- Tema: darbobatai.lt: Google rodo „Darbo batai Archives“
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau darbobatai.lt ir pastebėjau, kad Google kategorijas rodo kaip „Darbo batai Archives“, o pati svetainė veikia ant WordPress 4.9 ir WooCommerce 3.3, kurioms apie aštuoneri metai. Saugumo pataisymų tokios versijos nebegauna.

Atnaujinčiau viską atsargiai, pirma bandomojoje kopijoje, patikrinčiau krepšelį ir mokėjimus, sutvarkyčiau pavadinimus. Apie savaitė, preliminariai nuo 300 € + PVM. Po to galiu prižiūrėti už 20–30 € per mėnesį.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## dazas.lt
- Platforma: WooCommerce / WordPress 5.1.26 (`?ver=5.1.26`), jQuery 1.12.4, Revolution Slider rev=4.6.0
- Kategorija: big
- El. paštas: info@dazas.lt
- Įrodymai: `wp-includes/css/dist/block-library/style.min.css?ver=5.1.26`, `revslider/rs-plugin/css/settings.css?rev=4.6.0`; https://www.dazas.lt/parduotuve/ → `<title>Elekroninė amerikietiškų Coronado Paint dažų parduotuvė | Tikrasis dažas</title>`. Žr. cand_A.md.
- Trūkumas: WP 5.1, Revolution Slider 4.x, rašybos klaida parduotuvės pavadinime
- Kaina laiške: preliminariai nuo 300 € + PVM
- Tema: dazas.lt: „Elekroninė“ parduotuvės pavadinime ir senas WordPress
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau dazas.lt ir pastebėjau, kad svetainė veikia ant WordPress 5.1 iš 2019 m., o slaideris Revolution Slider dar 4-osios versijos, kurioje yra žinomų saugumo spragų. Dar parduotuvės pavadinime, kurį rodo Google, parašyta „Elekroninė“.

Atnaujinčiau WordPress, WooCommerce ir slaiderį, pirma bandomojoje kopijoje, ir patikrinčiau krepšelį. Apie 3–5 dienos, preliminariai nuo 300 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## foleta.lt
- Platforma: WordPress 5.1.1 + WooCommerce 3.5.6 (generator)
- Kategorija: big
- El. paštas: info@foleta.lt
- Įrodymai: generator `WordPress 5.1.1`, `WooCommerce 3.5.6`; https://www.foleta.lt/parduotuve/krosnele-romotop-laredo-t-04-5-2-kw/ → „Produkto kodas: HU3LG 21-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-2-1-2…“ (5 iš 24 patikrintų prekių); footer „© 2018“. Žr. cand_B.md.
- Trūkumas: WP 5.1 / WooCommerce 3.5 (2019), sugadinti prekių kodai
- Kaina laiške: preliminariai nuo 250 € + PVM
- Tema: foleta.lt: keistas prekės kodas ROMOTOP Laredo puslapyje
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau foleta.lt ir pastebėjau, kad svetainė veikia ant WordPress 5.1 ir WooCommerce 3.5 iš 2019 m., kurios nebegauna saugumo pataisymų. Dar kai kurių krosnelių, pvz. ROMOTOP LAREDO T 04, prekės kodas rodomas kaip „HU3LG 21-1-1-1-1…“ su dešimtimis „-1“.

Atnaujinčiau sistemą bandomojoje kopijoje, patikrinčiau ir sutvarkyčiau kodus. Apie 3–5 dienos, preliminariai nuo 250 € + PVM. Vėliau galiu prižiūrėti už 20–30 € per mėnesį.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## korleja.lt
- Platforma: WooCommerce 3.4.8 / WordPress 4.9.26 (generator), tema Savoy
- Kategorija: big
- El. paštas: info@korleja.lt
- Įrodymai: generator `WordPress 4.9.26`, `WooCommerce 3.4.8`; https://korleja.lt/parduotuve/kudikiu-tekstile/ciuziniai/ → „Produktų nerasta“ (patikrinta 3 kartus). Žr. cand_C.md.
- Trūkumas: WP 4.9 / WooCommerce 3.4 (2018), tuščia kategorija „Čiužiniai“
- Kaina laiške: preliminariai nuo 250 € + PVM
- Tema: korleja.lt: kategorija „Čiužiniai“ tuščia
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau korleja.lt ir pastebėjau, kad svetainė veikia ant WordPress 4.9 ir WooCommerce 3.4, kurioms apie aštuoneri metai. Saugumo pataisymų jos nebegauna, o hostingui atnaujinus PHP gali ir sustoti. Dar kategorija „Čiužiniai“ rodo tik „Produktų nerasta“.

Atnaujinčiau viską bandomojoje kopijoje, patikrinčiau krepšelį ir apmokėjimą. Apie 3–5 dienos, preliminariai nuo 250 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt neseniai įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## floravitas.lt
- Platforma: WooCommerce 2.4.13 / WordPress 4.9.26 (generator), Slider Revolution 5.2.5
- Kategorija: big
- El. paštas: floravitas@floravitas.lt
- Įrodymai: generator `WooCommerce 2.4.13`; pagrindinio puslapio blokas „TIK VILNIUJE“ → https://www.floravitas.lt/geles/tik-vilniuje/ → 404 (patikrinta 3 kartus). Žr. cand_C.md.
- Trūkumas: WooCommerce 2.4 (2015), pagrindinio puslapio blokas „TIK VILNIUJE“ veda į 404
- Kaina laiške: 50 € + PVM (nuoroda); preliminariai nuo 400 € + PVM (atnaujinimas)
- Tema: floravitas.lt: blokas „TIK VILNIUJE“ atidaro klaidos puslapį
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau floravitas.lt ir pastebėjau, kad pagrindiniame puslapyje raudonas blokas „TIK VILNIUJE“ atidaro „puslapis nerastas“. Be to, parduotuvė veikia ant WooCommerce 2.4 iš 2015 m., kuri nebegauna saugumo pataisymų ir anksčiau ar vėliau nustos veikti su nauja PHP.

Nuorodą pataisyčiau už 50 € + PVM. Visos sistemos atnaujinimas užtruktų 1–2 savaites, preliminariai nuo 400 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## geliulanka.lt
- Platforma: WooCommerce 3.8.3 / WordPress 5.4.23 (generator), tema Fiorello
- Kategorija: big
- El. paštas: info@geliulanka.lt
- Įrodymai: http://geliulanka.lt/ → 200 be peradresavimo (patikrinta 3 kartus); generator `WordPress 5.4.23`, `WooCommerce 3.8.3`. Žr. cand_C.md.
- Trūkumas: http neperadresuoja į https, WP 5.4 / WooCommerce 3.8
- Kaina laiške: 50–80 € + PVM (peradresavimas); preliminariai nuo 250 € + PVM (atnaujinimas)
- Tema: geliulanka.lt atsidaro ir be spynos
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau geliulanka.lt ir pastebėjau, kad įvedus adresą be https svetainė atsidaro kaip „Nesaugi“ ir nenukreipia į saugią versiją, nors sertifikatą turite. Dar ji veikia ant WordPress 5.4 ir WooCommerce 3.8, kurios nebegauna saugumo pataisymų.

Peradresavimą padaryčiau per valandą ar dvi už 50–80 € + PVM. Sistemos atnaujinimas bandomojoje kopijoje – preliminariai nuo 250 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt neseniai įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## spila.lt
- Platforma: WooCommerce 3.3.6 / WordPress 5.4.23 (generator), Divi
- Kategorija: big
- El. paštas: info@spila.lt
- Įrodymai: dienos pasiūlymo nuoroda → https://www.spila.lt/spirulina/spirulina-visiems-meduje-tabletemis-ir-supermaisto-misinyje/ → 404 (patikrinta 3 kartus); generator `WooCommerce 3.3.6`; footer „© 2019“. Žr. cand_C.md.
- Trūkumas: dienos pasiūlymo nuoroda veda į 404, WooCommerce 3.3 (2018)
- Kaina laiške: 50 € + PVM (nuoroda); preliminariai nuo 300 € + PVM (atnaujinimas)
- Tema: spila.lt: dienos pasiūlymas veda į „puslapis nerastas“
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau spila.lt ir pastebėjau, kad pagrindinio puslapio dienos pasiūlymas su laikmačiu atidaro „puslapis nerastas“. Akcija skirta tam, kad žmogus pirktų iš karto, tad čia prarandami pirkėjai. Dar parduotuvė veikia ant WooCommerce 3.3 iš 2018 m.

Nuorodą pataisyčiau už 50 € + PVM. WooCommerce ir Divi atnaujinimas bandomojoje kopijoje užtruktų 3–5 dienas, preliminariai nuo 300 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## wilara.lt
- Platforma: WooCommerce 3.1.1 / WordPress 4.9.33 (generator), WPML 3.7.1
- Kategorija: big
- El. paštas: info@wilara.lt
- Įrodymai: viršaus mygtukas „Prisijungimas“ `href="/paskyra/"` → https://wilara.lt/paskyra/ → 404 (patikrinta 3 kartus); generator `WordPress 4.9.33`, `WooCommerce 3.1.1`. PASTABA: footer'yje agentūros kreditas (Foxi AD), bet platforma nuo 2017 neatnaujinta.
- Trūkumas: mygtukas „Prisijungimas“ veda į 404, WP 4.9 / WooCommerce 3.1 (2017)
- Kaina laiške: 50 € + PVM (mygtukas); preliminariai nuo 400 € + PVM (atnaujinimas)
- Tema: wilara.lt: mygtukas „Prisijungimas“ atidaro klaidos puslapį
- Laiškas:
```
Sveiki,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau wilara.lt ir pastebėjau, kad viršuje esantis mygtukas „Prisijungimas“ atidaro klaidos puslapį, tad klientai nepatenka į savo paskyrą. Be to, svetainė veikia ant WordPress 4.9 ir WooCommerce 3.1 iš 2017 m., kurios nebegauna saugumo pataisymų.

Mygtuką sutvarkyčiau už 50 € + PVM. Sistemos atnaujinimas su daugiakalbe dalimi užtruktų 1–2 savaites, preliminariai nuo 400 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## v-s.lt
- Platforma: WooCommerce / WordPress 6.7.9 (generator), WPML
- Kategorija: quick
- El. paštas: info@v-s.lt
- Įrodymai: kategorijų sąraše „Uncategorized @lt“ → https://v-s.lt/produkto-kategorija/uncategorized-lt/ → „Pagal Jūsų pasirinkimą prekių nėra.“; http://v-s.lt/ → 200 be peradresavimo; „Grandininis pjūklas 54.0 cm³“ ir „54.5 cm³“ ta pati nuotrauka KJ5400Z-349x400.jpg; URL …/sodo-traktoriukas-bs-intek-20-ag-107-cm-kopijuoti/ su antrašte „SECO 16 Ag“. Žr. cand_A.md.
- Trūkumas: „Uncategorized @lt“ kategorija, http be peradresavimo, prekių kopijavimo likučiai
- Kaina laiške: 100–200 € + PVM
- Tema: v-s.lt: kategorijų sąraše matosi „Uncategorized @lt“
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau v-s.lt ir pastebėjau kelias smulkmenas. Kategorijų sąraše matosi techninė „Uncategorized @lt“, kuri atidaro tuščią puslapį. Pjūklai 54.0 cm³ ir 54.5 cm³ turi tą pačią nuotrauką, o įvedus adresą be https svetainė atsidaro kaip „Nesaugi“.

Visa tai sutvarkyčiau per 1–2 dienas, kaina 100–200 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt sukėliau virš 200 prekių su lietuviškais aprašymais ir nuotraukomis.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## stabdziudalys.lt
- Platforma: WooCommerce 10.3.8 / WordPress 7.1.2 (generator)
- Kategorija: quick
- El. paštas: info@stabdziudalys.lt
- Įrodymai: pagrindiniame prisijungimo langas „Sign in … Lost your password? … Create an Account“, antispam „7 + ten =“; https://stabdziudalys.lt/shop/ → `<title>Shop – Stabdžių dalys</title>`; pagrindiniame 2015 m. įrašai „Uncategorized“. Žr. cand_A.md.
- Trūkumas: angliški sistemos tekstai, „Shop“ pavadinimas, seni „Uncategorized“ įrašai pagrindiniame
- Kaina laiške: 100–150 € + PVM
- Tema: stabdziudalys.lt: prisijungimo langas angliškai
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau stabdziudalys.lt ir pastebėjau, kad prisijungimo langas visas angliškas („Sign in“, „Lost your password?“, net „7 + ten =“), parduotuvė Google rodoma kaip „Shop – Stabdžių dalys“, o pagrindiniame puslapyje matosi 2015 m. įrašai „Uncategorized“. Kartu tai sudaro neprižiūrimos svetainės įspūdį.

Vertimus, pavadinimus ir pagrindinį puslapį sutvarkyčiau per dieną, kaina 100–150 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, dėl mano SEO darbų viena iš jų Google rodosi beveik pirma.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## dviratininkams.lt
- Platforma: WooCommerce 10.8.1 / WordPress
- Kategorija: quick
- El. paštas: info@dviratininkams.lt
- Įrodymai: https://dviratininkams.lt/ → `<title> </title>`; kiti puslapiai `<title> Kontaktai : </title>`, `<title> Cube Nuroad Pro mysticpurple’n’black 2027-M : </title>`; meta description „UAB Dviratininkas“; dydžiai atskiromis prekėmis (…-2027-xs/-s/-m/-l/-xl/-xxl). Žr. cand_A.md.
- Trūkumas: tuščias pagrindinio puslapio pavadinimas, sugadinti puslapių pavadinimai Google
- Kaina laiške: 80–150 € + PVM
- Tema: dviratininkams.lt: pagrindinis puslapis neturi pavadinimo Google
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau dviratininkams.lt ir pastebėjau, kad pagrindinis puslapis neturi pavadinimo, o kitų puslapių pavadinimai baigiasi tuščiu dvitaškiu, pvz. „Kontaktai : “. Būtent šį tekstą Google rodo paieškos rezultatuose kaip nuorodą.

Pavadinimus ir aprašymus visai svetainei sutvarkyčiau per dieną, kaina 80–150 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, dėl mano SEO darbų viena iš jų Google rodosi beveik pirma.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## ofnis.lt
- Platforma: WooCommerce / WordPress 5.5.22 (generator)
- Kategorija: quick
- El. paštas: info@ofnis.lt
- Įrodymai: pagrindiniame matomas „[aws_search_form]“ (patikrinta 3 kartus); slaiderio „BUZIL VALYMO PRIEMONĖS“ → „PLAČIAU“ → https://ofnis.lt/product-category/buzil-valymo-priemones/ekologines-valymo-priemones/ → 404; meniu „PASLAUGOS, PASLAUGOS“; https://ofnis.lt/product-category/akcijos/ → „€ 5,548.00“. Žr. cand_A.md.
- Trūkumas: neveikiantis paieškos trumpasis kodas, slaiderio nuoroda 404, dubliuotas meniu, angliškas kainų formatas
- Kaina laiške: 100–200 € + PVM
- Tema: ofnis.lt: vietoj paieškos rodomas „[aws_search_form]“
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau ofnis.lt ir pastebėjau, kad pagrindiniame puslapyje vietoj paieškos rodomas tekstas „[aws_search_form]“, slaiderio „Buzil valymo priemonės“ mygtukas atidaro „Puslapis nerastas“, meniu du kartus kartojasi „Paslaugos“, o kainos rodomos „€ 5,548.00“. Brangios technikos pirkėjas į tokias smulkmenas žiūri atidžiai.

Visa tai sutvarkyčiau per 1–2 dienas, kaina 100–200 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, taip pat su kliento e.segris.lt parduotuve.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## elmega.lt
- Platforma: OpenCart 2.x (jQuery 2.1.1, tema lexus_megashop)
- Kategorija: quick
- El. paštas: info@elmega.lt
- Įrodymai: kiekviename puslapyje `<div id="pav-paneltool" …>` su „Panel Tool“, „Theme: default / aqua / christmas / orange / purple“ (patikrinta 3 kartus); path=106, 107, 102 → „Šioje kategorijoje prekių nėra“; https://elmega.lt/ → http://www.elmega.lt/ → https://www.elmega.lt/. Žr. cand_B.md.
- Trūkumas: paliktas temos „Panel Tool“, tuščios kategorijos, peradresavimas per http
- Kaina laiške: 60–120 € + PVM
- Tema: elmega.lt: šone liko temos nustatymų krumpliaratis
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau elmega.lt ir pastebėjau, kad kompiuteryje šone liko temos krumpliaratis „Panel Tool“, per kurį bet kuris lankytojas gali perjungti parduotuvės spalvas į „christmas“ ar „purple“. Dar kelios kategorijos meniu tuščios, pvz. „Termosusitraukiančios pirštinės“.

Tai sutvarkyčiau per pusdienį, kaina 60–120 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, taip pat su kliento e.segris.lt parduotuve.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## viskaszoo.lt
- Platforma: OpenCart 3.x (tema journal3)
- Kategorija: quick
- El. paštas: info@viskaszoo.lt
- Įrodymai: http://viskaszoo.lt/ ir http://www.viskaszoo.lt/ → 200 be peradresavimo; tuščios kategorijos: /egzotiniams-gyvunams/iranga/apsvietimas, /iranga/sildymas, /egzotiniams-gyvunams/maistas-egzotiniams-gyvunams, /vitaminai-ir-mineralai, /zuvims/vandens-prieziuros-priemones, /pauksciams/skanestai-pauksciams ir kt. (9 vnt.). Žr. cand_B.md.
- Trūkumas: http be peradresavimo, 9 tuščios meniu kategorijos
- Kaina laiške: 60–120 € + PVM
- Tema: viskaszoo.lt: tuščios kategorijos „Egzotiniams gyvūnams“ meniu
- Laiškas:
```
Laba diena,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau viskaszoo.lt ir pastebėjau, kad meniu „Egzotiniams gyvūnams“ beveik visos kategorijos tuščios: „Apšvietimas“, „Šildymas“, „Maistas“ rodo „Šioje kategorijoje nėra prekių“. Iš viso radau devynias tokias. Dar įvedus adresą be https svetainė atsidaro kaip „Nesaugi“.

Meniu ir peradresavimą į https sutvarkyčiau per pusdienį, kaina 60–120 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, taip pat su kliento e.segris.lt parduotuve.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## sildymasjums.lt
- Platforma: OpenCart 2.x (jQuery 2.1.1)
- Kategorija: quick
- El. paštas: info@sildymasjums.lt
- Įrodymai: http://sildymasjums.lt/ → 200 be peradresavimo; tuščios: /sildymo-iranga/izoliacines-plokts, /sildymo-iranga/vamzdziai-sildymui-vandentiekiui, /sildymo-iranga/vamzdziu-fasonines-detales, /granuliniai-katilai/Granuliniai-degikliai-NBE, /granuliniai-katilai/nbe-black-star- ; SEO URL be LT raidžių: /vonios-ranga, /montavimo-priedai-ilumos-siurbliams, /dmtraukiai-dujiniams-katilams. Žr. cand_B.md.
- Trūkumas: http be peradresavimo, 5 tuščios kategorijos, SEO adresai su išmestomis raidėmis
- Kaina laiške: 100–200 € + PVM
- Tema: sildymasjums.lt: adresuose dingsta lietuviškos raidės
- Laiškas:
```
Sveiki,

Esu Kernius Zigmantas, užsiimu el. parduotuvių taisymu ir atnaujinimu. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir turiu dvejų metų darbo patirtį tėčio įmonėje.

Peržiūrėjau sildymasjums.lt ir pastebėjau, kad nuorodose lietuviškos raidės tiesiog išmestos: „Vonios įranga“ tapo /vonios-ranga, „dūmtraukiai“ tapo „dmtraukiai“. Tai blogina paiešką Google. Dar kelios kategorijos tuščios, o be https svetainė atsidaro kaip „Nesaugi“.

Adresus perrašyčiau su peradresavimais nuo senų, kad nedingtų tai, ką Google jau surinko. Kartu su kitais dalykais 1–2 dienos, kaina 100–200 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, dėl mano SEO darbų viena iš jų Google rodosi beveik pirma.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## balduideja.lt
- Platforma: OpenCart 2.x (jQuery 2.1.1, tema pav_furniture)
- Kategorija: quick
- El. paštas: balduideja.vilnius@gmail.com
- Įrodymai: meniu „Nature“ → http://balduideja.lt/svetaines-baldu-kolekcijos/nature-stalai-valgomojo-baldai-masyvas-lukstas-krysiak-baldu-ideja → 404 (patikrinta 3 kartus); „Mango“ → 404; „Atelie“, „Čiužiniai“ (/miegamojo-baldai/ciuziniai), „Roma“, „Mestre“ → „Šioje kategorijoje prekių nėra“; http://balduideja.lt/ → 200 be peradresavimo, meniu nuorodos su http://. Žr. cand_B.md.
- Trūkumas: meniu kolekcijos 404, tuščios kategorijos, meniu nuorodos į http
- Kaina laiške: 80–150 € + PVM
- Tema: balduideja.lt: kolekcijos „Nature“ ir „Mango“ meniu neatsidaro
- Laiškas:
```
Laba diena,

Esu Kernius Zigmantas, taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.

Peržiūrėjau balduideja.lt ir pastebėjau, kad meniu kolekcijos „Nature“ ir „Mango“ atidaro „Kategorija nerasta!“, o „Atelie“ ir „Čiužiniai“ tušti. Dar meniu nuorodos veda į nesaugią http versiją. Baldai brangus pirkinys, tad tokios vietos krenta į akis.

Meniu, peradresavimą į https ir kainų formatą sutvarkyčiau per dieną, kaina 80–150 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, o klientui e.segris.lt neseniai įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

## senora.lt
- Platforma: OpenCart 2.x (jQuery 2.1.1, tema luxshop)
- Kategorija: quick
- El. paštas: uzsakymai@senora.lt
- Įrodymai: https://www.senora.lt/home/ → „Wishlist“, „Compare“, „Everywhere“, „Products, total 0.00€“, „It's never too late to fix it :)“, „Subscribe to our newsletter“, „Subscribe“. Žr. cand_C.md.
- Trūkumas: neišversti angliški temos tekstai
- Kaina laiške: 50–100 € + PVM
- Tema: senora.lt: krepšelyje „It's never too late to fix it :)“
- Laiškas:
```
Sveiki,

Mano vardas Kernius Zigmantas, tvarkau el. parduotuves ant OpenCart ir WordPress. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir jau du metus dirbu su svetainėmis tėčio įmonėje.

Peržiūrėjau senora.lt ir pastebėjau, kad nemažai temos tekstų liko angliškai: tuščiame krepšelyje rašo „It's never too late to fix it :)“, apačioje „Subscribe to our newsletter“, viršuje „Wishlist“ ir „Compare“.

Išversčiau viską ir patikrinčiau visus puslapius per pusdienį, kaina 50–100 € + PVM.

Esu dirbęs su siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv, taip pat su kliento e.segris.lt parduotuve.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę mokate prieš darbą, pusę po.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

Iš viso: 23 laiškai (big: 14, quick: 9)

Rezervas (nesiųsti be vartotojo sprendimo): motogama.lt (svetainė su temos demo prekėmis ir neveikiančiu HTTPS — tikrų prekių nėra), kamtojabaldai.lt (katalogas ir krepšelis 404, kainų nematyti), zookatalogas.lt (nurodytas el. paštas neveikiančiame domene), natureselement.lt (tik http peradresavimas — per maža).
