# Kandidatai D (platformos senumas + kelios problemos, ~250-350 EUR + PVM)

Tyrimo data 2026-10-06. Metodas: 1551.lt kategorijos + e-komercijos katalogo puslapiai (~1900 .lt domenu), automatinis atrinkimas (platforma, versija, viewport, https, PHP klaidos, matomi angliski tekstai), tada rankinis tikrinimas curl/python3. Nieko nesiusta ir niekam neparasyta.

## laptop.lt
- Įmonė / ką parduoda: nešiojamųjų kompiuterių, jų dalių (baterijos, įkrovikliai, ekranai, klaviatūros) ir naudotų kompiuterių parduotuvė (kainos EUR, pvz. Dell Latitude E5550 150,00 EUR).
- Platforma: WordPress + WooCommerce, tema Woodmart. `<meta name="generator" content="WooCommerce 6.4.1">` (2022 m. versija) ir WordPress 7.0.6; `wc-blocks-style.css?ver=7.2.2` (irgi senas). WooCommerce atsilieka kelias versijas nuo WordPress.
- El. paštas: info@laptop.lt (https://laptop.lt/kontaktai/)
- Įrodymai:
  - https://laptop.lt/ : HTML turi 36x `class="... add_to_cart_button ajax_add_to_cart">Add to cart</a>` (angliškas mygtukas prekių blokuose; pvz. "Dell Latitude 13 7300 ... to your cart" aria-label). Tikrinta 2026-10-06 11:24:57 UTC ir 11:28:15 UTC (curl, ne lazy-load, tai matomas tekstas).
  - https://laptop.lt/product-category/atnaujinti-ir-naudoti-nesiojamieji-kompiuteriai/ : matomas tekstas "Showing 1–12 of 22 results", "Sort by popularity / Sort by latest / Sort by price: low to high", "Compare", "Add to wishlist", "Shopping cart". 11:24:57 ir 11:28:15 UTC.
  - Prekės puslapis https://laptop.lt/product/dell-latitude-13-7300-intel-core-i5-8365u/ : "Related products", "Description", "Previous", "Add to cart", "Wishlist" angliškai. 11:24:57 UTC (crawl) ir pakartota pagal tą patį šabloną kitose 2 prekėse (11:24:57).
  - Kategorijų filtre matoma kategorija "Uncategorized" (nuoroda https://laptop.lt/product-category/uncategorized/ , HTTP 200). Pagrindiniame ir visuose puslapiuose. 11:24:57 ir 11:28:15 UTC.
  - Tuščia kategorija: https://laptop.lt/product-category/atnaujinti-ir-naudoti-nesiojamieji-kompiuteriai/acer-atnaujinti-ir-naudoti-nesiojamieji-kompiuteriai/ rodo "No products were found matching your selection." (11:28:15 UTC; meniu rodo Acer kaip veikiančią kategoriją).
  - viewport yra, HTTPS veikia, PHP klaidų nėra (tai ne trūkumai).
- Problema klientui suprantama kalba: lietuviškoje parduotuvėje pirkėjas mato angliškus mygtukus ir užrašus ("Add to cart", "Sort by", "Related products", "Shopping cart"), o meniu rodo "Uncategorized" kategoriją ir bent vieną kategoriją be prekių. Tai atrodo nebaigta ir mažina pasitikėjimą pirkti. Pati parduotuvės sistema (WooCommerce) yra kelerių metų senumo, todėl vėluoja saugumo ir mokėjimų atnaujinimai.
- Siūlomas darbas: išversti visą pirkėjo matomą sąsają (mygtukai, rikiavimas, krepšelis, prekės kortelė, filtrai, el. laiškai), pašalinti "Uncategorized" ir tuščias kategorijas iš meniu/filtrų, saugiai atnaujinti WooCommerce su testavimu (kopija, krepšelio ir DPD įskiepio patikra). Trukmė 3-5 darbo dienos.
- Kaina: 250-350 EUR + PVM
- Pastaba: WooCommerce versija nėra "<=3.x", bet 4 metų atsilikimas + matomas neišverstas UI + tuščios/neteisingos kategorijos = 3 skirtingos patikrintos problemos.

## neidukas.lt  (SU IŠLYGA: vizualiai pirkėjui matoma tik valiutų pasirinkimas, kita techninė)
- Įmonė / ką parduoda: prekės vaikams ir kūdikiams (čiulptukai, kėdutės, žaislai, čiužinukai), kainos EUR.
- Platforma: OpenCart 1.5.x tipo (https://neidukas.lt/catalog/view/theme/theme411/..., `route=checkout/cart`, jquery-ui-1.8.16, jQuery 1.10.2 + 3.0.5 + jquery-migrate-1.2.1 vienu metu). Konkreti OC versija nepatvirtinta (nėra generator), pagrindas: tema ir bibliotekos.
- El. paštas: info@neidukas.lt (rastas pagrindiniame puslapyje, 2026-10-06 11:19 UTC)
- Įrodymai:
  - https://neidukas.lt/ : valiutų pasirinkime kartu su € yra `<a title="Litai" ... value','LTL'...><span>2</span></a>` (litų valiuta, kurios nebėra nuo 2015 m., simbolis rodomas kaip "2"). Tikrinta 11:19:47 UTC ir 11:39:03 UTC.
  - Pagrindinio puslapio HTML 647 159 B, 50 `<script>` žymių, 38 išoriniai .js failai, 25 stiliaus failai; kategorijos puslapis https://neidukas.lt/prekes-kudikiams/ciulptukai/avent-ciulptukai 556 542 B. Atsakas 1,1-1,3 s (curl, 11:19 ir 11:39 UTC). Serveris nutraukia ryšį (connection reset) po kelių greitų užklausų.
  - Poraštėje "&copy; 2009" (11:19:47 ir 11:39:03 UTC); `<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, , initial-scale=1.0">` su sugadinta sintakse (dvigubas kablelis, pasikartojantis initial-scale).
  - Du paveikslėliai pagrindiniame puslapyje grąžino 404 vieną kartą (failų pavadinimai su `Å¾`/`°`; 11:17 UTC); NEPATVIRTINTA antru kartu dėl rate limit, laiške nenaudoti.
- Problema klientui suprantama kalba: telefone/kompiuteryje svetainė kraunasi lėtai, nes siunčia daugiau nei pusę megabaito tik puslapio kodo ir dešimtis skirtingų scenarijų, o viršuje matomas litų valiutos mygtukas su simboliu "2". Seną OpenCart 1.5 šabloną sunku patikimai prižiūrėti.
- Siūlomas darbas: išvalyti nebenaudojamus skriptus ir dubliuotas jQuery versijas, pašalinti litų valiutą, sutaisyti viewport, sumažinti puslapio svorį (meniu išvedimas, lazy-load), patikrinti krepšelį/atsiskaitymą po pakeitimų. 3-5 darbo dienos.
- Kaina: 250-350 EUR + PVM (jei tik valiutos/viewport/skriptų valymas, užtektų 150-250 EUR)
- Išlyga: nėra aiškios sistemos klaidos, kurią pirkėjas pamatytų be matavimų; stiprumas silpnesnis nei laptop.lt.

## citreum.lt  (SU IŠLYGA: B2B katalogas, kainos svečiui nematomos)
- Įmonė / ką parduoda: automobilių aksesuarų ir buities prekių didmeninis katalogas su užsakymu per krepšelį (Kaunas; vaistinėlės, gesintuvai, atšvaitai, autochemija).
- Platforma: OpenCart 1.5.x tipo su stipriai modifikuotu šablonu (`catalog/view/theme/default/stylesheet/`, `route=product/category`, `jquery-1.7.2.min.js`, `jquery.fancybox-1.3.4`). Poraštėje "© Tėja-commerce, sprendimas" (anksčiau svetainę kūrusi agentūra; dizainas senas).
- El. paštas: info@citreum.lt (https://citreum.lt/, "el. paštas: info@citreum.lt")
- Įrodymai:
  - https://citreum.lt/ : HTML neturi jokios `viewport` meta žymės (`grep -ci viewport` = 0). Tikrinta 11:26:44 UTC ir 11:38:51 UTC.
  - Viršuje/filtre "Valiuta : LTL EUR" (litų parinktis 2026 m.) ir "Kaina : Su PVM / Be PVM". 11:27:14 UTC ir 11:38:51 UTC.
  - jQuery 1.7.2 (2012) + fancybox 1.3.4 (2010 m. bibliotekos). 11:38:51 UTC.
  - Kategorijų puslapyje https://citreum.lt/index.php?route=product/category&path=78 prekių sąrašas rodomas lentele (kodas, pavadinimas, "Į krepšelį"), kainų svečiui nerodo (nerasta nė vieno EUR/€ ženklo, 11:27:14 UTC); tikėtina kainos tik prisijungus.
- Problema klientui suprantama kalba: svetainė neprisitaiko prie telefono (reikia mastelį didinti pirštais), o viršuje vis dar siūloma litų valiuta. Prekių sąrašas senoviškos lentelės formos, kainų nematyti kol neprisijungsi.
- Siūlomas darbas: pridėti viewport ir mobilų išdėstymą (CSS, lentelę paversti kortelėmis/horizontaliu slinkimu), pašalinti LTL, atnaujinti senas jQuery/fancybox bibliotekas, patikrinti krepšelį. 4-6 darbo dienos.
- Kaina: 250-350 EUR + PVM
- Išlyga: B2B, kainų nematome; agentūros kreditas poraštėje (galimai turi savo programuotoją); prieš rašant patikrinti, ar tikrai veikia kainos prisijungus.

## Atmesti
- orinukas.lt — labai sena OpenCart (jQuery 1.3.2, thickbox, ie6.css), 118 kainų, bet svetainėje nėra viešo el. pašto (tik telefonas ir "Rašyti žinutę" forma; `route=information/contact` be adreso).
- pego.lt — WooCommerce 3.7.0 + WordPress 5.2.2 (labai sena), rankinių parduotuvė, bet nerasta jokio el. pašto, ir matomų klaidų nėra (viewport, vertimas, krepšelis tvarkingi).
- monokopa.lt — WooCommerce 3.7.3, matomi angliški "Showing", "Sort by", "Buy product", "Related products", "Uncategorized", bet tai Canon katalogas be kainų (mygtukai veda į išorę), ne parduotuvė su kainomis.
- charged.lt — WooCommerce 5.0.0 su angliškais mygtukais, bet visa svetainė angliška (ne LT turinys).
- alvita.lt — daug angliškų užrašų, bet svetainė angliška (verslui į užsienį).
- laikrodistau.lt — pirmas rezultatas rodė 404 paveikslėlius (DOVANOS JAM/JAI.jpg), bet jie yra HTML komentare (`<!-- -->`), ne matomi; atmesta.
- agni.lt, ievossodai.lt — "sugedę paveikslėliai" buvo mano URL dekodavimo klaida; patikrinus nepatvirtinta.
- krivita.lt (WP 4.9.26, ©2017), mususervisas.lt (WP 5.3.25, Woo 3.8.3), fitpulse.lt (WP 4.5.32, Woo 2.6.4), svarossimfonija.lt (WP 5.4.8, Woo 3.6.6) — sena platforma, bet nėra aktyvios parduotuvės su kainomis ir matomų klaidų (prekių/kainų nerodo, arba tik vizitinė).
- ekovala.lt, krivita.lt, techcoat.lt, inzineringas.lt — sertifikato/hostname klaidos ar sena WP, bet vizitinės įmonių svetainės, ne parduotuvės.
- bacoma.lt, artistic.lt, sands.lt, harmonylife.lt ir kiti OpenCart 2.x (jQuery 2.1.1) — veikia, nerasta pirkėjui matomų klaidų (tikrinti paveikslėliai, vidinės nuorodos, PHP klaidos).
- sargiai.lt — OpenCart, tvarkingas, viewport yra (mano pirmas "nėra viewport" buvo regex klaida dėl tarpų žymėje); tik Google+ nuoroda palikta, per menka.
- klinkera.lt, medicata.lt, grindininkai.lt — nuomojama eshoprent platforma.
- Pastaba apie metodą: automatinis tikrinimas rado tik ~3 tikrus kandidatus iš ~1900 domenų, nes dauguma .lt parduotuvių jau atnaujintos (WooCommerce 10-11, OpenCart 2-3 su viewport).

Iš viso: 3 (1 stiprus: laptop.lt; 2 su išlyga: neidukas.lt, citreum.lt)
