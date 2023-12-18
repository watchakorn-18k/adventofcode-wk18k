This Python code solves the **Manhattan distance puzzle** based on two sets of instructions: one for Part 1 and another for Part 2.

**Here's a breakdown of the code:**

- **Imports:**
  - `numpy`: Used for array manipulations.
- **Data loading:**
  - Opens the file "input" and reads each line into a list of words (`ws`).
  - Extracts direction and distance from each line.
- **Direction dictionary:**
  - Defines a dictionary (`dirs`) mapping letters ("R", "L", "U", "D") to complex numbers representing directions.
- **`solve` function:**
  - Takes a list of instructions (pairs of direction and distance) as input.
  - Converts each instruction pair to a complex number using the `dirs` dictionary.
  - Calculates the cumulative sum of these complex numbers (`vs`).
  - Calculates the Manhattan distance by:
    - Absolute value of the imaginary part of the final position.
    - Half the sum of absolute values of all positions.
    - Adding 1.
- **Part 1:**
  - Uses the original instructions.
  - Prints the answer for Part 1 using the `solve` function and formatting the output.
- **Part 2:**
  - Creates a dictionary (`table`) that maps the second character of each color string in the input to a direction.
  - Converts each instruction pair to a direction and distance using the color string and `table`.
  - Calls the `solve` function with the modified instructions and prints the answer for Part 2.

**Here's what you can add to your TODO.md:**

- **Function documentation:** Add docstrings to `dirs` and `solve` explaining their functionality and arguments.
- **Variable descriptions:** Briefly explain the purpose of variables like `ws`, `dirs`, and `vs`.
- **Logic clarification:** Add comments to complex sections like the Part 2 instruction conversion to improve clarity.
- **Further optimization:** Briefly mention potential optimizations for performance or code simplification.

By adding these explanations, you'll make your code more easily understandable for future reference and collaboration.
