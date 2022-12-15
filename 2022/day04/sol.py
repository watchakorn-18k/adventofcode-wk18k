"""
Day 4: Camp Cleanup
"""

import re

with open("input.txt") as f:
    ls = f.readlines()

ns = [list(map(int, re.findall("\d+", x))) for x in ls]
ranges = [(set(range(n1, n2 + 1)), set(range(n3, n4 + 1))) for n1, n2, n3, n4 in ns]

"""
PART 1: In how many assignment pairs does one range fully contain the other?
"""
print(sum(s1 <= s2 or s2 <= s1 for s1, s2 in ranges))

"""
PART 2: In how many assignment pairs do the ranges overlap?
"""
print(sum(not s1.isdisjoint(s2) for s1, s2 in ranges))
