"""The Vacuum's Alibi: one deadpan line from a robot vacuum.

The vacuum's excuse for a missed spot, written as a flat incident
report: it never admits fault, it cites its sensors instead.
"""

import os

# v2: same setup, sharper punch. "For safety" ended flat, so the
# reroute now ends on the vacuum refusing to argue with the
# building itself -- deadpan, smug, and the joke lands last.
LINE = (
    "I did not miss the spot. My lidar classified the crumbs as a "
    "load-bearing structure, so I rerouted around them. I do not "
    "argue with architecture."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
