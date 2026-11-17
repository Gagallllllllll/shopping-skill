# Changelog

All notable changes to this skill. Newest first. Versions up to 1.10.0 were published as the `sport` skill.

## 2.4.0 (2026-11-17)
- Facebook Marketplace search without an account: `scripts/marketplace_search.py` renders the public search pages (Obscura, else Scrapling) and lists price, title, place and link. Tested around Lyon (19 to 24 listings per search). Unknown city slugs fall back to a US city: check the places.
- Obscura adopted where it is better: `scripts/setup-obscura.sh` (pinned v0.2.7, non-stealth, SHA-256 checked); `shop_fetch.py` renders all pages in parallel with Obscura first and retries blocked pages with Scrapling.
- Leboncoin search tested on real items (Photon BOA 43, D.O.A. 156, Union Strata): 3 to 10 relevant ads per search.

## 2.3.0 (2026-11-17)
- Optional Leboncoin search with the unofficial `lbc` client (MIT, pinned 1.1.9; code read before install: only Leboncoin hosts, no telemetry): `scripts/setup-leboncoin.sh`, `scripts/leboncoin_search.py` (3 searches and 35 ads max per run, pauses, no proxy, no login). Tested: works.
- Evaluated and not adopted: Obscura 0.2.7 non-stealth headless browser. On 8 shop pages it was about 7× faster in parallel and returned far less text, but was blocked on eBay, Ricardo and idealo, where Scrapling got through.

## 2.2.0 (2026-11-17)
- `scripts/listing_preview.py`: reads the public preview of a listing link (OpenGraph tags and schema.org Product data: title, description, photo, price, condition) with an honest User-Agent, no login, no dependency. Tested on Facebook Marketplace and Vinted listings; Leboncoin answers 403. Idea credited to ChocoData's MIT Facebook Marketplace scraper.
- Listing check runs it first on any link.

## 2.1.1 (2026-11-17)
- Sport pack: the interview asks the current gear's flex and how it feels, and sets the target relative to it.

## 2.1.0 (2026-11-17)
- Marketplaces by region (Leboncoin, Facebook Marketplace, Vinted, Ricardo, tutti, anibis, Kleinanzeigen, Willhaben, Subito, Wallapop, Marktplaats...) with search link patterns and saved-search alerts (`references/core/marketplaces.md`).
- Listing check mode: the client brings a listing (link, screenshot or text) and gets identification, fit and size check, wear, fair price, risks, verdict, questions and a ready-to-send message.
- Interview asks which marketplaces the client uses and the pickup distance.

## 2.0.0 (2026-11-16)
- **Renamed `sport` to `shopping`:** a shopping advisor for any category, with category packs in `references/categories/` (sport: tested; electronics, fashion and shoes, furniture and bedding: drafts built from sourced research). Unknown categories get a draft pack written during the session.
- Core method moved to `references/core/` and made category-neutral (client profile instead of athlete profile).
- Deals: official recall check (EU Safety Gate, France RappelConso), refurbished and ex-display sources.
- Sensitive categories (medicines, medical devices, child car seats, weapons, financial products): general information only.
- README, contributing guide and template updated; repository renamed to `shopping-skill`.

## 1.10.0 (2026-11-16)
- Buying sheets: a "Your picks" option, added first once the client chooses exact listings, with per-item checklist and fallback.
- First full real session completed (snowboard park set): interview, research, deals, Deep search, second-hand alternatives, seller messages.

## 1.9.1 (2026-11-16)
- Deals: check the same shop's other country sites (prices and shipping differ).

## 1.9.0 (2026-11-16)
- Search depth chosen by the client: Quick, Standard (default) or Deep, with tool-call limits per agent and second-hand coverage per level.
- When a budget runs out, the client is offered a targeted extension for the missing part only.
- Deals agents must search second-hand for every item before stopping.

## 1.8.2 (2026-11-16)
- Rule: every item gets its own deals pass before it enters the buying sheets. Brand list prices are marked `ref: true` and never shown as a place to buy.

## 1.8.1 (2026-11-16)
- Buying sheets: offers with the client's size not confirmed (`sizeOk: false`) never count as best or in the total; the model switch is larger and labelled.

## 1.8.0 (2026-11-16)
- Buying sheets: alternative models per slot (for example straps or quick-entry bindings) with a model switch inside each set; the sheet and the total follow the choice. Template and README updated.

## 1.7.2 (2026-11-16)
- Interview (snowboard): asks the binding entry type early, because some step-in systems need their own boots and change the whole set.

## 1.7.1 (2026-11-16)
- README rewritten for everyone: what a session looks like, what you get, how to fill the buying sheets template (field reference), search budget, optional Scrapling, FAQ.
- Removed a committed Python cache folder; added `.gitignore`.

## 1.7.0 (2026-11-16)
- `templates/buying-sheets.html`: reusable interactive buying sheets (option picker, New / Second-hand per item, delivery country switch, offers sorted by delivered price, specs, checklists, print one sheet per page, choices remembered).
- Agents are stopped once their report is in.

## 1.6.0 (2026-11-16)
- Search budget: 20 tool calls per research agent, 25 per deals agent, stop early once targets are met, comparison sites first, agents run on Sonnet. A first unbudgeted deals run took about 70 tool calls for 2 items.

## 1.5.0 (2026-11-16)
- Buying sheets: after the client picks an option, an interactive page with a New / Second-hand switch per item, live set total, one sheet per item (offers by site sorted by landed price, specs and size, checklist), printable one sheet per page.
- Interview always asks the delivery country.

## 1.4.0 (2026-11-16)
- Optional protected-shop reading with Scrapling 0.5.1 (`scripts/shop_fetch.py`, `scripts/setup-scrapling.sh`): stealth browser, at most 10 pages per run, pauses, no login, proxy or paid bypass. Tested: works on eBay.fr and Ricardo.ch; Leboncoin still blocked (strong protection).
- Deals agent retries blocked sites once with it, then falls back to a search link for the client.

## 1.3.0 (2026-11-16)
- Best price hunt: deals agent, landed price (shipping, VAT, customs, returns), price history, discount codes and sales marked verified or not confirmed, buy-now-or-wait advice, second-hand fair price and scam checks (`references/deals.md`).
- Report gains a "Best price plan" section.

## 1.2.0 (2026-11-16)
- Report delivered as a designed page: option cards side by side with the recommended set highlighted, a comparison table, sizing reasoning, sources (`references/report-design.md`).
- Version bump is now automatic at the end of every use that changes the skill.
- Lessons from the first real use (snowboard): blocked-site handling, sizing-conflict rule, board width vs boot size question, shops searched by target specs.

## 1.1.0 (2026-11-16)
- Self-improvement loop: after each use the skill records lessons in `LESSONS.md` and refines its references (no client data).
- Public release: MIT license, README, contributing guide.

## 1.0.0 (2026-11-16)
- Client interview in up to 3 rounds, with a validated athlete profile and target specs.
- Parallel web research by source type (tests, communities, brand specs, shops and second-hand), in several languages, 2 independent sources per model.
- Recommendation report template.

## 0.1.0 (2026-11-16)
- First version: profile, sizing, web research, 3 to 5 picks.
