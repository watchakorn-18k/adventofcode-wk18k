import math
import re
from collections import Counter


def parse_input():
    INPUT = "input.txt"
    robots: list[tuple[tuple[int, int], tuple[int, int], int]] = []
    with open(INPUT) as file:
        lines = file.read().splitlines()
        for line in lines:
            matches = re.findall(r"(-?\d+)", line)
            robot = (
                (int(matches[0]), int(matches[1])),
                (int(matches[2]), int(matches[3])),
                0,  # quadrant
            )
            robots.append(robot)
    return robots


WIDTH, HEIGHT = 101, 103
QUADRANT_W, QUADRANT_H = (WIDTH - 1) / 2, (HEIGHT - 1) / 2


def move(robots, i) -> None:
    position, velocity, _ = robots[i]
    new_x = (position[0] + velocity[0]) % WIDTH
    new_y = (position[1] + velocity[1]) % HEIGHT

    new_quadrant = 0
    if new_x < QUADRANT_W and new_y < QUADRANT_H:
        new_quadrant = 1
    elif new_x > QUADRANT_W and new_y < QUADRANT_H:
        new_quadrant = 2
    elif new_x < QUADRANT_W and new_y > QUADRANT_H:
        new_quadrant = 3
    elif new_x > QUADRANT_W and new_y > QUADRANT_H:
        new_quadrant = 4

    robots[i] = ((new_x, new_y), velocity, new_quadrant)


def solve():
    SECONDS = 100
    robots = parse_input()
    for _ in range(SECONDS):
        for i in range(len(robots)):
            move(robots, i)
    # quadrants
    counter = Counter([q for _, _, q in robots])
    robots_in_quadrants = [counter[1], counter[2], counter[3], counter[4]]
    print(math.prod(robots_in_quadrants))


def parse_input2():
    INPUT = "input.txt"
    robots: list[tuple[tuple[int, int], tuple[int, int]]] = []
    with open(INPUT) as file:
        lines = file.read().splitlines()
        for line in lines:
            matches = re.findall(r"(-?\d+)", line)
            robot = (
                (int(matches[0]), int(matches[1])),
                (int(matches[2]), int(matches[3])),
            )
            robots.append(robot)
    return robots


WIDTH, HEIGHT = 101, 103


def move2(robots, i) -> None:
    position, velocity = robots[i]
    new_x = (position[0] + velocity[0]) % WIDTH
    new_y = (position[1] + velocity[1]) % HEIGHT
    robots[i] = ((new_x, new_y), velocity)


def solve2():
    robots = parse_input2()
    seconds = 1
    while True:
        for i in range(len(robots)):
            move2(robots, i)
        if len(set(pos for pos, _ in robots)) == len(robots):
            break
        seconds += 1
    print(seconds)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    solve2()
    print("--- %s seconds ---" % (time.time() - start_time))
