import re
from collections import Counter

direction_to_vector = {"e": (1, 0), "w": (-1, 0),
                       "ne": (0, 1), "sw": (0, -1),
                       "nw": (-1, 1), "se": (1, -1)}

with open("24/input.txt") as f:
    flipped_tiles = []
    for line in f.readlines():
        e = ne = 0
        for x in re.findall("(e|w|se|sw|ne|nw)", line):
            e_diff, ne_diff = direction_to_vector[x]
            e += e_diff
            ne += ne_diff

        flipped_tiles.append((e, ne))

    flipped = sum(v % 2
                  for v in Counter(flipped_tiles).values())

    print(flipped)
