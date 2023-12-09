import re

def main():
    # f = open("day9\example.txt", "r")
    f = open("day9\input.txt", "r")
    input = f.read().split('\n')

    # print([int(numb) for numb in (input[0].split(' '))])

    total = 0
    for line in input:
        last_array = find_next_numb([int(numb) for numb in (line.split(' '))])
        total += last_array[0]

    print(total)


    # print(input)

def find_next_numb(numb_list):

    if all(numb == 0 for numb in numb_list):
        numb_list.append(0)
        return numb_list

    # print(numb_list)
    new_numb_list = []
    for i in range(len(numb_list)):
        # print("i = ", i)
        # print("len(numb) = ", len(numb_list))

        if i == (len(numb_list) - 1):
            break
        
        gap = numb_list[i + 1] - numb_list[i]
        new_numb_list.append(gap)

    return_list = find_next_numb(new_numb_list)
    numb_list.insert(0, numb_list[0] - return_list[0] )
    print(numb_list)

    return numb_list

# a = [1,2,3].append(4)
# print(a)

main()