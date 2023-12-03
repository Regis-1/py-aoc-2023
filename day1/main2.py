import sys

def findall(p, s):
    i = s.find(p)
    while (i != -1):
        yield i
        i = s.find(p, i+1)

def extract_digits_from_file(file):
    digits = []
    word_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for line in file:
        indexes = []
        for wd in word_digits:
            indexes = [*indexes, *[(i, word_digits.index(wd)) for i in findall(wd, line)]]
        for nd in num_digits:
            indexes = [*indexes, *[(i, int(nd)) for i in findall(nd, line)]]
        indexes.sort()
        digits.append(10*indexes[0][1] + indexes[-1][1])

    return digits


def main():
    if (len(sys.argv) <= 1):
        return

    with open(sys.argv[1], 'r') as my_file:
        calib_values = extract_digits_from_file(my_file)

    print(f'The result is: {sum(calib_values)}.')

main()
