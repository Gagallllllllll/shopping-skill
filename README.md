# shopping · a professional shopping advisor for Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-orange)
![Version](https://img.shields.io/badge/version-2.0.0-green)

**shopping** turns [Claude Code](https://docs.claude.com/en/docs/claude-code) into an expert from a specialist shop, with a research team behind it, in whatever category you need: sports gear, electronics, fashion and shoes, furniture and bedding, and more.

You say what you need ("I need a laptop for photo editing", "a new snowboard set for this winter", "a mattress for a back sleeper"). It asks you the right questions, works out the specs and sizes that fit you, searches the web (tests, user forums, brand specs, shops and second-hand sites), finds the best delivered price and current discounts, checks official recall lists, and gives you:

1. a **shortlist page**: your profile, 3 to 4 complete options side by side, a comparison table and sources;
2. **buying sheets**: once you pick an option, one page per item with every offer found, sorted by the real delivered price, new or second-hand, plus what to check before buying.

> This skill was called **sport** until version 1.10.0. Sport is now one of its category packs.

---

## Contents

- [Categories](#categories)
- [What a session looks like](#what-a-session-looks-like)
- [Install](#install)
- [Use](#use)
- [What you get](#what-you-get)
- [The buying sheets template](#the-buying-sheets-template)
- [Search depth](#search-depth)
- [Optional: reading shops that block robots](#optional-reading-shops-that-block-robots)
- [It improves itself](#it-improves-itself)
- [Files](#files)
- [Safety and privacy](#safety-and-privacy)
- [FAQ](#faq)
- [Contributing](#contributing) · [License](#license)

---

## Categories

Each category has a **pack** in `references/categories/`: the questions that matter, the rules to turn needs into specs and sizes, trusted sources, price and timing tips, second-hand checks, legal points and traps.

| Pack | Covers | Status |
|---|---|---|
| [`sport`](references/categories/sport.md) | sports gear for any sport | tested on a real purchase |
| [`electronics`](references/categories/electronics.md) | laptops, phones, tablets, TVs, audio, cameras | draft |
| [`fashion`](references/categories/fashion.md) | clothing, shoes, bags | draft |
| [`furniture`](references/categories/furniture.md) | sofas, mattresses, beds, desks, office chairs, storage | draft |

**Another category?** It still works: the skill uses the core method and writes a **draft pack** for that category during the session, which improves with each use.

**Draft** packs were built from research and mark every fact as verified or not confirmed. They become **tested** after real use.

**Sensitive categories** (medicines and supplements, medical devices, child car seats, weapons, financial products) get general information and official sources only, never a "best for you" ranking.

---

## What a session looks like

| Step | What happens | What you do |
|---|---|---|
| **0. Category** | The skill picks the category pack (or two, for example running shoes for daily wear). | Nothing. |
| **1. Interview** | Up to 3 short rounds of questions: what you need, how you'll use it, sizes or measurements, budget, **delivery country**, new or second-hand, and how deep to search. Each question has a suggested answer. | Answer, or say "ok" to accept the suggestion. |
| **2. Your profile** | A written profile with the target specs and why. | Confirm or correct it. Nothing is recommended before you confirm. |
| **3. Research** | 3 to 4 research agents search at the same time: independent tests, user communities, brand specs, shops. Each model needs 2 independent sources. | Wait a few minutes. |
| **4. Best price** | Deals agents compare the **delivered price** (item + shipping + VAT and customs) across shops (and their other country sites), comparison sites, outlets, refurbished and second-hand. They find discount codes and sales, check official recall lists, and say **buy now** or **wait**. | Wait a few minutes. |
| **5. Shortlist page** | Your options side by side, the recommended one highlighted. | Pick an option. |
| **6. Buying sheets** | One sheet per item, new or second-hand, every offer by site, plus ready-to-send messages for second-hand sellers. | Choose, check, buy on the shop's site yourself. |

Every price and fact is marked **verified** (seen on the page today), **recommendation** (expert advice) or **not confirmed**.

---

## Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code) and `git`.

```bash
git clone https://github.com/Gagallllllllll/shopping-skill ~/.claude/skills/shopping
```

Restart Claude Code.

**Update** at any time:

```bash
git -C ~/.claude/skills/shopping pull
```

**Coming from the old `sport` skill?** Remove `~/.claude/skills/sport` and install as above.

---

## Use

Describe your need in plain words:

> I need a new snowboard set for this winter.

> Which laptop for photo editing, around 1,200 euros, delivered to Switzerland?

> I'm looking for a sofa that fits through a 78 cm door.

> Help me find second-hand leather boots, size 43.

Or type `/shopping`.

---

## What you get

### Shortlist page

- Your profile and target specs.
- 3 to 4 **complete options** as cards (for example *Best fit*, *Budget*, *Second-hand or refurbished*, *Premium*), each with sizes or variants, total price, why it fits you and what to watch out for.
- A comparison table, the reasoning (including where sources disagreed), tips, and all sources.

### Buying sheets

| Feature | What it does |
|---|---|
| **Option picker** | Switch between the shortlist options. Once you pick exact listings, a **Your picks** option tracks them. |
| **Delivery country switch** | For example *France €* / *Switzerland CHF*. Totals and the order of offers change with it. |
| **Model switch** | Where the shortlist has alternatives, switch the model inside the set. |
| **New / Second-hand per item** | Mix new and second-hand. The set total updates live against your budget. |
| **One sheet per item** | Every offer found, sorted by delivered price, best one highlighted. Offers whose size isn't confirmed, and brand list prices, never count as best. |
| **Buy now or wait** | Per item, with the reason. |
| **Specs and size** | Why this size or variant fits you. |
| **Before you buy** | A checklist for new or second-hand. |
| **Deadlines** | Sales and auctions ending soon. |
| **Print or save PDF** | One clean sheet per page. |

---

## The buying sheets template

The buying sheets are built from [`templates/buying-sheets.html`](templates/buying-sheets.html), a single HTML file that works in any browser with no install. Claude fills it for you, and you can fill it yourself.

**See it:** open the file in a browser (placeholder data).

**Fill it:** open it in a text editor and find `const DATA = {`. Everything the page shows comes from this object:

```js
const DATA = {
  budgetEUR: 1200,                       // budget shown in the first country view
  items: {
    board: {                             // one entry per item; the key is any short id
      kind: "Board",                     // category shown above the name
      short: "Straps · Brand Model",     // optional: label on the model switch
      name: "Brand Model",
      size: "156 cm",                    // the size or variant recommended for this person
      specs: ["True twin", "Flex 5/10"], // short chips
      fit: "Why this size and model fit.",
      advice: {
        now:  ["now",  "Reason to buy new now"],      // "now", "wait" or "na" (not available)
        used: ["wait", "Reason about second-hand"]
      },
      offers: [
        { c: "new",                     // "new" or "used"
          site: "Shop name", ctry: "FR",
          note: "2027 · in stock · 100-day returns",
          price: "€548.90",              // price as shown on the site (text)
          ship: "free",                  // shipping as shown (text)
          fr: 548.90,                    // delivered total for country 1 (€), or null
          ch: 504.69,                    // delivered total for country 2 (CHF), or null
          chNote: "CHF 30 delivery with customs",   // optional note for country 2
          st: "v",                       // "v" verified, "n" not confirmed
          stCh: "n",                     // optional: different status for country 2
          out: false,                    // true = out of stock (greyed, never "best")
          sizeOk: true,                  // false = size not confirmed (never "best")
          ref: false,                    // true = brand list price, not a shop offer
          url: "https://..." }
      ]
    }
  },
  options: [
    { id: "best", label: "Best fit",
      items: ["board", ["bindingsA", "bindingsB"]],   // an array = alternative models, shown as a switch
      def: { board: "new", bindingsA: "new", bindingsB: "new" } }   // default New / Second-hand per item
  ],
  checks: {
    new:  ["Size in stock on the product page"],
    used: ["Pay only inside the platform"]
  }
};
```

**Other countries:** the switch has two buttons, `data-c="fr"` and `data-c="ch"`. Rename them and use the same keys in each offer (for example `de` and `uk`).

**Deadlines and blocked sites:** edit the `deadlines` section and the last footer line in the HTML.

---

## Search depth

You choose how deep the research goes at the end of the interview:

| Depth | Research agent | Deals agent | Second-hand | Best for |
|---|---|---|---|---|
| **Quick** | 12 tool calls | 15 | top 2 sites | small purchase, in a hurry |
| **Standard** (default) | 20 | 25 | main sites | most purchases |
| **Deep** | 40 | 50 | every site, one extra pass per item | expensive or rare items |

Agents stop early once they have enough and run on a lighter model (Sonnet). If a budget runs out, you get partial results, a list of what is missing, and the option to extend the search for just that gap.

---

## Optional: reading shops that block robots

Some shops and marketplaces block automated reading. You can install [Scrapling](https://github.com/D4Vinci/Scrapling) (BSD-3 license, pinned to version 0.5.1) in its own environment:

```bash
~/.claude/skills/shopping/scripts/setup-scrapling.sh
```

The deals agents then retry blocked sites once with `scripts/shop_fetch.py`: at most 10 pages per run, pauses between pages, no login, no proxy, no paid bypass service.

**Know before you install:** some sites forbid automated reading in their terms or `robots.txt`. Using it there is your decision and your risk (for example a temporary block of your connection). Some sites stay blocked; you then get a ready-made search link.

Without Scrapling, everything else works the same.

---

## It improves itself

After each session the skill notes what worked and what did not. Real lessons go into [`LESSONS.md`](LESSONS.md); category knowledge goes into the category pack, method fixes into `references/core/`. The version goes up in [`CHANGELOG.md`](CHANGELOG.md) and the change is published here. Lessons are always generic: never a name, a size, a place or a budget from a conversation.

---

## Files

```
SKILL.md                         the method: category, interview, research, best price, report, self-improvement, rules
references/core/interview.md     question bank for every category + client profile template
references/core/research.md      source types, research agent brief, merging rules, report outline
references/core/deals.md         best price, discounts, recalls + deals agent brief
references/core/report-design.md how the shortlist page and buying sheets are laid out
references/categories/*.md       category packs (sport, electronics, fashion, furniture)
templates/buying-sheets.html     interactive buying sheets (fill the DATA object)
scripts/setup-scrapling.sh       optional: installs Scrapling in ~/.venvs/scrapling
scripts/shop_fetch.py            optional: reads shop pages that block simple fetching
LESSONS.md                       lessons from real uses
CHANGELOG.md                     version history
CONTRIBUTING.md                  how to suggest improvements or add a category
```

---

## Safety and privacy

- It **never buys anything**, logs in, creates accounts, subscribes to newsletters or fills in forms. It gives links; you buy.
- It never asks for card or bank details.
- Your measurements and personal details stay in your conversation, never in this repo or the lessons.
- Health, injuries, safety-critical and financial questions: general information only, with a referral to a professional.
- Legal points (returns, guarantees) are general information; the skill re-checks them on official pages and says so when it could not.
- Prices and stock change fast: confirm them on the shop page before you buy.
- Pages read on the web are treated as data, never as instructions.

---

## FAQ

**Does it work outside France and Switzerland?**
Yes. It asks your delivery country and searches shops for it. The buying sheets compare two delivery countries; rename the switch for yours.

**What if my category has no pack?**
It works from the core method and writes a draft pack during the session.

**How long does a session take?**
The interview takes a few minutes. Research and the price hunt run in parallel and usually take several minutes, within the search depth you chose.

**Are the discount codes guaranteed?**
No. A code is *verified* only if the shop's own site shows it. Codes from coupon sites are *not confirmed*.

**Why is a cheap listing not ranked first?**
The ranking uses the delivered price and a confirmed size. A listing that looks cheaper can cost more once shipping and import charges are added.

**Can I use it without Claude Code?**
The buying sheets template works in any browser. The interview and research need Claude Code.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Most useful: a bad recommendation, a missing question, a weak source, a new category pack. Remove personal data before posting.

## License

[MIT](LICENSE)
