---
name: consulting-linkedin-publisher
description: Turn a consulting insight or content draft into a published or scheduled LinkedIn post. Use on "post this to LinkedIn", "publish my draft", "schedule a LinkedIn post", or after consulting-content-drafter produces a draft. Publishes via Postbridge.
---

# Consulting LinkedIn Publisher

Ship content from the flywheel to LinkedIn. The off-ramp of `content/` → distribution.

## Steps
1. **Pick the source.** A draft in `content/03-drafts/`, an insight in `knowledge/insights/`, or text
   the user gives. If it's an insight (not yet post-shaped), run `consulting-content-drafter` first.
2. **Shape for LinkedIn.** Hook in line 1, short lines, one idea, soft CTA. Keep the practice's
   positioning (see `positioning/`). No hashtag spam.
3. **Choose the account.** `sidney` (id 34429, default — personal authority) or `recoupable`
   (id 34430 — company). Confirm if ambiguous.
4. **Publish.** Save the final caption to a file, then run:
   `python integrations/linkedin/_work/publish.py --caption-file <file> --account sidney`
   Add `--schedule <ISO-UTC>` to schedule, or `--draft` to stage. The script confirms before sending.
   - **Attach media** with `--media <path>` (repeatable): `.png`/`.jpg` image, `.mp4`/`.mov` video, or a
     `.pdf` to ship a swipeable LinkedIn document/carousel (the highest-dwell format; add `--document-title`).
   - **Animated post?** Postbridge takes **no `.gif`** — render/convert to an MP4 loop first with
     `python integrations/linkedin/_work/make_loop.py <clip-or.gif> [--pad]`, then attach the `-loop.mp4`.
     For a *literal* GIF, upload it by hand in the LinkedIn composer (<5MB). Full playbook:
     `knowledge/sops/animated-media-for-posts-and-article-headers.md`.
5. **Log it.** Write the published post + timestamp + account to `integrations/linkedin/published/`
   and move the source from `content/03-drafts/` → `content/04-published/`.
6. **Close the loop.** Note the post URL so `consulting-linkedin-audience` can pull its engagement later.

Never auto-send without the user's go-ahead on the final copy.
