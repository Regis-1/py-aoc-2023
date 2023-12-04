def evaluate_game(line: str, num_r: int, num_g: int, num_b: int):
    result = True
    splitted_game = line.split(' ')
    id = int(splitted_game[1][:-1])
    splitted_game = splitted_game[2:]
    for i in range(0, len(splitted_game), 2):
        if (('red' in splitted_game[i+1]) and (int(splitted_game[i]) > num_r)) or \
        (('green' in splitted_game[i+1]) and (int(splitted_game[i]) > num_g)) or \
        (('blue' in splitted_game[i+1]) and (int(splitted_game[i]) > num_b)):
            result = False

    return (id, result)

def day2_1(filename: str):
    with open(filename, 'r') as my_file:
        valid_games = []
        for line in my_file:
            valid_games.append(evaluate_game(line, 12, 13, 14))

    valid_indexes = [x[0] for x in valid_games if x[1]]
    print(f'The result of day2_2 is: {sum(valid_indexes)}.')
