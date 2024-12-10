from collections import deque

# Read the input
with open("input.txt") as f:
    ls = f.read().strip().split("\n")

# Create a dictionary representing the board
board = {i + 1j * j: int(x) for i, l in enumerate(ls) for j, x in enumerate(l)}

# Define the valid moves (up, down, left, right)
directions = [1, -1, 1j, -1j]

# Create the graph as an adjacency list
graph = {z: [] for z in board}

# Build the graph based on the condition
for z, h in board.items():
    for dz in directions:
        neighbor = z + dz
        if neighbor in board and board[neighbor] == h + 1:
            graph[z].append(neighbor)

# Find the positions of zeros and nines
zeros, nines = [[z for z, x in board.items() if x == v] for v in (0, 9)]


# Function to find all simple paths using BFS
def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in path:
                continue
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))


# Part 1: Check if there is any path from each zero to any nine
part1_result = sum(any(bfs_paths(graph, z1, z2)) for z1 in zeros for z2 in nines)
print(part1_result)

# Part 2: Count the total number of paths from each zero to each nine
part2_result = sum(len(list(bfs_paths(graph, z1, z2))) for z1 in zeros for z2 in nines)
print(part2_result)
