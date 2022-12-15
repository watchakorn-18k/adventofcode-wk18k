"""
Day 1: Calorie Counting
"""
"""
PART 1 : Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
f = open("data.txt")
data_all = f.read().strip().split("\n\n")  # ตัดบรรทัดที่ว่างออกไป
data_group_sum = [
    sum(map(int, g.split("\n"))) for g in data_all
]  # แบ่งกลุ่มตามบรรทัดที่ว่างแล้ว sum
print(f"Part 1 : {max(data_group_sum)}")

"""
PART 2 : Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
data_sort = sorted(data_group_sum)
data_top_three = data_sort[-3:]
print(f"Part 2 : {sum(data_top_three)}")
