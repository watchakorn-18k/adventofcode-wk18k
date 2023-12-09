"""
https://github.com/fuglede/adventofcode/blob/master/2023/day09/solutions.py
"""

import re

import numpy as np

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = np.array([list(map(int, re.findall(r"-?\d+", x))) for x in ls])

i = 1
for a in (ns, np.flip(ns, 1)):
    print(f"PART {i}.",np.sum([np.diff(a, k)[:,-1] for k in range(ns.shape[1])]))
    i += 1