from itertools import *

data = [
    [(*map(int, p.split(",")),) for p in l.split("->")]
    for l in open("input.txt").readlines()
]
solid = {
    *chain(
        *[
            product(*[range(min(z), max(z) + 1) for z in zip(i, j)])
            for l in data
            for i, j in pairwise(l)
        ]
    )
}
ybound, sand, p1, pos = max([y for _, y in solid]), -1, None, None
while (500, 0) not in solid:
    solid |= {pos}
    p1 = sand if (p1 == None and pos != None and pos[1] > ybound) else p1
    pos = (500, 0)
    sand += 1
    while (
        n := next(
            (
                c
                for c in [(pos[0] + x, pos[1] + 1) for x in [0, -1, 1]]
                if c not in solid
            ),
            None,
        )
    ) and n[1] < ybound + 2:
        pos = n

"""
PART 1:
"""
print(p1)

"""
PART 2:
"""
print(sand)
