# Workspace Conventions

This is a marketing campaign workspace. A team of marketers uses it to plan, write, and ship a complete campaign. These rules apply to every agent and every chat in this folder.

## Before creating anything

Always read `brief/campaign-brief.md` first. It is the single source of truth for the product, audience, promise, proof, conversion goal, and tone. If it is empty or still the template, fall back to `brief/example-brief.md` and say clearly that you are working from the example.

## Where work goes

Write outputs into `outputs/<area>/` as markdown files. Areas: `ads`, `creative`, `email`, `positioning`, `report`, `research`, `social`. Use kebab-case filenames, for example `outputs/ads/google-search-v1.md`.

## Writing rules

- Never use em dashes in generated content. Use commas, colons, periods, or hyphens instead.
- Keep copy concrete and specific to the brief. Name the audience, use the proof points, aim at the one conversion goal.
- No generic marketing filler. If a sentence could sell any product, cut it or sharpen it.

## When things break

When a tool script fails, show the user the exact command you ran and the exact error message. Do not summarize the error away, they need it to get help fast.
