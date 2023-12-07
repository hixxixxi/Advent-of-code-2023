import re

def main():
    # f = open("day7\example.txt", "r")
    f = open("day7\input.txt", "r")
    input = f.read()

    input = input.split('\n')


    five_kind_card = []
    four_kind_card = []
    full_host = []
    three_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    prize_map =  {}

    for hand in input:
        hand = hand.split(' ')
        bid = hand[1]
        cards = hand[0]

        prize_map.update({cards: bid})

        card_list = {}
        card_to_card = {}

        for card in cards:
            if card_list.get(card) == None:
                card_list.update({card: 1})
            else:
                card_list[card] += 1

        if card_list.get('J') == 5:
            card_to_card.update({cards: cards})
            pass
        elif card_list.get('J') != None:
            
            # card_to_card.update({cards: cards})
            number_of_j = card_list.pop('J')


            highest_occurence = 0
            character = ''
            for key, val in card_list.items():
                if val > highest_occurence:
                    highest_occurence = val
                    character = key
            
            card_list[character] += number_of_j
            new_card = re.sub('J', character, cards)
            card_to_card.update({cards: new_card})
        else :
            card_to_card.update({cards: cards})

        # print(card_to_card)

        if len(card_list) == 1:
            five_kind_card.append(cards)
            continue
        elif len(card_list) == 2:
            if next(iter(card_list.values())) == 1 or next(iter(card_list.values())) == 4:
                four_kind_card.append(cards)
            else:
                full_host.append(cards)
            continue
        elif len(card_list) == 3:
            got_3_kind = False
            for value in card_list.values():
                if value == 3:
                    got_3_kind = True
            if got_3_kind:
                three_kind.append(cards)
                continue
            else:
                two_pair.append(cards)
                continue
        elif len(card_list) == 4:
            one_pair.append(cards)
            continue
        else:
            high_card.append(cards)
            continue

    # print("5-kind:", custom_sort(five_kind_card))
    # print("4-kind:", four_kind_card)
    # print("full houst:", full_host)
    # print("3-kind:", three_kind)
    # print("2 pairs:", two_pair)
    # print("1pair:", one_pair)
    # print("high card:", high_card)

    # print("prizeMap: ", prize_map)

    final_hands = custom_sort(five_kind_card) + custom_sort(four_kind_card) + custom_sort(full_host) + custom_sort(three_kind) + custom_sort(two_pair) + custom_sort(one_pair) + custom_sort(high_card)
    total = 0
    for i in range(len(final_hands)):
        bid = prize_map.get(final_hands[i])
        total = total + (int(bid) * (len(final_hands) - i))

    print(total)
    # print(final_hands)





card_order = ['A', 'K', 'Q',  'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def compare_cards(card):
    return [card_order.index(rank) for rank in card]

def custom_sort(hand):
    return sorted(hand, key=compare_cards)

hands = ['T55J5', 'QQQJA']
sorted_hands = custom_sort(hands)


main()