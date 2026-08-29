# Build Your First Agent

This is the self-serve version of the live masterclass exercise. You will build the "headline roaster": an agent that fetches a landing page, roasts its hero headline, and rewrites it 10 ways. It takes about 10 minutes.

## First, the secret

An agent is just a markdown file. That is the whole trick.

- The **description** at the top tells VS Code when to use it and what to show in the agent picker.
- The **body** is its standing instructions: what it always does, every time, without you re-explaining.

Every agent in `.github/agents/` works this way. Once you can edit a markdown file, you can build agents.

## The steps

1. **Copy the template.** In the file list on the left, right-click `masterclass/template.agent.md` and choose Copy. Right-click the `.github/agents/` folder and choose Paste. Rename the pasted file to `headline-roaster.agent.md`.

2. **Edit the three marked lines.** Open your new file. There are three spots marked EDIT ME:
   - EDIT ME 1: the description, one sentence saying what the agent does.
   - EDIT ME 2: the mission paragraph, the agent's personality and job.
   - EDIT ME 3: the output path, where it saves its work.

   The template is prefilled and already works. Change a word or two so it feels like yours, or leave it as-is for the first run.

3. **Reload the window.** Open the Command Palette (Cmd+Shift+P on Mac, Ctrl+Shift+P on Windows) and run **Developer: Reload Window**. VS Code re-reads the agents folder on reload.

4. **Pick it.** Open Chat, click the agent picker at the top of the chat box, and choose **headline-roaster**.

5. **Point it at your landing page.** Paste your Grona page URL and hit enter. Watch it fetch the page, roast the headline, and save 10 rewrites into `outputs/research/`.

## What just happened

You gave a model a job description and a place to file its work. That is agent building. The 30-point "quality of your agent" judging category is scored on exactly this kind of file, run against a brief you have never seen. So the sharper and more specific your agent's instructions, the better it performs without you in the room.

## Where to go next

- `masterclass/10-ideas.md`: ten agent ideas, tagged by difficulty.
- `masterclass/stretch-social-agents.md`: the stretch challenge, build an agent that can see social media.
