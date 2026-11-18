# Lessons learned

What real uses of the skill taught us (with the category). One entry per lesson, newest first. Generic only: never a client's name, measurements, location or any other personal data.

Format: `- YYYY-MM-DD · <category> · <what happened> → <what changed in the skill>`

- 2026-11-18 · all · The client asked for a daily search with notifications; in-session schedules expire, several Swiss and French city slugs fell back to the US on Facebook, and Vinted search could not be automated → marketplaces.md lists working slugs and the out-of-session daily-watch pattern (seen-list, alert on new only, Vinted saved search).
- 2026-11-18 · sport · The client bought boots one size up after the board was chosen; nobody re-checked the board width, and the chosen size was rated for smaller boots → the sport pack now re-checks boot outsole length against the board width at the inserts (waist + stance²/sidecut radius) whenever boots change, and asks for the outsole length in cm.
- 2026-11-18 · sport · Second-hand Burton bindings are often EST (Channel only) without saying so; a 4x2 board cannot take them → compatibility rule: name the binding mount version and ask for a baseplate photo.
- 2026-11-18 · sport · A binding listing the client found turned out to have no discs → listing check now asks what hardware is included and lowers the target price by the replacement cost.
- 2026-11-18 · all · The client changed a key requirement (quick entry) after a strap-binding deals pass → re-ask entry type and other deal-breakers before any new deals pass in a returning session.
- 2026-11-17 · sport · A binding new this season had no private second-hand offer anywhere (Vinted, Ricardo, Marketplace); the only used pair was a shop's test unit on Leboncoin, 28% under new. Facebook share links resolve to the listing but hide the price → deals.md points to shop test units for new-season models; ask the client for the price of a Facebook listing.
- 2026-11-17 · sport · Facebook Marketplace returned nothing for model names around Lyon but many listings for generic queries, and an unknown city slug silently showed California → automatic warning and generic-query advice. Leboncoin and Vinted gave the best second-hand finds for the set.
- 2026-11-17 · all · Facebook Marketplace search looked impossible without an account with plain requests, but rendering its public search page with a headless browser lists local listings → marketplace_search.py; a tool that loses on one task (Obscura on protected shops) can win on another (JavaScript pages): use each where it is better.
- 2026-11-17 · all · A faster headless browser (Obscura, non-stealth) lost on exactly the protected sites that matter; speed is not the bottleneck, access is → measure on real target pages before adopting a fetcher.
- 2026-11-17 · all · Facebook Marketplace and Vinted listing links publish a public preview (OpenGraph, schema.org Product) readable without login, while search pages need an account → listing_preview.py reads links the client sends.
- 2026-11-17 · sport · A boot flex was chosen from level and style alone; the client then said their current flex 5 boots already felt too soft → the sport pack now asks how the current gear feels and sets the target relative to it.
- 2026-11-17 · sport · The client found boots on Facebook Marketplace, which robots cannot read; the seller said they "fit a size smaller" than labelled → listing check mode (client brings the listing) and the rule: a seller's fit feeling is not a measurement, check the brand chart and ask for a measurement.
- 2026-11-16 · snowboard · The client ended up choosing an all second-hand set and messaged sellers; ready-to-send seller messages (questions first, offer second) and a per-item checklist were the most used outputs → "Your picks" option and fallbacks per item.
- 2026-11-16 · snowboard · The same shop was cheaper on its German site than on its French site, with free EU shipping → deals method now checks a shop's other country sites.
- 2026-11-16 · snowboard · A Deep search (50 tool calls) on one new-season item found 8 new offers but only 1 second-hand lead → for brand-new models, say early that second-hand will be thin and suggest close alternatives.
- 2026-11-16 · snowboard · A deals agent hit its budget before searching second-hand; the client wanted more search → search depth levels and a targeted extension offer.
- 2026-11-16 · snowboard · A late alternative (quick-entry bindings) went into the sheets with only a list price and no shops → every item now needs its own deals pass; list prices are reference only.
- 2026-11-16 · all · The set total used a cheap offer whose size was not confirmed, about €130 too optimistic → such offers are shown but never count as best.
- 2026-11-16 · all · An alternative model shown as a separate option was easy to miss → alternatives now appear as a model switch inside each set.
- 2026-11-16 · snowboard · The client asked for quick-entry bindings after the boots were chosen; one system needs its own boots → the interview now asks the binding entry type up front.
- 2026-11-16 · all · Two deals agents kept running background work after delivering their report → stop agents once the report is in.
- 2026-11-16 · all · The client wanted to compare offers per item and per condition, not one fixed set → buying sheets template with per-item New / Second-hand switch.
- 2026-11-16 · all · An unbudgeted deals agent used about 70 tool calls and 24 minutes for 2 items → search budget with stop rules added to every agent brief.
- 2026-11-16 · snowboard · A marketplace listing looked about 10% cheaper than a shop, but its shipping made it about 20% more expensive in total → listing prices are never compared before adding shipping (deals method, section 1).
- 2026-11-16 · snowboard · Many shops and forums block automated reading (several big FR/CH shops, eBay, Swiss classifieds, Reddit) and some brand sites rate-limit → the research brief now tells agents to name blocked sites in the report and to fall back on shops that expose page data; the report lists sites the client should check by hand.
- 2026-11-16 · snowboard · Brand size charts and rider forums disagreed on length for a heavier park rider → merging rule added: prefer a tester with a similar build, then the size where the client's weight sits mid-range, and show the conflict in the report.
- 2026-11-16 · snowboard · The client's complaint about their current board ("too heavy") was partly explained by a wide board with medium boots → interview now compares the current board's width with the boot size.
- 2026-11-16 · all · The shops agent was seeded with candidate models from memory → shops are now briefed with the target specs first; seed lists are only a starting point.
