# Partija 7 — perdavimas lokaliai Mac sesijai (siuntimas)

Šis failas paruoštas debesies sesijoje. Debesyje Gmail SMTP užblokuotas, todėl siunčiame iš Mac.

## Instrukcija Claude (lokali sesija ~/Documents/SiteVersa)

1. Iš žemiau esančio kodo bloko sukurk failą `~/Documents/SiteVersa/mac_bundle/send_batch7.py` (turinį kopijuok tiksliai, nieko nekeisk).
2. Paleisk bandomąjį režimą: `cd ~/Documents/SiteVersa/mac_bundle && python3 send_batch7.py`. Jis patikrina 9 laiškus pagal `../outreach_tracking.csv` ir parodo `DRY:` eilutes. Parodyk rezultatą vartotojui.
3. TIK vartotojui parašius „siųsk“: `python3 send_batch7.py --send`. Siunčia po vieną su 9 s pertrauka, From = „Kernius Zigmantas“, kredencialai iš `gmail_credentials.env` (niekada jų nespausdink). Parodyk `SENT/FAILED` ir `BATCH_DONE`.
4. Scriptas pats prideda išsiųstus į `outreach_tracking.csv` (batch 7, status no_reply). CSV ir kredencialų į GitHub nekelti.
5. Gavus atsakymų — nieko nesiųsti pačiam, parodyti vartotojui su atsakymo juodraščiu.

Laiškai (9): enbaterija.lt, apolina.lt, rykliukas.lt, topirankiai.lt, duper.lt, ofnis.lt, elmega.lt, eimezaisti.lt, ortopedineskuprines.lt.
Pastaba: prieš siunčiant ortopedineskuprines.lt verta naršyklėje atidaryti https://ortopedineskuprines.lt ir įsitikinti, kad rodo saugumo įspėjimą; jei ne — išimk tą laišką iš EMAILS sąrašo.

## send_batch7.py

