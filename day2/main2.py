def evaluate_game(line: str):
    result = True
    splitted_game = line.split(' ')
    splitted_game = splitted_game[2:]
    max_rgb = [0,0,0]
    for i in range(0, len(splitted_game), 2):
        if ('red' in splitted_game[i+1] and int(splitted_game[i]) > max_rgb[0]):
            max_rgb[0] = int(splitted_game[i])
        elif ('green' in splitted_game[i+1] and int(splitted_game[i]) > max_rgb[1]):
            max_rgb[1] = int(splitted_game[i])
        elif ('blue' in splitted_game[i+1] and int(splitted_game[i]) > max_rgb[2]):
            max_rgb[2] = int(splitted_game[i])

    return max_rgb

def day2_2(filename: str):
    with open(filename, 'r') as my_file:
        games_balls = []
        for line in my_file:
            games_balls.append(evaluate_game(line))

    games_power = [x[0]*x[1]*x[2] for x in games_balls]
    print(f'The result of day2_1 is: {sum(games_power)}.')
