"""
Day 5: Supply Stacks
"""

import re

with open("input.txt") as f:
    ls = f.readlines()

ns = [list(map(int, re.findall("\d+", x))) for x in ls[10:]]
stacks = [
    "GDVZJSB",
    "ZSMGVP",
    "CLBSWTQF",
    "HJGWMRVQ",
    "CLSNFMD",
    "RGCD",
    "HGTRJDSQ",
    "PFV",
    "DRSTJ",
]


def solve(stacks, part1):
    stacks = list(stacks)
    for amount, from_stack, to_stack in ns:
        top = stacks[from_stack - 1][-amount:]
        if part1:
            top = top[::-1]
        stacks[from_stack - 1] = stacks[from_stack - 1][:-amount]
        stacks[to_stack - 1] += top
    return "".join(s[-1] for s in stacks)


"""
PART 1: After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
print(solve(stacks, True))

"""
PART 2: After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
print(solve(stacks, False))
