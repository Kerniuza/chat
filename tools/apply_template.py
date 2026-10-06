import re, sys
P = sys.argv[1]; DATA = sys.argv[2]
exec(open(DATA, encoding="utf-8").read())  # defines D = {domain: (price, problem, offer)}
INTRO = "Esu Kernius Zigmantas. Junior Achievement mokinių programoje kuriu savo startuolį SiteSolvo – taisau ir atnaujinu el. parduotuves ant WordPress ir OpenCart. Esu baigęs KTU Jaunųjų kompiuterininkų mokyklos programavimo kursus ir du metus dirbu tėčio įmonėje."
WORK = "Esu atnaujinęs siuvimomanija.lt, e.segris.lt padaręs naują dizainą ir SSL, prižiūriu husqvarna-viking.lt, babylock.lt, elna.lt, siuvimomasina.lt ir juki.lv. Darau ir SEO, prekių kėlimą, dizaino atnaujinimą."
PAY = "Sąskaitą su PVM išrašome per UAB Siuvimo Manija, mokėti galima dalimis."
END = "Jei neaktualu, tiesiog ignoruokite – daugiau nerašysiu.\n\nKernius Zigmantas"
s = open(P, encoding="utf-8").read()
blocks = re.split(r"(?m)^(?=## )", s); out = []; n = 0
for b in blocks:
    m = re.match(r"## (\S+)", b)
    if m and m.group(1) in D:
        price, prob, offer = D[m.group(1)]
        greet = "Laba diena," if n % 2 == 0 else "Sveiki,"
        body = "\n\n".join([greet, INTRO, prob, offer, WORK, PAY, END])
        b = re.sub(r"- Laiškas:\n```\n.*?\n```", lambda _: "- Laiškas:\n```\n" + body + "\n```", b, flags=re.S)
        b = re.sub(r"(?m)^- Kaina laiške:.*$", lambda _: "- Kaina laiške: " + price, b)
        n += 1
    out.append(b)
open(P, "w", encoding="utf-8").write("".join(out)); print("applied", n)
