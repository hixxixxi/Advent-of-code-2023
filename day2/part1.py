import re
red_max = 12
green_max = 13
blue_max = 14

def main():
    f = open("/Users/aiden/Documents/Git/Advent-of-code-2023/day2/input1.txt", "r")
    input = f.read()
    input = re.sub("Game ", "", input)
    list = input.split("\n")

    total_part_1 = 0
    total_part_2 = 0
    for item in list:
        biggest_red = 0
        biggest_green = 0
        biggest_blue = 0
        game = item.split(":")
        turns = game[1].split(";")
        for turn in turns:
            sets = turn.split(",")
            for set in sets:
                if(set.find(" blue") > 0):
                    blue = re.sub(" blue", "", set)
                    if (int(blue) > biggest_blue):
                        biggest_blue = int(blue)

                elif(set.find(" red") > 0):
                    red = re.sub(" red", "", set)
                    if (int(red) > biggest_red):
                        biggest_red = int(red)
                        

                elif(set.find(" green") > 0):
                    green = re.sub(" green", "", set)
                    if (int(green) > biggest_green):
                        biggest_green = int(green)
                        
        # print("biggest_blue: ", biggest_blue)
        # print("biggest_red: ", biggest_red)
        # print("biggest_green: ", biggest_green)

        # Part 1
        if biggest_red <= red_max and biggest_blue <= blue_max and biggest_green <= green_max:
            total_part_1 += int(game[0])

        # Part 2
        power = biggest_green * biggest_blue * biggest_red
        total_part_2 += power



    print("Total Part 1: ", total_part_1)
    print("Total Part 2: ", total_part_2)

    f.close()

main()
