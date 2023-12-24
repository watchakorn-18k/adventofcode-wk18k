"""
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day24/part1.py
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day24/part2.py
"""

import sys
from z3 import *


def is_after(pos: list[int], vel: list[int], x: float, y: float) -> bool:
    return abs(pos[0] + vel[0] - x) <= abs(pos[0] - x) and abs(pos[1] + vel[1] - y) <= abs(pos[1] - y)


def main1(data) -> None:

    stones = []
    for line in data.split("\n"):
        pos, vel = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        vel = list(map(int, vel.split(", ")))

        x1, y1, z1 = pos
        x2, y2, z2 = x1 + vel[0], y1 + vel[1], z1 + vel[2]
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1

        stones.append((pos, vel, slope, intercept))

    min_bound = 200000000000000
    max_bound = 400000000000000

    t = 0
    for i, a in enumerate(stones):
        for b in stones[i + 1:]:
            if a[2] == b[2]:
                continue

            x = (b[3] - a[3]) / (a[2] - b[2])
            y = a[2] * x + a[3]

            if x < min_bound or x > max_bound or y < min_bound or y > max_bound:
                continue

            if is_after(a[0], a[1], x, y) and is_after(b[0], b[1], x, y):
                t += 1

    print("PART 1:", t)


def main2(data) -> None:
    stones = []
    for line in data.split("\n"):
        pos, vel = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        vel = list(map(int, vel.split(", ")))

        stones.append((pos, vel))

    solver = Solver()

    x = Real("x")
    y = Real("y")
    z = Real("z")

    vx = Real("vx")
    vy = Real("vy")
    vz = Real("vz")

    for i, stone in enumerate(stones):
        t_intercept = Real(f"t_{i}")

        sp = stone[0]
        sv = stone[1]

        solver.add(x + vx * t_intercept == sp[0] + sv[0] * t_intercept)
        solver.add(y + vy * t_intercept == sp[1] + sv[1] * t_intercept)
        solver.add(z + vz * t_intercept == sp[2] + sv[2] * t_intercept)

    solver.check()
    print("PART 2:", solver.model().eval(x + y + z))


if __name__ == "__main__":
    with open("input", encoding="utf-8") as f:
        data = f.read()
    main1(data)
    main2(data)
