with open("4/input.txt") as f:
    input = f.read()

passports = input.split("\n\n")

essential = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_passports = 0
validated_passports = 0


def valid(k, v):
    if k == "byr":
        return 1920 <= int(v) <= 2002

    if k == "iyr":
        return 2010 <= int(v) <= 2020

    if k == "eyr":
        return 2020 <= int(v) <= 2030

    if k == "hgt":
        if not (v.endswith("cm") or v.endswith("in")):
            return False
        num, unit = int(v[:-2]), v[-2:]
        if unit == "cm":
            return 150 <= num <= 193
        if unit == "in":
            return 59 <= num <= 76

    if k == "hcl":
        if not v.startswith("#"):
            return False
        try:
            int(v.lstrip("#"), base=16)
        except ValueError:
            return False
        return True

    if k == "ecl":
        return v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    if k == "pid":
        return len(v) == 9 and v.isdecimal()


for passport in passports:
    kvs = passport.split()
    keys = []
    valid_keys = []
    for kv in kvs:
        k, v = kv.split(":")
        if valid(k, v):
            valid_keys.append(k)
        keys.append(k)

    if not essential.difference(keys):
        valid_passports += 1
    print(essential.difference(valid_keys))
    if not essential.difference(valid_keys):
        validated_passports += 1

print(valid_passports)
print(validated_passports)
