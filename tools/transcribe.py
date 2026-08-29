#!/usr/bin/env python3
"""Transcribe an audio recording with Gemini. Stdlib only.

Usage: python3 tools/transcribe.py data/recording.mp3 [out.md]
"""
import base64
import mimetypes
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import REPO_ROOT, http_json, read_key

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent"
MAX_BYTES = 15 * 1024 * 1024
PROMPT = "Transcribe this recording verbatim. Then add a section listing the 5 key points."


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 tools/transcribe.py data/recording.mp3 [out.md]")
    in_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(REPO_ROOT, "outputs", "research", "transcript.md")
    if not os.path.exists(in_path):
        sys.exit("File not found: {}".format(in_path))
    size = os.path.getsize(in_path)
    if size > MAX_BYTES:
        sys.exit("File is {:.1f}MB, the inline limit is 15MB. Trim or compress the recording first.".format(size / (1024.0 * 1024.0)))
    mime = mimetypes.guess_type(in_path)[0] or "audio/mpeg"
    with open(in_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    key = read_key()
    payload = {
        "contents": [{
            "parts": [
                {"inlineData": {"mimeType": mime, "data": b64}},
                {"text": PROMPT},
            ]
        }]
    }
    print("Transcribing {} ({:.1f}MB)...".format(in_path, size / (1024.0 * 1024.0)))
    resp = http_json(URL, payload, key)
    try:
        parts = resp["candidates"][0]["content"]["parts"]
        text = "\n".join(p["text"] for p in parts if "text" in p)
    except (KeyError, IndexError):
        text = ""
    if not text:
        sys.exit("No text in the response. Check that the file is a supported audio format.")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved {}".format(out_path))


if __name__ == "__main__":
    main()
