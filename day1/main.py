def extract_digits_from_file(file: str):
    numbers = []
    for line in file:
        digits = [int(x) for x in line if x.isdigit()]
        numbers.append(10*digits[0] + digits[len(digits)-1])

    return numbers

def day1_1(filename: str):
    with open(filename, 'r') as my_file:
        calib_values = extract_digits_from_file(my_file)

    print(f'The result of day1_1 is: {sum(calib_values)}.')
