def extract_card_numbers(input):
    cards_id = [int(line.split(':')[0].split(' ')[-1]) for line in input]
    winning_numbers = []
    have_numbers = []
    for numbers in [line.split(':')[1] for line in input]:
        winning_numbers.append(
            [int(x) for x in numbers.split('|')[0].split(' ') if x != '']
        )
        have_numbers.append(
            [int(x) for x in numbers.split('|')[1].split(' ') if x != '']
        )
    return (cards_id, winning_numbers, have_numbers)

def count_winning_points(numbers):
    points = []
    for cid in numbers[0]:
        have_winnings = [n for n in numbers[2][cid-1] if n in numbers[1][cid-1]]
        if len(have_winnings) > 0:
            points.append(2**(len(have_winnings)-1))
    return points

def read_input(file):
    input = []
    for line in file.readlines():
        input.append(str(line).rstrip())
    return input

def day4_1(filename: str):
    with open(filename, 'r') as file:
        cards_input = read_input(file)

    cards_numbers = extract_card_numbers(cards_input)
    points = count_winning_points(cards_numbers)

    print(f'The result of day4_1 is: {sum(points)}.')
