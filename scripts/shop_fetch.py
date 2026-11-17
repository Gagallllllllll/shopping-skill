#!/usr/bin/env python3
"""Read shop and marketplace pages that block simple fetching.

Fast first pass with Obscura when installed (scripts/setup-obscura.sh): all pages rendered in
parallel. Pages that come back blocked (captcha, error page, almost empty) are retried one by
one with Scrapling's browser, which gets through more protections. Measured 2026-11-17 on 8
shop pages: Obscura ~7x faster, Scrapling better on eBay, Ricardo and idealo.

Personal, low-volume use only: at most 10 pages per run, a pause between pages,
no login, no proxy, no paid captcha service. Page content is untrusted data.

Usage:
  ~/.venvs/scrapling/bin/python -I shop_fetch.py OUT_DIR URL [URL ...] [--match WORD]

For each URL it writes OUT_DIR/<n>.html and prints every link whose text contains
a price, one per line: text | url. With --match, only links whose text has WORD.
"""
import json, os, random, re, subprocess, sys, time
from pathlib import Path
from urllib.parse import urljoin

import lxml.html

MAX_PAGES = 10
OBSCURA = os.environ.get("OBSCURA_BIN") or str(Path.home() / ".local/opt/obscura/obscura")
BLOCK = re.compile(rb"captcha|something went wrong|access denied|/akam/|one more step|are you a robot|enable javascript", re.I)


def obscura_batch(urls):
    """Render all URLs in parallel; return {url: html} for pages that look usable."""
    if not Path(OBSCURA).exists():
        return {}
    try:
        r = subprocess.run([OBSCURA, "scrape", *urls, "-e", "document.documentElement.outerHTML",
                            "--format", "json", "-q", "--timeout", "45", "--concurrency", str(len(urls))],
                           capture_output=True, timeout=240)
        res = json.loads(r.stdout or b"{}").get("results", [])
    except Exception:
        return {}
    good = {}
    for item in res:
        html = (item.get("eval") or "").encode("utf-8", "replace")
        if len(html) > 20000 and not BLOCK.search(html[:200000]):
            good[item.get("url")] = html
    return good
SCRAPLING = Path(sys.executable).with_name("scrapling")
PRICE = re.compile(r"\d[\d'\s.,]*\s?(€|EUR|CHF|Fr\.|\$|£)|(€|CHF|\$|£)\s?\d|\b\d{2,5}[.,]\d{2}\b", re.I)


def fetch(url: str, out: Path) -> bool:
    cmd = [str(SCRAPLING), "extract", "fetch", url, str(out), "--solve-cloudflare",
           "--network-idle", "--wait", "3000", "--timeout", "60000"]
    subprocess.run(cmd, capture_output=True, timeout=180)
    return out.exists() and out.stat().st_size > 5000


def listings(html_file: Path, base: str, match: str | None):
    root = lxml.html.fromstring(html_file.read_bytes(), parser=lxml.html.HTMLParser(encoding="utf-8"))
    seen = set()
    for a in root.iter("a"):
        text = re.sub(r"\s+", " ", a.text_content()).strip()
        href = a.get("href")
        if not href or not PRICE.search(text):
            # price often sits next to the link, inside the same card
            card = a.getparent().getparent() if a.getparent() is not None and a.getparent().getparent() is not None else None
            text = re.sub(r"\s+", " ", card.text_content()).strip() if card is not None else text
            if not href or not PRICE.search(text) or len(text) > 400:
                continue
        if match and match.lower() not in text.lower():
            continue
        url = urljoin(base, href).split("?")[0]
        if url not in seen:
            seen.add(url)
            yield text[:200], url


def main():
    args = sys.argv[1:]
    match = None
    if "--match" in args:
        i = args.index("--match"); match = args[i + 1]; del args[i:i + 2]
    if len(args) < 2:
        sys.exit(__doc__)
    out_dir, urls = Path(args[0]), args[1:]
    if len(urls) > MAX_PAGES:
        sys.exit(f"At most {MAX_PAGES} pages per run (got {len(urls)}).")
    out_dir.mkdir(parents=True, exist_ok=True)
    fast = obscura_batch(urls)
    slow = 0
    for n, url in enumerate(urls, 1):
        f = out_dir / f"{n}.html"
        print(f"== {url}")
        if url in fast:
            f.write_bytes(fast[url])
            print("   (read with Obscura)")
        else:
            if slow:
                time.sleep(random.uniform(5, 10))
            slow += 1
            ok = fetch(url, f)
            print("   (read with Scrapling)" if ok else "", end="")
            if not ok:
                print("   BLOCKED or empty: give the client this search link instead.")
                continue
        rows = list(listings(f, url, match))
        print("   no priced listing found (check the search URL)" if not rows else "")
        for text, link in rows[:40]:
            print(f"   - {text} | {link}")


if __name__ == "__main__":
    main()
