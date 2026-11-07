# Stretch Challenge: An Agent That Can See Social

Here is an honest limitation: none of the built-in agents can see inside LinkedIn, Instagram, or TikTok. Those platforms are logged-in walled gardens, and a plain URL fetch bounces off them.

Your stretch goal: design an agent that can.

There are three doors in. Pick one.

## Door 1: Exports

The platforms will hand you your own data if you ask through the right menu. LinkedIn page admins can export analytics as an XLS file from the page's Analytics tab. Drop the file into `data/` and your agent reads it like any other file. Hint: the analytics-analyst agent already shows the pattern for reading files from `data/`.

## Door 2: Scraping tools

An Apify MCP connection is already wired into `.vscode/mcp.json`. It gives agents real scraping actors for public social pages. You need your own Apify token and runs cost money, so test with one profile before running a list.

## Door 3: The paste route

Do not underestimate this one. Copy 20 posts from any profile into a file in `data/`. That IS a data source. An agent that reads 20 real posts and extracts the hooks, formats, and posting patterns is genuinely useful, and you can build it in 15 minutes with zero tokens and zero permissions.

## Why bother

Whoever ships a working social agent has designed a real product feature, the kind teams pay for.
