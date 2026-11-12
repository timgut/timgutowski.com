# Design options (review only)

Three design directions (options 2, 4, and 5; 1 and 3 were dropped 11/12) for the timgutowski.com redesign, at /design-options/. These pages are
`noindex`, blocked in robots.txt, and not linked from the site.

- `index.html`: the review page; `preview.html`: phone-size view.
- `assets/palettes.css`: the color palettes. Add or edit a block to try new colors (keep text
  contrast at 4.5:1 or better).
- `_src/`: the Python generator. Edit `content.py` (copy), `palettes.py`, or `options.py` (layouts),
  then regenerate (below).

Regenerate from the repo root:

    python3 design-options/_src/build.py .

Screenshots in `shots/` were rendered with Playwright.
