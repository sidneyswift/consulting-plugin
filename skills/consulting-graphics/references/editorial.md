# Template: Editorial (minimal)

The restrained, premium option — a quiet serif headline on a crisp light field. **One choice in the
kit, not the default.** Reach for it when the *content* wants calm authority (a reflective essay
thumbnail, a single sober quote), not when you're defaulting. A whole feed of these is what made the
old system forgettable, so use it sparingly and mix it with the bolder templates. Uses the shared DNA
in `consulting-tasteful-design` (`DESIGN.md`).

> This replaces the old `elegant-founder` template. Key change: **no pale washed-out gradient** (that's
> on the anti-slop list). Editorial is now *crisp* light (clean `--paper`/`--tint`), not a faded blue
> haze — minimal, but still committed and on-brand.

## Visual identity
- **Field:** crisp light — flat `--paper` (`#ffffff`) or a very subtle `--tint` panel. No multi-stop
  pale gradient. Calm, lots of air, but a clear focal line.
- **Headline:** `Instrument Serif` italic, `--ink`/`--navy`, large (66–84px). This is the one template
  where the serif leads — that's its whole identity.
- **Supporting text:** `Plus Jakarta Sans` 500, `--mute`, noticeably quieter than the headline.
- **One restraint-friendly accent:** a single short `--accent` (not `--signal`) rule or a small kicker
  label. Keep it whisper-quiet — energy is not this template's job.
- **Footer:** the standard mark + `Sidney Swift` · `recoupable.com` (see DESIGN.md), light variant.

## Layout rules
- Content anchored upper-third to center, generous left margin (80px). Left-aligned.
- Headline ≤ ~12 words; let the air do the work. This is the *only* place "lots of empty" is on-brand
  (because the type is doing something deliberate), but it must still have a clear focal line, never a
  blank washed-out field.
- Works at 1200×630 (OG card), 1080×1350 (feed), 1080×1080 (square).

## HTML shell (complete, renderable — 1200×630 OG card)

```html
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
  :root{--ink:#0b1020;--navy:#14254a;--accent:#3f5fb0;--mute:#6b7d8f;--paper:#ffffff;--tint:#f3f6fc;}
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1200px;height:630px;position:relative;overflow:hidden;background:var(--paper);font-family:'Plus Jakarta Sans',sans-serif;padding:80px;}
  .kicker{font-size:15px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--accent);}
  .headline{font-family:'Instrument Serif',serif;font-style:italic;font-size:78px;line-height:1.05;letter-spacing:-1px;color:var(--ink);margin-top:18px;max-width:980px;}
  .sub{font-size:23px;font-weight:500;color:var(--mute);margin-top:26px;max-width:760px;line-height:1.5;}
  .footer{position:absolute;bottom:48px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-weight:700;}
  .footer .who{display:flex;align-items:center;gap:11px;}
  .footer .nm{font-size:18px;color:var(--ink);letter-spacing:-0.01em;}
  .footer .url{font-size:15px;color:#8aa0b6;}
</style></head><body>
  <div class="kicker">AGENT ARCHITECTURE</div>
  <div class="headline">Wrong side of the line.</div>
  <div class="sub">Why most AI reliability failures aren't wrong answers — and why the fix is architecture, not prompting.</div>
  <div class="footer">
    <div class="who">
      <svg viewBox="0 0 223 223" width="24" height="24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#0b1020"/></svg>
      <span class="nm">Sidney Swift</span>
    </div>
    <span class="url">recoupable.com</span>
  </div>
</body></html>
```

## Quality checklist
- [ ] Crisp light field — **no** pale multi-stop gradient (anti-slop)
- [ ] Instrument Serif italic headline leads; it's the focal element
- [ ] Supporting text clearly quieter; at most one quiet `--accent` mark
- [ ] Footer = mark + Sidney Swift · recoupable.com
- [ ] Used sparingly and mixed with bolder templates across a series (not the default)
