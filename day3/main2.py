def findall(p, s):
    i = s.find(p)
    while (i != -1):
        yield i
        i = s.find(p, i+1)

def extract_engine_schematic(file):
    schematic = []
    for line in file.readlines():
        schematic.append(str(line).rstrip())

    return schematic

def get_gears(schematic):
    

def extract_gear_ratios(schematic):
    gear_ratios = []
    gears = get_gears(schematic)
    
    for gear in gears:
        gear_ratios.append(gear[0] * gear[1])

    return gear_ratios

def day3_2(filename: str):
    with open(filename, 'r') as file:
        schematic = extract_engine_schematic(file)

    gear_ratios = extract_gear_ratios(schematic)

    print(f'The result of day3_1 is: {sum(gear_ratios)}.')
