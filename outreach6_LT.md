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

Žiūrėjau Pyramis plautuves ir užėjau į pyramis.lt. Atidarius svetainę per https, naršyklė meta įspėjimą, kad sertifikatas pasibaigęs. Per paprastą http ji atsidaro, bet su užrašu „Nesaugi“, ir per tą patį nešifruotą ryšį keliauja ir paskyros prisijungimas su slaptažodžiu. Tokiame puslapyje nemažai žmonių nieko neperka, o Google tokias svetaines rodo žemiau.

Įdiegčiau naują sertifikatą, kuris atsinaujintų pats, ir nukreipčiau visą svetainę į https. Tai viena darbo diena, kaina 80–120 € + PVM. Parduotuvė veikia ant OpenCart 1.5, su šia versija esu daug dirbęs, tad sistemos keisti nereikėtų.

Apie save trumpai. Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir jau du metus dirbu tėčio įmonėje, kur tvarkau jos parduotuves: siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt, kuris irgi veikia ant OpenCart 1.5, įdiegiau SSL ir padariau naują dizainą telefonams, sistemos nekeisdamas.

Sąskaitą faktūrą su PVM išrašome per tėčio įmonę UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį, kai viskas padaryta ir patikrinta.

Jei įdomu, atsiųsiu trumpą planą.

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

Ieškojau kieto kuro katilų ir užėjau į raisantas.lt. Viršutiniame meniu paspaudus „Kieto kuro katilai“, atsidaro „Produktų kategorija nerasta!“. Taip pat neveikia „Anglies pluošto šildymo kilimėliai“, „Skysto kuro katilai“ ir „Infraraudonųjų spindulių šildytuvai“. Dabar kaip tik šildymo sezonas, o žmogus, radęs tuščią puslapį, dažnai tiesiog išeina.

Jei norite patys: tie punktai rodo į ištrintą kategoriją (adrese path=0), užtenka juos perrišti į esamas. Jei nėra kada, sutvarkyčiau per dieną už 50–100 € + PVM. Kadangi parduotuvė veikia ant OpenCart 1.5, vėliau galėčiau ir atnaujinti dizainą, kad gerai atrodytų telefone, sistemos nekeičiant, tai būtų 250–600 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau jos svetaines: siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 m. OpenCart, ją atnaujinau.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis: pusę prieš darbą, likutį po patikrinimo.

Jei įdomu, parašykite, atsiųsiu sąrašą, ką dar pastebėjau.

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

Užėjau į enbaterija.lt per telefoną ir pastebėjau, kad rodoma pilna kompiuterio versija, tik sumažinta, todėl tekstą ir mygtukus tenka didinti pirštais. Įdomiausia, kad jūsų temoje mobili versija yra, tik ji neįsijungia, nes puslapio antraštėje trūksta vadinamosios viewport eilutės. Dabar didžioji dalis pirkėjų ateina iš telefono, ir patogumas jiems daug lemia.

Kartais užtenka tą eilutę įdėti į header.tpl, bet dažniausiai po to dar reikia sutvarkyti kelias vietas, kurios telefone išsilieja. Padaryčiau viską ir patikrinčiau keliuose telefonuose per 1–2 dienas, kaina 100–250 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, kur prižiūriu siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt, kuris kaip ir jūsų parduotuvė veikia ant OpenCart 1.5, padariau naują, telefonams pritaikytą dizainą, sistemos nekeisdamas.

Sąskaitą faktūrą su PVM išrašome per tėčio įmonę UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį, kai viskas veiks.

Jei norite, atsiųsiu ekrano nuotrauką, kaip tai atrodo telefone.

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

Naršydamas balticmobiles.lt pastebėjau keistą dalyką. Meniu „Mobilieji telefonai“ paspaudus „Blackview“, rašo „Rodoma nuo 1 iki 102 iš 872“, bet sąraše vien Apple iPhone, nė vieno Blackview. O Blackberry, Asus, Microsoft ir eStar kategorijos visai tuščios. Žmogus, ieškantis konkretaus gamintojo, tokiu atveju greičiausiai eina pirkti kitur.

