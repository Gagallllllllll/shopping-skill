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
- Facebook Marketplace: `https://www.facebook.com/marketplace/<city>/search/?query=<q>` (search shows no listings without an account: the client searches, the skill checks the listing links they send)

In the report and buying sheets, give one link per item and marketplace, and tell the client which **saved-search alerts** to set (most marketplaces notify new listings for a saved search).

## Listing check (the client brings a listing)

Triggered when the client sends a listing: a link, a screenshot, or pasted text. **For a link, first run** `python3 -I <skill>/scripts/listing_preview.py "<url>"`: it reads the public preview (title, description, photo, and price and condition when the site publishes them) with no login. Tested: Facebook Marketplace listing links and Vinted work; Leboncoin returns 403. If it fails, ask for a screenshot or the text, never for the client's password.

1. **Identify** the exact model, version, year and size from the title, photos and description. Name what is missing.
2. **Fit to the profile:** compare with the target specs from the profile and the category pack (flex, size, compatibility, use). Check the size on the brand's own chart (for shoes and boots: Mondopoint in cm). A seller's "fits like a size smaller or bigger" is their feeling, not a measurement: ask for a measurement.
3. **Age and wear:** what the use so far means for this category (for example boot liners pack out, batteries wear, foam sags). Say how it changes the fit or value.
4. **Fair price:** compare with 3 or more comparable listings and the new price (deals method). Give a target offer.
5. **Risks:** scam signs from the category pack and the core rules (payment outside the platform, links sent in chat, pressure, price far below market).
6. **Verdict:** good fit / only if ... / skip, with the reason, and a better option if one is known.
7. **Questions and message:** the questions that settle what is missing, and a ready-to-send message in the seller's language (or the client's), questions first, offer second. For a local pickup: what to check on the spot (try on, test, measure), and pay at handover.

Add good finds to the buying sheets as second-hand offers (status "verified" only for what the listing shows).
