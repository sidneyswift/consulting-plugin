---
name: consulting-content-extraction
description: Extract reusable content, insights, and knowledge-base entries from a call transcript or meeting note. Use whenever a new transcript lands in content/raw/ or a client's meetings/ folder, after any client/sales call, or when the user says "extract content", "mine this call", "turn this into posts/insights". Powers the content flywheel ("never answer the same question twice").
---

# Consulting Content Extraction

Turn a raw transcript into compounding assets.

## When to run
Automatically after any new transcript is saved (content/raw/ or clients/{client}/meetings/), or on request.

## Steps
1. Read the transcript.
2. Extract and output, grouped:
   - Quotable insights shared about AI/consulting
   - Useful analogies or frameworks used
   - Industry-specific examples given
   - Questions that revealed deep insight
   - Moments that reframed the client's thinking
3. Format each as a candidate LinkedIn post or blog topic.
4. Deposit results:
   - Reusable explanations → `knowledge/insights/`
   - Post/blog candidates → `content/ideas/`
   - Recurring question already answered before → `knowledge/faqs/`
5. If the same topic now appears 2+ times, flag it as a strong content piece.