Greičiausiai Blackview kategorijai priskirtos ne tos prekės arba sugedęs filtras, o tuščias kategorijas galima tiesiog išjungti administravime. Sutvarkyčiau per pusdienį už 50–100 € + PVM. Jei vėliau norėtumėte daugiau, parduotuvė veikia ant OpenCart 1.5, kurią galiu atnaujinti ir prižiūrėti nekeisdamas visos sistemos.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt sukėliau virš 200 prekių su lietuviškais aprašymais ir susiejau jas su tinkamais priedais.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, pusę galima mokėti prieš darbą, likutį po patikrinimo.

Jei įdomu, atsiųsiu ekrano nuotraukas.

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

Užėjau į kosmetikavisiems.lt ir iš kodo mačiau, kad parduotuvė veikia ant OpenCart 1.5, failai datuoti 2014 metais. Šiandien ji veikia, bet tokia versija nesuderinama su naujomis PHP versijomis, o hostingai senąsias anksčiau ar vėliau išjungia. Tada parduotuvė gali tiesiog nustoti veikti, ir dažniausiai tai įvyksta netikėtai.

Smulkus dalykas, kurį galite pašalinti ir patys: temos antraštėje kraunamas skriptas iš html5shim.googlecode.com, kuris jau seniai nebeegzistuoja. Be to, puslapyje vienu metu įkeliamos dvi skirtingos jQuery versijos.

Galėčiau sutvarkyti parduotuvę taip, kad ji veiktų su nauja PHP ir gerai atrodytų telefone, nekeičiant visos sistemos ir neperkeliant prekių iš naujo. Preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs viską.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje: siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt, juki.lv. Klientui e.segris.lt, veikiančiam ant OpenCart 1.5, padariau naują dizainą telefonams, sistemos nekeisdamas.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Žiūrėjau jūsų sukneles mocca.lt ir pastebėjau, kad atidarius svetainę per https naršyklė rodo įspėjimą, jog ryšys nėra privatus. Sertifikatas išduotas ne mocca.lt, o bendras hostingo *.serveriai.lt. Per paprastą http svetainė atsidaro, bet su užrašu „Nesaugi“, ir per tą patį nešifruotą ryšį siunčiamas ir prisijungimo slaptažodis. Drabužius dažnai perka iš telefono, ir toks užrašas daug ką atbaido.

Dažnai hostingo valdymo skydelyje galima įjungti nemokamą Let's Encrypt sertifikatą, tai pirmas žingsnis. Po to dar reikia nukreipti visą svetainę į https ir sutvarkyti nuorodas, kad niekas nesulūžtų. Visa tai padaryčiau per dieną, kaina 80–120 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Neseniai klientui e.segris.lt įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą faktūrą su PVM išrašome per UAB Siuvimo Manija. Pusė prieš darbą, likutis, kai patikrinsite.

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

Ieškojau darbo batų ir Google rezultatuose jūsų kategorija rodoma kaip „Darbo batai Archives“. Tai WordPress paliktas angliškas žodis puslapio pavadinime. Pažiūrėjęs atidžiau pamačiau, kad svetainė veikia ant WordPress 4.9 ir WooCommerce 3.3, abiem jau apie aštuoneri metai. Tokios versijos saugumo pataisymų nebegauna, o su parduotuve tai rizika.

Pavadinimą galite pakeisti ir patys SEO įskiepio nustatymuose, archyvų pavadinimo šablone.

Atnaujinimą daryčiau atsargiai: pirma kopija, tada atnaujinimas atskiroje bandomojoje versijoje, patikrinimas, ar veikia krepšelis ir mokėjimai, ir tik tada perkėlimas į tikrą svetainę. Užtruktų apie savaitę, preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs. Po to galėčiau ją ir prižiūrėti už 20–30 € per mėnesį.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Ieškojau Coronado dažų ir užėjau į dazas.lt. Parduotuvės puslapio pavadinime, kuris rodomas ir Google rezultatuose, parašyta „Elekroninė amerikietiškų Coronado Paint dažų parduotuvė“, be „t“. Tai galite pataisyti ir patys, puslapio „Parduotuvė“ SEO nustatymuose.

