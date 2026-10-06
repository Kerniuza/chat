# Partija 7 (LT) - kandidatai (tyrimas, nieko nesiusta)

Sudaryta 2026-10-06 UTC. EXCLUDE: CSV (domain+email) + research/batch6/*.md + outreach6_LT.md + portfolio/segris (351 irasas). Visi patikrinti curl/python, be Browser. Visi kandidatai nera exclude sarase.

## apolina.lt
- Ka parduoda: darbo rubai, batai, pirstines, asmenines apsaugos priemones (didele kategoriju struktura, ~75 kategoriju)
- Platforma: WordPress 4.9.26 + WooCommerce 2.6.4 (`<meta name="generator">` titulinio puslapio HTML; woocommerce.css?ver=2.6.4; tema "oxy" + Visual Composer). Tai 2016-2017 m. versijos.
- El. pastas: info@apolina.lt (titulinio puslapio HTML)
- Irodymai:
  - `curl https://www.apolina.lt/` -> `content="WordPress 4.9.26"`, `content="WooCommerce 2.6.4"`. Patikrinta 13:20 UTC ir 13:40 UTC.
  - `https://www.apolina.lt/produkto-kategorija/darbo-pirstines/aplietos-pirstines/aplietos-pvc/` -> HTTP 200, tekstas "Nerasta jokių produktų" (tuscia kategorija meniu). 13:34 UTC ir 13:40 UTC.
  - `https://www.apolina.lt/produkto-kategorija/darbo-rubai/zieminiai-rubai/kombinezonai-pasiltinti/` -> tuscia ("Nerasta jokių produktų"). 13:35 UTC (scan) ir 13:40 UTC (pakartota is scan 75 kategoriju: is viso 2 tuscios).
  - Titulinio puslapio `<title>`: "Apolina | Darbo rūbai-Darbo batai-Darbo pirštinės-Asmeninės apsaugos priemonės-Darbo drabužiai-UAB Apolina" (raktazodziu sarasas vietoj pavadinimo). 13:20 UTC ir 13:40 UTC.
  - Pastaba: serveris kelis kartus nutraukinejo rysi (connection reset) esant daugeliui uzklausu - tikrinti retai.
- Kodel tai kenkia verslui: 9 metu senumo WooCommerce/WordPress be saugumo atnaujinimu - viena is dazniausiu nulauzimo priezasciu, o checkout'as gali nustoti veikti pakeitus PHP versija; tuscios kategorijos meniu vercia pirkeja galvoti, kad prekiu nera.
- Siulomas darbas: WP + Woo atnaujinimas i dabartines versijas (su kopija ir temos suderinamumo patikra), tusciu kategoriju sutvarkymas, title/meta. 3-5 d. d.; preliminariai nuo 300 € + PVM (didelis darbas, kaina nespeti kol nematyta tema/plaginai).

## rykliukas.lt
- Ka parduoda: povandenines medziokles ir nardymo iranga (SpearLab)
- Platforma: WordPress 6.1.14 + WooCommerce 6.9.5 (generator meta; WPBakery, Slider Revolution 6.5.25). Versijos 2022-2023 m.
- El. pastas: info@rykliukas.lt (titulinio puslapio HTML; taip pat international@rykliukas.lt)
- Irodymai:
  - 7 is 7 patikrintu kategoriju puslapiu `<title>` baigiasi "Archives - RYKLIUKAS", pvz. `https://rykliukas.lt/product-category/kojines-ir-pirstines-ir-kiti-neopreno-aksesuarai/` -> "Neopreno gaminiai Archives - RYKLIUKAS"; `.../plaukmenys-ir-ju-kaliosai/kaliosai/` -> "Kaliošai Archives - RYKLIUKAS"; `.../svoriai-ir-ju-sistemos/` -> "Svoriai ir jų sistemos Archives - RYKLIUKAS". 13:38 UTC ir 13:40 UTC.
  - `https://rykliukas.lt/product-category/priedai-ginklams-ir-aksesuarai/neopreno-klijavimui-skirti-klijai/` -> 200, "Produktų nerasta" (tuscia). `https://rykliukas.lt/product-category/laisvojo-nardymo-iranga/plaukmenys/mono-fins-ir-bi-fins/` -> 200, "Produktų nerasta". 13:38 UTC ir 13:40 UTC.
  - `curl https://rykliukas.lt/` -> `WordPress 6.1.14`, `WooCommerce 6.9.5` (13:38 / 13:40 UTC).
- Kodel tai kenkia verslui: Google rezultatuose kategorijos rodomos kaip "... Archives" - maziau paspaudimu ir silpnesnes pozicijos; tuscios kategorijos meniu; pasenusi versija be saugumo atnaujinimu.
- Siulomas darbas: kategoriju title/meta sutvarkymas, tusciu kategoriju paslepimas, WP/Woo atnaujinimas. 2-3 d. d.; 250-300 € + PVM.
- Pastaba: check_site rodo "en_strings" tik del JS DataTables konfiguracijos (nematoma pirkejui) - netraukti i laiska.

## topirankiai.lt
- Ka parduoda: elektriniai ir akumuliatoriniai irankiai, sodo technika, auto prekes
- Platforma: OpenCart 1.5.x (jquery-1.7.1.min.js, `index.php?route=module/cgp`, tema "sellya", footer "© 2015-2026").
- El. pastas: info@topirankiai.lt (titulinio puslapio HTML)
- Irodymai:
  - Meniu kategorijos tuscios (4 is 4 patikrintu): `https://www.topirankiai.lt/akumuliatoriniai-irankiai/irankiu-komplektai`, `.../akumuliatoriniai-irankiai/langu-valytuvai`, `.../akumuliatoriniai-irankiai/tiesiniai-pjuklai-103`, `.../auto-prekes/automobiliniai-saldytuvai` -> kiekvienas HTTP 200, tekstas "Šioje kategorijoje nėra prekių." 13:27 UTC ir 13:40 UTC.
  - `<meta name="viewport" content="width=device-width; initial-scale=1.0">` (kabliataskis vietoj kablelio - neteisingas formatas). Pirminis HTML 13:25 UTC; pakartoti nespejau - **patikrinti dar kartą prie rasant** ir nerasyti, kad "neveikia telefone".
  - Kategoriju puslapiai sveria ~280 KB HTML (be paveiksleliu) - sunkus.
- Kodel tai kenkia verslui: tuscios kategorijos meniu nuveda pirkeja i "nera prekiu" ir mazina pasitikejima; OpenCart 1.5 nebeturi saugumo atnaujinimu.
- Siulomas darbas: tusciu kategoriju sutvarkymas, viewport/mobilios versijos patikra, bazinis atnaujinimas / saugumo lopai. 2-4 d. d.; preliminariai nuo 250 € + PVM.

## eimezaisti.lt
- Ka parduoda: surenkami modeliai, klijai ir dazai (SPRAGTUKAS - "Eime zaisti")
- Platforma: OpenCart 2.x (jquery-2.1.1, `route=extension/module/...`, tema "simplica"); footer "© 2014".
- El. pastas: spragtukas@eimezaisti.lt (titulinis ir kontaktu puslapis)
- Irodymai:
  - Kategoriju sarase uzvedus pele rodomas antras paveikslelis (`hover-image`) turi dubliuota prefiksa: `src="https://eimezaisti.lt/image/https://eimezaisti.lt/image/cache/catalog/Academy/12334-254x308.jpg"` -> HTTP 404 (teisingas URL be dublio -> 200). `index.php?route=product/category&path=76_124` -> 8 is 12 hover paveikslelių 404; `path=76_128` -> 11 is 12. 13:24 UTC ir 13:40 UTC.
  - `https://eimezaisti.lt/index.php?route=product/category&path=75_133` ("Profesionalams", meniu) -> "Šioje kategorijoje nėra prekių." 13:25 UTC ir 13:40 UTC.
- Kodel tai kenkia verslui: prekiu nuotraukos "dingsta" uzvedus pele - atrodo kaip sugedusi parduotuve; tuscia kategorija meniu.
- Siulomas darbas: hover paveikslelio kelio klaidos pataisymas, tuscios kategorijos paslepimas. 1 d. d.; 80-130 € + PVM.
- Silpnoka (maza apimtis) - tinka kaip "quick".

## ortopedineskuprines.lt
- Ka parduoda: ortopedines kuprines
- Platforma: OpenCart 2.x (jquery-2.1.1, `route=module/tm`)
- El. pastas: info@ortopedineskuprines.lt (titulinio puslapio HTML)
- Irodymai:
  - `curl -v https://ortopedineskuprines.lt/` -> "SSL certificate problem: unable to get local issuer certificate"; `curl -k -v` rodo `subject: CN=*.serveriai.lt`, issuer PerfectSSL (sertifikatas skirtas hosting'o domenui, ne parduotuvei, taigi narsykle rodys sertifikato klaida). 13:05 UTC ir 13:38/13:40 UTC. (Palyginimui: kiti .lt domenai per ta pati kanala tikrinami normaliai.)
  - `http://ortopedineskuprines.lt/` -> HTTP 200 (veikia tik be HTTPS); prisijungimo forma `action="http://ortopedineskuprines.lt/index.php?route=account/login"` siunciama nesifruotai. 13:38 UTC.
- Kodel tai kenkia verslui: pirkejas su HTTPS nuoroda mato pilno ekrano perspejima ir issiunciantis; HTTP puslapiai zymimi "Nesaugu", slaptazodziai ir adresai keliauja nesifruotai; Google silpniau rodo svetaines be HTTPS.
- Siulomas darbas: tinkamo SSL sertifikato idiegimas, HTTP->HTTPS nukreipimas, OpenCart nustatymu (config.php) pataisymas, mixed content patikra. 1 d. d.; 80-120 € + PVM.
- Ribotumas: sertifikato isdavejo/hostname neatitikima matau per tarpini serveri; prie rasant verta dar karta patvirtinti narsykle.

## duper.lt
- Ka parduoda: hidroponikos sistemos, LED apsvietimas augalams, ismaniuju apyrankiu priedai, dviraciu priedai
- Platforma: WordPress 5.7.14 + WooCommerce 4.7.4 (generator meta), tema gardener-lite. 2020-2021 m. versijos.
- El. pastas: info@duper.lt (check_site, Cloudflare uzkoduotas data-cfemail - dekoduota)
- Irodymai:
  - `curl https://www.duper.lt/` -> `WordPress 5.7.14`, `WooCommerce 4.7.4` (13:07 UTC ir 13:40 UTC).
  - `https://www.duper.lt/produkto-kategorija/led-lemputes-augalams/` -> `<title>LED apšvietimas augalams LED apšvietimas augalams - DUPER.LT` (pavadinimas pasikartoja). 13:07 UTC ir 13:40 UTC.
  - Titulinio puslapio `<title>` yra tik "Parduotuvė - DUPER.LT" (be prekiu aprasymo). 13:07 / 13:40 UTC.
  - Produktu nuotraukos veikia (40 is 40 -> 200), tuscios kategorijos nerastos.
- Kodel tai kenkia verslui: pasenusi versija be saugumo atnaujinimu; Google rodo bendra "Parduotuvė" ir dubliuota pavadinima - mažiau paspaudimu.
- Siulomas darbas: WP/Woo atnaujinimas su temos patikra, title/meta sutvarkymas. 2-3 d. d.; 200-280 € + PVM.
- Silpnoka: viena tikra problema (versija) + SEO smulkmenos.

## Atmesti
- 7arai.lt - nera e-parduotuve (kategorijose nera kainu/krepselio), nors WP 4.9.26/Woo 3.3.6 ir sertifikatas *.serveriai.lt.
- stirnele.lt, olandukepure.lt, miegoklinika.lt - sodybos/apgyvendinimas, ne parduotuves.
- ukmega.lt - B2B katalogas be kainu; "mojibake" pavadinimai buvo mano nuskaitymo klaida (content-type be charset), ne tikra problema.
- hobbyshop.lt - "Add to cart" tik aria-label, nematomas; platforma Woo, svari.
- alyva.lt (pirklys.lt) - 404 paveikslelis uzkomentuotas HTML komentare; kitaip svari; el. pasto nerasta.
- avyte.lt / avytenamams.lt - PHP Warning virs HTML (open_basedir) yra, bet avyte.lt nera parduotuve, avytenamams.lt neatsako (connection reset); galima patikrinti vėliau.
- pirotechnika.lt, gph.lt, viskasskardininkams.lt, baisogalosagroprekyba.lt, pitema.lt, dmndstyle.lt, siulogalas.lt, ustukiumalunas.lt, margirastai.lt - tik viena problema (kategoriju title su "Archives"), modernios versijos; per silpna.
- siulupalepe.lt - 2 kategoriju puslapiai grazino HTTP 500 vienu metu, bet nepasikartojo/nepatikrinta antrą kartą; el. pasto nerasta.
- elsistemos.lt, candles.lt - kategoriju nuorodos 404 buvo mano spėta nuorodu forma, ne is navigacijos.
- inega.lt, vyras24.lt, tercija.lt, stiliausfilosofija.lt, ventaine.lt, baldaipl.lt, sildymoabc.lt, pasauliogeles.lt, safety1.lt, gardenplius.lt, riposo.lt, balticarms.lt, greenlita.lt, kibs.lt, bicsportas.lt, scantechnika.lt, berganso.lt, italiskakrautuvele.lt - patikrinta po ~8 kategoriju puslapiu: nera tikru trukumu (bicsportas.lt: tik 2 slaideriu paveiksleliai no_image.jpg 404 - per silpna).
- heradas.lt, omrina.lt, snackbox.lt, valkor.lt ir kiti modernus WP/Woo/OC is pradinio filtro - modernios versijos, viewport yra, HTTPS ok.

Pastaba del apimties: is ~480 naujai surinktu ir ~50 anksciau rinktu domenu daugumos jau buvo exclude saraso arba jie moderniai prižiūrimi; surasta tik 6 kandidatai (2 stipresni: apolina.lt, rykliukas.lt). Geriau mažiau, bet tikri.

Iš viso: 6
