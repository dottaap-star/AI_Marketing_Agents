---
description: Generate UTM-tagged URLs for a campaign as a markdown table
---

Generate UTM-tagged URLs for the campaign. The input provides a base URL and a channel list; if either is missing, ask for it before generating.

Apply one consistent naming convention:
- All values lowercase, words separated by hyphens, no spaces or special characters.
- utm_source: the platform (linkedin, instagram, x, facebook, google, newsletter).
- utm_medium: the traffic type (social, paid-social, cpc, email, referral).
- utm_campaign: one stable campaign slug reused across every URL, derived from the brief or the input.
- utm_content: what distinguishes this specific link (post-1, story, bio-link, ad-variant-a).

Output a markdown table with columns: Channel, Purpose, Full URL.
URL-encode values where needed and verify every row starts with the same base URL.
After the table, print the campaign slug on its own line so later batches can reuse it.
