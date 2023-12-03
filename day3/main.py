import array
import re

def main():
    f = open("day3\input.txt", "r")
    input = f.read()
    result_string = re.sub(r'[^0-9.\n]', '$', input)
    f.close()

    input_1 = result_string.split("\n")
    input_2 = input.split("\n")

    part_1(make_martrix(input_1))
    part_2(make_martrix(input_2))
    
def make_martrix(input):
    martrix = []
    for i in range(len(input)):
        line = input[i]
        line_array = []
        for character in line:
            line_array.append(character)
        
        martrix.append(line_array)
    return martrix


def check(y, x, martrix):
    if y <= 0 and x <= 0 and y > len(martrix) and x > len(martrix[0]):
        return 0
    value = martrix[y][x]
    if value.isnumeric():
        number = value
        martrix[y][x] = "X"
        left_number = check_number_left(y, x-1, martrix) #check left
        right_number = check_number_right(y, x+1, martrix) #check right
        return left_number + number + right_number
    else:
        return 0

def check_number_left(y,x,martrix):
    if x < 0:
        return ''
    value = martrix[y][x]
    if value == '.' or value == '':
        return ''
    
    if value.isnumeric():
        return_value = value
        martrix[y][x] = "X"
        return check_number_left(y,x-1,martrix) + return_value
    else:
        return ''
    
def check_number_right(y,x,martrix):
    if x > (len(martrix[0]) -1):
        return ''
    value = martrix[y][x]
    if value == '.' or value == '':
        return ''
    
    if value.isnumeric():
        return_value = value
        martrix[y][x] = "X"
        return return_value + check_number_right(y,x+1,martrix)
    else:
        return ''
    
def part_1(martrix):
    sum = 0
    for y in range(0, len(martrix)):
        for x in range(0, len(martrix[0])):
            if martrix[y][x] == "$":
                sum += (int(check(y-1,x-1,martrix)) # top left
                + int(check(y-1,x,martrix)) # top
                + int(check(y-1,x+1,martrix)) # top right
                + int(check(y,x+1,martrix)) # mid right
                + int(check(y+1,x+1,martrix)) # bot right
                + int(check(y+1,x,martrix)) # bot 
                + int(check(y+1,x-1,martrix)) # bot left
                + int(check(y,x-1,martrix))) # mid left
                
    print(sum)

def part_2(martrix):
    sum = 0
    for y in range(0, len(martrix)):
        for x in range(0, len(martrix[0])):
            if martrix[y][x] == "*":
                number_set = {int(check(y-1,x-1,martrix)), int(check(y-1,x,martrix)), int(check(y-1,x+1,martrix)),int(check(y,x+1,martrix)), int(check(y+1,x+1,martrix)),int(check(y+1,x,martrix)),int(check(y+1,x-1,martrix)), int(check(y,x-1,martrix))}
                if len(number_set) == 3:
                    number_set.remove(0)
                    ratio = 1
                    for number in number_set:
                        ratio = ratio * number

                    sum += ratio
    print(sum)

main()