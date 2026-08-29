#!/usr/bin/env python3
"""Generate an image with Gemini. Stdlib only.

Usage: python3 tools/genimage.py "prompt" [out.png]
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import REPO_ROOT, http_json, read_key

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent"


def default_out():
    out_dir = os.path.join(REPO_ROOT, "outputs", "creative")
    n = 1
    while True:
        path = os.path.join(out_dir, "image-{}.png".format(n))
        if not os.path.exists(path):
            return path
        n += 1


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 tools/genimage.py "prompt" [out.png]')
    prompt = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else default_out()
    key = read_key()
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    print("Generating image...")
    resp = http_json(URL, payload, key)
    data = None
    try:
        for part in resp["candidates"][0]["content"]["parts"]:
            if "inlineData" in part:
                data = part["inlineData"]["data"]
                break
    except (KeyError, IndexError):
        pass
    if data is None:
        sys.exit("No image in the response. Try rephrasing the prompt.")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(data))
    print("Saved {}".format(out_path))
    print("Reminder: each image costs about $0.07, so iterate on the prompt in text first.")


if __name__ == "__main__":
    main()
