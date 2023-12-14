from itertools import count

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}


def tilt(board, d=1):
    while True:
        dirty = False
        newboard = {}
        for z in board:
            if z in newboard:
                continue
            if z - d in board and board[z] == "O" and board[z - d] == ".":
                newboard[z] = "."
                newboard[z - d] = "O"
                dirty = True
            else:
                newboard[z] = board[z]
        if not dirty:
            return board
        board = newboard


def load(board):
    return sum(100 - z.real for z, val in board.items() if val == "O")


# Part 1
print("PART 1:", int(load(tilt(board))))


# Part 2
def cycle(board):
    for d in (1, 1j, -1, -1j):
        board = tilt(board, d)
    return board


seen = []
for i in count():
    board = cycle(board)
    if board in seen:
        start = seen.index(board)
        break
    seen.append(board)

print("PART 2:", load(seen[((1000000000 - i) % (start - i)) + i - 1]))
