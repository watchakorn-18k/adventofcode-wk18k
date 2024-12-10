from collections import defaultdict, deque

with open("input.txt") as f:
    sections = f.read().strip().split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in sections[0].split("\n")]
updates = [tuple(map(int, line.split(","))) for line in sections[1].split("\n")]

violating_updates = {
    update
    for update in updates
    if any(
        a in update and b in update and update.index(a) > update.index(b)
        for a, b in rules
    )
}

valid_updates = [update for update in updates if update not in violating_updates]
part1_result = sum(update[len(update) // 2] for update in valid_updates)
print(part1_result)


def topological_sort(elements, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in rules:
        if a in elements and b in elements:
            graph[a].append(b)
            in_degree[b] += 1
            if a not in in_degree:
                in_degree[a] = 0

    queue = deque([node for node in elements if in_degree[node] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list


sorted_updates = [topological_sort(update, rules) for update in violating_updates]

part2_result = sum(update[len(update) // 2] for update in sorted_updates)
print(part2_result)
