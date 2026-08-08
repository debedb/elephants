#!/usr/bin/env python3
"""
Draw the adjudication sample.

Uniform random draw over every row of one named export of the Trump Action
Tracker dataset, with a published seed. The output of this script is committed
before any adjudication begins, so that the draw is verifiable from git history
and no drawn row can be quietly dropped for coming out inconveniently.

The dataset itself is not mirrored into this repository. Point this script at a
local copy of the export obtained from trumpactiontracker.info.

Usage:
    python3 draw-sample.py <path-to-export.csv> [--seed N] [--n N]
"""

import argparse
import csv
import hashlib
import io
import json
import os
import random
import sys

DEFAULT_SEED = 1729
DEFAULT_N = 30
EXPORT_NAME = "trump-actions-6-26-26.csv"
SOURCE_CREDIT = "Trump Action Tracker, Christina Pagel. Source: trumpactiontracker.info"


def read_export(path):
    """Return (rows, theme_columns, sha256) for one export file.

    The export carries a licensing preamble ahead of the header row, so the
    header is located rather than assumed to be line one.
    """
    with open(path, "rb") as fh:
        raw_bytes = fh.read()
    digest = hashlib.sha256(raw_bytes).hexdigest()

    text = raw_bytes.decode("utf-8-sig")
    lines = text.split("\n")
    header_at = None
    for position, line in enumerate(lines):
        if line.startswith("Index,"):
            header_at = position
            break
    if header_at is None:
        raise ValueError("no header row starting with 'Index,' found in " + path)

    reader = csv.DictReader(io.StringIO("\n".join(lines[header_at:])))
    rows = list(reader)
    theme_columns = list(rows[0].keys())[4:]
    retval = (rows, theme_columns, digest)
    return retval


def tags_for(row, theme_columns):
    retval = [name for name in theme_columns if (row[name] or "").strip() == "Yes"]
    return retval


def draw(rows, theme_columns, seed, count):
    """Uniform random draw without replacement, ordered by Index for readability."""
    generator = random.Random(seed)
    picked = generator.sample(rows, count)
    picked.sort(key=lambda row: int(row["Index"]))

    drawn = []
    for row in picked:
        drawn.append(
            {
                "index": int(row["Index"]),
                "date": row["Date"],
                "claim": row["Title"],
                "citedUrl": row["URL"],
                "tags": tags_for(row, theme_columns),
            }
        )
    return drawn


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", help="path to a local copy of the export CSV")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--n", type=int, default=DEFAULT_N)
    parser.add_argument("--out", default="sample.json")
    args = parser.parse_args()

    rows, theme_columns, digest = read_export(args.export)
    drawn = draw(rows, theme_columns, args.seed, args.n)

    payload = {
        "note": (
            "Drawn before adjudication. Committed in its own commit so the draw is "
            "verifiable from git history. Every row here ships, including rows that "
            "come out fully carried."
        ),
        "credit": SOURCE_CREDIT,
        "export": os.path.basename(args.export),
        "exportSha256": digest,
        "populationRows": len(rows),
        "seed": args.seed,
        "drawnCount": len(drawn),
        "method": "random.Random(seed).sample over all rows, uniform, without replacement",
        "rubricVersion": 1,
        "rows": drawn,
    }

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print("export        " + os.path.basename(args.export))
    print("sha256        " + digest)
    print("population    " + str(len(rows)))
    print("seed          " + str(args.seed))
    print("drawn         " + str(len(drawn)))
    print("indexes       " + ", ".join(str(entry["index"]) for entry in drawn))
    print("written to    " + args.out)


if __name__ == "__main__":
    sys.exit(main())
