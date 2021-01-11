from functools import reduce

allowed_for_field = dict()

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

            allowed_for_field[field] = allowed_nums

        elif line.startswith("your"):
            yours = True

        elif line.startswith("nearby"):
            continue

        else:
            line = line.strip()
            if line:
                nearby_tickets.append([int(i) for i in line.split(",")])

all_allowed = reduce(set.union, allowed_for_field.values())

error_rate = 0

for ticket in nearby_tickets:
    for value in ticket:
        if value not in all_allowed:
            error_rate += value

print(error_rate)

# Part 2

valid_tickets = [t
                 for t in nearby_tickets
                 if all(value in all_allowed
                        for value in t)]

results = dict()

for i, place in enumerate(zip(*valid_tickets)):
    results[i] = {p
                  for p in allowed_for_field
                  if all(val in allowed_for_field[p]
                         for val in place)
                  }


used_fields = []

while any(len(v) > 1 for v in results.values()):
    for k, v in results.items():
        if len(v) == 1:
            used_fields.append(next(iter(v)))
        else:
            results[k] = {f
                          for f in results[k]
                          if f not in used_fields}


results = (v.pop()
           for v in results.values())
results = [your_ticket[i]
           for i, v in enumerate(results)
           if v.startswith("departure")]
print(reduce(int.__mul__, results))
