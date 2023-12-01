import sys

def extract_digits_from_file(file):
    numbers = []
    for line in file:
        digits = [int(x) for x in line if x.isdigit()]
        numbers.append(10*digits[0] + digits[len(digits)-1])

    return numbers


def main():
    if (len(sys.argv) <= 1):
        return

    with open(sys.argv[1], 'r') as my_file:
        calib_values = extract_digits_from_file(my_file)

    print(f'The result is: {sum(calib_values)}.')

main()
