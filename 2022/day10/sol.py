with open("input.txt") as f:
    ls = f.read().strip().split("\n")

xs = [1]
for l in ls:
    x = xs[-1]
    xs.append(x)
    if a := l[5:]:
        xs.append(x + int(a))

"""
PART 1 : What is the sum of these six signal strengths?
"""
print(sum(i * xs[i - 1] for i in (20, 60, 100, 140, 180, 220)))

"""
PART 2 : What eight capital letters appear on your CRT?
"""
for i, x in enumerate(xs):
    print("█" if abs(i % 40 - x) <= 1 else " ", end="" if (i + 1) % 40 else "\n")
