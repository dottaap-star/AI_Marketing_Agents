# Mailchimp: Create an API Key

1. In Mailchimp, click your profile icon, then **Account & billing**.
2. Go to **Extras > API keys**.
3. Click **Create A Key**, name it "hackathon", and copy it right away. It is shown only once.
4. Open `.env` in this folder and add a line: `MAILCHIMP_API_KEY=your-key-here`

No key access? Export instead: open a campaign, **View report > Download > CSV**, and drop the file into `data/`.

Then open Chat and pick **analytics-analyst**.

Try asking:

> Read data/campaign-report.csv. Which subject lines earned the best open rates, and why do you think that is?
