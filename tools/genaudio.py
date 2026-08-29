#!/usr/bin/env python3
"""Generate spoken audio with Gemini TTS. Stdlib only.

Usage: python3 tools/genaudio.py "text to speak" [out.wav] [--voice Kore]
"""
import base64
import os
import sys
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import REPO_ROOT, http_json, read_key

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent"
RATE = 24000  # response is raw PCM, 16-bit little-endian mono at 24000 Hz


def default_out():
    out_dir = os.path.join(REPO_ROOT, "outputs", "creative")
    n = 1
    while True:
        path = os.path.join(out_dir, "audio-{}.wav".format(n))
        if not os.path.exists(path):
            return path
        n += 1


def main():
    args = sys.argv[1:]
    voice = "Kore"
    if "--voice" in args:
        i = args.index("--voice")
        if i + 1 >= len(args):
            sys.exit("--voice needs a value, for example: --voice Kore")
        voice = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit('Usage: python3 tools/genaudio.py "text to speak" [out.wav] [--voice Kore]')
    text = args[0]
    out_path = args[1] if len(args) > 1 else default_out()
    key = read_key()
    payload = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    print("Generating audio with voice {}...".format(voice))
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
        sys.exit("No audio in the response. Try shorter text or a different voice.")
    pcm = base64.b64decode(data)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with wave.open(out_path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(RATE)
        wf.writeframes(pcm)
    duration = len(pcm) / (2.0 * RATE)
    print("Saved {} ({:.1f} seconds)".format(out_path, duration))


if __name__ == "__main__":
    main()