```python
#!/usr/bin/env python3
# Partija 7 (LT) — 9 laiškai. Paleisti iš ~/Documents/SiteVersa/mac_bundle/
#   python3 send_batch7.py          -> bandomasis (nieko nesiunčia)
#   python3 send_batch7.py --send   -> tikras siuntimas
import csv, os, sys, time, smtplib
from datetime import date, datetime
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid

EMAILS = [
 {
  "domain": "enbaterija.lt",
  "email": "info@eurobaterija.lt",
  "subject": "enbaterija.lt telefone rodoma kompiuterio versija",
  "body": "Laba diena,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad enbaterija.lt telefone rodoma kaip sumažinta kompiuterio versija: tekstas smulkus, mygtukus tenka didinti pirštais. Dauguma žmonių šiandien parduotuves naršo telefonu, ir jei nepatogu, jie užsako kitur. Be to, Google telefono paieškoje aukščiau rodo svetaines, kurios telefone veikia gerai.\n\nGera žinia, kad mobili versija jūsų temoje jau yra, tik neįsijungia. Siūlau ją įjungti, sutvarkyti ir patikrinti keliuose telefonuose. Taip daugiau lankytojų iš telefono taps pirkėjais. Darbas užtruktų 1–2 dienas, kaina 100–250 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "big",
  "platform": "OpenCart 1.5 (jQuery 1.7.1)",
  "price": "100–250 € + PVM",
  "flaw": "telefone rodoma kompiuterio versija (nėra viewport)"
 },
 {
  "domain": "apolina.lt",
  "email": "info@apolina.lt",
  "subject": "apolina.lt veikia ant 2016 m. WooCommerce versijos",
  "body": "Sveiki,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad apolina.lt veikia ant WordPress 4.9 ir WooCommerce 2.6, tai 2016–2017 metų versijos. Jos nebegauna saugumo pataisymų, todėl tokios svetainės dažniausiai ir būna nulaužiamos, o hostingui atnaujinus PHP užsakymai gali tiesiog nustoti veikti. Be to, kai kurios kategorijos, pvz. „Aplietos PVC“ pirštinės, rodo „Nerasta jokių produktų“, ir pirkėjas pagalvoja, kad prekės nėra.\n\nSiūlau atnaujinti sistemą atskiroje bandomojoje kopijoje, patikrinti krepšelį ir užsakymus, sutvarkyti kategorijas ir Google rodomą pavadinimą. Parduotuvė būtų saugi ir patikima dar daugelį metų. Darbas užtruktų 3–5 dienas, preliminariai nuo 300 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "big",
  "platform": "WooCommerce 2.6.4 / WordPress 4.9.26 (generator)",
  "price": "preliminariai nuo 300 € + PVM",
  "flaw": "WooCommerce 2.6 / WP 4.9, tuščios kategorijos, raktažodžių title"
 },
 {
  "domain": "rykliukas.lt",
  "email": "info@rykliukas.lt",
  "subject": "rykliukas.lt kategorijos Google rodomos su „Archives“",
  "body": "Laba diena,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad rykliukas.lt kategorijos Google paieškoje rodomos su angliška priesaga, pvz. „Svoriai ir jų sistemos Archives – RYKLIUKAS“. Tas pavadinimas yra pirmas dalykas, kurį žmogus mato paieškoje, ir nuo jo priklauso, ar paspaus jūsų nuorodą, ar konkurento. Dar kelios kategorijos meniu tuščios, pvz. „Mono fins ir bi fins“.\n\nSiūlau sutvarkyti visų kategorijų pavadinimus ir aprašymus Google, paslėpti tuščias kategorijas ir atnaujinti WordPress su WooCommerce. Taip daugiau žmonių jus ras paieškoje ir paspaus. Darbas užtruktų 2–3 dienas, kaina 250–300 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "big",
  "platform": "WooCommerce 6.9.5 / WordPress 6.1.14 (generator)",
  "price": "250–300 € + PVM",
  "flaw": "kategorijų title „Archives“, tuščios kategorijos, WP 6.1 / Woo 6.9"
 },
 {
  "domain": "topirankiai.lt",
  "email": "info@topirankiai.lt",
  "subject": "topirankiai.lt meniu kategorijos rodo „nėra prekių“",
  "body": "Sveiki,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad topirankiai.lt meniu nemažai kategorijų tuščios: „Įrankių komplektai“, „Langų valytuvai“, „Automobiliniai šaldytuvai“ rodo „Šioje kategorijoje nėra prekių“. Pirkėjas, kelis kartus užėjęs į tuščią puslapį, nusprendžia, kad parduotuvė neprižiūrima, ir eina pirkti kitur. Be to, parduotuvė veikia ant senos OpenCart 1.5, kuri nebegauna saugumo pataisymų.\n\nSiūlau sutvarkyti meniu ir kategorijas, kad pirkėjas visada rastų prekes, ir apsaugoti seną sistemą jos nekeičiant. Darbas užtruktų 2–4 dienas, preliminariai nuo 250 € + PVM, tikslią kainą pasakysiu peržiūrėjęs.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "big",
  "platform": "OpenCart 1.5 (jQuery 1.7.1, tema sellya)",
  "price": "preliminariai nuo 250 € + PVM",
  "flaw": "tuščios meniu kategorijos, OpenCart 1.5"
 },
 {
  "domain": "duper.lt",
  "email": "info@duper.lt",
  "subject": "duper.lt pavadinimai Google ir sena WooCommerce versija",
  "body": "Laba diena,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad duper.lt pagrindinis puslapis Google rodomas tik kaip „Parduotuvė – DUPER.LT“, o LED kategorijos pavadinimas kartojasi du kartus. Iš tokio pavadinimo žmogus paieškoje nesupranta, ką parduodate, todėl paspaudžia ant kito. Be to, svetainė veikia ant WordPress 5.7 ir WooCommerce 4.7, kurios nebegauna saugumo pataisymų.\n\nSiūlau sutvarkyti pavadinimus ir aprašymus Google, kad iš karto būtų aišku, jog parduodate hidroponiką ir LED apšvietimą augalams, ir saugiai atnaujinti sistemą. Darbas užtruktų 2–3 dienas, kaina 200–280 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "big",
  "platform": "WooCommerce 4.7.4 / WordPress 5.7.14 (generator)",
  "price": "200–280 € + PVM",
  "flaw": "WP 5.7 / Woo 4.7, dubliuoti ir bendri title"
 },
 {
  "domain": "ofnis.lt",
  "email": "info@ofnis.lt",
  "subject": "ofnis.lt: vietoj paieškos rodomas „[aws_search_form]“",
  "body": "Sveiki,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad ofnis.lt pagrindiniame puslapyje vietoj paieškos rodomas tekstas „[aws_search_form]“, slaiderio „Buzil valymo priemonės“ mygtukas atidaro „Puslapis nerastas“, meniu du kartus kartojasi „Paslaugos“, o kainos rodomos „€ 5,548.00“. Kai technika kainuoja tūkstančius, pirkėjas tokias smulkmenas pastebi ir pradeda abejoti.\n\nSiūlau visa tai sutvarkyti, kad svetainė atrodytų taip pat profesionaliai kaip jūsų siūloma technika, o paieška padėtų pirkėjams greitai rasti prekę. Darbas užtruktų 1–2 dienas, kaina 100–200 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "quick",
  "platform": "WooCommerce / WordPress 5.5.22 (generator)",
  "price": "100–200 € + PVM",
  "flaw": "neveikianti paieška, 404 slaideryje, dubliuotas meniu, kainų formatas"
 },
 {
  "domain": "elmega.lt",
  "email": "info@elmega.lt",
  "subject": "elmega.lt: šone liko temos nustatymų krumpliaratis",
  "body": "Laba diena,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad elmega.lt kompiuteryje šone liko temos krumpliaratis „Panel Tool“, per kurį bet kuris lankytojas gali perjungti parduotuvės spalvas į „christmas“ ar „purple“. Be to, kelios meniu kategorijos tuščios, pvz. „Termosusitraukiančios pirštinės“. Įmonėms, kurios perka iš jūsų, svetainė yra pirmas įspūdis apie tiekėją.\n\nSiūlau tai išjungti ir sutvarkyti meniu, kad svetainė atrodytų tvarkingai ir kiekviena kategorija vestų į prekes. Darbas užtruktų pusdienį, kaina 60–120 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "quick",
  "platform": "OpenCart 2.x (jQuery 2.1.1, tema lexus_megashop)",
  "price": "60–120 € + PVM",
  "flaw": "paliktas temos Panel Tool, tuščios kategorijos"
 },
 {
  "domain": "eimezaisti.lt",
  "email": "spragtukas@eimezaisti.lt",
  "subject": "eimezaisti.lt: užvedus pelę dingsta prekių nuotraukos",
  "body": "Sveiki,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad eimezaisti.lt prekių sąraše užvedus pelę ant prekės vietoj antros nuotraukos rodomas tuščias langelis, nes nuotraukos adresas sugadintas. Vienoje kategorijoje taip yra 8 prekėse iš 12, kitoje 11 iš 12. Modelių pirkėjai renkasi pagal nuotraukas, tad tai tiesiogiai mažina norą pirkti. Dar kategorija „Profesionalams“ tuščia.\n\nSiūlau pataisyti nuotraukų rodymą visoje parduotuvėje ir sutvarkyti tuščią kategoriją. Darbas užtruktų dieną, kaina 80–130 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "quick",
  "platform": "OpenCart 2.x (jQuery 2.1.1, tema simplica)",
  "price": "80–130 € + PVM",
  "flaw": "užvedus pelę dingsta prekių nuotraukos, tuščia kategorija"
 },
 {
  "domain": "ortopedineskuprines.lt",
  "email": "info@ortopedineskuprines.lt",
  "subject": "ortopedineskuprines.lt: naršyklė rodo, kad svetainė nesaugi",
  "body": "Laba diena,\n\nEsu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje.\n\nPastebėjau, kad ortopedineskuprines.lt neturi tinkamo SSL sertifikato, todėl naršyklė rodo, kad svetainė nesaugi, o prisijungimo ir užsakymo duomenys keliauja nešifruoti. Tėvai, perkantys kuprinę vaikui, ypač atkreipia dėmesį į tokius įspėjimus ir dažnai tiesiog uždaro langą. Google tokias svetaines irgi rodo žemiau.\n\nSiūlau įdiegti tinkamą sertifikatą ir nukreipti visą svetainę į saugų https. Prie adreso atsiras spynelė, ir pirkėjai jaus, kad pirkti saugu. Darbas užtruktų dieną, kaina 80–120 € + PVM.\n\nEsu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Su svetainėmis darau viską: nuo klaidų taisymo ir SEO iki prekių kėlimo ir viso dizaino atnaujinimo.\n\nSąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis.\n\nJei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas\n",
  "category": "quick",
  "platform": "OpenCart 2.x (jQuery 2.1.1)",
  "price": "80–120 € + PVM",
  "flaw": "sertifikatas ne domenui, http be peradresavimo, prisijungimas per http"
 }
]

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "..", "outreach_tracking.csv")
CRED = os.path.join(HERE, "gmail_credentials.env")
BATCH = "7"

def nd(d):
    d = d.strip().lower().replace("https://", "").replace("http://", "").split("/")[0]
    return d[4:] if d.startswith("www.") else d

rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
if len(rows) < 90:
    sys.exit(f"STOP: CSV turi tik {len(rows)} eiluciu - ne tas failas?")
dnc_d = {nd(r["domain"]) for r in rows} | {"siuvimomanija.lt","husqvarna-viking.lt","babylock.lt","elna.lt","siuvimomasina.lt","juki.lv","segris.lt","e.segris.lt"}
dnc_e = {r["contact_email"].strip().lower() for r in rows}
todo = []
for e in EMAILS:
    if e["domain"] in dnc_d or e["email"].lower() in dnc_e:
        print("SKIP (jau kontaktuota):", e["domain"])
    else:
        todo.append(e)

if "--send" not in sys.argv:
    for e in todo:
        print("DRY:", e["domain"], "->", e["email"], "|", e["subject"])
    print(f"DRY_DONE: would_send={len(todo)}")
    sys.exit()

cred = {}
for line in open(CRED, encoding="utf-8"):
    k, _, v = line.strip().partition("=")
    cred[k] = v.strip().strip('"')
addr, pw = cred.get("GMAIL_ADDRESS"), cred.get("GMAIL_APP_PASSWORD")
if not addr or not pw:
    sys.exit("STOP: nera GMAIL_ADDRESS / GMAIL_APP_PASSWORD faile gmail_credentials.env")

sent, failed = [], 0
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(addr, pw)
    for i, e in enumerate(todo):
        msg = MIMEText(e["body"], "plain", "utf-8")
        msg["From"] = formataddr(("Kernius Zigmantas", addr))
        msg["To"] = e["email"]
        msg["Subject"] = e["subject"]
        msg["Message-ID"] = make_msgid()
        try:
            s.sendmail(addr, [e["email"]], msg.as_string())
            print("SENT:", e["domain"], "->", e["email"])
            e["sent_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            sent.append(e)
        except Exception as ex:
            print("FAILED:", e["domain"], "->", e["email"], f"({type(ex).__name__}: {ex})")
            failed += 1
        if i < len(todo) - 1:
            time.sleep(9)

with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for e in sent:
        w.writerow([e["domain"], "LT", e["email"], BATCH, e["category"], date.today().isoformat(),
                    e["platform"], e["flaw"], "no_reply",
                    f"sent_at={e['sent_at']}; subject={e['subject']}; price={e['price']}"])
print(f"BATCH_DONE: sent={len(sent)} failed={failed}")
```
