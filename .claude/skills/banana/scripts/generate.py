#!/usr/bin/env python3
"""Generate/edit an image via the Gemini API. Key comes from GEMINI_API_KEY."""
import argparse, base64, json, mimetypes, os, sys, urllib.request

MODEL = os.environ.get("BANANA_MODEL", "gemini-2.5-flash-image")

p = argparse.ArgumentParser()
p.add_argument("prompt")
p.add_argument("-i", "--input", help="optional image to edit")
p.add_argument("-o", "--output", default="banana.png")
a = p.parse_args()

key = os.environ.get("GEMINI_API_KEY")
if not key:
    sys.exit("GEMINI_API_KEY is not set")

parts = [{"text": a.prompt}]
if a.input:
    mime = mimetypes.guess_type(a.input)[0] or "image/png"
    with open(a.input, "rb") as f:
        parts.append({"inline_data": {"mime_type": mime,
                                      "data": base64.b64encode(f.read()).decode()}})

req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
    data=json.dumps({"contents": [{"parts": parts}]}).encode(),
    headers={"Content-Type": "application/json", "x-goog-api-key": key},
)
with urllib.request.urlopen(req) as r:
    resp = json.load(r)

for part in resp["candidates"][0]["content"]["parts"]:
    d = part.get("inlineData") or part.get("inline_data")
    if d:
        with open(a.output, "wb") as f:
            f.write(base64.b64decode(d["data"]))
        print(a.output)
        sys.exit(0)
sys.exit("No image returned: " + json.dumps(resp)[:500])
