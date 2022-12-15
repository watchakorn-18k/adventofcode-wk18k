"""
Day 3: Rucksack Reorganization
"""
from itertools import islice
import string

with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]

score = (" " + string.ascii_lowercase + string.ascii_uppercase).index

"""
PART 1: What is the sum of the priorities of those item types?
"""
s = 0
for l in ls:
    mid = len(l) // 2
    p1, p2 = l[:mid], l[mid:]
    (o,) = set(p1) & set(p2)
    s += score(o)
print(s)

"""
PART 2: What is the sum of the priorities of those item types?
"""
sets = map(set, ls)
s = 0
for _ in range(len(ls) // 3):
    (o,) = set.intersection(*islice(sets, 3))
    s += score(o)
print(s)
