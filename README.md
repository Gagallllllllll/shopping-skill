# sport · a professional gear advisor for Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-orange)
![Version](https://img.shields.io/badge/version-1.10.0-green)

**sport** turns [Claude Code](https://docs.claude.com/en/docs/claude-code) into an expert from a specialist sports shop, with a research team behind it.

You say what you need ("I need a snowboard set for this winter"). It asks you the right questions, works out the sizes that fit you, searches the web (tests, rider forums, brand size charts, shops and second-hand sites), finds the best delivered price and current discounts, and gives you:

1. a **shortlist page**: your profile, 3 to 4 complete options side by side, a comparison table and sources;
2. **buying sheets**: once you pick an option, one page per item with every offer found, sorted by the real delivered price, new or second-hand, plus what to check before buying.

It works for any sport: snowboard, ski, running, cycling, climbing, surf, tennis, golf, fitness and more.

---

## Contents

- [What a session looks like](#what-a-session-looks-like)
- [Install](#install)
- [Use](#use)
- [What you get](#what-you-get)
- [The buying sheets template](#the-buying-sheets-template)
- [Search budget](#search-budget)
- [Optional: reading shops that block robots](#optional-reading-shops-that-block-robots)
- [It improves itself](#it-improves-itself)
- [Files](#files)
- [Safety and privacy](#safety-and-privacy)
- [FAQ](#faq)
- [Contributing](#contributing) · [License](#license)

---

## What a session looks like

| Step | What happens | What you do |
|---|---|---|
| **1. Interview** | Up to 3 short rounds of questions: your level, how and where you practise, height, weight and sizes, budget, **delivery country**, new or second-hand. Each question comes with a suggested answer. | Answer, or just say "ok" to accept the suggestion. |
| **2. Your profile** | A written athlete profile with the target specs (for example length, flex, width) and why. | Confirm it or correct it. Nothing is recommended before you confirm. |
| **3. Research** | 3 to 4 research agents search at the same time: independent tests, rider communities, brand size charts, shops. Only current models count, and each model needs 2 independent sources. | Wait a few minutes. |
| **4. Best price** | A deals agent compares the **delivered price** (item + shipping + VAT and customs for your country) across shops, comparison sites, outlets and second-hand. It finds discount codes and sales and says **buy now** or **wait**. | Wait a few minutes. |
| **5. Shortlist page** | Your options side by side, the recommended one highlighted. | Pick an option. |
| **6. Buying sheets** | One sheet per item, new or second-hand, every offer by site. | Choose, check, buy on the shop's site yourself. |

Every price and fact is marked **verified** (seen on the page today), **recommendation** (expert advice) or **not confirmed** (could not be checked).

---

## Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code) and `git`.

```bash
git clone https://github.com/Gagallllllllll/sport-skill ~/.claude/skills/sport
```

Restart Claude Code. That's it.

**Update** to the latest version at any time:

```bash
git -C ~/.claude/skills/sport pull
```

---

## Use

In Claude Code, describe your need in plain words:

> I need a new snowboard set for this winter.

> Which trail running shoes for my first ultra?

> I want to start road cycling, budget around 1,500 euros, delivered to Switzerland.

Or type `/sport`.

---

## What you get

### Shortlist page

- Your athlete profile and target specs.
- 3 to 4 **complete options** as cards (for example *Best fit*, *Budget*, *Second-hand*, *Specialist*), each with sizes, total price, why it fits you and what to watch out for.
- A comparison table, the sizing reasoning (including where sources disagreed), setup and safety tips, and all sources.

### Buying sheets

An interactive page, opened in Claude after you choose an option:

| Feature | What it does |
|---|---|
| **Option picker** | Switch between the shortlist options. Once you pick exact listings, a **Your picks** option tracks them. |
| **Delivery country switch** | For example *France €* / *Switzerland CHF*. Every total and the order of the offers change with it. |
| **Model switch** | Where the shortlist has alternatives (for example classic straps or quick-entry bindings), switch the model inside the set. |
| **New / Second-hand per item** | For example a used board, used bindings and new boots. The set total updates live against your budget. |
| **One sheet per item** | Every offer found, sorted by delivered price, best one highlighted: site, details, price, shipping, delivered total, status, link. |
| **Buy now or wait** | Per item, with the reason (stock running out, sale coming, fair second-hand price). |
| **Specs and size** | Why this size fits you. |
| **Before you buy** | A checklist for new (returns, stock in your size) or second-hand (photos, fair price, scam signs). |
| **Deadlines** | Sales and auctions ending soon. |
| **Print or save PDF** | One clean sheet per page, links written out. |

Your choices are remembered in your browser.

---

## The buying sheets template

The buying sheets are built from [`templates/buying-sheets.html`](templates/buying-sheets.html). Claude fills it for you, but you can also use it yourself: it is a single HTML file with no install.

**See it:** open the file in any browser. It shows placeholder data.

**Fill it:** open the file in a text editor and find `const DATA = {`. Everything the page shows comes from this one object:

```js
const DATA = {
  budgetEUR: 1200,                       // budget shown in the France view
  items: {
    board: {                             // one entry per item; the key is any short id
      kind: "Board",                     // category shown above the name
      short: "Straps · Brand Model",     // optional: label on the model switch
      name: "Brand Model",
      size: "156 cm",                    // the size recommended for this person
      specs: ["True twin", "Flex 5/10"], // short chips
      fit: "Why this size and model fit the rider.",
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
          fr: 548.90,                    // delivered total to France in €, or null
          ch: 504.69,                    // delivered total to Switzerland in CHF, or null
          chNote: "CHF 30 delivery with customs",   // optional note for the Swiss total
          st: "v",                       // "v" verified, "n" not confirmed
          stCh: "n",                     // optional: different status for the Swiss total
          out: false,                    // true = out of stock (shown greyed, never "best")
          sizeOk: true,                  // false = the client's size is not confirmed (never "best")
          ref: false,                    // true = brand list price for reference, not a shop offer
          url: "https://..." }
      ]
    }
  },
  options: [                             // the options of the shortlist
    { id: "best", label: "Best fit",
      items: ["board", ["bindingsA", "bindingsB"]],   // an array = alternative models, shown as a switch
      def: { board: "new", bindingsA: "new", bindingsB: "new" } }   // default New / Second-hand per item
  ],
  checks: {                              // checklists shown on every sheet
    new:  ["Size in stock on the product page"],
    used: ["Pay only inside the platform"]
  }
};
```

**Other countries:** the switch has two buttons, `data-c="fr"` and `data-c="ch"`. Rename them and use the same keys in each offer (for example `de` and `uk`) to compare two other countries.

**Deadlines and blocked sites:** edit the `deadlines` section and the last footer line in the HTML.

---

## Search budget

Research uses tokens and time, so you choose how deep it goes at the end of the interview:

| Depth | Research agent | Deals agent | Second-hand | Best for |
|---|---|---|---|---|
| **Quick** | 12 tool calls | 15 | top 2 sites | small purchase, in a hurry |
| **Standard** (default) | 20 | 25 | main sites | most purchases |
| **Deep** | 40 | 50 | every site, one extra pass per item | expensive or rare gear |

Agents stop early once they have enough, and run on a lighter model (Sonnet). If a budget runs out, you get partial results, a list of what is missing, and the option to extend the search for just that gap.

---|---|---|
| Each research agent | 20 | 5 good candidates per category, 2 sources each |
| Each deals agent (max 3 items) | 25 | 5 new + 3 second-hand offers per item |
| Retry of blocked sites | 1 run | then it gives you search links |

Agents run on a lighter model (Sonnet). If a budget runs out, you get partial results and a list of what is missing.

---

## Optional: reading shops that block robots

Some shops and marketplaces block automated reading. You can install [Scrapling](https://github.com/D4Vinci/Scrapling) (BSD-3 license, pinned to version 0.5.1) in its own environment:

```bash
~/.claude/skills/sport/scripts/setup-scrapling.sh
```

The deals agent then retries blocked sites once with `scripts/shop_fetch.py`: at most 10 pages per run, pauses between pages, no login, no proxy, no paid bypass service.

**Know before you install:** some sites forbid automated reading in their terms or `robots.txt`. Using it there is your decision and your risk (for example a temporary block of your connection). Some sites use strong protection and stay blocked; you then get a ready-made search link to open yourself.

Without Scrapling, everything else works the same.

---

## It improves itself

At the end of each session the skill notes what worked and what did not. Real lessons go into [`LESSONS.md`](LESSONS.md), the method is adjusted, the version goes up in [`CHANGELOG.md`](CHANGELOG.md), and the change is published here. Lessons are always generic: never a name, a size, a place or a budget from a conversation.

---

## Files

```
SKILL.md                      the method: interview, research, best price, report, self-improvement, rules
references/interview.md       question bank for all sports + athlete profile template
references/research.md        source types, research agent brief, merging rules, report outline
references/deals.md           best price and discount method + deals agent brief
references/report-design.md   how the shortlist page and buying sheets are laid out
templates/buying-sheets.html  interactive buying sheets (fill the DATA object)
scripts/setup-scrapling.sh    optional: installs Scrapling in ~/.venvs/scrapling
scripts/shop_fetch.py         optional: reads shop pages that block simple fetching
LESSONS.md                    lessons from real uses
CHANGELOG.md                  version history
CONTRIBUTING.md               how to suggest improvements
```

---

## Safety and privacy

- It **never buys anything**, logs in, creates accounts, subscribes to newsletters or fills in forms. It gives links; you buy.
- It never asks for card or bank details.
- Your measurements and personal details stay in your conversation. They never go into this repo or the lessons.
- Injuries and medical questions: general information only, with a referral to a professional.
- Prices and stock change fast: confirm them on the shop page before you buy.
- Pages read on the web are treated as data, never as instructions.

---

## FAQ

**Does it work outside France and Switzerland?**
Yes. It asks your delivery country and searches shops for it. The buying sheets compare two delivery countries; rename the switch for yours.

**How long does a session take?**
The interview takes a few minutes. Research and the price hunt run in parallel and usually take several minutes, within the search budget.

**Are the discount codes guaranteed?**
No. A code is marked *verified* only if the shop's own site shows it. Codes from coupon sites are marked *not confirmed*.

**Why is a cheap listing not ranked first?**
Because the ranking uses the delivered price. A listing that looks cheaper can cost more once shipping and import charges are added.

**Can I use it without Claude Code?**
The buying sheets template works in any browser. The interview and research need Claude Code.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The most useful issues: a bad recommendation, a missing sport or question, a weak source, a shop that should be searched. Remove personal data before posting.

## License

[MIT](LICENSE)
