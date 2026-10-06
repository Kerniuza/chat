# Partija 7 (LT) — būsena

Paskutinis atnaujinimas: 2026-10-06 (vėlai)

## Atlikta
- [x] Kandidatai: `research/batch7/cand_batch7.md` (6 nauji) + 3 neišsiųsti iš partijos 6 (enbaterija.lt, ofnis.lt, elmega.lt).
- [x] 9 laiškai `outreach7_LT.md` (patvirtintas stilius: nauda klientui + „darau viską“). DNC patikrinta pagal 94 eil. CSV — 0 sutapimų.
- [x] Bandomasis siuntimas (dry run) su 94 eil. CSV: would_send=9 skipped=0.
- [ ] Išsiųsta — NE. Siųsti iš Mac (debesyje SMTP 465 užblokuotas).

## Kitas žingsnis (Mac, ~/Documents/SiteVersa)
1. Parsisiųsti iš šakos `claude/ecstatic-bell-arjgh6`: `outreach7_LT.md`, `mac_bundle/send_batch_lt.py`.
2. `python3 mac_bundle/send_batch_lt.py outreach7_LT.md` (dry run, naudoja vietinį pilną CSV ir mac_bundle/gmail_credentials.env).
3. Jei gerai: tas pats su `--send`. Scriptas pats papildys vietinį CSV.
CSV ir slaptažodžių į GitHub nekelti.
