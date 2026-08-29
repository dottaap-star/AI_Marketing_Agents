"""Shared helpers for the marketing-agents-starter tools."""
import json
import os
import sys
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_key():
    """Return the Gemini API key from the environment or the .env file at repo root."""
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if key:
        return key
    env_path = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                name, _, value = line.partition("=")
                if name.strip() == "GEMINI_API_KEY":
                    value = value.strip().strip('"').strip("'")
                    if value:
                        return value
    sys.exit("No GEMINI_API_KEY found: copy .env.example to .env and paste your key from the handout card.")


def http_json(url, payload, key):
    """POST payload as JSON to url with the API key header, return the parsed JSON response."""
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            message = json.loads(body)["error"]["message"]
        except Exception:
            message = body[:500]
        raise RuntimeError("API error {}: {}".format(e.code, message)) from None
