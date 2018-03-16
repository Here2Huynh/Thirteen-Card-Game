"""
Somethings is wrong with the data structure of the cards.
Need to think of more elegant way for easier card rank comparison.
Example card data structure (dict):
{
    'name' : 'Queen',
    'suit' : 'Clubs'
    'value' : 12,
    'suit_value' : 2
    'display' : 'QC'
}

value for card comparison -> Queens > 10
suit_ value for suit comparison -> Clovers > Spades
1 = Spades
2 = Clovers
3 = Diamonds
4 = Hearts

#Need to rename functions to _ convention

#sortHand is a function that sorts that hand based on 13's rules
#2 are highes 3 are lowest, S<C<D<H

"""


from random import shuffle
#not using this module anymore 
#from sortHand import sort_hand
#from game_state import GameState
from Player import Player
from checkInstantWin import check_for_instant_win
from gameState import game_state 

def create_deck():
    """
    deck = list of dict() = list of cards
    suit_list = list of str = all possible suits
    card_list = list of str = all possible cards in deck
    """
    deck = []
    suit_list = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    card_list = ['3', '4', '5', '6', '7',
                 '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2']
    for card in card_list:
        for suit in suit_list:
            card_dict = {} #make dict to represent card
            card_dict['name'] = card #make the card
            card_dict['suit'] = suit #assign it a suit
            #assign card value 
            card_dict['value'] = card[0]
            card_dict['display'] = (card[0] + suit[0])
            #assign special 'display' for 10
            if card[0] == '1':
                card_dict['display'] = (card + suit[0])
            deck.append(card_dict)
    for card in deck:
        card['value'] = (deck.index(card)+1)
    return deck


#to sort, assign each card a spefic value and sort by that value 
    
def shuffle_deck(deck):
    shuffle(deck)
    return deck

    
def deal_hand(deck,hand_size):
    """
    make a list of 13 cards for a players hand
    :param deck: list
    :param hand_size: 13
    :return: list
    """
    hand=[]
    for i in range(hand_size):
        hand.append(deck.pop())
        #technically deals from the bottom of deck
    return hand

def find_first_player(list_of_players):
    """ finds player to go first FOR THE VERY FIRST STARTING GAME
    in which is the player with the 3S (three of spades)
    list_of_players = list of Player objects 
    """
    for player in list_of_players:
        for card in player.Hand:
            if card['value'] == 1:
                print 'Player ' + str(player.get_ID()) + ' has 3S. Player ' + str(player.get_ID()) + ' goes first.'
                #set game_state to first player who has 3S
                #start game 
                return
            #else:
            
##########################

def printTurn(Player):
    print '========================================'
    print 'It is Player'+str(Player.ID)+' turn.'
    print Player.Hand
    for card in Player.Hand:
        print '|'+card+'|',

    move = raw_input("\nPlease enter your move : ")
    str(move)
    print move

#def checkValidMove(currentBoard,PlayerMove):
    #check card count is the same
    #check highest suit beats this suit


