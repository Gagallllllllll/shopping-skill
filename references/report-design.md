# Report page design

The final report is a single HTML page published with the Artifact tool. It should look like a premium buyer's guide from a specialist shop: calm, precise, easy to compare. Load the `artifact-design` skill (or the quickstart) before writing it.

## Structure (top to bottom)

1. **Header:** sport, purchase ("Park set: board, bindings, boots"), date checked, one-line verdict.
2. **Athlete profile:** a compact card with key facts as label/value pairs (level, use, body and boot size, budget, where to buy) and the target specs as small chips (e.g. "True twin", "Flex 5-6", "155-157", "Regular width").
3. **Option cards, side by side (3 to 4):** the decision area.
   - One card per *complete* option (a set, not a single item): e.g. **Best fit** (highlighted, with a "Recommended" badge), **Budget**, **Premium**, **Second-hand / last season**.
   - Each card: option name, total price range (large), the items with sizes, 3 "why it fits you" points, 1 "watch out" point, and shop links.
   - Wraps into one column on phones.
4. **Comparison table:** rows = items or criteria (jumps, rails, butters, stability at 85 kg, price), columns = options. Use short ratings and words, not only colour. Wrapped in a horizontal scroll container on small screens.
5. **Why these sizes:** the sizing reasoning in 3 to 5 lines, including where sources disagreed and which one you trusted.
6. **Kit and compatibility, fitting and safety tips, before you keep it:** short lists.
7. **Sources:** grouped by type (tests, communities, brand specs, shops), each with its link. Status legend: verified / recommendation / not confirmed.

## Principles

- Cards for the decision, a table for the detail (pricing-page pattern). The recommended option is visually distinct (accent border and badge), never only by colour.
- One accent colour inspired by the sport (snow: ice blue or a warm signal orange), neutral greys, generous spacing, clear numeric typography for prices (tabular figures).
- Prices always show currency, date checked and "approx." if from list prices. Never invent a price: write "not confirmed".
- Light and dark themes, readable at 400 px wide, accessible contrast, real links.
- No stock photos or brand logos. Optional: simple inline SVG icons.