Rimčiau tai, kad svetainė veikia ant WordPress 5.1 iš 2019 metų, o slaideris Revolution Slider dar 4-osios versijos. Senose to įskiepio versijose yra žinomų saugumo spragų, per kurias įsilaužiama į svetaines.

Atnaujinčiau WordPress, WooCommerce ir slaiderį atsargiai, pirma bandomojoje kopijoje, patikrinčiau krepšelį ir tik tada perkelčiau. Apie 3–5 dienos, preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, kur tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą faktūrą su PVM išrašome per UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį po patikrinimo.

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

Žiūrėjau krosneles foleta.lt ir ROMOTOP LAREDO T 04 puslapyje prekės kodas rodomas kaip „HU3LG 21-1-1-1-1-1-1-1-1…“, su kelias dešimtis kartų pasikartojančiu „-1“. Tas pats yra dar keliose prekėse. Panašu, kad tai likę po prekių kopijavimo.

Svarbiau, kad svetainė veikia ant WordPress 5.1 ir WooCommerce 3.5 iš 2019 metų. Tokios versijos nebegauna saugumo pataisymų, o parduotuvėje su tokiomis kainomis tai nereikalinga rizika.

Atnaujinčiau WordPress, WooCommerce ir temą, pirma bandomojoje kopijoje, patikrinčiau, ar viskas veikia, ir sutvarkyčiau prekių kodus. Apie 3–5 dienos, preliminariai nuo 250 € + PVM, tikslią kainą pasakysiu peržiūrėjęs viską. Vėliau galėčiau prižiūrėti už 20–30 € per mėnesį.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis: pusę prieš, likutį po darbo.

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

Žiūrėjau kūdikių tekstilę korleja.lt ir kategorijoje „Čiužiniai“ rodoma tik „Produktų nerasta“, nors ji matosi kategorijų sąraše. Jei čiužinių nebeturite, ją galima tiesiog paslėpti, tai užtrunka minutę.

Pažiūrėjęs atidžiau pamačiau, kad svetainė veikia ant WordPress 4.9 ir WooCommerce 3.4, abiem apie aštuoneri metai. Kol kas veikia, bet saugumo pataisymų tokios versijos nebegauna, o hostingui atnaujinus PHP sena svetainė gali ir sustoti.

Atnaujinčiau viską atsargiai: kopija, atnaujinimas bandomojoje versijoje, patikrinimas, ar veikia krepšelis ir apmokėjimas, tada perkėlimas. Apie 3–5 dienos, preliminariai nuo 250 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt neseniai padariau naują dizainą telefonams ir sukėliau virš 200 prekių.

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

Ieškojau gėlių pristatymo Vilniuje ir užėjau į floravitas.lt. Pagrindiniame puslapyje paspaudus raudoną bloką „TIK VILNIUJE“ ar „Spalvotos Hydrangėjos VILNIUJE“, atsidaro puslapis nerastas. Tai vienas ryškiausių blokų pirmame puslapyje, todėl jį spaudžia daug žmonių.

Nuorodą galima pakeisti į esamą kategoriją, ir tai galite padaryti patys. Jei nėra kada, padaryčiau už 50 € + PVM.

Dar pastebėjau, kad parduotuvė veikia ant WooCommerce 2.4, tai 2015 metų versija. Ji nebegauna saugumo pataisymų ir anksčiau ar vėliau nustos veikti su naujesne PHP. Atnaujinimas iš tokios senos versijos yra didesnis darbas, 1–2 savaitės, preliminariai nuo 400 € + PVM, tikslią kainą pasakysiu peržiūrėjęs viską.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį po patikrinimo.

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

