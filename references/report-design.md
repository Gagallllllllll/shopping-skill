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
5. **Best price plan:** per item, the best landed offer (price + shipping + VAT/customs) and the runner-up, discounts with their status, a clear "buy now" or "wait until <sale>" chip, and the cheapest total per option.
6. **Why these sizes:** the sizing reasoning in 3 to 5 lines, including where sources disagreed and which one you trusted.
7. **Kit and compatibility, fitting and safety tips, before you keep it:** short lists.
8. **Sources:** grouped by type (tests, communities, brand specs, shops), each with its link. Status legend: verified / recommendation / not confirmed.

## Buying sheets (after the client picks an option)

When the client picks an option, build a second interactive page, "buying sheets":

1. **Option picker:** the shortlist's option cards; selecting one loads its items.
2. **Set summary:** one row per item with a **New / Second-hand** switch per item (default: boots new). The set total updates live from the best landed offer of each choice and is shown against the budget.
3. **One sheet per item:**
   - **Offers by site:** every offer found for the chosen condition, sorted by landed price (price + shipping + VAT/customs for the client's delivery country): site, condition, size in stock, price, shipping, landed total, returns, status chip, link. Best offer highlighted; an offer whose size is not confirmed for the client never counts as best.
   - **Specs and size:** key specs, recommended size and why it fits the client.
   - **Before you buy:** checklist for new (returns, size, sale end) or second-hand (condition checks, fair price range, scam signs).
   - Blocked sites: a ready-made search link per site.
4. **Printable:** `@media print` puts one item sheet per page, hides switches and picker, shows the chosen condition and links as text.
5. **Your picks:** once the client names the exact listings or offers they are going for, add a "Your picks" option first in the picker, pre-set to those items and conditions, with fallbacks kept in the model switch. Give the client a short checklist per item and a fallback per item in the chat.
6. Choices persist per viewer in `localStorage` (wrapped in try/catch); the page renders fully without it.

Start from `templates/buying-sheets.html`: fill the `DATA` object (items, offers with `fr`/`ch` landed prices, options with default conditions, checklists), the deadlines and the blocked-site links. Add or rename the country switch buttons for the client's delivery countries. **No item enters the buying sheets without its own deals pass (new and second-hand).** If the client adds an item late (a new model or alternative), run the deals agent for it first. A brand list price is marked `ref: true`: shown as a reference, never as a place to buy, never in the total. Offer data lives in that one object so the next run can refresh prices without redesigning.

## Principles

- Cards for the decision, a table for the detail (pricing-page pattern). The recommended option is visually distinct (accent border and badge), never only by colour.
- One accent colour inspired by the sport (snow: ice blue or a warm signal orange), neutral greys, generous spacing, clear numeric typography for prices (tabular figures).
- Prices always show currency, date checked and "approx." if from list prices. Never invent a price: write "not confirmed".
- Light and dark themes, readable at 400 px wide, accessible contrast, real links.
- No stock photos or brand logos. Optional: simple inline SVG icons.
