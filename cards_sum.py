on_hand = [2, 3, 4, 10, 'Q', 5]
cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}

cards_sum = sum([cards[x] for x in on_hand])
print(cards_sum)