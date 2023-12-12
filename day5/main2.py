def read_input(file):
    seeds = []
    ranges = []
    mapping = []
    for i, line in enumerate(file.readlines()):
        line = line.rstrip()
        if (i == 0):
            tmp = [int(n) for n in line.split(' ')[1:]]
            seeds = [(tmp[n], tmp[n+1]) for n in range(0, len(tmp), 2)]
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

def map_in_range(tup, ranges):
    low = tup[0] 
    high = tup[1]
    for r in ranges:
        if (r[1][0] <= tup[0] <= r[1][1]):
            low = r[0][0] + low - r[1][0]
        if (r[1][0] <= tup[1] <= r[1][1]):
            high = r[0][0] + high - r[1][0]

    return (low, high)

def fillet_map(sr, mr):
    result = []
    edges = [n for r in mr for n in r[1]]
    edges.extend([sr[0], sr[1]])
    edges.sort()
    s_l_idx = edges.index(sr[0])
    s_h_idx = edges.index(sr[1])
    _prev = -1
    in_seed_range = False
    is_offset = False
    for i, e in enumerate(edges):
        if (in_seed_range):
            if (not _prev + int(is_offset) == e):
                result.append((_prev + int(is_offset), e))
            is_offset = not is_offset
        if(i == s_l_idx):
            in_seed_range = True
        elif(i == s_h_idx):
            in_seed_range = False
            break
        _prev = e

    return result

def map_via_almanac(sr, m, lvl):
    mr = m[lvl]
    result = [fillet_map(s, mr) for s in sr]
    result = [x for y in result for x in y]
    mapped = [map_in_range(t, mr) for t in result]
    if (lvl == len(m) - 1):
        return mapped

    mapped = [map_via_almanac([mp], m, lvl+1) for mp in mapped]
    mapped = [m for x in mapped for m in x]
    return mapped

def get_seeds_locations(s_and_m):
    seed_ranges, mapping = s_and_m
    seed_ranges = [(sr[0], sr[0]+sr[1]-1) for sr in seed_ranges]
    for i, m in enumerate(mapping):
        mapping[i] = [((st, st+l-1), (ss, ss+l-1)) for st, ss, l in m]
    locations = [map_via_almanac([sr], mapping, 0) for sr in seed_ranges]

    return [range_tup[0] for seed_ranges in locations for range_tup in seed_ranges]

def day5_2(filename: str):
    with open(filename, 'r') as file:
        seeds_and_mapping = read_input(file)

    locations = get_seeds_locations(seeds_and_mapping)
    locations.sort()
    print(f'The result of day5_2 is: {min(locations)}. Small bug - to check')
