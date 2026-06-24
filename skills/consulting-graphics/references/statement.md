# Template: Statement

One huge line on a dark field. For hooks, contrarian POVs, manifestos, announcements, and pull-quote
cards. The opposite end of the kit from `framework-blocks` — minimal content, maximum conviction.
Uses the shared brand DNA in the project's `DESIGN.md`.

## Visual identity
- **Field:** full-bleed dark — `--ink` (`#0b1020`) base with a subtle `--navy`→`--ink` gradient and one
  soft `--signal` glow for depth. No pale gradients ever.
- **Headline:** the whole design. Two styles, pick per piece:
  - **Display** — `Space Grotesk` 700, white, 88–110px, tight. For punchy hooks/POVs.
  - **Editorial** — `Instrument Serif` italic, white, 84–104px. For reflective quotes (the signature
    serif, used deliberately — not by default).
- **Accent:** one short `--signal` rule under or beside the headline, OR a single highlighted word.
- **Kicker** (optional): small uppercase label in `--signal`/muted at top-left.
- **Footer:** standard, dark variant (mark + name white, url `#9bb2ec`).
- **Texture (optional):** the dotwave motif faint in a corner, or the signal glow. Depth, not clutter.

## Layout rules
- Headline anchored center-left, vertically a little above center. Generous margins (80px).
- ≤14 words. If it needs more, it's a `framework-blocks`, not a statement.
- Optional small attribution/context line under the headline in `--on-dark`/muted.
- Works at 1080×1350 (feed), 1080×1080 (square), 1200×630 (OG card) — scale type to width.

## HTML shell (complete, renderable — 1080×1350)

```html
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
  :root{--ink:#0b1020;--navy:#14254a;--accent:#3f5fb0;--signal:#3d6bff;--on-dark:#dfe5f3;}
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@1&display=swap');
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Plus Jakarta Sans',sans-serif;
       background:linear-gradient(160deg,#16294f 0%,#0b1020 62%);}
  body::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 45% at 80% 12%, rgba(61,107,255,0.40) 0%, transparent 60%);pointer-events:none;}
  .wrap{position:absolute;inset:0;padding:96px 80px;display:flex;flex-direction:column;}
  .kicker{font-size:19px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#7f9bff;}
  .spacer{flex:1;}
  .headline{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:96px;line-height:1.03;letter-spacing:-2.5px;color:#fff;}
  .headline em{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;color:#7f9bff;letter-spacing:-1px;}
  .rule{width:96px;height:6px;background:var(--signal);border-radius:3px;margin:38px 0 0;}
  .context{font-size:24px;font-weight:500;color:#aebdd6;margin-top:30px;max-width:760px;line-height:1.5;}
  .footer{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-weight:700;}
  .footer .who{display:flex;align-items:center;gap:11px;}
  .footer .nm{font-size:19px;color:#fff;letter-spacing:-0.01em;}
  .footer .url{font-size:16px;color:#9bb2ec;}
</style></head><body>
  <div class="wrap">
    <div class="kicker">AGENT ARCHITECTURE</div>
    <div class="spacer"></div>
    <div class="headline">Most AI failures aren't wrong answers.<br>They're exact work on the <em>wrong side of the line.</em></div>
    <div class="rule"></div>
    <div class="context">The fix is architecture, not a better prompt.</div>
    <div class="spacer"></div>
    <div class="footer">
      <div class="who">
        <svg viewBox="0 0 223 223" width="26" height="26" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#ffffff"/></svg>
        <span class="nm">Sidney Swift</span>
      </div>
      <span class="url">recoupable.com</span>
    </div>
  </div>
</body></html>
```

## Quality checklist
- [ ] Dark field, full saturation (no pale gradient); one signal glow/rule for depth
- [ ] Headline ≤14 words and is by far the biggest element
- [ ] Display (Space Grotesk) for punchy; serif italic only for deliberate quote moments
- [ ] One signal accent (rule or highlighted word) — not more
- [ ] Footer = mark + Sidney Swift · recoupable.com, white on dark
- [ ] Reads at thumbnail scale
