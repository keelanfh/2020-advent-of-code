with open("input.txt") as f:
    input = f.read()

passports = input.split("\n\n")

essential = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_passports = 0

for passport in passports:
    kvs = passport.split()
    print(kvs)
    break
    # {k: v for k, v in kvs.split(":")}

    # if not essential.difference(keys):
    #     valid_passports += 1

print(valid_passports)
