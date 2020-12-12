from collections import namedtuple
from typing import Sequence

CodeLine = namedtuple("CodeLine", ["op", "arg"])

with open("8/input.txt") as f:

    ORIGINAL_SOURCE = []
    for line in f.readlines():
        op, arg = line.split()
        ORIGINAL_SOURCE.append(CodeLine(op, int(arg)))


def execute_line(index: int, acc: int, op: str, arg: int) -> (int, int):
    if op == "nop":
        return index + 1, acc

    if op == "acc":
        return index + 1, acc + arg

    if op == "jmp":
        return index + arg, acc


def execute_source(source: Sequence[CodeLine]) -> int:
    index = 0
    acc = 0
    completed = set()

    while index < len(source):
        if index in completed:
            raise RuntimeError(f"{acc}")
        else:
            new_index, acc = execute_line(index, acc, *source[index])
            completed.add(index)
            index = new_index
    else:
        return acc

# Part 1


try:
    execute_source(ORIGINAL_SOURCE)
except RuntimeError as e:
    print(e)


# Part 2


class ModifiedSource:
    def __init__(self, mod_line_key: int):
        self.mod_line_key = mod_line_key

    def __len__(self):
        return len(ORIGINAL_SOURCE)

    def __getitem__(self, key: int):
        if key == self.mod_line_key:
            original_line = ORIGINAL_SOURCE[self.mod_line_key]
            if original_line.op == "jmp":
                return CodeLine(op="nop", arg=original_line.arg)
            if original_line.op == "nop":
                return CodeLine(op="jmp", arg=original_line.arg)
        else:
            return ORIGINAL_SOURCE[key]


for index, line in enumerate(ORIGINAL_SOURCE):
    if line.op in ("jmp", "nop"):
        try:
            print(execute_source(ModifiedSource(index)))
        except RuntimeError:
            pass
