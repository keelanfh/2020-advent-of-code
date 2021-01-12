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

            allowed_for_field[field] = set()
            for r in ranges:
                fr, to = (int(i) for i in r.split("-"))
                allowed_for_field[field].update(n for n in range(fr, to+1))

        elif line.startswith("your"):
            yours = True

        elif line.startswith("nearby"):
            continue

        elif line.strip():
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

possible_fields = dict()

for pos, values_in_pos in enumerate(zip(*valid_tickets)):
    possible_fields[pos] = {field_name
                            for field_name in allowed_for_field
                            if all(val in allowed_for_field[field_name]
                                   for val in values_in_pos)}


used_fields = []

while any(len(v) > 1 for v in possible_fields.values()):
    for k, v in possible_fields.items():
        if len(v) == 1:
            used_fields.append(next(iter(v)))
        else:
            possible_fields[k] = {f
                                  for f in possible_fields[k]
                                  if f not in used_fields}

your_ticket_values = [your_ticket[i]
                      for i, v in enumerate(v.pop()
                                            for v in possible_fields.values())
                      if v.startswith("departure")]

print(reduce(int.__mul__, your_ticket_values))
