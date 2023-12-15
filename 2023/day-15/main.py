"""
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day15/part1.py
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day15/part2.py
"""

with open("input") as f:
    data = f.read().strip()

t = 0
for step in data.split(","):
    v = 0
    for ch in step:
        v += ord(ch)
        v *= 17
        v %= 256

    t += v

print("PART 1:", t)

boxes = [[] for _ in range(256)]
for step in data.split(","):
    if "=" in step:
        label, length = step.split("=")
        length = int(length)

        v = 0
        for ch in label:
            v += ord(ch)
            v *= 17
            v %= 256

        for arr in boxes[v]:
            if arr[0] == label:
                arr[1] = length
                break
        else:
            boxes[v].append([label, length])
    elif step.endswith("-"):
        label = step[:-1]

        v = 0
        for ch in label:
            v += ord(ch)
            v *= 17
            v %= 256

        boxes[v] = [arr for arr in boxes[v] if arr[0] != label]

t = 0
for i, box in enumerate(boxes):
    for j, arr in enumerate(box):
        t += (i + 1) * (j + 1) * arr[1]


print("PART 2:", t)
