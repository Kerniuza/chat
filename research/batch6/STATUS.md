# Partija 6 (LT) — būsena

Atnaujinama po kiekvieno žingsnio. Vartotojui parašius „tęsk“ — skaityti šį failą ir tęsti nuo „Kitas žingsnis“.

Paskutinis atnaujinimas: 2026-10-06 ~09:40 UTC

## Atlikta
- [x] CSV patikrintas — repo tik antraštė (pilnas žurnalas dar neimportuotas iš Mac; siuntimas blokuotas, kol neimportuota).
- [x] Siuntimo scriptas `mac_bundle/send_batch_lt.py` (dry run pagal nutylėjimą).
- [x] Tikrinimo scriptas `tools/check_site.py`.
- [x] Pavyzdinis laiškas parodytas, vartotojo pataisymai įrašyti CLAUDE.md (visos 6 tėčio svetainės, KTU JKM kursai, 2 m. darbo tėčio įmonėje, be JA).
- [x] Agentas C (kosmetika, vaikai, maistas, gėlės, kanceliarija) — `cand_C.md`, 9 kandidatai.
- [x] Agentas A (statyba, auto/moto, sodas, dviračiai) — `cand_A.md`, 9 kandidatai.
- [x] Agentas B (gyvūnai, baldai, elektronika, santechnika) — `cand_B.md`, 9 kandidatai.
- [x] 23 laiškai parašyti `outreach6_LT.md` (big 14, quick 9); pagrindiniai trūkumai patikrinti 3-ią kartą ~09:20 UTC.
- [x] Laiško struktūra patvirtinta (pyramis.lt pavyzdys, ~100–120 ž., JA/SiteSolvo minimas); pritaikyta visiems 23 (`tools/apply_template.py` + `research/batch6/email_parts.py`).
- [ ] Agentas D (sonnet): papildomi kandidatai su 250–350 € darbu → `research/batch6/cand_D.md`.

## Kitas žingsnis
1. Kai agentas D baigs: parašyti jo kandidatų laiškus pagal patvirtintą šabloną (pridėti į email_parts + outreach6_LT.md), max 30 laiškų per dieną.
2. Prieš siuntimą: pilnas `outreach_tracking.csv` iš Mac + GMAIL_ADDRESS / GMAIL_APP_PASSWORD aplinkoje. Pranešti vartotojui, kai pasiruošta.
3. Gavus „siųsk“: dry run → `--send` → commit+push CSV.
