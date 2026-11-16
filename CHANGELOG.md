# Changelog

All notable changes to this skill. Newest first.

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
