# open input.txt
with open("input.txt", "r") as file:
    data = file.read()

# split data into lines
lines = data.split("\n")

# split the lines into 8 row chunks
chunks = [lines[i : i + 7] for i in range(0, len(lines), 8)]


def get_height(chunk):
    height = [
        sum([2**i for i in range(len(chunk)) if chunk[i][j] == "#"]) for j in range(5)
    ]
    return height


def count_pairs(heights):
    ctr = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            if all(heights[i][k] & heights[j][k] == 0 for k in range(5)):
                ctr += 1
    return ctr


heights = [get_height(chunk) for chunk in chunks]
print(count_pairs(heights))
