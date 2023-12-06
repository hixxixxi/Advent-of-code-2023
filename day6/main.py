def main():
    # time = [52,94,75,94]
    # distance = [426, 1374, 1279, 1216]
    # time = [7]
    # distance = [9]

    # time = [71530]
    # distance = [940200]

    time = [52947594]
    distance = [426137412791216]

    way_to_win_all = []
    for i in range (len(time)):
        way_to_win = 0
        for distance_per_second in range (1, time[i] + 1):
            # print("distance per second: ", distance_per_second)
            distance_travel = distance_per_second * (time[i] - distance_per_second)
            # print("distance travel:", distance_travel)
            if distance_travel > distance[i]:
                way_to_win += 1
        way_to_win_all.append(way_to_win)
    print(way_to_win_all)

    total = 1
    for way_to_win in way_to_win_all:
        total = total * way_to_win

    print(total)

main()