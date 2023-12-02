import re

def main():
    # Part 1
    f = open("/Users/aiden/Documents/Git/Advent-of-code-2023/day1/input1.txt", "r")
    input = f.readlines()
    f.close()

    total = 0
    for line in input:
        total += int(get_two_digit_number(line))

    print("Total Part 1 = ", total)

def get_two_digit_number(input):
    number_only = re.sub("[a-zA-Z\n]", "", input)
    return number_only[0] + number_only[-1]

main()