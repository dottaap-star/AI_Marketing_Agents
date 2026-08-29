#!/usr/bin/env python3
"""Generate a short video clip with Gemini. Requires the google-genai package.

Usage: python3 tools/genvideo.py "prompt" [out.mp4]

Cost note: about $1 per 8-second clip, so write the prompt carefully before running.
"""
import base64
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import REPO_ROOT, read_key

try:
    from google import genai
except ImportError:
    sys.exit("The google-genai package is missing. Install it with: pip install google-genai")

POLL_SECONDS = 10
MAX_WAIT_SECONDS = 15 * 60


def default_out():
    out_dir = os.path.join(REPO_ROOT, "outputs", "creative")
    n = 1
    while True:
        path = os.path.join(out_dir, "video-{}.mp4".format(n))
        if not os.path.exists(path):
            return path
        n += 1


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 tools/genvideo.py "prompt" [out.mp4]')
    prompt = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else default_out()
    key = read_key()
    client = genai.Client(api_key=key)
    print("Starting video generation (about $1 per 8-second clip)...")
    ix = client.interactions.create(
        model="gemini-omni-1.1-flash",
        input=prompt,
        response_modalities=["video"],  # must be lowercase "video"
        background=True,
    )
    waited = 0
    while ix.status in ("in_progress", "queued"):
        if waited >= MAX_WAIT_SECONDS:
            print()
            sys.exit("Timed out after 15 minutes, last status: {}".format(ix.status))
        time.sleep(POLL_SECONDS)
        waited += POLL_SECONDS
        print(".", end="", flush=True)
        ix = client.interactions.get(ix.id)
    print()
    d = ix.model_dump(exclude_none=True)
    if ix.status != "completed":
        sys.exit("Generation failed, status: {}, error: {}".format(ix.status, d.get("error", "none")))
    video = d.get("output_video")
    if not video or "data" not in video:
        sys.exit("Completed but no video data in the response. Top-level keys: {}".format(list(d.keys())))
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(video["data"]))
    print("Saved {}".format(out_path))
    print("Reminder: each clip costs about $1 per 8 seconds, budget your runs.")


if __name__ == "__main__":
    main()
