from functools import reduce
from pprint import pprint

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
            if line == "":
                continue
            nearby_tickets.append([int(i) for i in line.split(",")])

all_allowed = reduce(set.union, field_range_dict.values())

error_rate = 0

for ticket in nearby_tickets:
    for value in ticket:
        if value not in all_allowed:
            error_rate += value

print(error_rate)

possible_fields = dict()
used_fields = set()

for ticket in nearby_tickets:
    for i, value in enumerate(ticket):
        # print()
        # print(i, value)
        # print(used_fields)
        # print(possible_fields)

        # If there is a dict in there for possible fields, which isn't 1, remove any used_fields from it, since they can't be used again.
        if possible_fields.get(i):
            if len(possible_fields[i]) != 1:
                possible_fields[i] = {
                    f for f in possible_fields[i] if f not in used_fields}

            # In this case, there was an entry in possible_fields to begin with, so we set the entry to the intersection between that and the new ones
            else:
                possible_fields[i] = set(
                    (field for field, allowed_values in field_range_dict.items() if value in allowed_values)).intersection(possible_fields[i])

            # Again, we add this to the used_fields if there is only one.
            if len(possible_fields[i]) == 1:
                used_fields |= possible_fields[i]

        # Otherwise (entry in possible_fields is empty):
        # check if the value is in the allowed values for all fields - if it is, add those fields to the entry.
        else:
            possible_fields[i] = set(
                (field for field, allowed_values in field_range_dict.items() if (value in allowed_values)))

            # If there's only one possible field for that value, add that field to used_fields
            if len(possible_fields[i]) == 1:
                used_fields |= possible_fields[i]

    # break


for k, v in possible_fields.items():
    print(k, len(v))
