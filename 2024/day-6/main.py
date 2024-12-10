# อ่านข้อมูลจากไฟล์
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# สร้างแผนที่ (board)
board = {
    complex(row, col): char
    for row, line in enumerate(lines)
    for col, char in enumerate(line)
}

# ส่วนที่ 1: นับตำแหน่งที่เคยเดินผ่าน
start_position = next(pos for pos, char in board.items() if char == "^")
wall_positions = {pos for pos, char in board.items() if char == "#"}
visited_positions = set()

current_position = start_position
direction = -1  # ทิศทางเริ่มต้น (ซ้าย)

while current_position in board:
    visited_positions.add(current_position)

    # ถ้าทิศทางข้างหน้ามี "กำแพง" ให้เปลี่ยนทิศทาง
    if current_position + direction in wall_positions:
        direction *= -1j  # หมุนทิศทาง 90 องศา
        continue

    # เดินไปข้างหน้า
    current_position += direction

print(len(visited_positions))  # จำนวนตำแหน่งที่เคยเดินผ่าน


# ส่วนที่ 2: ตรวจสอบว่าการเพิ่ม "กำแพง" ใหม่จะทำให้เกิด "ลูป" หรือไม่
def causes_loop(new_wall):
    all_walls = wall_positions | {new_wall}  # เพิ่มกำแพงใหม่
    current_position = start_position
    direction = -1
    visited_states = set()

    while current_position in board:
        # ถ้าสถานะนี้ (ตำแหน่ง + ทิศทาง) เคยเจอมาแล้ว แสดงว่าเกิดลูป
        if (current_position, direction) in visited_states:
            return True

        visited_states.add((current_position, direction))

        # ถ้าทิศทางข้างหน้ามีกำแพง ให้เปลี่ยนทิศทาง
        if current_position + direction in all_walls:
            direction *= -1j
            continue

        # เดินไปข้างหน้า
        current_position += direction

    return False


# คำนวณว่าการเพิ่มกำแพงในตำแหน่งที่เคยเดินผ่านจะทำให้เกิดลูปกี่ครั้ง
loop_count = sum(causes_loop(pos) for pos in visited_positions)
print(loop_count)
