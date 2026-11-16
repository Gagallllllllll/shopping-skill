# sport

A professional Claude Code skill that gives gear and training advice for any sport: snowboard, ski, running, cycling, climbing, surf, tennis, golf, fitness and more.

1. **Interview:** it asks the client up to 3 rounds of questions, suggesting a default for each, and builds a detailed athlete profile with target specs. The client confirms the profile before anything else happens.
2. **Research:** 3 to 4 research agents search the web in parallel, each on one type of source: independent tests, athlete communities, brand specs, and shops (including second-hand). Searches run in several languages and only current-season models count. Each model needs 2 independent sources or it is dropped.
3. **Report:** a top pick plus alternatives, with sizes, the reasons each one fits, weaknesses, dated prices, shop links and compatibility notes. Every claim is marked as verified, a recommendation, or not confirmed.

It never buys anything, logs in to accounts, or asks for payment details.

## Install

```bash
git clone https://github.com/Gagallllllllll/sport-skill ~/.claude/skills/sport
```

Then ask Claude Code something like "which snowboard should I buy this winter?" or type `/sport`.
