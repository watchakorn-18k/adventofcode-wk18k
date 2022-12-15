from collections import defaultdict
from math import lcm, prod

# We manually include our input; it's small enough
# that that's much easier than writing something to
# parse it.
ops = [
    lambda l: l * 13,
    lambda l: l + 7,
    lambda l: l + 2,
    lambda l: l * 2,
    lambda l: l * l,
    lambda l: l + 6,
    lambda l: l + 1,
    lambda l: l + 8,
]
divs = [2, 13, 5, 3, 11, 17, 7, 19]
if_trues = [5, 4, 5, 6, 7, 4, 0, 6]
if_falses = [2, 3, 1, 7, 3, 1, 2, 0]


def solve(num_rounds, part1):
    monkeys = [
        [91, 54, 70, 61, 64, 64, 60, 85],
        [82],
        [84, 93, 70],
        [78, 56, 85, 93],
        [64, 57, 81, 95, 52, 71, 58],
        [58, 71, 96, 58, 68, 90],
        [56, 99, 89, 97, 81],
        [68, 72],
    ]
    i = 0
    # The lcm below could have just been prod; all elements in
    # `divs` are prime, so it comes out as the same thing.
    # For part 1, it's unnecessary entirely, but it helps keep
    # the numbers small for part 2.
    lcm_divs = lcm(*divs)
    inspected = defaultdict(int)
    for _ in range(num_rounds):
        for i, (monkey, op, div, if_true, if_false) in enumerate(
            zip(monkeys, ops, divs, if_trues, if_falses)
        ):
            while monkey:
                item = monkey.pop()
                inspected[i] += 1
                new = op(item) % lcm_divs
                if part1:
                    new //= 3
                monkeys[if_false if new % div else if_true].append(new)
    return prod(sorted(inspected.values())[-2:])


"""
PART 1: What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
"""
print(solve(20, True))

"""
PART 2: what is the level of monkey business after 10000 rounds?
"""
print(solve(10_000, False))
