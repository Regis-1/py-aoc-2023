def read_input(file):
    seeds = []
    ranges = []
    mapping = []
    for i, line in enumerate(file.readlines()):
        line = line.rstrip()
        if (i == 0):
            seeds = [int(n) for n in line.split(' ') if n.isdigit()]
        elif (line == ''):
            if (len(ranges) != 0):
                mapping.append(ranges)
                ranges = []
        elif (not line[0].isdigit()):
            header = line.split(' ')[0]
        else:
            ranges.append([int(n) for n in line.split(' ')])
    if (len(mapping) != 0):
        mapping.append(ranges)
    return (seeds, mapping)

def in_source_range_idx(i, r):
    r_end = r[1] + r[2] - 1
    if (i >= r[1]) and (i <= r_end):
        return i - r[1]
    return -1

def almanac_map(input, ranges, level):
    result = 0
    index = 0
    for r in ranges[level]:
        index = in_source_range_idx(input, r)
        if (index >= 0):
            result = r[0] + index
            break

    if (index < 0):
        result = input
    if (level == len(ranges) - 1):
        return result

    level += 1
    return almanac_map(result, ranges, level)

def get_seeds_locations(data):
    seeds, ranges = data
    locations = [almanac_map(s, ranges, 0) for s in seeds]
    return locations

def day5_1(filename: str):
    with open(filename, 'r') as file:
        seeds_and_mapping = read_input(file)

    locations = get_seeds_locations(seeds_and_mapping)
    print(f'The result of day5_1 is: {min(locations)}.')
