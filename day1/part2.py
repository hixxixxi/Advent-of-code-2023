import re

def main():
    f = open("/Users/aiden/Documents/Git/Advent-of-code-2023/day1/input1.txt", "r")
    input_text = f.read()
    print(input_text)
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
    print(num_list)

    total = 0
    for num in num_list:
        print(int(get_two_digit_number(num)))
        total += int(get_two_digit_number(num))


    print("Total Part 2 = ", total)

def get_two_digit_number(input):
    number_only = re.sub("[a-zA-Z\n]", "", input)
    return number_only[0] + number_only[-1]

main()