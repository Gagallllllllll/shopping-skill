# Second-hand marketplaces and listing check

Local marketplaces (Leboncoin, Facebook Marketplace and similar) often have the best second-hand finds, and the chance to try before paying. Many of them block robots or need an account. The skill **never logs in or creates an account**, so it works with them in two ways: search links and alerts for the client, and a **listing check** of what the client finds.

## Marketplaces by region

Ask the client which ones they use and how far they can travel for a pickup (or whether shipping is fine).

| Region | Marketplaces | Notes |
|---|---|---|
| France | Leboncoin, Vinted, Facebook Marketplace, eBay.fr, Back Market (refurbished electronics), Selency (design furniture) | Leboncoin blocks robots; Vinted pages are readable |
| Switzerland | Ricardo, tutti.ch, anibis.ch, Facebook Marketplace | Vinted France does not serve Switzerland [NC] |
| Germany, Austria | Kleinanzeigen, Willhaben (AT), eBay.de, Vinted.de | |
| Italy | Subito, Vinted.it, eBay.it | |
| Spain | Wallapop, Vinted.es | |
| Netherlands, Belgium | Marktplaats, 2dehands / 2ememain, Vinted | |
| Elsewhere | Facebook Marketplace, eBay, local classifieds | ask the client |

**Search link patterns** (fill `<q>` with model + size; seen working during research, re-check if one fails):
- Leboncoin: `https://www.leboncoin.fr/recherche?text=<q>`
- Vinted: `https://www.vinted.fr/catalog?search_text=<q>` (also .de, .it, .es, .nl)
- Ricardo: `https://www.ricardo.ch/fr/s/<q>/`
- tutti: `https://www.tutti.ch/fr/q/<q>`
- anibis: `https://www.anibis.ch/fr/q/<q>`
- Kleinanzeigen: `https://www.kleinanzeigen.de/s-<q>/k0`
- eBay: `https://www.ebay.fr/sch/i.html?_nkw=<q>` (used only: add `&LH_ItemCondition=3000`)
- Facebook Marketplace: `https://www.facebook.com/marketplace/<city>/search/?query=<q>`

**Facebook Marketplace search (optional):** its search pages load listings with JavaScript, so a plain request gets none, but a headless browser gets the public listings shown to logged-out visitors. Run `~/.venvs/scrapling/bin/python -I <skill>/scripts/marketplace_search.py <city> "<query>" ["<query 2>"] [--match WORD]` (Obscura if installed, otherwise Scrapling; at most 3 searches per run, pauses, no login). It prints price, title, place and link per listing. Tested 2026-11-17: `lyon` returned French listings from the whole region. **Check the places:** an unknown city slug (for example `geneva`, `geneve`, `lausanne`, `montreux`, `annecy` as of 2026-11-18) silently falls back to a US city, while `zurich`, `bern` and `fribourg` work; a nearby working city usually covers the area; then use a slug that works or the numeric city id from the client's own Marketplace address bar. Automated reading may go against Facebook's terms: sparing use. Generic queries ("boots snowboard 43") return far more than model names, which often return nothing logged out. The script warns when the city slug fell back to the US. Check promising listings with `listing_preview.py`.

**Daily watch (when the client asks to be told about new listings):** a small script that runs these searches plus `listing_preview.py` on watched items, keeps a seen-list, and alerts only on new ones, scheduled outside the session (Windows Task Scheduler via `wsl.exe` on WSL, cron elsewhere), because in-session schedules die with the session. Keep it out of the skill repo (it holds client queries). Vinted search can't be automated here: tell the client to save the search in the Vinted app for native alerts.

**Leboncoin search (optional):** if `~/.venvs/lbc` exists (installed by `scripts/setup-leboncoin.sh`), the deals agent may run `~/.venvs/lbc/bin/python -I <skill>/scripts/leboncoin_search.py "<model size>" ["<query 2>"] [--max-price N]`: at most 3 searches per run and 35 ads each, pauses between searches, no proxy, no login. It prints title, price, city, date and link per ad. Tested 2026-11-17: works. It imitates the Leboncoin app to get past its robot protection, which is against Leboncoin's terms: use it sparingly, and on any block fall back to search links.

In the report and buying sheets, give one link per item and marketplace, and tell the client which **saved-search alerts** to set (most marketplaces notify new listings for a saved search).

## Listing check (the client brings a listing)

Triggered when the client sends a listing: a link, a screenshot, or pasted text. **For a link, first run** `python3 -I <skill>/scripts/listing_preview.py "<url>"`: it reads the public preview (title, description, photo, and price and condition when the site publishes them) with no login. Tested: Facebook Marketplace listing links and Vinted work; Leboncoin returns 403. If it fails, ask for a screenshot or the text, never for the client's password.

1. **Identify** the exact model, version, year and size from the title, photos and description. Name what is missing.
2. **Fit to the profile:** compare with the target specs from the profile and the category pack (flex, size, compatibility, use). Check the size on the brand's own chart (for shoes and boots: Mondopoint in cm). A seller's "fits like a size smaller or bigger" is their feeling, not a measurement: ask for a measurement.
3. **Completeness:** what is included (for bindings: discs and screws; for electronics: charger, box). Anything missing lowers the target price by its replacement cost.
4. **Age and wear:** what the use so far means for this category (for example boot liners pack out, batteries wear, foam sags). Say how it changes the fit or value.
5. **Fair price:** compare with 3 or more comparable listings and the new price (deals method). Give a target offer.
6. **Risks:** scam signs from the category pack and the core rules (payment outside the platform, links sent in chat, pressure, price far below market).
7. **Verdict:** good fit / only if ... / skip, with the reason, and a better option if one is known.
8. **Questions and message:** the questions that settle what is missing, and a ready-to-send message in the seller's language (or the client's), questions first, offer second. For a local pickup: what to check on the spot (try on, test, measure), and pay at handover.

Add good finds to the buying sheets as second-hand offers (status "verified" only for what the listing shows).

## Set check (the client brings the whole set)

Triggered when a returning client lists the items they found or bought for a set, often with prices already agreed. Short answer, no new research unless a price looks off:

1. **Per item:** price against the ceiling set earlier and against the new or sale price, fit to the profile, and what is still unconfirmed (size, year, included parts). A small overshoot on an item already bought is noted once, not re-argued.
2. **Across the set:** compatibility between items (boot size vs binding size vs board width, mount pattern, flex balance), and the total in each currency as given; convert only with a rate checked today, otherwise give a range marked as an estimate.
3. **What blocks payment:** the one or two points to settle before paying (usually the size of the item not yet bought, and parts to confirm), with a ready-to-send message.
4. **Pickup checklist** from the category pack, and what to stop afterwards (watches, alerts).
