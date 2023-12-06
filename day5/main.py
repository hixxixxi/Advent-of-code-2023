import re

def main():
    f = open("day5\input.txt", "r")
    input = f.readlines()
    i = 0
    list = [[] for _ in range(8)]
    for line in input:
        numbers = re.search(r'\d+(?:\s+\d+)*', line)
        if numbers:
            extracted_numbers = numbers.group()
            extracted_numbers = re.sub('\n', '', extracted_numbers)
            list[i].append(extracted_numbers)
        else:
            i += 1

    seeds = list.pop(0)[0].split(' ')
    seeds = [int(num) for num in seeds]

    seeds_range = []
    for i in range(0, len(seeds), 2): 
        seeds_range.append([seeds[i], seeds[i] + seeds[i+1]])

    # Out of memory solution hahahaha
    # initial_sources = [int(num) for num in seeds]
    # for connection in list:
    #     map_connect = calculateRange(connection)
    #     new_source_list = []
    #     for initial_source in initial_sources:
    #         if map_connect.get(int(initial_source)) != None:
    #             new_source_list.append(map_connect.get(int(initial_source)))
    #         else:
    #             new_source_list.append(initial_source)

    #     initial_sources = new_source_list
    #     initial_sources = [int(num) for num in seeds]

    # for connection in list:
    #     map_connect = calculateRange(connection)
    #     new_source_list = []
    #     for initial_source in initial_sources:
    #         if map_connect.get(int(initial_source)) != None:
    #             new_source_list.append(map_connect.get(int(initial_source)))
    #         else:
    #             new_source_list.append(initial_source)

    #     initial_sources = new_source_list

    for object_map in list:
        new_seeds = []
        for seed in seeds:
            new_seeds.append(find_in_list(int(seed), object_map))
        seeds = new_seeds
    
    print(min(seeds))


def find_in_list(seed, list):
    for value in list:
        value_list = [int(num) for num in value.split(' ')]
        new_seed = find_if_belong(int(seed), value_list)
        if new_seed != 0:
            return new_seed
    return seed


def find_if_belong(seed, array):
    if  array[1] <= seed <= (array[1] + array[2]):
        new_seed = seed - array[1] + array[0]
        return new_seed
    return 0

def calculateRange(input):
    number_map = {}
    for line in input:
        list = line.split(' ')
        destination = int(list[0])
        source = int(list[1])
        ranges = int(list[2])

    
        for i in range(ranges):
            number_map.update({source + i: destination + i})

    # for i in range(1,100):
    #     if number_map.get(i) == None:
    #         number_map.update({i:i})
    return number_map

main()

