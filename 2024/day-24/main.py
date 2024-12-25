from itertools import combinations

# open input.txt
with open("input.txt", "r") as file:
    data = file.read().strip()

# split data into lines
lines = data.split("\n")

initial_values = {}
# for lines that contain : and a number, split into key and value
for line in lines:
    if ":" in line:
        key, value = line.split(":")
        initial_values[key] = int(value)

# gates = []
gate_map = {}
# if the lines contain AND OR XOR, split the line into 4 parts: input1, input2, operator, output
for line in lines:
    if "->" in line:
        input1, operator, input2, _, output = line.split(" ")
        gate_map[output] = (operator, input1, input2, output)


def evaluate_gate(gate, gate_map, initial_values):
    operator, input1, input2, _ = gate

    if input1 in initial_values:
        input1_value = initial_values[input1]
    else:
        input1_value = evaluate_gate(gate_map[input1], gate_map, initial_values)

    if input2 in initial_values:
        input2_value = initial_values[input2]
    else:
        input2_value = evaluate_gate(gate_map[input2], gate_map, initial_values)

    if operator == "AND":
        return input1_value & input2_value
    elif operator == "OR":
        return input1_value | input2_value
    elif operator == "XOR":
        return input1_value ^ input2_value


def evaluate_system(gate_map, initial_values):
    outputs = []
    terminal_gates = [
        (out, gate) for out, gate in gate_map.items() if out.startswith("z")
    ]
    for out, terminal_gate in terminal_gates:
        p = int(out[1:])
        outputs.append((p, evaluate_gate(terminal_gate, gate_map, initial_values)))

    return sum([2**p * value for p, value in outputs])


print("PART 1:", evaluate_system(gate_map, initial_values))

op_map = {}

for out, gate in gate_map.items():
    op_map[(gate[0], gate[1], gate[2])] = out

terminal_gates = [(out, gate) for out, gate in gate_map.items() if out.startswith("z")]
num_outputs = len(terminal_gates)


def check_op_map(x_var, y_var, op):
    # print("Checking op map for ", op, x_var, y_var)
    if (op, x_var, y_var) in op_map:
        out = op_map[(op, x_var, y_var)]
    elif (op, y_var, x_var) in op_map:
        out = op_map[(op, y_var, x_var)]
    else:
        out = ""
    # print("Out is ", out)
    return out


def carry_forward_check(op_map):
    carry_forward = ""
    new_carry = ""

    to_be_verified_list = []
    checked_list = []

    for i in range(num_outputs):
        index = f"%02d" % i
        x_var = f"x{index}"
        y_var = f"y{index}"
        z_var = f"z{index}"

        # follow through the two half-adders, and check that all the right operations are there
        digit1 = check_op_map(x_var, y_var, "XOR")
        carry1 = check_op_map(x_var, y_var, "AND")

        if i == 0:
            if digit1 != z_var:
                return 0, checked_list

            checked_list.append(digit1)
            carry_forward = carry1
        else:
            digit2 = check_op_map(carry_forward, digit1, "XOR")

            if digit2 != z_var:
                return i - 1, checked_list

            checked_list.append(digit1)
            for item in to_be_verified_list:
                checked_list.append(item)

            new_carry = check_op_map(carry_forward, digit1, "AND")
            carry_forward = check_op_map(carry1, new_carry, "OR")

            to_be_verified_list.append(carry_forward)
            to_be_verified_list.append(new_carry)

    return num_outputs, checked_list


swaps = set()
personal_best, checked_list = carry_forward_check(op_map)
for _ in range(4):
    for op1, op2 in combinations(gate_map.keys(), 2):
        gate1 = gate_map[op1]
        gate2 = gate_map[op2]

        if op1 in checked_list or op2 in checked_list:
            continue

        op_map[(gate1[0], gate1[1], gate1[2])] = op2
        op_map[(gate2[0], gate2[1], gate2[2])] = op1

        gate_map[op1] = gate2
        gate_map[op2] = gate1

        new_attempt, checked_in_attempt = carry_forward_check(op_map)

        if new_attempt > personal_best:
            personal_best = new_attempt
            checked_list = checked_in_attempt

            print(f"Found a better attempt: {personal_best}")
            swaps.add((op1, op2))
            print("swap = ", op1, op2)

            break

        # revert the swap
        op_map[(gate1[0], gate1[1], gate1[2])] = op1
        op_map[(gate2[0], gate2[1], gate2[2])] = op2

        gate_map[op1] = gate1
        gate_map[op2] = gate2
# flatten swaps and sort
swaps_sorted = sorted(sum(swaps, start=tuple()))
print("PART 2:", ",".join(swaps_sorted))
