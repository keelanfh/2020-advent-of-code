from functools import reduce
from pprint import pprint
import operator

field_range_dict = dict()

yours = False
nearby_tickets = []

with open("16/input.txt") as f:
    for line in f.readlines():
        if yours:
            your_ticket = [int(i) for i in line.split(",")]
            yours = False
        elif "or" in line:
            field, ranges = line.split(": ")

            ranges = ranges.split(" or ")
            allowed_nums = set()
            for r in ranges:
                fr, to = [int(i) for i in r.split("-")]
                for n in range(fr, to+1):
                    allowed_nums.add(n)

            field_range_dict[field] = allowed_nums

        elif line.startswith("your"):
            yours = True
            continue

        elif line.startswith("nearby"):
            continue

        else:
            line = line.strip()
            if not line:
                continue
            nearby_tickets.append([int(i) for i in line.split(",")])

all_allowed = reduce(set.union, field_range_dict.values())

error_rate = 0

for ticket in nearby_tickets:
    for value in ticket:
        if value not in all_allowed:
            error_rate += value

valid_tickets = [t for t in nearby_tickets if all(
    value in all_allowed for value in t)]

print(len(nearby_tickets))
print(len(valid_tickets))

print(error_rate)

possible_fields = dict()
used_fields = set()

print(valid_tickets)
print()
valid_tickets = [*zip(*valid_tickets)]

possibles = field_range_dict.keys()

results = dict()

for i, place in enumerate(valid_tickets):
    results[i] = {*possibles}
    bads = set()
    for val in place:
        for p in results[i]:
            if val not in field_range_dict[p]:
                bads.add(p)
    for bad in bads:
        results[i].remove(bad)

print(results)


used_fields = []

while True:
    for k, v in results.items():
        if len(v) > 1:
            results[k] = {
                f for f in results[k] if f not in used_fields}
        else:
            used_fields.append(next(iter(v)))
    if all(len(v) == 1 for k, v in results.items()):
        break


results = [v.pop() for k, v in results.items()]
results = [your_ticket[i]
           for i, v in enumerate(results) if v.startswith("departure")]
print(reduce(operator.mul, results))