Užėjau į geliulanka.lt ir pastebėjau, kad įvedus adresą be https svetainė atsidaro nesaugi, naršyklė rodo „Nesaugi“ ir nenukreipia į saugią versiją. Sertifikatą jūs turite, tik trūksta peradresavimo. Google tokiu atveju gali rodyti abi versijas, o pirkėjas, pamatęs „Nesaugi“ prie užsakymo formos, dažnai išeina.

Tai sutvarkyti nedidelis darbas, valandą ar dvi, kaina 50–80 € + PVM. Kartu pastebėjau, kad svetainė veikia ant WordPress 5.4 ir WooCommerce 3.8, tai 2019–2020 metų versijos be saugumo pataisymų. Jei norėtumėte, atnaujinčiau ir jas, pirma bandomojoje kopijoje, preliminariai nuo 250 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt neseniai įdiegiau SSL ir padariau naują dizainą telefonams.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis: pusę prieš darbą, likutį po.

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

Užėjau į spila.lt ir pagrindiniame puslapyje paspaudžiau dienos pasiūlymą su laikmačiu, spiruliną meduje ir tabletėmis. Atsidarė „puslapis nerastas“. Akcija su laikmačiu kaip tik skirta tam, kad žmogus spaustų iš karto, tad čia prarandami pirkėjai, kurie jau norėjo pirkti.

Nuorodą galite pakeisti ir patys, nukreipę ją į esamą prekę. Jei nėra kada, padaryčiau už 50 € + PVM.

Dar matau, kad parduotuvė veikia ant WooCommerce 3.3, tai 2018 metų versija be saugumo pataisymų. Ją atnaujinčiau kartu su Divi tema, pirma bandomojoje kopijoje, kad niekas nesugriūtų. Apie 3–5 dienos, preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, kur tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Žiūrėjau bitininkystės pirštines wilara.lt ir viršuje paspaudžiau „Prisijungimas“. Atsidarė klaidos puslapis „nerasta“. Nuolatiniai pirkėjai, kurie nori pažiūrėti savo užsakymus, taip prie paskyros nepatenka.

Greičiausiai mygtukas rodo į seną adresą, o WooCommerce nustatymuose „Mano paskyra“ puslapis yra kitur. Jei nerasite patys, sutvarkyčiau už 50 € + PVM.

Kartu pastebėjau, kad svetainė veikia ant WordPress 4.9 ir WooCommerce 3.1, tai 2017 metų versijos. Saugumo pataisymų jos nebegauna, o hostingui atnaujinus PHP gali ir nustoti veikti. Atnaujinimas su daugiakalbe dalimi užtruktų 1–2 savaites, preliminariai nuo 400 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą faktūrą su PVM išrašome per UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį po patikrinimo.

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

Žiūrėjau sodo techniką v-s.lt ir kategorijų sąraše pamačiau „Uncategorized @lt“. Paspaudus rašo, kad prekių nėra. Tai techninė WordPress kategorija, kuri pirkėjui neturėtų matytis.

Pastebėjau ir daugiau smulkmenų. Įvedus adresą be https svetainė atsidaro nesaugi ir nenukreipia į saugią versiją. Grandininiai pjūklai 54.0 cm³ ir 54.5 cm³ turi tą pačią nuotrauką, o traktoriuko SECO 16 Ag adrese parašyta „bs-intek-20-ag-kopijuoti“, matyt, likę po kopijavimo.

„Uncategorized @lt“ galite paslėpti patys prekių kategorijų nustatymuose. Kitką sutvarkyčiau per 1–2 dienas, kaina 100–200 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt sukėliau virš 200 prekių su lietuviškais aprašymais ir nuotraukomis.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Ieškojau stabdžių žarnelių ir užėjau į stabdziudalys.lt. Prisijungimo langas visas angliškas, „Sign in“, „Lost your password?“, „Create an Account“, ir net apsaugos klausimas „7 + ten =“. Parduotuvės puslapis Google rodomas kaip „Shop – Stabdžių dalys“, o pagrindiniame puslapyje dar matosi 2015 metų įrašai su „Uncategorized“.

