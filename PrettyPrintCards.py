#pretty print hand / text UI
#from gameLogic import create_deck


CARD = """\
┌────┐
│{}  │
│ {}  │
│  {}│
└────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD = """\
┌────┐
│░░░░│
│░░░░│
│░░░░│
└────┘
"""



def join_lines(strings):
    """ """
    linesS = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*linesS))


def pp_card(deck):
    """ """ 
    name_to_symbol = {
    'Spades':   '♠',
    'Diamonds': '♦',
    'Hearts':   '♥',
    'Clubs':    '♣',
    }
    #print cards
    for card in deck:
        def card_to_string(card):
            #print card
        
            #10 is the only card with a 2 character rank abbreviation
            rank = card['name'] if card['name'] == '10' else card['name'][0]

            #add the individual card on a line by line basis
            return CARD.format(rank = rank, suit = name_to_symbol[card['suit']])

    print join_lines(map(card_to_string, deck))

def print_hidden_cards(deck):
    """ """
    for card in deck:
        def card_to_string(card):
            #10 is the only card with a 2 character rank abbreviation
            rank = card['name'] if card['name'] == '10' else card['name'][0]

            #add the individual card on a line by line basis
            return HIDDEN_CARD.format('░')
    print join_lines(map(card_to_string, deck))

"""
def pp_card(*cards):
    name_to_symbol = {
    'Spades':   '♠',
    'Diamonds': '♦',
    'Hearts':   '♥',
    'Clubs':    '♣',
    }
    #print cards        
    def card_to_string(card):
        print card
        
        #10 is the only card with a 2 character rank abbreviation
        rank = card['name'] if card['name'] == '10' else card['name'][0]

        #add the individual card on a line by line basis
        return CARD.format(rank = rank, suit = name_to_symbol[card['suit']])

    return join_lines(map(card_to_string, cards))
"""

""""
#test cases
deck = create_deck()
test_card_1 = deck[28]
#print test_card_1
test_hand = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'},{'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '5H', 'name': '5', 'value': 12, 'suit': 'Hearts'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'},{'display': '7S', 'name': '7', 'value': 17, 'suit': 'Spades'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '9D', 'name': '9', 'value': 27, 'suit': 'Diamonds'}, {'display': '10S', 'name': '10', 'value': 29, 'suit': 'Spades'}, {'display': 'JD', 'name': 'Jack', 'value': 35, 'suit': 'Diamonds'}, {'display': 'QC', 'name': 'Queen', 'value': 38, 'suit': 'Clubs'}, {'display': 'KD', 'name': 'King', 'value': 43, 'suit': 'Diamonds'}, {'display': 'AC', 'name': 'Ace', 'value': 46, 'suit': 'Clubs'}, {'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'}] 

four_twos_test = [{'display': 'QH', 'name': 'Queen', 'value': 40, 'suit': 'Hearts'}, {'display': 'KS', 'name': 'King', 'value': 41, 'suit': 'Spades'}, {'display': 'KC', 'name': 'King', 'value': 42, 'suit': 'Clubs'}, {'display': 'KD', 'name': 'King', 'value': 43, 'suit': 'Diamonds'}, {'display': 'KH', 'name': 'King', 'value': 44, 'suit': 'Hearts'}, {'display': 'AS', 'name': 'Ace', 'value': 45, 'suit': 'Spades'}, {'display': 'AC', 'name': 'Ace', 'value': 46, 'suit': 'Clubs'}, {'display': 'AD', 'name': 'Ace', 'value': 47, 'suit': 'Diamonds'}, {'display': 'AH', 'name': 'Ace', 'value': 48, 'suit': 'Hearts'}, {'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}, {'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clubs'}, {'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'}, {'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'}]
six_pairs_test = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clubs'}, {'display': '3D', 'name': '3', 'value': 3, 'suit': 'Diamonds'}, {'display': '3H', 'name': '3', 'value': 4, 'suit': 'Hearts'}, {'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '4D', 'name': '4', 'value': 7, 'suit': 'Diamonds'}, {'display': '4H', 'name': '4', 'value': 8, 'suit': 'Hearts'}, {'display': '5S', 'name': '5', 'value': 9, 'suit': 'Spades'}, {'display': '5C', 'name': '5', 'value': 10, 'suit': 'Clubs'}, {'display': '5D', 'name': '5', 'value': 11, 'suit': 'Diamonds'}, {'display': '5H', 'name': '5', 'value': 12, 'suit': 'Hearts'}, {'display': '6S', 'name': '6', 'value': 13, 'suit': 'Spades'}]



pp_card(test_hand)
print_hidden_cards(test_hand)

pp_card(four_twos_test)
print_hidden_cards(four_twos_test)


pp_card(six_pairs_test)
print_hidden_cards(six_pairs_test)


"""



