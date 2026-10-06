#!/usr/bin/env python3
"""Siuncia juodrascius is outreach<N>_LT.md per Gmail SMTP.

Naudojimas (is repo saknies):
    python3 mac_bundle/send_batch_lt.py outreach6_LT.md            # tik perziura (dry run)
    python3 mac_bundle/send_batch_lt.py outreach6_LT.md --send     # tikras siuntimas

Prisijungimas imamas TIK is aplinkos kintamuju GMAIL_ADDRESS ir GMAIL_APP_PASSWORD.
Pries siunciant patikrina do-not-contact sarasa is outreach_tracking.csv.
Po siuntimo prideda eilutes i outreach_tracking.csv (status=no_reply).
"""
import csv
import os
import re
import smtplib
import sys
import time
from datetime import date, datetime
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "outreach_tracking.csv")
MAX_PER_DAY = 30
PAUSE_SECONDS = 9
MIN_CSV_ROWS = 70  # pilnas zurnalas turi bent 73 eilutes; maziau = CSV dar neimportuotas

ALWAYS_EXCLUDE = {
    "siuvimomanija.lt", "husqvarna-viking.lt", "babylock.lt", "elna.lt",
    "siuvimomasina.lt", "juki.lv", "segris.lt", "e.segris.lt",
}


def norm_domain(d):
    d = d.strip().lower()
    d = re.sub(r"^https?://", "", d).split("/")[0]
    return d[4:] if d.startswith("www.") else d


def parse_drafts(path):
    text = open(path, encoding="utf-8").read()
    drafts = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        domain = block.splitlines()[0].strip()

        def field(name):
            m = re.search(rf"^- {name}:\s*(.+)$", block, flags=re.M)
            return m.group(1).strip() if m else ""

        body_m = re.search(r"^- Laiškas:\s*\n```\n(.*?)\n```", block, flags=re.M | re.S)
        if not body_m:
            continue
        drafts.append({
            "domain": norm_domain(domain),
            "platform": field("Platforma"),
            "category": field("Kategorija"),
            "email": field("El. paštas").split()[0] if field("El. paštas") else "",
            "price": field("Kaina laiške"),
            "subject": field("Tema"),
            "flaw": field("Trūkumas"),
            "body": body_m.group(1).strip() + "\n",
        })
    return drafts


def load_dnc():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    domains = {norm_domain(r.get("domain", "")) for r in rows if r.get("domain")}
    emails = {r.get("contact_email", "").strip().lower() for r in rows if r.get("contact_email")}
    return rows, domains | ALWAYS_EXCLUDE, emails


def main():
    if len(sys.argv) < 2:
        sys.exit("Nurodyk juodrasciu faila, pvz. outreach6_LT.md")
    drafts_path = sys.argv[1]
    do_send = "--send" in sys.argv
    batch = re.search(r"outreach(\d+)", drafts_path)
    batch = batch.group(1) if batch else "?"

    rows, dnc_domains, dnc_emails = load_dnc()
    if len(rows) < MIN_CSV_ROWS:
        sys.exit(f"STOP: outreach_tracking.csv turi tik {len(rows)} eiluciu. "
                 "Pirma importuok pilna zurnala, kitaip nera do-not-contact saraso.")

    drafts = parse_drafts(drafts_path)
    ok, skipped = [], []
    for d in drafts:
        email_domain = d["email"].split("@")[-1].lower()
        if not d["email"] or "@" not in d["email"]:
            skipped.append((d["domain"], "nera el. pasto"))
        elif d["domain"] in dnc_domains or norm_domain(email_domain) in dnc_domains:
            skipped.append((d["domain"], "jau kontaktuota / draudziama"))
        elif d["email"].lower() in dnc_emails:
            skipped.append((d["domain"], "el. pastas jau kontaktuotas"))
        else:
            ok.append(d)

    for dom, why in skipped:
        print(f"SKIP: {dom} ({why})")
    if len(ok) > MAX_PER_DAY:
        print(f"Daugiau nei {MAX_PER_DAY} laisku - siunciami tik pirmi {MAX_PER_DAY}.")
        ok = ok[:MAX_PER_DAY]

    if not do_send:
        for d in ok:
            print(f"DRY: {d['domain']} -> {d['email']} | {d['subject']}")
        print(f"DRY_DONE: would_send={len(ok)} skipped={len(skipped)}")
        return

    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not gmail_address or not gmail_password:
        sys.exit("STOP: nenustatyti GMAIL_ADDRESS / GMAIL_APP_PASSWORD aplinkos kintamieji.")

    sent, failed = [], 0
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_address, gmail_password)
        for i, d in enumerate(ok):
            msg = MIMEText(d["body"], "plain", "utf-8")
            msg["From"] = formataddr(("Kernius Zigmantas", gmail_address))
            msg["To"] = d["email"]
            msg["Subject"] = d["subject"]
            msg["Message-ID"] = make_msgid()
            try:
                server.sendmail(gmail_address, [d["email"]], msg.as_string())
                print(f"SENT: {d['domain']} -> {d['email']}")
                d["sent_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                sent.append(d)
            except Exception as e:
                print(f"FAILED: {d['domain']} -> {d['email']} ({type(e).__name__}: {e})")
                failed += 1
            if i < len(ok) - 1:
                time.sleep(PAUSE_SECONDS)

    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        for d in sent:
            notes = f"sent_at={d['sent_at']}; subject={d['subject']}; price={d['price']}"
            w.writerow([d["domain"], "LT", d["email"], batch, d["category"],
                        date.today().isoformat(), d["platform"], d["flaw"], "no_reply", notes])

    print(f"BATCH_DONE: sent={len(sent)} failed={failed} skipped={len(skipped)}")


if __name__ == "__main__":
    main()
