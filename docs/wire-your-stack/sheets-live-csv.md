# Google Sheets: A Live Data Feed

1. Open your sheet and go to **File > Share > Publish to web**.
2. Pick the tab you want and choose **Comma-separated values (.csv)**, not Web page.
3. Click **Publish** and copy the link.

That link is a live CSV. When the sheet changes, the link serves the new data. Agents can read it directly with #fetch, no download, no file in `data/` needed.

Then open Chat and pick **analytics-analyst**.

Try asking:

> #fetch <your-published-link> and summarize what changed since yesterday.
