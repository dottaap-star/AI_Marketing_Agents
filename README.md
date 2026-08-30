# Marketing Agents Starter

A ready-made team of 16 AI marketing agents that live inside VS Code. Open the folder, add one key, start building.

This is your toolkit for the AI Marketing Hackathon. The objective, word for word:

> "A complete campaign, and a live website experience in Grona it points at. Then 1,000 synthetic customers walk your funnel, ad to page to decision. Best conversion wins."

Schedule and judging are in [EVENT.md](EVENT.md). How to submit is in [SUBMIT.md](SUBMIT.md).

## Three steps to running

### Step 1: Get the folder

1. On this repo's page, click the green **Code** button, then **Download ZIP**.
2. Unzip it anywhere you like.
3. Open VS Code. Go to **File > Open Folder** and pick the unzipped folder.

You need VS Code 1.122 or newer. If yours is older, the agents will not show up. Update first.

### Step 2: Add your Gemini key

Keys are handed out at the door, one per person.

1. Open Chat in VS Code (the chat icon in the top bar).
2. In the Chat panel, click the gear icon and choose **Manage Language Models**. Or open the Command Palette and run **Chat: Manage Language Models**.
3. Click **Add Models**, choose **Gemini**, and paste your key.
4. Pick **gemini-3.7-flash (or gemini-3.1-pro-preview for advanced reasoning)** as your model.


The image, video, and audio tools read the same key from a file:

1. In the file list on the left, find `.env.example`.
2. Make a copy of it and rename the copy to `.env`.
3. Open `.env` and paste your key after `GEMINI_API_KEY=`.

The media tools need Python 3 on your machine. The video tool needs one extra install: run `pip install google-genai` in the terminal.

### Step 3: Talk to your first agent

1. Open Chat.
2. Click the agent picker, the dropdown at the top of the chat box.
3. Choose **brand-strategist** and say hello.

It will interview you and write your campaign brief. Every other agent reads that brief before doing anything, so this is always the right place to start.

## Your 16 agents

| Agent | What it does |
|---|---|
| brand-strategist | Interviews you, then writes the campaign brief every other agent reads. Start here. |
| campaign-builder | Turns the brief into a full channel plan with budgets and timing. |
| copy-studio | Writes headlines, landing page copy, and ad copy variants. |
| google-ads | Builds search campaigns: keywords, ad groups, responsive search ads. |
| meta-ads | Writes Facebook and Instagram ad sets that fit the format limits. |
| email-writer | Drafts email sequences, from welcome flows to launch announcements. |
| creative-director | Sets the visual direction and generates on-brief images. |
| report-maker | Packages your team's work into one clean, shareable report. |
| competitor-teardown | Dissects a competitor's site and finds the weak spots. |
| seo-auditor | Audits any page for search visibility and quick wins. |
| analytics-analyst | Reads data files you drop into `data/` and tells you the story inside them. |
| price-watch | Compares your pricing against competitor pages. |
| community-listener | Mines reviews and comments for the words customers actually use. |
| video-studio | Generates short video from a script. Needs `.env` and Python 3. |
| audio-studio | Generates voiceover and music. Needs `.env` and Python 3. |
| repurposer | Turns one strong piece into posts, threads, and snippets for every channel. |

## Slash prompts

Type `/` in the chat box to see these. They are quick one-shot helpers:

| Prompt | What it does |
|---|---|
| `/hooks` | 10 scroll-stopping opening lines for any topic. |
| `/rewrite-for` | Rewrites any copy for a different channel and its limits. |
| `/persona` | Builds a detailed buyer persona from your brief. |
| `/utm` | Builds correctly tagged campaign links so your analytics stay clean. |

## Troubleshooting

| Problem | Fix |
|---|---|
| Model returns 404 | That model name is retired. Use **gemini-3.7-flash** or **gemini-3.1-pro-preview**. |
| Agent picker is empty | Update VS Code to 1.122 or newer, then close and reopen the folder. |
| GEMINI_API_KEY missing | Copy `.env.example` to `.env` and paste your key inside it. |
| 429 errors | Wait a minute, the room shares capacity. The mentor desk has backup keys. |
| python not found | Install Python 3. On a Mac it is already there, just type `python3` instead of `python`. |

Stuck on anything else? Raise a hand. A mentor will come to you.

---

Built by the [Grona](https://grona.ai) team for the AI Marketing Hackathon, Riyadh, 30 August 2026.
Grona is agentic AI for your website: it reads what visitors do, rewrites the page, and ships the change.
