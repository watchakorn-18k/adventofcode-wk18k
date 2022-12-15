"""
Day 6: Tuning Trouble
"""
from itertools import count

with open("input.txt") as f:
    data = f.read()


def solve(length):
    return next(i for i in count() if len(set(data[i - length : i])) == length)


"""
PART 1: How many characters need to be processed before the first start-of-packet marker is detected?
"""
print(solve(4))

"""
PART 2: How many characters need to be processed before the first start-of-message marker is detected?
"""
print(solve(14))
