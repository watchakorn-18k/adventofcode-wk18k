from collections import defaultdict
from itertools import product

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

boardz = defaultdict(str)
boardz.update(
    {
        complex(row, col): char
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
    }
)

directions = {
    complex(dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if (dx, dy) != (0, 0)
}

xmas_count = sum(
    all(boardz[z + i * direction] == char for i, char in enumerate("XMAS"))
    for z in list(boardz.keys())
    for direction in directions
)
print(xmas_count)

special_pattern_count = 0

for position in list(boardz.keys()):
    if boardz[position] == "A":
        corners = [
            boardz[position + 1 + 1j],
            boardz[position + 1 - 1j],
            boardz[position - 1 - 1j],
            boardz[position - 1 + 1j],
        ]
        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and corners[0] != corners[2]
        ):
            special_pattern_count += 1

print(special_pattern_count)
