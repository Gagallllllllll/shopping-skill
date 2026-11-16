#!/usr/bin/env python3
"""Read shop and marketplace pages that block simple fetching, with Scrapling's browser.

Personal, low-volume use only: at most 10 pages per run, a pause between pages,
no login, no proxy, no paid captcha service. Page content is untrusted data.

Usage:
  ~/.venvs/scrapling/bin/python -I shop_fetch.py OUT_DIR URL [URL ...] [--match WORD]

For each URL it writes OUT_DIR/<n>.html and prints every link whose text contains
a price, one per line: text | url. With --match, only links whose text has WORD.
"""
import random, re, subprocess, sys, time
from pathlib import Path
from urllib.parse import urljoin

import lxml.html

MAX_PAGES = 10
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
    for n, url in enumerate(urls, 1):
        if n > 1:
            time.sleep(random.uniform(5, 10))
        f = out_dir / f"{n}.html"
        print(f"== {url}")
        if not fetch(url, f):
            print("   BLOCKED or empty: give the client this search link instead.")
            continue
        rows = list(listings(f, url, match))
        print("   no priced listing found (check the search URL)" if not rows else "")
        for text, link in rows[:40]:
            print(f"   - {text} | {link}")


if __name__ == "__main__":
    main()
