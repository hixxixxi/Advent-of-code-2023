import re

def main():
    f = open("day1\input1.txt", "r")
    input_text = f.read()
    f.close()

    number_map = {
        "twone": "twoone",
        "oneight": "oneeight",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, number in number_map.items():
        input_text = re.sub(word, number, input_text)
        
    num_list = input_text.split("\n")

    total = 0
    for num in num_list:
        total += int(get_two_digit_number(num))


    print("Total Part 2 = ", total)

def get_two_digit_number(input):
    number_only = re.sub("[a-zA-Z\n]", "", input)
    return number_only[0] + number_only[-1]

main()