#!/usr/bin/env python3
"""Write the funniest cat voicemail greeting to /output/entry.txt."""

import os

ENTRY = "You've reached Miso. I'm asleep in a box and you woke me up. Leave a message \u2014 I'll knock it off the shelf at 4 a.m."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
