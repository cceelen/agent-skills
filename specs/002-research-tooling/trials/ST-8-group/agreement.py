"""Agreement of the groupings of the runs.

For each two runs: the share of the pairs of lines that the two runs put together, of the pairs
that one run at least puts together (Jaccard of the pairs).
"""

import itertools
import json
import re
import sys


def pairs(text):
    rows = [row for row in text.splitlines() if re.match(r"\|\s*G-\d+", row)]
    groups = [re.findall(r"P-\d{3}", row.split("|")[3]) for row in rows]
    seen = [line for group in groups for line in group]
    together = {frozenset(p) for g in groups for p in itertools.combinations(sorted(set(g)), 2)}
    return together, len(groups), len(seen), len(set(seen))


with open(sys.argv[1]) as rows_of_runs:
    runs = [pairs(json.loads(line)["files"].get("groups.md", "")) for line in rows_of_runs]
for number, (_, groups, seen, different) in enumerate(runs, 1):
    print(f"run {number}: groups {groups}, lines placed {seen}, different lines {different}")
for (i, a), (j, b) in itertools.combinations(enumerate(runs, 1), 2):
    both, one = len(a[0] & b[0]), len(a[0] | b[0])
    share = both / max(1, one)
    print(f"runs {i} and {j}: pairs in the two runs {both}, in one run at least {one}, share {share:.2f}")
