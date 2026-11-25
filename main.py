#!/usr/bin/env python3
"""Family Scene - make.fun bounty entry.

Writes one short family scene (a single line, at most 280 characters)
to /output/entry.txt, where the bounty grader reads it.

The scene: Dad reads the bedtime story in three voices, and his little
son, who knows the story by heart, whispers the dragon's line when Dad
forgets it - then corrects Dad's accent. Warm, funny, heartfelt, and
specific, the way the judge brief asks.

Deterministic by design: no randomness, no clock, no network, no input
from the environment. Every run writes the exact same bytes.

Run: python3 main.py
"""

import os

SCENE = (
    "Every night Dad reads the bedtime story in three voices, and when he "
    "forgets the dragon's line, my little brother whispers it for him — "
    "then corrects his accent."
)

OUTPUT_PATH = "/output/entry.txt"


def build_scene() -> str:
    """Return the entry scene, checked against the bounty gate."""
    text = SCENE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"scene is {len(text)} chars, gate needs 1-280")
    if "\n" in text or "\r" in text:
        raise ValueError("scene must fit on one line")
    if text != text.strip():
        raise ValueError("scene must not start or end with whitespace")
    return text


def main() -> int:
    scene = build_scene()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(scene + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
