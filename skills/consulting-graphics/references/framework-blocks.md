# Template: Framework Blocks

The "save this" teaching infographic — a named framework or numbered list, color-coded, with worked
detail. This is the reach + lead-magnet engine (people screenshot and re-share reference assets).
Bold, scannable, confident. Uses the shared brand DNA in `consulting-tasteful-design` (`DESIGN.md`).

## Visual identity
- **Field:** light (`--paper`) body with a full-bleed **dark navy header band** (`--navy`/`--ink`) up top.
  The dark band is the brand signature and the contrast that makes it pop in-feed.
- **Headline:** `Space Grotesk` 700, white, large (60–78px on 1080). Pattern: `How to {specific outcome}`
  with an optional muted parenthetical subtitle, exactly like a great reference card.
- **Blocks:** white cards on the light field, each with a **colored number chip** that cycles through
  `--accent → --signal → --navy` for rhythm (color-coded, but all in the blue family — never rainbow).
- **One signal pop:** the `Fix:`/payoff line uses `--signal` for the eye-hit.
- **Footer:** the standard mark + `Sidney Swift` · `recoupable.com` (see DESIGN.md).

## Layout rules
- Header band ~30–38% of height. Body cards fill the rest with even gaps (22–28px).
- 3 blocks is the sweet spot; 4 max. More than 4 → split into a carousel (one idea per slide).
- Each block: big number chip · bold title (28–32px) · plain-language line (`--mute`) · `Fix:` payoff.
- Keep one idea per block. If a block needs two sentences of setup, it's two blocks.
- An optional closing italic `Instrument Serif` line under the blocks = the takeaway.

## Acronym variant (the mnemonic infographic)

When the framework is a **named acronym** (PLACE, STORM — see `positioning/swipe/posts/magali-dereu/ANALYSIS.md`),
swap the vertical numbered blocks for a horizontal **letter row**: each big `Space Grotesk` letter in
its own column with a label + one-line description, in a single white card on the light field. Add an
**"Examples"** band below with 2–3 **worked examples** (real ones, with a proof number where you have
it) in cards whose left edge cycles `--accent → --signal → --navy`. Same dark header band, same footer.
This is the highest-leverage "save this" lead-magnet format — a mini version of what Sid sells.
(Keep it on-brand: navy/blue tokens, not the warm-orange palette of the swipe source.)

## HTML shell (complete, renderable — 1080×1350)

```html
<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
  :root{--ink:#0b1020;--navy:#14254a;--accent:#3f5fb0;--signal:#3d6bff;--tint:#f3f6fc;--hairline:#e3e9f5;--paper:#fff;--mute:#6b7d8f;}
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@1&display=swap');
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--paper);font-family:'Plus Jakarta Sans',sans-serif;color:var(--ink);}
  .band{background:var(--navy);padding:64px 72px 56px;position:relative;overflow:hidden;}
  .band::after{content:'';position:absolute;right:-80px;top:-80px;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(61,107,255,0.45),transparent 68%);} /* signal glow, subtle depth */
  .kicker{font-size:18px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#7f9bff;}
  .headline{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:70px;line-height:1.02;letter-spacing:-1.5px;color:#fff;margin-top:18px;}
  .sub{font-size:23px;font-weight:500;color:#aebdd6;margin-top:20px;max-width:840px;}
  .body{padding:46px 72px 0;display:flex;flex-direction:column;gap:24px;}
  .block{display:flex;gap:26px;align-items:flex-start;background:var(--paper);border:1px solid var(--hairline);border-radius:22px;padding:30px 34px;box-shadow:0 10px 30px rgba(20,37,74,0.05);}
  .chip{flex:none;width:62px;height:62px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-weight:700;font-size:32px;color:#fff;}
  .b1 .chip{background:var(--accent);} .b2 .chip{background:var(--signal);} .b3 .chip{background:var(--navy);}
  .b-title{font-size:30px;font-weight:800;letter-spacing:-0.01em;}
  .b-line{font-size:21px;color:var(--mute);margin-top:5px;line-height:1.4;}
  .b-fix{font-size:21px;font-weight:700;margin-top:13px;}
  .b-fix span{color:var(--signal);}
  .close{font-family:'Instrument Serif',serif;font-style:italic;font-size:38px;color:var(--navy);padding:40px 72px 0;}
  .footer{position:absolute;bottom:48px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;font-weight:700;}
  .footer .who{display:flex;align-items:center;gap:11px;}
  .footer .nm{font-size:19px;color:var(--ink);letter-spacing:-0.01em;}
  .footer .url{font-size:16px;color:#8aa0b6;}
</style></head><body>
  <div class="band">
    <div class="kicker">AI AGENTS · MUSIC &amp; MEDIA</div>
    <div class="headline">Why AI agents stall<br>(and how to clear each block)</div>
    <div class="sub">Three things stop most teams. None of them is the model.</div>
  </div>
  <div class="body">
    <div class="block b1"><div class="chip">1</div><div>
      <div class="b-title">Data</div>
      <div class="b-line">Your data isn't ready for agents to use.</div>
      <div class="b-fix"><span>Fix:</span> make it agent-readable — clean, connected, permissioned.</div>
    </div></div>
    <div class="block b2"><div class="chip">2</div><div>
      <div class="b-title">Process</div>
      <div class="b-line">Your processes block fast iteration.</div>
      <div class="b-fix"><span>Fix:</span> map the workflow, remove the approval steps an agent can own.</div>
    </div></div>
    <div class="block b3"><div class="chip">3</div><div>
      <div class="b-title">People</div>
      <div class="b-line">Your team is too busy to up-skill.</div>
      <div class="b-fix"><span>Fix:</span> ship one shared agent the whole team actually uses.</div>
    </div></div>
  </div>
  <div class="close">Own the capability, not just the experiment.</div>
  <div class="footer">
    <div class="who">
      <svg viewBox="0 0 223 223" width="26" height="26" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#0b1020"/></svg>
      <span class="nm">Sidney Swift</span>
    </div>
    <span class="url">recoupable.com</span>
  </div>
</body></html>
```

## Quality checklist
- [ ] Dark header band present; headline is the biggest thing and reads as a thumbnail
- [ ] 3 (max 4) blocks, one idea each; number chips color-cycle accent→signal→navy
- [ ] Exactly one `--signal` pop per block (the Fix line) — not rainbow
- [ ] Plain-language problem line + a concrete, specific fix (no fluff verbs)
- [ ] Footer = mark + Sidney Swift · recoupable.com (from DESIGN.md)
- [ ] Renders clean at 1080×1350 and legible small
