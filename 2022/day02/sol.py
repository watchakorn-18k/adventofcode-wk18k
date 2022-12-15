"""
Day 2: Rock Paper Scissors
"""

f = open("input.txt")
data_all = f.readlines()


def score(l, data=True):
    x1, x2 = l.split()
    l1 = "ABC".index(x1)
    l2 = "XYZ".index(x2)
    play = l2 if data else (l1 + l2 + 2) % 3
    won = (l2 - l1 + 1) % 3 if data else l2
    return 1 + play + 3 * won


"""
PART 1: What would your total score be if everything goes exactly according to your strategy guide?
"""
print(sum(score(l, True) for l in data_all))

"""
PART 2: what would your total score be if everything goes exactly according to your strategy guide?
"""
print(sum(score(l, False) for l in data_all))
