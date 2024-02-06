"""
Author: Blake Freer
Date Created: 2024-02-05
"""

import logging
import re
import sys

# logging.getLogger().setLevel("DEBUG")

with open(sys.argv[1]) as f:
    games = f.readlines()

cube_count = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total_power = 0

pat_game_number = re.compile(r"Game ([\d]*):")

pat_count = {col: re.compile(rf"([\d]*) {col}") for col in cube_count.keys()}

for game in games:
    game_number = int(pat_game_number.search(game).groups()[0])

    max_count = {}
    for col in cube_count.keys():
        found = pat_count[col].findall(game)
        logging.debug(found)
        m = max(map(int, found))
        logging.debug(m)
        max_count[col] = m

    power = 1
    for v in max_count.values():
        power *= v

    total_power += power

print(total_power)
