def extract_engine_schematic(file):
    schematic = []
    for line in file.readlines():
        schematic.append(str(line).rstrip())

    return schematic

def extract_parts_and_gears(schematic):
    part_numbers = []
    gear_symbols = []
    for i, line in enumerate(schematic):
        num_buffer = []
        for j, ch in enumerate(line):
            if (ch.isdigit()):
                num_buffer.append(ch)
                if (j == len(line) - 1):
                    part_numbers.append((
                        int(''.join(num_buffer)),
                        i,
                        j - len(num_buffer),
                        j - 1
                    ))
            else:
                if (ch == '*'):
                    gear_symbols.append((i, j))

                if (len(num_buffer) != 0):
                    part_numbers.append((
                        int(''.join(num_buffer)),
                        i,
                        j - len(num_buffer),
                        j - 1
                    ))
                    num_buffer.clear()
    return (part_numbers, gear_symbols)

def find_gears(p_and_s):
    parts, symbols = p_and_s
    gears = {}
    for symbol in symbols:
        gears[symbol] = []
    for part in parts:
        surroundings = []
        for i in range(part[2]-1, part[3]+2):
            surroundings.append((part[1]-1, i))
            surroundings.append((part[1]+1, i))
        surroundings.extend([
            (part[1], part[2]-1),
            (part[1], part[3]+1)
        ])
        for symbol in symbols:
            if symbol in surroundings:
                gears[symbol].append(part[0])
    return [g for g in gears.values() if len(g) == 2]

def get_gears(schematic):
    parts_and_symbols = extract_parts_and_gears(schematic)
    gears = find_gears(parts_and_symbols)
    return gears

def day3_2(filename: str):
    with open(filename, 'r') as file:
        schematic = extract_engine_schematic(file)
    gears = get_gears(schematic)
    ratios = [r[0]*r[1] for r in gears]
    print(f'The result of day3_2 is: {sum(ratios)}.')
