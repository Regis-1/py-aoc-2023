def read_input(file):
    input = []
    for line in file.readlines():
        input.append(str(line).rstrip())
    return input

def day4_2(filename: str):
    with open(filename, 'r') as file:
        cards_input = read_input(file)

day4_2('inp_test.txt')
