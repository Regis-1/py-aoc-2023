def prepare_part_number(number, pos_x, pos_y):
    _num = ''.join(number)
    _len = len(_num)
    _num = int(_num)
    _num = (_num, pos_x, pos_y-1, _len)

    return _num

def find_parts_numbers(schematic):
    numbers = []
    for i, line in enumerate(schematic):
        number = []
        for j, ch in enumerate(line):
            if (ch.isdigit()):
                number.append(ch)
            else:
                if (len(number) != 0):
                    numbers.append(prepare_part_number(number, i, j))
                    number.clear()
        if (len(number) != 0):
            numbers.append(prepare_part_number(number, i, len(line)))

    return numbers

def extract_engine_schematic(file):
    schematic = []
    for line in file.readlines():
        schematic.append(str(line).rstrip())

    return schematic

def check_num(schema, num):
    result = False
    height = len(schema)
    width = len(schema[0])
    bounds = [
        0 if num[2] - num[3] < 0 else num[2] - num[3], #left
        width - 1 if num[2] + 1 >= width else num[2] + 1, #right
        0 if num[1] - 1 < 0 else num[1] - 1, #top
        height - 1 if num[1] + 1 >= height else num[1] + 1 #bottom
    ]

    for i in range(bounds[2], bounds[3]+1):
        for j in range(bounds[0], bounds[1]+1):
            if (schema[i][j] != '.') and (not schema[i][j].isdigit()):
                result = True

    return result


def check_part_numbers(schema, part_nums):
    valid_parts = []
    for num in part_nums:
        if(check_num(schema, num)):
            valid_parts.append(num[0])

    return valid_parts

def read_schematics_parts(schematic):
    part_numbers = find_parts_numbers(schematic)
    valid_parts = check_part_numbers(schematic, part_numbers)

    return valid_parts

def day3_1(filename: str):
    with open(filename, 'r') as file:
        schematic = extract_engine_schematic(file)

    part_numbers = read_schematics_parts(schematic)

    print(f'The result of day3_1 is: {sum(part_numbers)}.')
