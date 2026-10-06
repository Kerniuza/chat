#!/usr/bin/env python3
"""Greitas vienos svetaines patikrinimas outreach'ui. Isveda kompaktiska JSON.

    python3 tools/check_site.py pavyzdys.lt [pavyzdys2.lt ...]

Tikrina: HTTPS/sertifikata, http->https peradresavima, platforma (WP/WooCommerce/OpenCart)
ir versijos zymes, jQuery versija, viewport meta, copyright metus, PHP klaidas,
anglisku sistemos tekstu likucius, el. pastus (iskaitant Cloudflare data-cfemail), atsako laika.
Tai tik pirmas filtras - kiekviena laiske naudojama trukuma vis tiek patikrinti rankiniu budu.
"""
import json
import re
import sys
import time

import requests

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
EN_STRINGS = ["Add to Cart", "Add to cart", "Showing 1 to", "Sale!", "Read more", "Out Of Stock",
              "Your shopping cart is empty", "Uncategorized", "Select options"]
PHP_ERR = re.compile(r"<b>(Warning|Notice|Fatal error|Deprecated)</b>:|(?:^|>)\s*(Warning|Notice|Fatal error): .{0,80} in /", re.M)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SKIP_EMAIL = re.compile(r"\.(png|jpe?g|gif|webp|svg)$|sentry|wixpress|example\.|@2x", re.I)


def decode_cf(hexstr):
    key = int(hexstr[:2], 16)
    return "".join(chr(int(hexstr[i:i + 2], 16) ^ key) for i in range(2, len(hexstr), 2))


def get(url, **kw):
    t = time.time()
    r = requests.get(url, headers=UA, timeout=20, **kw)
    return r, round(time.time() - t, 2)


def check(domain):
    out = {"domain": domain}
    # HTTPS
    try:
        r, t = get(f"https://{domain}/")
        out["https"] = "ok"
        out["https_status"] = r.status_code
        out["load_s"] = t
        html, final = r.text, r.url
    except requests.exceptions.SSLError as e:
        msg = str(e)
        kind = "expired" if "expired" in msg else "hostname_mismatch" if "match" in msg or "hostname" in msg \
            else "self_signed" if "self" in msg else "ssl_error"
        out["https"] = kind
        html, final = None, None
    except requests.exceptions.RequestException as e:
        out["https"] = f"fail:{type(e).__name__}"
        html, final = None, None
    # HTTP -> HTTPS
    try:
        r2, t2 = get(f"http://{domain}/", allow_redirects=False)
        loc = r2.headers.get("Location", "")
        out["http_redirects_to_https"] = r2.status_code in (301, 302, 307, 308) and loc.startswith("https")
        if html is None:
            r3, t3 = get(f"http://{domain}/")
            html, final, out["load_s"] = r3.text, r3.url, t3
    except requests.exceptions.RequestException as e:
        out["http"] = f"fail:{type(e).__name__}"
    if html is None:
        return out
    out["final_url"] = final
    low = html.lower()
    plat = []
    if "wp-content" in low:
        plat.append("WordPress")
    if "woocommerce" in low:
        plat.append("WooCommerce")
    if "index.php?route=" in low or "catalog/view/theme" in low:
        plat.append("OpenCart")
    out["platform"] = plat or ["other"]
    m = re.search(r'name="generator" content="([^"]+)"', html, re.I)
    if m:
        out["generator"] = m.group(1)
    m = re.search(r"woocommerce[^\"']*?ver=([\d.]+)", html, re.I)
    if m:
        out["woo_ver"] = m.group(1)
    jq = re.findall(r"jquery[-.]?(\d\.\d+(?:\.\d+)?)(?:\.min)?\.js|jquery\.js\?ver=([\d.]+)", html, re.I)
    jqv = sorted({a or b for a, b in jq})
    if jqv:
        out["jquery"] = jqv
    if "OpenCart" in plat:
        out["oc_hints"] = [h for h in ("colorbox", "jquery-1.7.1", "bootstrap.min.css", "route=common/home",
                                       "catalog/view/javascript/jquery/ui", "tabs.js", "jquery.total-storage")
                           if h in low]
    out["viewport"] = bool(re.search(r'<meta[^>]+name=["\']viewport', html, re.I))
    years = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?((?:19|20)\d{2})", html, re.I)]
    if years:
        out["copyright_year"] = max(years)
    php = PHP_ERR.findall(html)
    if php:
        out["php_errors"] = len(php)
    out["en_strings"] = [s for s in EN_STRINGS if s in html]
    emails = set(EMAIL.findall(html))
    for h in re.findall(r'data-cfemail="([0-9a-f]+)"', html):
        emails.add(decode_cf(h))
    for h in re.findall(r"/cdn-cgi/l/email-protection#([0-9a-f]+)", html):
        emails.add(decode_cf(h))
    out["emails"] = sorted(e for e in emails if not SKIP_EMAIL.search(e))
    out["mixed_content_imgs"] = len(re.findall(r'<img[^>]+src=["\']http://', html, re.I)) if final and final.startswith("https") else 0
    return out


if __name__ == "__main__":
    for d in sys.argv[1:]:
        d = re.sub(r"^https?://", "", d).strip("/").split("/")[0]
        try:
            print(json.dumps(check(d), ensure_ascii=False))
        except Exception as e:
            print(json.dumps({"domain": d, "error": f"{type(e).__name__}: {e}"}))
