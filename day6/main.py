def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        times = [int(n) for n in lines[0].split(' ') if n.rstrip().isdigit()]
        distances = [int(n) for n in lines[1].split(' ') if n.rstrip().isdigit()]
    return (times, distances)

def calculate_ways(t_and_dist):
    times, distances = t_and_dist
    outcomes = [[(t-i)*i for i in range(t+1)] for t in times]
    filtered_outcomes = [[o for o in outs if o > d] for outs, d in zip(outcomes, distances)]
    return [len(fo) for fo in filtered_outcomes]

def day6_1(filepath: str):
    input = parse_input_file(filepath)
    num_of_ways = calculate_ways(input)

    prod_result = 1
    for now in num_of_ways:
        prod_result *= now

    print(f'The result of day6_1 is: {prod_result}.')
