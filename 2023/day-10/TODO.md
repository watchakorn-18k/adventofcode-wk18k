**Part 1:** Find the shortest distance from "S" to any other reachable point on the map.

- **Input:**
  - A file named "input" containing the map layout.
  - The map is represented by a grid of characters, where:
    - "S" is the starting position.
    - "." is an empty space.
    - "J", "L", "F", "7", "|" and "-" are special characters defining paths with specific direction changes.
- **Algorithm:**
  1. Breadth-first search (BFS) is used to explore the map starting from "S".
  2. A `dist` matrix is used to store the shortest distance from "S" to each visited point.
  3. The `vis` matrix keeps track of visited points to avoid revisiting them.
  4. The code iterates through the neighbors of the current position based on the character at that position.
  5. For special characters, the code takes into account the direction change and checks for "J" and "L" characters that act as end points.
  6. The code updates the `dist` and `vis` matrices for each visited neighbor.
  7. Finally, the maximum value in `dist` corresponds to the longest shortest distance (farthest reachable point).
- **Output:**
  - The code prints the value for "PART 1" as the maximum value in the `dist` matrix.

**Part 2:** Find the number of special characters encountered while traversing the map from any unvisited point without encountering "S" again.

- **Algorithm:**
  1. A new matrix `k` is used to store the number of special characters encountered for each unvisited point.
  2. The code iterates through each unvisited point and performs ray tracing.
  3. Ray tracing starts at the current point and iterates vertically downwards until it encounters a visited point or the end of the map.
  4. For each encountered special character, the counter in `k[r][c]` is incremented.
  5. If the character is "F", "J", or "L", additional checks are performed to determine if the character acts as an end point and whether it affects the counter.
  6. Finally, the code counts the number of unvisited points where the counter is odd (meaning an uneven number of special characters were encountered).
- **Output:**
  - The code prints the count of unvisited points with an odd number of special characters as "PART 2".
