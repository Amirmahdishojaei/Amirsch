---
name: banana
description: Generate or edit images with Google's Gemini image model ("nano banana"). Use when the user runs /banana or asks to create, generate, or edit an image from a text prompt.
---

# /banana

Generate an image from the user's prompt (optionally editing an input image).

1. Require `GEMINI_API_KEY` in the environment. If it is missing, tell the user to set it; never ask them to paste it into a file, and never write it to disk or commit it.
2. Turn the request into a clear, descriptive prompt (subject, style, lighting, composition).
3. Run:
   `python3 .claude/skills/banana/scripts/generate.py "<prompt>" [-i input.png] [-o output.png]`
4. Report the saved file path and show the image if possible.
