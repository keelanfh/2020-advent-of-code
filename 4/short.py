e = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
s = str.split
print(sum(not e-{s(k, ":")[0]for k in s(p)}
          for p in s(open("4/input.txt").read(), "\n\n")))
