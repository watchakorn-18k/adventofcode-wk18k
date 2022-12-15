"""

"""
from collections import defaultdict

with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]

sizes = defaultdict(int)
stack = []
for l in ls:
    match l.split():
        case [_, _, "/"]:
            stack = []
        case [_, _, ".."]:
            stack.pop()
        case [_, _, x]:
            stack.append(x)
        case [a, _] if a.isdigit():
            for i in range(len(stack) + 1):
                path = "/" + "/".join(stack[:i])
                sizes[path] += int(a)

"""PART 1: What is the sum of the total sizes of those directories?"""
print(sum(filter(lambda v: v <= 100000, sizes.values())))

"""PART 2: """
unused = 70000000 - sizes["/"]
need = 30000000 - unused
print(min(filter(lambda v: v >= need, sizes.values())))
