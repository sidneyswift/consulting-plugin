---
name: consulting-linkedin-audience
description: Turn LinkedIn engagement into leads. Use on "who engaged with my post", "pull LinkedIn leads", "find warm leads from LinkedIn", or after a post gets traction. Pulls reactors/commenters via Apify and cross-references Attio to surface engaged-but-not-in-CRM outreach candidates.
---

# Consulting LinkedIn Audience

Social selling: mine post engagement for warm leads and feed them into the pipeline.

## Steps
1. **Pull engagement.** For a post URL, run:
   `python integrations/linkedin/_work/pull_engagement.py --post-url "<url>"`
   → writes normalized engaged people (name, headline, profile URL) to
   `integrations/linkedin/engagement/<date>-engagement.json`. (Apify run = pay-per-result.)
2. **Cross-reference Attio (live).** For each engaged person, check if they already exist in Attio
   (`POST /v2/objects/people/records/query` by name/handle). Split into: **already a contact** vs.
   **new** vs. **existing product-user**.
3. **Score & prioritize.** Rank by fit to the ICP (`positioning/`) — title/seniority, company in a
   target account (`integrations/attio/` Target Accounts list), and engagement depth (comment > like).
4. **Act.**
   - New high-fit people → create an Attio person (`relationship = lead`) and draft outreach in Sid's
     voice (`consulting-email-voice` for email, `consulting-linkedin-engage` for a LinkedIn DM),
     grounded in the post they engaged with.
   - Existing contacts who re-engaged → flag for `consulting-followup-sequencer`.
5. **Record.** Save the ranked candidate list to `integrations/linkedin/engagement/` and note any
   new Attio records created.

Don't mass-add scraped people to Attio as "lead" — only real, qualified-fit people. Keep the CRM clean.
