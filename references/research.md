# Research method and report

## Source types (search all of them)

| Type | What it gives | Examples of what to look for |
|---|---|---|
| Independent tests | measured performance, comparisons | lab or field test sites, specialised magazines, long-term reviews |
| Communities | real-world use, durability, problems | sport subreddits, forums, club groups, video reviews with comments |
| Brand specs | exact sizes, shapes, technologies | official product pages, size charts, catalogues for the current season |
| Shops | real prices, stock, sizes available | large online shops and specialist shops in the client's region, brand stores |
| Deals and second-hand | lower prices, last season | outlets, end-of-season sales, second-hand marketplaces in the region |

Search in several languages (the client's language, English, and the language of the sport's leading markets). The `WebSearch` tool may lean towards US results: for prices and stock in another region, open the regional shops with `WebFetch`.

## Research agent brief (paste into each agent)

```
You are a research agent for a sports gear recommendation. Source type: <TYPE>.

Client athlete profile (validated):
<PROFILE + TARGET SPECS>

Task:
1. Search the web widely (several queries, several languages: <LANGUAGES>) for current-season (<YEAR/SEASON>) products that match the target specs. For each candidate, open the pages (WebFetch) and read them; do not rely on search snippets.
2. For each model, return: exact name and season, the specs that matter for this profile, the evidence (quote or figure + URL), positives and negatives seen, and for shops: price, currency, size availability, URL, and today's date.
3. Flag sponsored or affiliate-only rankings as weak sources.
4. Return 5 to 10 candidates ranked by fit to the profile, with a one-line reason each. Say clearly what you could not find or confirm, and list every site that blocked you.
5. Shops agent: search by the target specs first; any model list given to you is a starting point, not the scope.
Budget: stop after <N: 12 Quick / 20 Standard / 40 Deep> tool calls, or as soon as you have 5 good candidates per category with 2 sources each, and report what you have and what is missing.
Do not buy anything, log in, or fill any form.
```

## Blocked sites

Many large shops, classifieds, Reddit and some brand sites block automated reading or rate-limit it. Agents list every site they could not open; the report tells the client which ones to check by hand. Shops that expose page data (stock per size, prices) are the most reliable to read.

## Merging rules

- Sizing conflicts (brand chart vs riders vs testers): prefer a tester with a build close to the client's, then the size where the client's weight sits in the middle of the brand range, and explain the conflict in the report.

- Keep a model only if at least 2 independent sources support its fit (a brand page plus an independent test counts; two pages of the same shop does not).
- When sources disagree, say so and explain which one you trust and why.
- Prices: keep the lowest reliable new price and, if relevant, a second-hand range. Always give the date checked.

## Report template

```
# Your <gear> recommendation: <client>

## Your profile in short
<3 to 5 lines + target specs>

## Top pick: <model, season, size>
Why it fits you: ...
Key specs: ...
Weakness to know: ...
Price: <range> (checked <date>): <shop links>

## Alternatives
- Budget: ...
- Premium: ...
- If you progress fast: ...
- Last season / second-hand: ...

## Comparison
| Model | Size | Fit to you (1-5) | Main strength | Main weakness | Price |

## Full kit and compatibility
## Setup, fitting and safety tips
## Before you keep it (try in shop / check on delivery)
## Sources
```
