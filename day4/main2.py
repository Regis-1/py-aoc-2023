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

def count_scratchcards(numbers):
    for cid in numbers[0]:
        have_winnings = [n for n in numbers[2][cid-1] if n in numbers[1][cid-1]]
        for i in range(len(have_winnings)):
            numbers[0].append(cid+i+1)
    return numbers[0]

def read_input(file):
    input = []
    for line in file.readlines():
        input.append(str(line).rstrip())
    return input

def day4_2(filename: str):
    with open(filename, 'r') as file:
        cards_input = read_input(file)

    cards_numbers = extract_card_numbers(cards_input)
    all_scratchcards = count_scratchcards(cards_numbers)

    print(f'The result of day4_2 is: {len(all_scratchcards)}.')
