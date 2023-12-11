## Explanation of the Python code for TODO.md

This Python code calculates the sum of distances between all pairs of galaxies in a given map, taking into account unoccupied spaces and adjusting for potential gaps.

**Here's a breakdown of the code:**

**1. Imports:**

- `typing`: Used for type annotations.
- `math`: Used for the `comb` function to calculate combinations.

**2. Functions:**

- `get_locations`:

  - Parses the map and returns a list of coordinates for all "#" symbols (representing galaxies).

- `unocuppied_space`:

  - Identifies empty spaces in both X and Y directions by excluding coordinates occupied by galaxies.

- `manhattan_distance`:

  - Calculates the Manhattan distance between two points.

- `is_between`:

  - Checks if a value lies between two other values.

- `galaxies_distance`:

  - Calculates the adjusted distance between two galaxies, considering unoccupied spaces and a gap offset.
  - The `offset` function takes an axis and calculates the additional distance due to gaps on that axis.

- `calculate_distances`:
  - Calculates the distances between all pairs of galaxies.
  - Gets galaxy locations.
  - Generates all pairs of different galaxy indices.
  - Gets the unoccupied spaces.
  - Calculates the adjusted distance for each pair.
  - Returns the list of distances.
