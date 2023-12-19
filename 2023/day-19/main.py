"""
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day19/part1.py
https://github.com/jmerle/advent-of-code-2023/blob/master/src/day19/part2.py
"""

from math import *
import re


def parse_workflows(data):
    workflows = {}

    for line in data.split("\n"):
        id, steps = line.split("{")
        workflows[id] = []

        for step in steps[:-1].split(","):
            if any(ch + op in step for ch in "xmas" for op in "<>"):
                ch, op, value, nxt = re.findall(
                    r"([xmas])([<>])(\d+):(\w+)", step)[0]
                workflows[id].append((ch, op, int(value), nxt))
            else:
                workflows[id].append((step,))

    return workflows


def evaluate_part1(workflows, data):
    t = 0
    for part in data.split("\n"):
        nums = list(map(int, re.findall(r"(\d+)", part)))
        d = {"x": nums[0], "m": nums[1], "a": nums[2], "s": nums[3]}

        workflow = "in"
        while workflow not in {"A", "R"}:
            for step in workflows[workflow]:
                if len(step) == 4 and step[1] == "<" and d[step[0]] < step[2]:
                    workflow = step[3]
                    break
                elif len(step) == 4 and step[1] == ">" and d[step[0]] > step[2]:
                    workflow = step[3]
                    break
                elif len(step) == 1:
                    workflow = step[0]
                    break

        if workflow == "A":
            t += sum(nums)

    return t


def evaluate_part2(workflows):
    queue = [("in", 0, {ch: (1, 4000) for ch in "xmas"})]
    t = 0

    while queue:
        workflow, idx, bounds = queue.pop()

        if workflow == "A":
            t += prod(bounds[ch][1] - bounds[ch][0] + 1 for ch in "xmas")

        if workflow in {"A", "R"} or idx >= len(workflows[workflow]):
            continue

        step = workflows[workflow][idx]

        if len(step) == 4 and step[1] == "<":
            iff = bounds.copy()
            els = bounds

            iff[step[0]] = (iff[step[0]][0], step[2] - 1)
            els[step[0]] = (step[2], els[step[0]][1])

            queue.append((step[3], 0, iff))
            queue.append((workflow, idx + 1, els))
        elif len(step) == 4 and step[1] == ">":
            iff = bounds.copy()
            els = bounds

            iff[step[0]] = (step[2] + 1, iff[step[0]][1])
            els[step[0]] = (els[step[0]][0], step[2])

            queue.append((step[3], 0, iff))
            queue.append((workflow, idx + 1, els))
        elif len(step) == 1:
            queue.append((step[0], 0, bounds))

    return t


with open("input") as f:
    data = f.read().strip()

sections = data.split("\n\n")
workflows = parse_workflows(sections[0])

part1_result = evaluate_part1(workflows, sections[1])
print("PART 1:", part1_result)

part2_result = evaluate_part2(workflows)
print("PART 2:", part2_result)
