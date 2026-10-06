# Partija 6 (LT) — būsena

Atnaujinama po kiekvieno žingsnio. Vartotojui parašius „tęsk“ — skaityti šį failą ir tęsti nuo „Kitas žingsnis“.

Paskutinis atnaujinimas: 2026-10-06 08:50 UTC

## Atlikta
- [x] CSV patikrintas — repo tik antraštė (pilnas žurnalas dar neimportuotas iš Mac; siuntimas blokuotas, kol neimportuota).
- [x] Siuntimo scriptas `mac_bundle/send_batch_lt.py` (dry run pagal nutylėjimą).
- [x] Tikrinimo scriptas `tools/check_site.py`.
- [x] Pavyzdinis laiškas parodytas, vartotojo pataisymai įrašyti CLAUDE.md (visos 6 tėčio svetainės, KTU JKM kursai, 2 m. darbo tėčio įmonėje, be JA).
- [x] Agentas C (kosmetika, vaikai, maistas, gėlės, kanceliarija) — `cand_C.md`, 9 kandidatai.
- [x] Agentas A (statyba, auto/moto, sodas, dviračiai) — `cand_A.md`, 9 kandidatai.
- [ ] Agentas B (gyvūnai, baldai, elektronika, santechnika) — `cand_B.md`, vykdomas (5 kandidatai 08:23).

## Kitas žingsnis
1. Jei agentas B nebaigė — perskaityti `cand_B.md` tokį, koks yra (arba paleisti naują sonnet agentą B nišoms, jei failas tuščias).
2. Peržiūrėti visus `cand_*.md`, atmesti silpnus (vienas izoliuotas 404 nėra „big“), dukart patikrinti kiekvieną laiške naudojamą trūkumą.
3. Parašyti laiškus į `outreach6_LT.md` (formatas — vartotojo užduotyje / CLAUDE.md „NAUJOS LAIŠKŲ TAISYKLĖS“).
4. Parodyti vartotojui suvestinę + 2–3 laiškus, laukti „siųsk“.
5. Prieš siunčiant: importuoti pilną `outreach_tracking.csv` iš Mac, nustatyti GMAIL_* aplinkos kintamuosius.
