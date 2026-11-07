# How to Use, Improve and Combine the Agents

Every agent here is a plain text file of instructions. That is why they work almost anywhere, and why you can change them. This guide covers three things: running them, making them better, and getting them to work together.

Start with `use brand-strategist`. Every other agent reads the brief it writes.

## 1. Use them

### In Claude or ChatGPT (nothing to install)

Good for trying one agent, or if you have never opened a code editor.

1. Open `AGENTS.md`, `brief/campaign-brief.md` and the agent you want, for example `.github/agents/meta-ads.agent.md`.
2. Paste all three into one message, or add them to a Claude or ChatGPT project so you only do it once.
3. Add this line: "You have no file access, so show everything in this chat instead of saving it."
4. Copy what you like into your own document.

Chat can't save files or run the scripts in `tools/`, so you do the saving yourself.

### In Claude Code

Use the desktop app, the VS Code extension, or run `claude` in a terminal. You need a paid Claude plan.

1. Open this folder.
2. Type `use brand-strategist`.

Claude Code reads `CLAUDE.md`, which points it at the rules in `AGENTS.md`. Files land in `outputs/`.

### In an IDE (VS Code, Cursor) or with Codex

1. Open this folder in VS Code or Cursor. For Codex, add the extension to VS Code or run `codex` in a terminal.
2. Sign in with the AI subscription you already have.
3. Type `use brand-strategist`.

In VS Code with Copilot you can also pick agents from the agent picker at the top of the chat box.

Your tool may ask permission to run or edit something. That's normal. Read it, and allow it if it stays inside this folder.

## 2. Improve them

An agent gets better the same way a new hire does: you correct it, and the correction sticks. So when the output is wrong, fix the instruction as well as the output.

- **Change one agent:** open its file in `.github/agents/` and edit it. Plain English is all it takes. You can also ask your AI: "Update `.github/agents/meta-ads.agent.md` so it never uses exclamation marks."
- **Change every agent:** add a rule to `AGENTS.md`. Every agent reads it before starting.
- **Give it better material:** put real customer quotes, reviews or exports in `data/`, and name the file in your prompt.
- **Sharpen the brief:** most weak output comes from a weak brief. Every agent reads `brief/campaign-brief.md`, so one better sentence there improves everything downstream.
- **Clear what's marked [ASSUMED]:** agents tag claims they can't back up, and later agents may drop them. Replace each tag with something true.
- **Build your own:** `masterclass/build-your-first-agent.md` takes about 10 minutes. Or ask your AI: "Create a new agent at `.github/agents/review-miner.agent.md`, based on `masterclass/template.agent.md`, that finds the top complaints in `data/reviews.md`."

## 3. Combine them

Agents share work through files. One writes a file, the next one reads it. Nothing is hidden, and you can open or edit anything between steps.

**The relay.** Run them one after another:

```
use brand-strategist
use campaign-builder
use landing-page
use meta-ads
use report-maker
```

**The fan-out.** Once the brief and plan are agreed, agents can run at the same time because they write to different files. Open several chats, or split them across teammates:

```
use landing-page
use copy-studio
use google-ads
use email-writer
```

Each teammate needs the same `brief/campaign-brief.md` and `outputs/positioning/campaign-plan.md`. Put everything in one shared folder at the end, then run `use preflight` and `use report-maker`.

## 4. Play them off each other

One agent writes and another attacks. Run the attacker in a fresh chat or on a teammate's laptop, so it reads the work cold, without knowing what the writer was thinking.

**Writer against critic.** The basic move.

1. `use landing-page`
2. In a fresh chat: `use buyer-panel`
3. Read the objections and decide which are fair. Then, in a fresh chat: "use landing-page. Read `outputs/research/buyer-panel.md` and fix the two objections I agree with."

**The rival's reply.** Find out how a competitor would respond.

1. `use competitor-teardown`
2. In a fresh chat: "Read `outputs/research/competitor-teardown.md` and `outputs/website/landing-page.md`. You run marketing at our biggest rival. Write your response to this launch."
3. Use their best attack to find your weakest claim.

**The budget fight.** Make your channels argue.

1. `use google-ads`, then `use meta-ads`
2. In a fresh chat: "Read both files in `outputs/ads/`. Each channel gets one paragraph arguing for the whole budget. Then use campaign-builder to decide the split and explain why."

**Your own critic.** Build an agent that plays your hardest customer, using the steps in section 2, then point it at anything you write.

Two rules for every fight:

- **You decide.** A critic finds problems, but rewrites aren't always better. They can water down your best line, so check your promise and your proof survive.
- **Stop when the objections repeat.** Two rounds usually show you what matters.
