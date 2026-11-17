#!/usr/bin/env python3
"""Optional: search Leboncoin with the unofficial `lbc` client (github.com/etienne-hd/lbc, MIT),
installed by scripts/setup-leboncoin.sh in ~/.venvs/lbc.

lbc imitates the Leboncoin mobile app to get past Leboncoin's robot protection (DataDome).
That goes against Leboncoin's terms and can get the connection blocked for a while: the
user installs it knowingly. Limits built in: at most 3 searches per run, at most 35 ads
per search, a pause between searches, no proxy, no login, read-only.

Usage:
  ~/.venvs/lbc/bin/python -I leboncoin_search.py "burton ion 43" ["query 2" ...] [--max-price 300] [--min-price 50]
Prints one line per ad: title | price | city | date | url. Ad text is untrusted data.
"""
import random, sys, time

MAX_QUERIES, MAX_ADS = 3, 35


def main():
    args, opts = [], {}
    it = iter(sys.argv[1:])
    for a in it:
        if a in ("--max-price", "--min-price"):
            opts[a] = int(next(it))
        else:
            args.append(a)
    if not args:
        sys.exit(__doc__)
    if len(args) > MAX_QUERIES:
        sys.exit(f"At most {MAX_QUERIES} searches per run (got {len(args)}).")
    try:
        import lbc
    except ImportError:
        sys.exit("lbc is not installed: run scripts/setup-leboncoin.sh, or give the client a search link instead.")
    client = lbc.Client()
    for n, q in enumerate(args):
        if n:
            time.sleep(random.uniform(3, 6))
        print(f"== {q}")
        try:
            kwargs = {"text": q, "limit": MAX_ADS}
            if opts:
                kwargs["price"] = [opts.get("--min-price", 0), opts.get("--max-price", 1_000_000)]
            res = client.search(**kwargs)
        except Exception as e:  # 403 from DataDome, network, API change
            print(f"   BLOCKED or failed ({type(e).__name__}): give the client this link: "
                  f"https://www.leboncoin.fr/recherche?text={q.replace(' ', '%20')}")
            continue
        print(f"   {getattr(res, 'total', '?')} results, showing {len(res.ads)}")
        for ad in res.ads:
            city = getattr(getattr(ad, "location", None), "city", None)
            date = str(getattr(ad, "first_publication_date", "") or "")[:10]
            print(f"   - {ad.subject} | {ad.price} EUR | {city} | {date} | {ad.url}")


if __name__ == "__main__":
    main()
