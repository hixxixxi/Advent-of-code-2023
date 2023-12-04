import re
def main():
    f = open("day4/input.txt", "r")
    input = f.readlines()

    total = 0
    occurence_card = {}
    for i in range(len(input)):
        occurence_card.update({i:1})

    for i in range(len(input)):
        number_of_card = occurence_card.get(i)
        card = input[i]
        number_list = re.sub(r'[|\n]', '',card[(card.find(':') + 2):])
        number_list = re.sub(r'  ', ' ', number_list).split(' ')

        numb_dict = {}
        for number in number_list:
            if numb_dict.get(number) == None:
                numb_dict.update({number: 1})
            else :
                numb_dict[number] += 1
        winning_numb = 0
        for key, val in numb_dict.items():
            if val == 2:
                winning_numb += 1

        if winning_numb > 0:
            for y in range(1, winning_numb + 1):
                if occurence_card.get(y) == None:
                    pass
                else:
                    occurence_card[i + y] += (number_of_card * 1)

        if winning_numb > 0:
            total += 2**(winning_numb - 1)
    total_2 = 0
    for val in occurence_card.values():
        total_2 += val
    
    print(total_2)

main()

