"""
Author: Blake Freer
Date Created: 2024-02-05
"""

import logging
import re
import sys

logging.basicConfig(
    format="[%(levelname)s] %(message)s",
    # level="DEBUG",  # uncomment to show debugging
)


with open(sys.argv[1]) as f:
    lines = f.readlines()

keys = r"(one|two|three|four|five|six|seven|eight|nine|\d)"

first_dig = re.compile(rf".*?{keys}.*")
last_dig = re.compile(rf".*{keys}.*?")

mapper = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
} | {str(i): i for i in range(1, 9 + 1)}

total = 0

for L in lines:
    first = first_dig.match(L).groups()[0]
    last = last_dig.match(L).groups()[0]

    value = mapper[first] * 10 + mapper[last]
    logging.debug(f"{first} {last} = {value}")

    total += value

print(total)
