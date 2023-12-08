import re
import math

def main():
    # f = open("day8\example.txt", "r")
    f = open("day8\input.txt", "r")
    input = f.readlines()

    instruction = re.sub('\n', '', input.pop(0))
    instruction = instruction * 1000
    input.pop(0)
    print(instruction)
    
    map_moves = {}

    star_pos_p2 = []

    for line in input:
        line = re.sub('\n', '', line)
        
        words = line.split(' = ')
        key = words[0]

        if key[2] == 'A':
            star_pos_p2.append(key)

        values = words[1][1:-1].split(', ')
        instruction_map = (values[0], values[1])

        map_moves.update({key: instruction_map})
        
    

    # print(star_pos_p2)

    multiplier = []

    # for direction in instruction:
    #     new_star_pos = []


    #     for node in star_pos_p2:
    #         choices = map_moves.get(node)
    #         if direction == 'L':
    #             step = choices[0]
    #         else:
    #             step = choices[1]

    #         if step[2] == 'Z':


    #         new_star_pos.append(step)
    #     steps_taken += 1
    #     star_pos_p2 = new_star_pos
    #     print(star_pos_p2)

    #     go_out = True
    #     for node_after in star_pos_p2:
    #         if node_after[2] != 'Z':
    #             go_out = False
        
    #     if go_out:
    #         break
    
    for node in star_pos_p2:
        # print('node: ', node)

        inital = node
        move_to_get = 0
        for direction in instruction:
            # print('direction: ', direction)
            choices = map_moves.get(inital)

            # print(choices)
            if direction == 'L':
                step = choices[0]
            else:
                step = choices[1]

            # print('step: ', step)
            move_to_get += 1
            inital = step
            if step[2] == 'Z':
                multiplier.append(int(move_to_get))
                break
        pass

    print(math.lcm(multiplier[0],multiplier[1],multiplier[2],multiplier[3],multiplier[4]))


    
    # print(steps_taken)

    # print(input)



main()