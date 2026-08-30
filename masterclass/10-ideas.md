# 10 Agent Ideas

Built the headline roaster? Here are ten more, tagged by difficulty. Each one is a single markdown file in `.github/agents/`, exactly like the one you just made. The mechanism hint tells you the core trick.

1. **Price-comparison watcher** (stretch). Checks competitor pricing pages against yours and reports changes. Hint: scheduled tools come later, start by running it manually each time and let it compare against its last saved report.

2. **Review miner** (easy). Digs through app store or Google reviews for patterns, complaints, and quotable praise. Hint: paste the reviews into a file in `data/` and point the agent at it.

3. **UGC brief generator** (easy). Turns your campaign brief into shot-by-shot briefs for user-generated content creators. Hint: it reads `brief/campaign-brief.md` and outputs one brief per creator style.

4. **Influencer scout** (medium). Profiles potential collaborators from their public pages. Hint: use #fetch on public profile and press pages, then score fit against your brief.

5. **SEO content-gap finder** (medium). Finds topics one competitor ranks for that you do not cover. Hint: fetch their blog index and sitemap, compare against your own page list.

6. **Weekly analytics narrator** (medium). Turns a GA4 export into a story a CEO would actually read. Hint: drop the export in `data/`, see `docs/wire-your-stack/ga4-export.md`.

7. **Objection handler** (easy). Drafts calm, specific replies to the sales objections you hear most. Hint: give it your brief plus a pasted list of real objections, one reply per objection.

8. **Launch-day checklist runner** (easy). Walks your team through launch morning item by item, checking off what is done. Hint: the checklist lives in the agent's own instructions, it asks about one item at a time.

9. **Arabic-English localizer** (medium). Translates campaign copy both directions while keeping brand voice, not dictionary voice. Hint: feed it your tone words and two example posts as the voice reference.

10. **Lead qualifier** (medium). Scores inbound messages as hot, warm, or cold with a reason. Hint: paste the messages into a file in `data/`, define the scoring rules in the agent body.

## Go deeper (after the hackathon)

Two research directions once agents feel easy:

- **Loop engineering**: agents that check their own work and go again until it passes.
  Search: reflection loops, evaluator-optimizer pattern, Anthropic "Building Effective Agents".
- **Agent graphs**: whole teams of agents wired as a looping graph, where nodes are agents
  and edges route the work between them. This is the current production frontier.
  Search: LangGraph, graph-based agent orchestration, cyclic agent graphs.
