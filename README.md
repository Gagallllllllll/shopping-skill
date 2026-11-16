# sport · a professional gear advisor for Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-orange)
![Version](https://img.shields.io/badge/version-1.7.0-green)

A [Claude Code](https://docs.claude.com/en/docs/claude-code) skill that works like an expert in a specialist sports shop, with a research team behind it. It interviews you, builds your athlete profile, searches the whole web and recommends the gear that fits **you**, not just the best-reviewed product.

It covers any sport: snowboard, ski, running, cycling, climbing, surf, tennis, golf, fitness and more.

## How it works

| Phase | What happens |
|---|---|
| **1. Interview** | Up to 3 rounds of grouped questions, each with a suggested default: your need, level, goals, body and sizes, terrain, budget, country, taste. It asks again when an answer is vague and points out contradictions. |
| **Athlete profile** | A written profile with target specs (size, flex, shape...) and the reasoning behind each one. **Nothing is recommended until you confirm it.** |
| **2. Research** | 3 to 4 research agents search in parallel, one per source type: independent tests, athlete communities, brand specs and size charts, shops and second-hand. It searches in several languages and keeps current-season models only. Each model needs 2 independent sources. |
| **Best price** | A deals agent compares the landed price (shipping, VAT and customs included) across shops, comparison sites, outlets and second-hand, checks price history, finds discount codes and sales, and says buy now or wait. |
| **3. Report** | A designed report page (option cards side by side, comparison table) with a top pick plus budget, premium and second-hand alternatives, a comparison table, exact sizes, weaknesses, dated prices, shop links, compatibility and fitting tips. Every claim is marked *verified*, *recommendation* or *not confirmed*. |
| **4. Self-improvement** | After each use it records generic lessons in [`LESSONS.md`](LESSONS.md) and refines its own questions and research method. |

## Install

```bash
git clone https://github.com/Gagallllllllll/sport-skill ~/.claude/skills/sport
```

Update later with `git -C ~/.claude/skills/sport pull`.

### Optional: read shops that block simple fetching

```bash
~/.claude/skills/sport/scripts/setup-scrapling.sh
```

Installs [Scrapling](https://github.com/D4Vinci/Scrapling) (BSD-3, pinned to 0.5.1) in `~/.venvs/scrapling`. The deals agent then retries blocked shops with `scripts/shop_fetch.py`: at most 10 pages per run, pauses between pages, no login, no proxy, no paid bypass service. Some sites forbid automated reading in their terms or `robots.txt`; using it there is your decision and your risk.

## Use

In Claude Code, just describe your need:

> I need a snowboard for this winter.

> Which trail running shoes for my first ultra?

> I want to start road cycling, budget around 1,500 euros.

Or type `/sport`.

## Files

```
SKILL.md                  the method (4 phases + rules)
references/interview.md   question bank for all sports + athlete profile template
references/research.md    source types, research agent brief, merging rules, report template
references/deals.md       best price and discount method + deals agent brief
references/report-design.md  layout of the designed report page (option cards, comparison table)
scripts/shop_fetch.py     optional: read protected shop pages (Scrapling)
scripts/setup-scrapling.sh  optional: install Scrapling in its own environment
templates/buying-sheets.html  interactive buying sheets template (fill the DATA object)
LESSONS.md                lessons from real uses
CHANGELOG.md              version history
```

## Safety and privacy

- It never buys anything, logs in to an account or fills in a payment form. It gives links only.
- It never asks for card or bank details.
- Your measurements and personal details stay in your conversation and never go into the repo or the lessons.
- Injuries and medical questions: general information only, with a referral to a professional.
- Prices and stock change quickly: check them on the shop page before you buy.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues about a bad recommendation, a missing sport or a weak source are the most useful.

## License

[MIT](LICENSE)
