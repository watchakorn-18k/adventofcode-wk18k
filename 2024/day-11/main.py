with open("input.txt") as f:
    stones = {}

    for num in f.read().split():
        num = int(num)
        if num in stones:
            stones[num] += 1
        else:
            stones[num] = 1


for blinks in range(1, 76):
    new_stones = {}

    for n, num_stone in stones.items():
        mid, rem = divmod(len(str(n)), 2)
        if n == 0:
            new_stones[1] = new_stones.get(1, 0) + num_stone
        elif rem:
            new_stones[2024 * n] = new_stones.get(2024 * n, 0) + num_stone
        else:
            for m in divmod(n, 10**mid):
                new_stones[m] = new_stones.get(m, 0) + num_stone

    stones = new_stones
    if blinks in (25, 75):
        print(sum(new_stones.values()))
