def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        time = [n for n in lines[0].split(' ') if n.rstrip().isdigit()]
        distance = [n for n in lines[1].split(' ') if n.rstrip().isdigit()]
        time = int(''.join(time))
        distance = int(''.join(distance))
    return (time, distance)

def calculate_ways(t_and_dist):
    time, distance = t_and_dist
    result = []
    lookup_params = [(0, time+1, 1), (time, 0, -1)]
    for lp in lookup_params:
        for i in range(*lp):
            _distance = i*(time-i)
            if (_distance > distance):
                break
            result.append(_distance)

    return time - len(result) + 1

def day6_2(filepath: str):
    input = parse_input_file(filepath)
    num_of_ways = calculate_ways(input)

    print(f'The result of day6_1 is: {num_of_ways}.')