Atskirai tai smulkmenos, bet kartu jos sudaro įspūdį, kad svetainė neprižiūrima, nors prekes jūs keliate dar ir dabar.

Dalį galite padaryti patys: WordPress nustatymuose įjungti lietuvių kalbą ir atnaujinti vertimus. Visą likusį vertimą, pavadinimus ir pagrindinį puslapį sutvarkyčiau per dieną, kaina 100–150 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Dėl mano SEO darbų viena iš jų Google rodosi beveik pirma.

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

Žiūrėjau Cube dviračius dviratininkams.lt ir pastebėjau, kad pagrindinis puslapis neturi pavadinimo, kodo eilutė <title> tuščia. Kituose puslapiuose pavadinimas baigiasi dvitaškiu be nieko, pavyzdžiui „Kontaktai : “. Būtent šį tekstą Google rodo kaip mėlyną nuorodą paieškoje, todėl dabar ten matosi atsitiktinis tekstas arba vien adresas.

Patys galite tai pataisyti SEO įskiepyje, nustatę pavadinimų šabloną, pavyzdžiui „Puslapio pavadinimas | Dviratininkams.lt“. Jei norite, kad sutvarkyčiau aš, pavadinimus ir aprašymus visai svetainei padaryčiau per dieną už 80–150 € + PVM.

Dar pastebėjau, kad kiekvienas dviračio dydis įkeltas kaip atskira prekė. Jei norėtumėte, galima sujungti į vieną prekę su dydžio pasirinkimu, bet tai atskiras pokalbis.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Dėl SEO darbų viena iš jų Google rodosi beveik pirma.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Užėjau į ofnis.lt ir pagrindiniame puslapyje vietoj paieškos laukelio matosi tekstas „[aws_search_form]“. Tai paieškos įskiepio kodas, kuris neveikia, greičiausiai pats įskiepis išjungtas. Slaideryje paspaudus „Buzil valymo priemonės“ ir „Plačiau“, atsidaro „Puslapis nerastas“, meniu du kartus kartojasi „Paslaugos“, o kainos rodomos angliškai, „€ 5,548.00“ vietoj „5 548,00 €“.

Su tokia technika, kur prekės kainuoja tūkstančius, pirkėjas į tokias smulkmenas žiūri kaip į ženklą, ar įmone galima pasitikėti.

Kainų formatą galite pakeisti patys WooCommerce nustatymuose: tūkstančių skirtukas tarpas, dešimtainis kablelis. Visa kita sutvarkyčiau per 1–2 dienas, kaina 100–200 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį po patikrinimo.

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

Žiūrėjau kabelių kanalus elmega.lt ir kompiuteryje šone pastebėjau krumpliaratį „Panel Tool“. Tai temos demonstracinis įrankis, per kurį bet kuris lankytojas gali perjungti parduotuvės spalvas į „christmas“ ar „purple“. Jis turėtų būti išjungtas, bet liko nuo temos įdiegimo.

Be to, kelios kategorijos meniu tuščios, pavyzdžiui „Termosusitraukiantys vamzdeliai su klijais“ ir „Termosusitraukiančios pirštinės“. Dar įvedus elmega.lt be www, svetainė trumpam peršoka į nesaugią http versiją ir tik tada grįžta į https.

Panelę galite pabandyti išjungti ir patys, temos nustatymuose. Visa tai sutvarkyčiau per pusdienį, kaina 60–120 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau jos OpenCart ir WordPress parduotuves: siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Žiūrėjau gyvūnų prekes viskaszoo.lt ir meniu „Egzotiniams gyvūnams“ beveik visos kategorijos tuščios: „Apšvietimas“, „Šildymas“, „Maistas“, „Vitaminai ir mineralai“ rodo „Šioje kategorijoje nėra prekių“. Tas pats su „Skanėstai paukščiams“ ir „Vandens priežiūros priemonės“ žuvims, iš viso radau devynias tokias. Žmogus, kelis kartus atsidaręs tuščią puslapį, dažniausiai nebeieško toliau.

Dar įvedus adresą be https svetainė atsidaro nesaugi ir nenukreipia į saugią versiją.

