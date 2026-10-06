# SiteSolvo — nuolatinis kontekstas šiam projektui

Šis failas automatiškai įsikelia į kiekvieną Claude Code sesiją, atidarytą šiame aplanke (`~/Documents/SiteVersa`). Tai yra sprendimas problemai "nauja sesija nieko neprisimena": **visada pradėk naują pokalbį su šiuo aplanku kaip projekto katalogu**, ne tuščią ("No folder") sesiją. Tada šis failas įsikels savaime, be jokio "ar prisimeni?" klausimo.

Bendrauk su vartotoju lietuviškai. Vartotojas — Kernius Zigmantas, vienas žmogus, Junior Achievement (JA) mokomasis startuolis, vidurinės mokyklos mokinys, dirba nešiojamu Mac (naudoja `python3`, ne `python`). Rašo be diakritikų, trumpai, žemos frikcijos triggeriais. Nori trumpų santraukų, ne ilgų aiškinimų, prieš tvirtindamas veiksmą.

**Vardas keitėsi:** startuolis anksčiau buvo **SiteVersa**, nuo 2026-09-19 pervadintas į **SiteSolvo**. Aplanko/failų pavadinimai išlaikė seną vardą (nekeisti be reikalo) — SiteSolvo yra dabartinis vardas, naudoti tik jį kalbant apie startuolį. Vardas šiaip niekada nepasirodo laiškuose klientams (žr. taisyklę #1 žemiau).

---

## PASTABA: debesies sesija (skaityti pirmiausia, 2026-09-26)

Šis repo (`Kerniuza/chat`, GitHub) nuo šiandien taip pat naudojamas SiteSolvo darbui tęsti **nuotoliniu būdu (Claude Code on the web/debesyje)**, greta lokalios Mac sesijos `~/Documents/SiteVersa`. Šis CLAUDE.md čia buvo įkeltas kaip pradinis kontekstas, bet dauguma realių darbo failų **dar nėra perkelti čia**:

- `outreach_tracking.csv` — pilnas 73+ eilučių žurnalas (čia repo yra TIK tuščias su antrašte, žr. `outreach_tracking.csv` šiame repo).
- Atminties failai: `MEMORY.md`, `project_siteversa.md`, `outreach_tracking.md`, `user_ja_startup.md`, `segris_mockup_artifact.md`.
- Siuntimo scriptai (`mac_bundle/send_batch*.py` ir kt.), juodraščiai (`outreach5_EE.md`, `outreach5_LT_LV_candidates.md`, `outreach_batch1_review.md`), research failai (`research/*.md`), Segris kliento failai.
- Gmail kredencialai.

**Kritiška, kol jie neperkelti:** šioje debesies sesijoje **negalima ruošti/siųsti naujos laiškų partijos** — be pilno `outreach_tracking.csv` nėra patikimo do-not-contact sąrašo, taigi kyla reali rizika pakartotinai kontaktuoti jau rašytą domeną (pažeidžia taisyklę #9). Prieš bet kokį naują outreach darbą čia, pirma importuoti realų CSV (ir idealiu atveju kitus atminties failus) iš lokalios Mac sesijos.

**Kredencialai debesyje:** laikytis taisyklės #12 — niekada nerašyti/nekomityti Gmail App Password į repo (jokio `.env` failo git'e). Šioje aplinkoje juos pridėti per sesijos "Edit environment" nustatymus kaip aplinkos kintamuosius `GMAIL_ADDRESS` / `GMAIL_APP_PASSWORD`, ne per commit'inamą failą.

---

## NAUJOS LAIŠKŲ TAISYKLĖS (2026-10-06, galioja virš §1–§2, kur skiriasi)

Vartotojas pakeitė outreach strategiją (LT partijos nuo #6):
- **Tik LT įmonės, tik lietuviškai.** Platforma tik WP/WooCommerce ir OpenCart (stiprybė — senas OpenCart 1.5.x/2.x).
- **Kaina laiške RAŠOMA** kaip intervalas „X–Y € + PVM“ (viena klaida 50–150; kelios/telefono versija 100–250; HTTPS/SSL 50–120; integracija 150–300; dizaino atnaujinimas 250–600; didelis darbas „preliminariai nuo X € + PVM“; prekių kėlimas — kainos nespėti; priežiūra 20–30 €/mėn, jei tinka). Ne „pigiai“, ne „nuolaida“.
- **Portfolio vadinamas „tėčio verslo“ svetainėmis** (ne „giminaičio“): siuvimomanija.lt, husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt, juki.lv.
- **Galima minėti klientą e.segris.lt** (medžioklės prekės): sena OpenCart 1.5, naujas modernus telefonams pritaikytas dizainas nekeičiant sistemos, SSL, 200+ prekių (Hikmicro, Nocpix, Work Sharp) su LT aprašymais/nuotraukomis/video, SEO, prekės susietos su priedais, naujienų slaideris. **Kiek mokėjo — niekada neminėti.**
- **Galima minėti SiteSolvo ir Junior Achievement:** SiteSolvo — vartotojo idėja Junior Achievement (jaunimo startuolių programos) rėmuose. **Įmonės dar neturi.** PVM sąskaitą faktūrą išrašo **UAB Siuvimo Manija** (tėčio įmonė) kaip IT konsultacijas/paslaugas — taip jau buvo išrašyta Segriui. Laiške formuluoti sąžiningai: „sąskaitą faktūrą su PVM išrašome per Siuvimo Maniją kaip IT paslaugas“, nesakyti „mano įmonė“.
- **Prisistatymas laiške (vartotojo patikslinta 2026-10-06):** JA/SiteSolvo laiške NEMINĖTI. Vietoj to: esu jaunas, bet esu baigęs KTU Jaunųjų kompiuterininkų mokyklos (KTU JKM) svetainių programavimo kursus ir 2 metus dirbu tėčio įmonėje (UAB Siuvimo Manija) — turiu darbo stažą. Tonas: žmogus su patirtimi, ne pradedantysis. Visada išvardinti VISAS 6 tėčio svetaines.
- Mokėjimas dalimis: paprastai 50 % avansu, likutis kai darbas atliktas ir klientas patikrino.
- Laiško struktūra: trūkumas su konkrečia detale → kodėl svarbu verslui (1–2 sak.) → ką padaryčiau, per kiek laiko, už kiek → kas aš (tėčio svetainės + Segris) → PVM sąskaita ir mokėjimas dalimis → švelnus kvietimas (trumpas planas/ekrano nuotrauka) → „Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.“ → „Kernius Zigmantas“. 120–200 žodžių, „Laba diena,“/„Sveiki,“, „Jūs“ forma, be šauktukų/sąrašų/emoji/HTML. Draudžiami AI žodžiai: „skaitmeninis buvimas“, „sprendimai“, „inovatyvus“, „efektyvus“, „sklandus vartotojo patyrimas“, „optimizuoti jūsų verslą“, „nedvejodami kreipkitės“, „džiaugčiausi galimybe“, „esu įsitikinęs“, „kelti į naują lygį“.
- **Prieš kiekvieną siuntimą parodyti vartotojui bent vieną (geriau 2–3) pilną laišką** — jis tikrina, ar neskamba kaip AI. Siųsti tik po „siųsk“. Maks. 30/d., 8–10 s pertrauka, `formataddr(("Kernius Zigmantas", GMAIL_ADDRESS))`.
- Atsakymus gavus — nieko nesiųsti pačiam, parodyti vartotojui su atsakymo juodraščiu. Prašantiems nebe rašyti — CSV status `do_not_contact`.
- Siuntimo scriptas: `mac_bundle/send_batch_lt.py` (dry run be `--send`, DNC tikrinimas iš CSV, CSV papildymas).

## Ryšio problemos ir „tęsk“ (vartotojo taisyklė 2026-10-06)

- Jei matosi, kad dingsta internetas / ryšys blogas (curl į kelias skirtingas svetaines nepavyksta, `$HTTPS_PROXY/__agentproxy/status` `recentRelayFailures` daug skirtingų hostų, agentai miršta su ECONNRESET) — **sustabdyti viską** (TaskStop agentams), išsaugoti progresą, commit+push, ir pasakyti vartotojui.
- Pavienis vienos svetainės blokas (pvz. 1551.lt rate-limit) NĖRA ryšio problema.
- Progresas visada laikomas `research/batch<N>/STATUS.md` (atlikta / kitas žingsnis) ir push'inamas po kiekvieno žingsnio.
- Vartotojui parašius **„tęsk“** — perskaityti naujausią `research/batch*/STATUS.md` ir tęsti nuo „Kitas žingsnis“.

## 0. Kas parduodama (SiteSolvo)

Svetainių **tobulinimo** paslaugos esamiems e-shopams — NE naujų svetainių kūrimas nuo nulio:
- klaidų taisymas gyvose svetainėse (formatavimas, sugadintos nuotraukos, dublikatai, importo šiukšlės)
- integracijos (siunta pvz. Swotzy, mokėjimai pvz. Paysera, daugiakalbiai filtrai)
- masinis produktų kėlimas su AI aprašymais
- dizaino atnaujinimai / temos modernizavimas
- SEO title/meta sutvarkymas (kukliai — tai ilgo laiko darbas, ne greitas per 9 mėn.)
- Platformos: **WordPress/WooCommerce ir OpenCart** (įsk. labai senas OpenCart 1.5.x versijas). Kitos platformos (Shopify, PrestaShop, Magento, Verskis, custom) — NE taikinys.

**Kainos (diapazonai, ne fiksuotos):** klaidos taisymas €50-150 · integracija €150-300 · masinis produktų kėlimas €X/100 prekių (X niekada nenustatytas — tuščia vieta) · dizaino atnaujinimas €200-500 · papildomai mėnesinis priežiūros abonementas €20-30/mėn (atmintis primygtinai sako tai visada minėti pasiūlyme — realybėje NĖ VIENAME laiške ar sandėryje jis dar nebuvo paminėtas; patikrinti su vartotoju, ar tikrai to nori).

---

## 1. AUKSINĖS TAISYKLĖS (nepažeisti be aiškaus vartotojo pakeitimo)

1. **Niekada neminėti įmonės/verslo laiškuose.** Laiškai rašomi kaip privataus asmens, pasirašomi tik "Kernius Zigmantas". Jokio "SiteSolvo", jokios kainos, jokio telefono, jokios svetainės nuorodos klientui skirtame laiške (išskyrus portfolio nuorodas, žr. #4).
2. **Kiekvienas trūkumas laiške privalo būti realiai patikrintas** gyvoje svetainėje/HTML prieš rašant — niekada nesugalvoti, niekada "papildyti" skaičių dirbtinai. Geriau parašyti mažiau patikrintų nei daugiau su spėjimais (precedentas: 50→35 partijoje #2).
3. **Tikslinės platformos: TIK WordPress/WooCommerce arba OpenCart.** Platforma patvirtinama iš `wp-content`/`woocommerce` arba `index.php?route=`/`catalog/view/theme` žymių gyvame HTML. Kita — atmesti, nesvarbu kokie trūkumai.
4. **Portfolio (nuo partijos 3): tikslios 6 nuorodos, tik jos:**
   `https://siuvimomanija.lt`, `https://elna.lt`, `https://babylock.lt`, `https://husqvarna-viking.lt` (**su brūkšneliu — būtinai**; `husqvarnaviking.lt` neveikia), `https://siuvimomasina.lt`, `https://juki.lv` (pridėta 2026-09-26; konkrečių, atskirai patikrintų teiginių apie darbus čia dar nėra — žr. leidžiamus teiginius žemiau, kol vartotojas nepapildys).
   Rėmas: šios svetainės priklauso **giminaičio verslui** (laiškuose "giminaičio", NIEKADA "tėčio" — tas žodis vartojamas tik Segris sąskaitos temoje su tėčio įmone). Leidžiami teiginiai (TIK šie, kitų negalvoti): siuvimomanija.lt buvo ~2010 m. OpenCart, atnaujinta; automatinis siuntimo kainos skaičiavimas įdiegtas; mokėjimas kortele veikia sklandžiai; SEO, dėl kurio viena svetainė rodosi beveik pirma Google.
5. **"Big job" laiškai NIEKADA neįvardija kainos.** Vietoj to — pasiūlymas atlikti pilną apžiūrą ir paruošti planą, "be konkretaus skaičiaus dabar, kol nepažiūrėjau atidžiau".
6. **Tonas: kaip rašo žmogus, ne AI/rinkodara.** Be sąrašų, be paryškintų antraščių/emoji, be "korporatyvinio" žodingumo. Paprasti sakiniai, teisinga gramatika, bet nekonstruotas. Vartotojo žodžiais: "rasyk kaip zmogus per zinute raso", "buk pohuistas".
7. **Kalba: LT parduotuvėms lietuviškai, LV/EE parduotuvėms angliškai.** (Sprendimas be pasipriešinimo — bet niekada nebandyta rašyti latviškai/estiškai; galima pasiūlyti kaip eksperimentą.)
8. **Prieš siunčiant NAUJĄ šablono variantą — parodyti vartotojui juodraštį ir palaukti patvirtinimo.** Kai šablonas jau žinomas/kartojasi, vartotojas gali iš anksto autorizuoti visą partiją savo užklausoje ("surask ir issiusk").
9. **Kartotinio kontakto DRAUDIMAS.** Kiekvienas laiškas žada "daugiau nerašysiu" / "I won't write again" — tai reiškia visi `no_reply` kontaktai (71 iš 73, žr. CSV) yra **do-not-contact sąrašas amžinai**, ne "kol neatsakys". Sekimo/follow-up klausimas atsakiusiems (Dmitry atveju) yra atviras — žr. §5.
10. **Niekada nebandyti pilnai autonominio/nesustabdomo siuntimo.** `/loop` skill buvo blokuotas klasifikatoriaus ("Unauthorized Persistence"). Nebandyti to apeiti (savo cron/launchd scriptu ir pns) — tas pats dalykas kitu keliu. Sutarta darbo eiga (žr. §3) yra rankiniu trigeriu, bet greita.
11. **Niekada neatskleisti klientams/adresatams, kad naudojamas Claude/AI.** Taikoma ir laiškams, ir bet kokiam kliento matomam turiniui (pvz. maketai).
12. **Kredencialai niekada nerašomi/nerodomi pokalbyje.** Gmail App Password gyvena TIK `mac_bundle/gmail_credentials.env` (raktai `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`), vartotojas pats įrašo. Scriptai skaito failą vykdymo metu. (Debesies sesijoje — žr. pastabą viršuje: per aplinkos kintamuosius, ne failą.)
13. **Prieš siunčiant sąskaitą/pasirašant su NAUJU klientu — priminti**, kad reikia patikrinti su JA mokytoju, kaip formaliai priimti mokėjimą per JA įmonę (žr. §7 atviri klausimai). Segris atveju tai apeita per tėčio UAB Siuvimo Manija subrangos sutartį (yra reali sutartis) — tai NE bendra taisyklė kitiems klientams, kol neaptarta iš naujo.

---

## 2. Šablonai (naudoti pakartotinai, koreguoti formuluotę, ne struktūrą)

Struktūra visada: pasveikinimas → 1 pastraipa (kaip radau + KONKRETUS patikrintas trūkumas su pavyzdžiais + švelni pasekmė) → (nuo partijos 3) portfolio pastraipa → pasiūlymas → atsisakymo eilutė → parašas. Plain text, be HTML, be priedų, be jokios kitos nuorodos nei portfolio.

### Quick lead, LT
```
Sveiki,

Naršydamas užtikau jūsų parduotuvę [domain] ir pastebėjau, kad [KONKRETUS PATIKRINTAS TRŪKUMAS]. Tikriausiai smulkmena, kurios niekas nepastebėjo, bet [pasekmė].

Aš jau kurį laiką tvarkau kelias parduotuves – jos priklauso mano giminaičio verslui, ir aš juo rūpinuosi. Štai keletas iš jų, jei norėtum pasižiūrėti: https://siuvimomanija.lt, https://elna.lt, https://babylock.lt, https://husqvarna-viking.lt, https://siuvimomasina.lt, https://juki.lv. Siuvimomanija.lt anksčiau veikė ant maždaug 2010 metų OpenCart versijos – aš ją atnaujinau, kad viskas atrodytų tvarkingai ir veiktų kaip reikia. Be to sutvarkiau automatinį siuntimo kainos skaičiavimą, kad kainą paskaičiuoja pati sistema, o ne žmogus ranka, sutvarkiau, kad mokėjimas kortele veiktų sklandžiai, ir padariau SEO darbus, dėl kurių viena iš svetainių dabar Google paieškoje rodosi beveik pirma.

Jei būtų įdomu, galėčiau pažiūrėti atidžiau ir pasakyti, ką verta taisyti pirmiausia – be jokių įsipareigojimų.

Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.

Geros dienos,
Kernius Zigmantas
```

### Quick lead, EN (LV/EE)
```
Hi,

While browsing I came across your shop [domain] and noticed that [SPECIFIC VERIFIED FLAW]. [natural consequence].

I've been taking care of a few online shops for a while now - they belong to a relative of mine who runs a business, and I handle the sites for him. A few examples if you want to take a look: https://siuvimomanija.lt, https://elna.lt, https://babylock.lt, https://husqvarna-viking.lt, https://siuvimomasina.lt, https://juki.lv. Siuvimomanija.lt was running on an OpenCart version from around 2010 when I started on it - I brought it up to date so it looks right and actually works properly. I also set up automatic shipping cost calculation instead of someone typing it in by hand, got card payments working smoothly, and did some SEO on one of them that now shows up basically first when you search for it.

If it's of interest, I could take a closer look and tell you what's worth fixing first - no obligation at all.

If this isn't relevant, just ignore this - I won't write again.

Have a good day,
Kernius Zigmantas
```

### Big lead — po trūkumo aprašymo įterpti šitą eilutę, tada portfolio, tada uždarymą pakeisti
LT: `Tai jau nebe smulkmena – panašu, kad čia reikėtų nemažo darbo, kol visa tai būtų sutvarkyta.` … uždarymas: `Jei įdomu, galėčiau atidžiai peržiūrėti visą svetainę ir paruošti planą, ką ir kokia tvarka verta taisyti – be jokių įsipareigojimų ir be konkretaus skaičiaus dabar, kol nepažiūrėjau atidžiau.`

EN: `That's not really a small thing - it looks like it'd take a proper chunk of work to sort out.` … closing: `If it's of interest, I could take a proper look at the whole site and put together a plan for what's worth tackling first - no obligation, and no number thrown out yet until I've actually looked.`

### Subject-line stilius
- Quick, generuota: LT `Pastebėjau vieną dalyką jūsų svetainėje`; EN `Noticed something on your website` (rotuoti variantus, kad nebūtų identiški).
- Quick, personalizuota (nuo partijos 3, geriau): domenas + trūkumas subjecte, pvz. `Maža detalė store24.lt prekės kortelėje`, `Quick heads-up about a broken product photo on minikid.lv`.
- Big: problema subjecte, pvz. `buvejam.lv is still running on 2011-era OpenCart files`, `No HTTPS at all on martaplus.lv — noticed while looking at your tools`.

### "Big" kvalifikavimo kriterijai (bet kuris iš šių, patikrintas su įrodymu)
- Iš viso nėra HTTPS arba sertifikatas netinka domenui (`curl -v https://domain`, `openssl s_client -connect host:443 -servername host`).
- Aiškiai dešimtmečio senumo platforma (jQuery/tema versija, `Last-Modified` header ant .js failo, footer copyright metai, changelog).
- Krepšelis/checkout realiai sugedęs arba neveikia visame puslapyje.
- Katalogo lygio duomenų korupcija — imti 10-15 prekių iš 3 kategorijų, skaičiuoti tik jei ~pusė+ turi problemą, su tiksliais skaičiais laiške ("patikrinau 15 iš 3 kategorijų, iš viso 45...").
"Vienas ar du izoliuoti dalykai NĖRA big — tai quick." Big emailų NIEKADA nebūna kainos.

### Verifikacijos taisyklės (svarbu — čia buvo klaida su tehnikajums.lv)
- **Patikrinti dukart per kelias minutes**, ar trūkumas ne lazy-load artefaktas (`data-src`, tikrinti realaus vaizdo URL su `curl -o /dev/null -w "%{http_code}"`).
- **Tikrinti realų dydį/atributus, ne tik ar failas egzistuoja** — nuotrauka gali įkeltis, bet būti `width="1" height="1"` (tikras atvejis, kur Claude klaidingai pasakė "nuotrauka trūksta"). Naršyklės JS: `Array.from(document.querySelectorAll('img')).map(i=>({src:i.src,naturalWidth:i.naturalWidth}))`.
- **WebFetch tekstas NĖRA įrodymas** — jis kartais rodo `.screen-reader-text` ar lazy placeholder kaip tikrą klaidą. Kiekvieną WebFetch pastebėtą "klaidą" patvirtinti su curl+grep arba naršyklės DOM užklausa prieš rašant laišką.
- Spėti URL neleidžiama — naudoti tik tikrus, iš navigacijos paimtus adresus.

---

## 3. Sutarta darbo eiga (nauja partija)

1. Vartotojas rašo **"nauja partija"**.
2. Perskaityti `outreach_tracking.csv`, ištraukti visus 73 (ir toliau augantį) domenus + 6 portfolio domenus kaip EXCLUDE sąrašą.
3. Paleisti **tris atskirus agentus fone (LT, LV, EE)**, kiekvienam savo self-contained prompt su exclude sąrašu, platformos/kategorijos/kalbos taisyklėmis iš šio failo. **SVARBU: agentai turi naudoti TIK curl/python, NE Browser tool** — trys agentai vienu metu naudojantys tą pačią Browser pane vienas kitam sugadino navigaciją praeitą kartą (žr. §6 klaidas). Naršyklė — tik pagrindinei sesijai arba vienam agentui vienu metu.
4. Tikslas: ~5 "big" + ~15 "quick" per dieną (vartotojo sprendimas), arba mažiau jei tiek nerandama tikrų trūkumų — geriau mažiau tikrų nei daug spėtų.
5. Kiekvienas agentas rašo į `outreach<N>_<CC>.md` **scratchpad** kataloge griežtu formatu (žr. §4) — **BET IŠKART nukopijuoti į `~/Documents/SiteVersa/`, kai agentas baigia**, kitaip failas pradingsta kai scratchpad išvalomas (tai atsitiko su batch 5 EE failu — atkurta rankiniu būdu, žr. `outreach5_EE.md`).
6. Perskaityti failus, pateikti vartotojui trumpą suvestinę (kiekiai, keli pavyzdžiai).
7. Vartotojas rašo **"siųsk"**.
8. Parašyti naują `send_batch<N>.py` `mac_bundle/` kataloge (nukopijuoti struktūrą iš `send_batch3_25.py` arba `send_batch_big7.py` — jie turi try/except, `time.sleep(6)`, `BATCH_DONE: sent=N failed=M` suvestinę pabaigoje). Vykdyti: `cd ~/Documents/SiteVersa/mac_bundle && python3 send_batch<N>.py`.
9. Po siuntimo: pridėti eilutes į `outreach_tracking.csv` (status `no_reply`), atnaujinti šį failą arba `project_siteversa.md` atmintį su nauja būsena.

Jei agentas mirė dėl tinklo klaidos (ECONNRESET, sesijos limitas), `SendMessage` su "tinklo klaida turėtų būti išsprendus, tęsk nuo tos vietos, kur sustojai, ir baik užduotį".

Jei vartotojas rašo "stop" / "stop for now" — sustabdyti VISKĄ nedelsiant, jokio siuntimo, agentai gali baigti fone, bet rezultatai laikomi, kol vartotojas nepasakys tęsti.

---

## 4. Agento prompt šablonas (kopijuoti, keisti šalį/kalbą)

```
Ieškok REALIŲ, dabar veikiančių lietuviškų (.lt) WordPress/WooCommerce arba OpenCart parduotuvių, dviejų kategorijų:

"Quick" (tikslas ~5-6): mažesni tikri trūkumai — sugadintos/placeholder nuotraukos, kainų formatavimo klaidos, dubliuoti meniu/kategorijų punktai, negyvos nuorodos, importo artefaktai. Kiekvienas trūkumas turi būti PATS pamatytas su cituotu įrodymu, patikrintas dukart, kad ne lazy-load.

"Big" (tikslas ~1-2): RIMTOS, sisteminės, patikrinamos problemos, kurias sutvarkyti užimtų savaites/mėnesius — visiškai nėra HTTPS (patikrinti realų schema/sertifikatą), aiškiai sena neatnaujinta platforma, sugedęs krepšelis/checkout visame puslapyje, arba katalogo lygio duomenų korupcija (imti 10-15 prekių, skaičiuoti tik jei pusė+). Vienas-du izoliuoti dalykai NĖRA "big".

JAU KONTAKTUOTA — NEKONTAKTUOTI šitų domenų (žr. outreach_tracking.csv pilną sąrašą; įklijuoti visus). Taip pat NIEKADA nekontaktuoti portfolio svetainių: siuvimomanija.lt, elna.lt, babylock.lt, husqvarna-viking.lt, siuvimomasina.lt, juki.lv.

Rasti realų publikuotą kontaktinį el. paštą (footer/kontaktų puslapis) — jei nerasta, kandidatą mesti.

LAIŠKO ŠABLONAS — lietuviškas, kasdieniškas žmogaus tonas (ne korporatyvinis/AI), pasirašyti tik "Kernius Zigmantas", niekada neminėti įmonės/verslo. [ĮKLIJUOTI QUICK/BIG ŠABLONĄ IŠ §2].

Vary formuluotę natūraliai kiekviename laiške, bet portfolio pastraipą laikyti arti pateikto teksto.

IŠVESTIS: rašyti rezultatus į `<scratchpad>/outreach<N>_<CC>.md` Markdown formatu. Kiekvienai svetainei:

## <domain>
- Platform: WooCommerce / OpenCart
- Category: quick / big
- Contact email: <email>
- Evidence URL: <url>
- Evidence quote/sampling: "<tikslus įrodymas>"
- Flaw description (internal, 1 sentence)
- Subject: <subject eilutė>
- Email body: <pilnas juodraštis>

Geriau parašyti mažiau nei papildyti nepatikrintomis svetainėmis. Pabaigoje "Total: N quick, M big".
```
LV/EE versijos skiriasi tik: šalies kodas, kalba (LANGUAGE: emails in ENGLISH), EN šablonas iš §2, EE quick tikslas "~4-5".

---

## 5. Dabartinė būsena (2026-09-26)

**73 laiškai išsiųsti** 4 partijomis (6+35+25+7). Autoritetingas žurnalas: `outreach_tracking.csv` (patikrinti/pataisyti 2026-09-26 — anksčiau turėjo neteisingai formatuotą eilutę tehnikajums.lv ir pasenusią e.segris.lt būseną; abu ištaisyti). Šalys: LT 23 · LV 30 · EE 20. Kategorijos: quick 66 · big 7. Do-not-contact sąrašas = visos 73 eilutės CSV faile + 6 portfolio domenai.

**2 atsakymai iš 73 (2.7%):**

- **tehnikajums.lv (Dmitry)** — `status: REPLIED`. Atsakė 2026-09-20 tą pačią dieną (per ~80 min): patvirtino "Uncategorized" + rusiškas kategorijas kaip realią problemą, paprašė pilno sąrašo, KAS reikia sutvarkyti; papildomai paprašė **daugiakalbio (LV/EN/RU) gamintojo/prekės ženklo filtro**, kuris veiktų (pvz. LG skalbimo maš. filtras). Kernius pirmą atsakymą (su nuotraukos "trūksta" teiginiu) išsiuntė, Dmitry atrėžė, kad nuotrauka jam rodosi — po to nusiųstas pataisytas atsakymas su tikslia priežastimi (nuotrauka kraunasi, bet `<img>` turi `width="1" height="1"` sugadintuose WP metaduomenyse) + pasiūlymas €90-130 kategorijų sutvarkymui ir kitų sugedusių nuotraukų peržiūrai, filtras — atskirai po įvertinimo (~€150-300 integracija). Papildomas portfolio/įrodymo laiškas buvo paruoštas, bet **nėra patvirtinta, kad išsiųstas**. Nuo Dmitry — tyla 6 dienas. **Kai grįši prie šito: atsakyk TAME PAČIAME Gmail thread, NEKARTOK kategorijų pastebėjimo, atsakyk į filtro klausimą.** (Kontakto adreso skirtumas: siųsta į `info@tehnikajums.lv`, atsakė iš `tehnikajums@inbox.lv` — CSV laiko pastarąjį.)
- **e.segris.lt** — `status: CLIENT` (CSV pataisyta, anksčiau klaidingai rodė `no_reply`). Pirmas mokantis klientas. Pilna istorija: `project_siteversa.md` atmintyje. Trumpai: €450+PVM (dizainas+SSL+importas €400, SEO €50), 50/50, avansas išrašytas per UAB Siuvimo Manija; SSL padaryta 2026-09-26 už €0; dizaino maketas nusiųstas klientui, laukiama atsakymo.

**Partija 5 — NIEKADA neišsiųsta, tyrimas pradėtas ir nutrauktas ("stop for now" 2026-09-22):**
- **EE — 6 pilni juodraščiai paruošti** (5 quick + 1 big), atkurti ir išsaugoti `outreach5_EE.md`. Duomenys 4+ dienų senumo — **patikrinti iš naujo prieš siunčiant** (ypač pruulimine.ee 0,00€ kaina — galimai tyčinis "kaina pagal pareikalavimą", nepatikrinta su krepšeliu).
- **LT/LV — jokio failo, agentai mirė nebaigę.** Rasti, bet neparašyti į laišką kandidatai (adresai, įrodymai) išsaugoti `outreach5_LT_LV_candidates.md` — reikia iššifruoti 1 el. paštą (grojam.lt, Cloudflare), patikrinti keletą su curl, ir tada parašyti juodraščius.

**Optimizavimo idėjos (duomenimis pagrįstos, iš 73 siųstų laiškų analizės):**
1. **From vardas nenustatytas kode** — visi 73 laiškai išėjo be "Kernius Zigmantas" vardo laiško antraštėje, tik su plika Gmail adresu (`msg["From"] = gmail_address`). Pigus pataisymas naujam scriptui: `from email.utils import formataddr; msg["From"] = formataddr(("Kernius Zigmantas", gmail_address))`. **Tai pirmas dalykas, kurį taisyti optimizuojant.**
2. Trūkumo tipai: 36% visų quick laiškų buvo apie trūkstamas/placeholder nuotraukas — 0 atsakymų. Neišverstas UI tekstas (9 laiškai, "Showing X of Y", "Sale!") davė 1 atsakymą. Apsvarstyti mažiau nuotraukų-trūkumų, daugiau duomenų/saugumo trūkumų.
3. "Big" takelis konvertavo 1/7 (14%) vs quick 1/66 (1.5%) — laikyti bent 5 big/15 quick mišinį arba didinti big dalį.
4. Subject eilutės: problema-pavadinimu subjectai (batch 4) turėjo vienintelį konversiją; domenu-pavadinti (batch 3) — 0/25. Verta A/B testo.
5. Portfolio pastraipa (~90 žodžių) davė 0 atsakymų 25 quick laiškuose po 5 dienų — galima išbandyti trumpesnę versiją (1-2 sakiniai, tik siuvimomanija.lt + Google reitingo teiginys).
6. LV/EE rašyta angliškai — niekada neišbandyta gimtoji kalba (bent LV/EE subject eilutę).
7. Kontaktų kokybė: 7 laiškai eina į asmeninius pašto adresus (gmail/yahoo/outlook/inbox.lv), 3 į kitą įmonės domeną — šie greičiau pasiekia tikrą savininką nei generic `info@`; vienintelis patvirtintas atsakymas (Dmitry) atėjo iš `inbox.lv` adreso.
8. CSV neturi `sent_at` (laikas, ne tik data), `subject`, `language`, `template_version`, `bounced` statuso — verta pridėti naujoms partijoms, kad būtų galima matuoti, kas veikia.
9. Nepatikrinta jokia atsimetimų (bounce) statistika — prieš skalę iki 20/d. patikrinti pašto dėžutę.

---

## 6. Techninės detalės ir žinomos klaidos (kad nekartotum)

- **Siuntimas:** `smtplib.SMTP_SSL("smtp.gmail.com", 465)`, `MIMEText(..., "plain", "utf-8")`, viena žinutė per gavėją, `time.sleep(6)` tarp siuntimų (batch 1 naudojo 2s). Scriptai NEIŠSAUGO log failo — tik stdout `SENT:`/`FAILED:`/`BATCH_DONE`. Vykdyti iš `mac_bundle/` katalogo (`CRED_PATH` yra reliatyvus).
- **Trys agentai vienu metu naudojantys Browser pane trypė vieni kitų tabus** (viena šalis matė kitos šalies puslapį) — praeitą kartą tai suklaidino EE agentą, kuris pervėjo prie curl/WebFetch ir todėl vienintelis baigė darbą. **Nauji agentai — TIK curl/python, jokio Browser tool.**
- **Zsh globbing:** neuždėti kabutėse `?route=...` URL'ai lūžta ("no matches found") — visada cituoti URL.
- **Cloudflare užkoduoti el. paštai:** `data-cfemail="hex"` reikia XOR dekoduoti (pirmas baitas = raktas), WebFetch parodo tik `[email protected]`.
- **Masinio siuntimo blokas klasifikatoriaus** (kartą, dėl "saugumo pažeidimų" temos big7 partijoje) — paprastas identiškas pakartojimas praėjo.
- **Scratchpad failai NEIŠLIEKA tarp sesijų** — visada nukopijuoti agentų rezultatus į `~/Documents/SiteVersa/` iškart, kai jie paruošti (taip pradingo `outreach5_EE.md` originalas — atkurtas rankiniu būdu iš pokalbio žurnalo).

---

## 6a. Modelių parinkimas ir tokenų taupymas (vartotojo sprendimas 2026-10-06)

Kiekvienam darbui rinktis pigiausią modelį, kuris jį atlieka beveik taip pat gerai kaip Opus. Agent tool'ui visada nurodyti `model` parametrą:
- **haiku** — mechaninis darbas: `tools/check_site.py` paleidimas sąrašui domenų ir JSON filtravimas, el. pašto ištraukimas, CSV papildymas, DNC sąrašo palyginimas, failų kopijavimas.
- **sonnet** — kandidatų paieška ir trūkumų verifikacija (WebSearch + curl/python), įrodymų rinkimas į `cand_*.md`. Tai didžiausia tokenų dalis — čia taupymas didžiausias.
- **opus** (pagrindinė sesija, ne agentas) — laiškų rašymas (tonas = konversija), kainos parinkimas, galutinė įrodymų peržiūra prieš rodant vartotojui, atsakymai klientams (Dmitry, Segris).

Kiti taupymo būdai:
- Pirmas filtras visada `python3 tools/check_site.py dom1.lt dom2.lt ...` (HTTPS/sertifikatas, platforma, jQuery, viewport, copyright, PHP klaidos, angliški tekstai, el. paštai, įskaitant Cloudflare) — vienas kompaktiškas JSON vietoj dešimčių curl komandų ir pilno HTML skaitymo. Rankiniu būdu tikrinti tik tai, kas pateks į laišką.
- Niekada nespausdinti viso HTML į kontekstą — tik `grep -o`/python ištraukas.
- Agentai rezultatus rašo į failą, o galutiniame atsakyme grąžina tik 5–10 eilučių suvestinę.
- Agentų promptuose nekartoti viso CLAUDE.md — tik kriterijai ir exclude sąrašas.
- WebSearch `mode: "standard"`, ne extended, nebent standard nieko neranda.
- Vartotojui rodyti suvestinę + 2–3 pavyzdžius, ne visus juodraščius pokalbyje (jie faile).

## 7. Atviri klausimai vartotojui (paklausti, kai aktualu, ne spėti)

1. Ką konkrečiai reiškia "optimizuoti" laiškų siuntinėjimą — didesnį apimtį (daugiau/dieną), didesnį atsakymų rodiklį (geresnis targeting/tekstas), ar mažiau rankinio darbo (labiau automatizuota drafting/sending)? (Paskutinė vartotojo žinutė šito neapibrėžia.)
2. Ar sekti Dmitry (tehnikajums.lv) dabar, ar palaukti dar? Jis tylus 6 dienas.
3. Ar bandyti LV/EE laiškus gimtąja kalba (bent subject eilutę), vietoj visada angliškai?
4. Ar tikrai reikia visada minėti €20-30/mėn abonementą pasiūlymuose (atmintis sako "taip", praktika — "niekad")?
5. JA mokytojo klausimas dėl mokėjimo per JA įmonę tebėra atviras (neturėtų blokuoti esamo Segris darbo, bet svarbu prieš KITĄ klientą).

---

## 8. Failų žemėlapis

- `outreach_tracking.csv` — autoritetingas žurnalas (73 eilutės + header; kolonos: domain,country,contact_email,batch,category,date_sent_approx,platform,flaw_summary,status,notes). **Skaityti PIRMĄ prieš atsakant į bet kokį inbound laišką.** (Šiame repo šiuo metu tik antraštė — žr. pastabą viršuje.)
- `outreach_batch1_review.md` — partijos #2 (35 laiškai) pilni juodraščiai (pavadinimas klaidinantis — tai NE partija #1).
- `outreach5_EE.md` — partijos #5 Estijos 6 paruošti juodraščiai (nesiųsti, 4+ d. senumo, patikrinti iš naujo).
- `outreach5_LT_LV_candidates.md` — partijos #5 LT/LV kandidatai be juodraščių (reikia baigti).
- `mac_bundle/send_sodasdarzas.py`, `send_batch1.py`, `send_batch_full35.py`, `send_batch3_25.py`, `send_batch_big7.py`, `send_test_to_self.py` — siuntimo scriptai; vykdyti `cd mac_bundle && python3 <script>`.
- `mac_bundle/gmail_credentials.env` — kredencialai (NIEKADA nespausdinti/nerodyti). `gmail_credentials_template.env` — tuščias šablonas.
- `mac_bundle/startuolio_santrauka.md`, `INSTRUKCIJOS.md` — **PASENĘ**, pažymėti STALE, palikti kaip istorija.
- `segris_catalog_review.md`, `Nocpix_produktai_pasirinkimas.xlsx` — Segris kliento darbas (ne outreach).
- `research/research_seo_opencart.md`, `research_opencart_qa_checklist.md`, `research_design_avoid_ai_look.md` — skaityti prieš SEO/dizaino/importo darbą BET KURIAM klientui.
- `_handoff_raw/` — šio perdavimo dokumento žaliavinė medžiaga (pilna 5-agentų analizė + kritiko patikra); paliktas archyvui, nebūtina skaityti — visa svarbu jau čia.
- Atmintis (skaitoma automatiškai): `~/.claude/projects/-Users-kerniuszigmantas-Documents-SiteVersa/memory/{MEMORY.md, project_siteversa.md, outreach_tracking.md, user_ja_startup.md, segris_mockup_artifact.md}`. (Debesies sesijose ši atmintis nepasiekiama — dirbti pagal šį CLAUDE.md ir repo turinį.)
