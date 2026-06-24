# Template: Stat

One giant number is the whole design. For data drops, proof, milestones, and before/after. The number
dwarfs everything; a small label sets it up and a short line lands the "so what." Uses the shared DNA
in the project's `DESIGN.md`.

> **Evidence discipline:** the number must be real and cited (a transcript, contract, or live metric) —
> never a placeholder dressed up as proof. A fake number on a proof card is the worst kind of slop.

## Visual identity
- **Field:** dark by default (`--ink`/`--navy` gradient + one `--signal` glow) so the number glows;
  a crisp light variant works too (number in `--navy`, glow off).
- **The number:** `Space Grotesk` 700, 200–300px, tight tracking. Color it white on dark, or `--signal`
  for the single energy pop. It is by far the largest thing on the canvas.
- **Label:** small uppercase `Plus Jakarta Sans` 700 above the number (`--accent` / muted) — what it measures.
- **Context line:** one sentence under the number — the meaning, with the contrast/source if there is one.
- **Footer:** standard mark + `Sidney Swift` · `recoupable.com`, adapted to the field.

## Layout rules
- Number centered or anchored left, vertically a touch above center. One number per card.
- Label → number → context, stacked tight so they read as one unit.
- For before/after, show the hero number huge and the comparison small ("up from 28").
- Works at 1080×1350, 1080×1080, 1200×630 — scale the numeral to the canvas width.

## HTML shell (complete, renderable — 1080×1350)

```html
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
  :root{--ink:#0b1020;--navy:#14254a;--accent:#3f5fb0;--signal:#3d6bff;--on-dark:#dfe5f3;}
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Plus Jakarta Sans',sans-serif;
       background:linear-gradient(160deg,#16294f 0%,#0b1020 64%);}
  body::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 55% 40% at 50% 34%, rgba(61,107,255,0.42) 0%, transparent 62%);pointer-events:none;}
  .wrap{position:absolute;inset:0;padding:96px 80px;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;}
  .label{font-size:22px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#7f9bff;}
  .num{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:280px;line-height:0.9;letter-spacing:-8px;color:#fff;margin-top:8px;}
  .context{font-size:30px;font-weight:600;color:var(--on-dark);margin-top:24px;max-width:760px;line-height:1.4;}
  .context b{color:#fff;}
  .footer{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-weight:700;}
  .footer .who{display:flex;align-items:center;gap:11px;}
  .footer .nm{font-size:19px;color:#fff;letter-spacing:-0.01em;}
  .footer .url{font-size:16px;color:#9bb2ec;}
</style></head><body>
  <div class="wrap">
    <div class="label">The real number</div>
    <div class="num">88</div>
    <div class="context">Minutes a task was actually out. The agent reported <b>28</b> — confident, formatted, wrong.</div>
  </div>
  <div class="footer">
    <div class="who">
      <svg viewBox="0 0 223 223" width="26" height="26" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#ffffff"/></svg>
      <span class="nm">Sidney Swift</span>
    </div>
    <span class="url">recoupable.com</span>
  </div>
</body></html>
```

## Quality checklist
- [ ] The number is real + cited (no fabricated proof)
- [ ] Number is by far the biggest element; reads instantly at thumbnail scale
- [ ] Label sets it up, one context line lands the meaning
- [ ] One signal moment (the number or its glow), not a rainbow
- [ ] Footer = mark + Sidney Swift · recoupable.com
