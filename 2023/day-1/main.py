def find_numbers(e, part):
    number_mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    search_for = [str(i + 1) for i in range(9)] + (number_mapping if part == 2 else [])
    indices = []
    numbers = []

    for number in search_for:
        start_index = 0
        while True:
            index = e.find(number, start_index)
            if index == -1:
                break
            indices.append(index)
            if number in number_mapping:
                numbers.append(number_mapping.index(number) + 1)
            else:
                numbers.append(int(number))
            start_index = index + 1

    min_index = indices.index(min(indices))
    max_index = indices.index(max(indices))
    return 10 * numbers[min_index] + numbers[max_index]


lines = open("input.txt").readlines()
part1_result = sum([find_numbers(line, part=1) for line in lines])
part2_result = sum([find_numbers(line, part=2) for line in lines])

print(part1_result)
print(part2_result)