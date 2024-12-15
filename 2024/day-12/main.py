def parse_input(filename):
    with open(filename) as f:
        return {
            i + 1j * j: x
            for i, l in enumerate(f.read().strip().split("\n"))
            for j, x in enumerate(l)
        }


def get_neighbors(z, board):
    directions = {1, -1, 1j, -1j}
    return {z + dz for dz in directions if board.get(z + dz) == board[z]}


def find_connected_components(board):
    visited = set()
    components = []

    for node in board:
        if node not in visited:
            # Perform BFS/DFS to find all connected nodes
            stack = [node]
            component = set()

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.add(current)
                    stack.extend(get_neighbors(current, board) - visited)

            components.append(component)

    return components


def calculate_wall_and_perimeter(component, board):
    directions = {1, -1, 1j, -1j}
    walls = {
        (z, dz * 1j) for dz in directions for z in component if z + dz not in component
    }
    perimeter = len(walls)
    interior_walls = sum((z + dz, dz) not in walls for (z, dz) in walls)
    return perimeter, interior_walls


def main():
    board = parse_input("input.txt")
    components = find_connected_components(board)

    res1 = 0
    res2 = 0

    for comp in components:
        perimeter, interior_walls = calculate_wall_and_perimeter(comp, board)
        res1 += len(comp) * perimeter
        res2 += len(comp) * interior_walls

    # Part 1
    print(res1)

    # Part 2
    print(res2)


if __name__ == "__main__":
    main()
