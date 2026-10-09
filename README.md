# timgutowski.com

Static site served by GitHub Pages from `main` (custom domain in `CNAME`).

## Editing copy
Edit the `.html` files directly. Copy-only changes need no build step.

## Styles
Tailwind is compiled to `css/tailwind.css` (the Play CDN isn't meant for production).
If you add or change Tailwind classes, rebuild before committing:

```
npm install        # first time only
npm run build:css  # or: npm run watch:css while editing
```

Hand-written styles live in `css/styles.css`.

## Deploy
Merge to `main` and push; GitHub Pages publishes automatically.
