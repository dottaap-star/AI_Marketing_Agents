# Marketing Agents Starter

A ready-made team of 16 AI marketing agents. Each one is a plain markdown file, so they work in VS Code, Cursor, Claude Code, Codex and any other AI tool that can read a folder. Bring the AI subscription you already have, open this folder and start.

Use it for a hackathon, a launch sprint or a normal Monday. At an event, the organiser's slides have the schedule, the rules and where to submit.

## Three steps to running

### Step 1: Get the folder

1. On this repo's page, click the green **Code** button, then **Download ZIP**.
2. Unzip it anywhere you like.

### Step 2: Open it in your AI tool

| You pay for | Use | How to start |
|---|---|---|
| ChatGPT Plus or Pro | [Codex](https://developers.openai.com/codex/ide) | Add the Codex extension to VS Code, or run `codex` in a terminal. Sign in with ChatGPT. |
| Claude Pro or Max | [Claude Code](https://code.claude.com/docs/en/setup) | Use the desktop app, the VS Code extension, or run `claude` in a terminal. Sign in with Claude. |
| Cursor | [Cursor](https://cursor.com) | Open the folder in Cursor and sign in. |
| GitHub Copilot | [VS Code](https://code.visualstudio.com/docs/copilot/setup) | Open the folder in VS Code and sign in with GitHub. |

No paid plan? Copilot and Cursor both have limited free tiers. Only use ChatGPT or Claude in a browser? See [No editor? Use chat](#no-editor-use-chat).

### Step 3: Talk to your first agent

Type this in your tool's chat:

```
use brand-strategist
```

It will interview you and write your campaign brief. Every other agent reads that brief before doing anything, so this is always the right place to start. In VS Code with Copilot you can also pick agents from the agent picker at the top of the chat box.

## Your 16 agents

Type `use` and the agent's name.

| Agent | What it does |
|---|---|
| brand-strategist | Interviews you, then writes the campaign brief every other agent reads. Start here. |
| campaign-builder | Turns the brief into a campaign plan: big idea, channel mix, 7-day calendar, budget split and KPIs. |
| copy-studio | Writes social copy: 5 LinkedIn posts, 5 Instagram captions, 3 X posts and 10 spare hooks. |
| google-ads | Builds a search campaign: 2 ad groups, counted headlines and descriptions, negative keywords. |
| meta-ads | Builds Meta ads: 3 angles by funnel stage, text and headlines, audiences and video hooks. |
| email-writer | Writes a 4-email launch sequence with A/B subject lines. |
| creative-director | Sets the visual direction and writes 6 image prompts. Generates the images if you add a key. |
| report-maker | Packages your team's work into one shareable HTML page. |
| competitor-teardown | Tears down up to 3 competitor sites and finds 3 gaps you can use. |
| seo-auditor | Audits your site's SEO and mobile speed, with a prioritised fix list. |
| analytics-analyst | Reads any export you drop into `data/`, explains it and recommends 3 actions. |
| price-watch | Snapshots competitor pricing and reports what changed since last time. |
| community-listener | Mines Reddit for customers' pains, objections and exact words. |
| video-studio | Writes 3 teaser concepts and a prompt. Generates the clip if you add a key. |
| audio-studio | Writes a 30-second ad read. Generates the voiceover if you add a key. |
| repurposer | Turns a recording in `data/` into a blog outline, 5 social posts and 1 email. |

## Helpers

Quick one-shot jobs. Type `use hooks`, for example.

| Helper | What it does |
|---|---|
| `hooks` | 10 scroll-stopping opening lines for any topic. |
| `rewrite-for` | Rewrites any copy for a different channel and its limits. |
| `persona` | Builds a detailed buyer persona from your brief. |
| `utm` | Builds correctly tagged campaign links so your analytics stay clean. |

Want to build your own agent? Start with `masterclass/build-your-first-agent.md`.

## Working as a team

Agree first, then split up. A first draft takes about a minute, so spend your time on decisions, not on drafting.

1. **Agree together.** Run `brand-strategist`, then `campaign-builder`. Read the results as a team. `brief/campaign-brief.md` and `outputs/positioning/campaign-plan.md` are now your shared plan.
2. **Share those two files.** Each person copies them into their own copy of this folder, or pastes them into their chat.
3. **Split by channel.** Each person takes different agents, such as `copy-studio`, `meta-ads`, `google-ads`, `email-writer` or `creative-director`. They write to different files, so nothing clashes.
4. **Bring it back.** Put everything in one shared folder, such as Google Drive or a repo, then run `report-maker` last.

To play agents off each other, use two chats or two people. One writes, the other attacks the result, and the writer answers. In a single chat, one AI plays both parts.

## No editor? Use chat

You can use the agents in ChatGPT or Claude in a browser.

1. Open `AGENTS.md`, `brief/campaign-brief.md` and the agent you want, for example `.github/agents/copy-studio.agent.md`.
2. Paste all three into one message and add this line: "You have no file access, so show everything in this chat instead of saving it."
3. Copy what you like into your team's shared folder.

Chat can't save files or run the tools in `tools/`, so you do the saving yourself.

## Images, video and voice (optional)

The agents write the concepts and prompts for you, and you can paste those into any image, video or voice tool you already have. To generate files from this folder instead, the scripts in `tools/` need your own Gemini API key:

1. Make a copy of `.env.example` and rename the copy to `.env`.
2. Open `.env` and paste your key after `GEMINI_API_KEY=`.
3. The tools need Python 3. The video tool also needs one install: run `pip install google-genai` in a terminal.

Video generation costs about $1 a clip on your key, so the agent asks first.

## Troubleshooting

| Problem | Fix |
|---|---|
| The tool doesn't find an agent | Use the exact name, like `use copy-studio`. Or say: read `.github/agents/copy-studio.agent.md` and follow it. |
| Agent picker is empty in VS Code | Update VS Code to 1.122 or newer, then close and reopen the folder. |
| Your tool asks permission to run or edit something | That's normal. Read it, and allow it if it stays inside this folder. |
| You hit your plan's limit | Wait for it to reset, or carry on from a teammate's account. |
| GEMINI_API_KEY missing | Only the `tools/` scripts need it. See [Images, video and voice](#images-video-and-voice-optional). |
| python not found | Install Python 3. On a Mac, type `python3` instead of `python`. |

---

Built by the [Grona](https://grona.ai) team.