Tuščias kategorijas galite patys išjungti administravime arba paslėpti Journal temos nustatymuose. Jei norite, kad padaryčiau aš, kartu su https peradresavimu ir meniu nuorodų sutvarkymu, tai pusdienio darbas, kaina 60–120 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

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

Žiūrėjau šilumos siurblius sildymasjums.lt ir atkreipiau dėmesį į nuorodas. Lietuviškos raidės jose ne pakeistos, o tiesiog išmestos: „Vonios įranga“ tapo /vonios-ranga, „Montavimo priedai šilumos siurbliams“ tapo /montavimo-priedai-ilumos-siurbliams, „dūmtraukiai“ tapo „dmtraukiai“. Google iš adreso irgi supranta, apie ką puslapis, tad tokie žodžiai paieškai nepadeda.

Dar kelios kategorijos meniu tuščios, pavyzdžiui „Izoliacinės plokštės“ ir „Vamzdžiai šildymui-vandentiekiui“, o įvedus adresą be https svetainė atsidaro nesaugi.

Tuščias kategorijas galite išjungti patys administravime. Adresus perrašyčiau teisingai ir nuo senų nustatyčiau peradresavimus, kad nedingtų tai, kas jau surinkta Google. Kartu su https 1–2 dienos, kaina 100–200 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Dėl SEO darbų viena iš jų Google rodosi beveik pirma.

Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.

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

Žiūrėjau baldų kolekcijas balduideja.lt ir meniu paspaudus „Nature“ arba „Mango“ atsidaro „Kategorija nerasta!“. „Atelie“, „Roma“, „Mestre“ ir „Čiužiniai“ atsidaro, bet tušti. Dar meniu nuorodos įrašytos su http, todėl paspaudus jas lankytojas iš saugios versijos numetamas į nesaugią, su užrašu „Nesaugi“.

Baldai brangus pirkinys, ir prieš pirkdamas žmogus svetainėje praleidžia daug laiko, tad tokios vietos krenta į akis.

Tuščias kategorijas galite išjungti patys administravime. Meniu, peradresavimą į https ir kainų formatą, kad būtų „1 890,00 €“, o ne „1,890.00 €“, sutvarkyčiau per dieną, kaina 80–150 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Klientui e.segris.lt neseniai padariau naują dizainą, pritaikytą telefonams.

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

Žiūrėjau raštinės prekes senora.lt ir pastebėjau, kad nemažai temos tekstų liko angliškai. Tuščiame krepšelyje rašo „It's never too late to fix it :)“, apačioje naujienlaiškio blokas „Subscribe to our newsletter“, prie paieškos „Everywhere“, o viršuje „Wishlist“ ir „Compare“. Didžiajai daliai pirkėjų tai nieko nesugadina, bet kai kam tai atrodo keistai.

Dalį frazių galima išversti per OpenCart kalbos failus, bet temos tekstai dažnai būna įrašyti pačiuose šablonuose, todėl juos reikia rasti rankiniu būdu. Išversčiau viską ir patikrinčiau visus puslapius per pusdienį, kaina 50–100 € + PVM.

Esu jaunas, bet baigęs KTU Jaunųjų kompiuterininkų mokyklos svetainių programavimo kursus ir du metus dirbu tėčio įmonėje, tvarkau jos OpenCart ir WordPress parduotuves: siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv.

Sąskaitą faktūrą su PVM išrašome per UAB Siuvimo Manija. Pusę galima mokėti prieš darbą, likutį po patikrinimo.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Kernius Zigmantas
```

Iš viso: 23 laiškai (big: 14, quick: 9)

Rezervas (nesiųsti be vartotojo sprendimo): motogama.lt (svetainė su temos demo prekėmis ir neveikiančiu HTTPS — tikrų prekių nėra), kamtojabaldai.lt (katalogas ir krepšelis 404, kainų nematyti), zookatalogas.lt (nurodytas el. paštas neveikiančiame domene), natureselement.lt (tik http peradresavimas — per maža).
