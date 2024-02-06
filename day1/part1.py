"""
Author: Blake Freer
Date Created: 2024-02-05
"""

import re
import sys

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    first_dig = re.compile(r"[^\d]*(\d).*")
    last_dig = re.compile(r".*(\d)[^\d]*")

    total = 0

    for L in lines:
        total += 10 * int(first_dig.match(L).groups()[0]) + int(
            last_dig.match(L).groups()[0]
        )

    print(total)
