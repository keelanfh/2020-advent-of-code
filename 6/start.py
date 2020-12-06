from functools import reduce

with open("6/input.txt") as f:
    data = f.read()
    groups = data.split("\n\n")

# Part 1

print(sum(len(set(x for x in g if x != "\n")) for g in groups))

total = 0

# Part 2

for group in groups:

    x = reduce(set.intersection, (set(x) for x in group.split()))
    total += len(x)

print(total)
