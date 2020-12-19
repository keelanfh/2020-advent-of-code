from typing import Callable

memory = dict()


def run(mask: str, addr: str, value: str) -> None:
    addr, value = int(addr), format(int(value), '036b')
    result = []
    for i, num in enumerate(value):
        if (m := mask[i]) == "X":
            result.append(num)
        else:
            result.append(m)

    memory[addr] = int("".join(result), base=2)


def run2(mask: str, addr: str, value: str) -> None:
    addr, value = format(int(addr), '036b'), int(value)
    new_addr = []
    for i, num in enumerate(addr):
        if (m := mask[i]) == "0":
            new_addr.append(num)
        elif m == "1":
            new_addr.append("1")
        else:
            new_addr.append("X")

    final_addrs = [list()]
    for x in new_addr:
        if x.isdigit():
            for a in final_addrs:
                a.append(x)
        else:
            f2 = []
            for a in final_addrs:
                f2.append(a + ["0"])
                f2.append(a + ["1"])
            final_addrs = f2

    final_addrs = [int("".join(x), base=2) for x in final_addrs]

    for a in final_addrs:
        memory[a] = value


def process(run_func: Callable):
    # Need to set memory as a global variable, otherwise `run_func` will not be able to access it
    global memory
    memory = dict()

    with open("14/input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("mask"):
                mask = line.split()[2]
            else:
                addr, value = line.split(" = ")
                addr = "".join(x for x in addr if x.isdigit())
                run_func(mask, addr, value)

    total = 0
    for _, v in memory.items():
        total += v

    return total


print(process(run))
print(process(run2))
