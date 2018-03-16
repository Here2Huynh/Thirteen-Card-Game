#!/usr/bin/env python
#game_executor
# this module will call all the neccessary fucntions to get the game running

import sys
from gameLogic import create_deck,shuffle_deck,deal_hand,find_first_player,print_turn
from checkInstantWin import check_for_four_twos_instant_win,check_for_six_pairs_instant_win,check_for_dragon_instant_win
from Player import Player
from gameState import game_state
from Rules import rules
from Help import Help
from PrettyPrintCards import pp_card,print_hidden_cards, join_lines

print "Welcome! Let's play a game of 13 shall we?"
response = None
while response not in {'ok', 'k'}:
    response = raw_input("Please enter OK, Rules, Help: ").lower()
    response = response.strip()
    if response in {'rules', 'r'}:
        print rules
    elif response in {'help', 'h'}:
        print Help
    elif response in {'exit'}:
        sys.exit()

print ''
print "Shuffling deck..."
print ''
print "Dealing hand..."
print''

#creates the deck
deck =  create_deck()
#print deck
#print deck
display_deck = []
for card in deck:
    display_deck.append(card['display'])
print('normal deck = ' + str(display_deck))
#print len(display_deck)
print ''

#prints a list of cards in their value form
value_deck = []
for card in deck:
    value_deck.append(card['value'])
print('list value of each card: ' + str(value_deck))
print ''

#shuffle the deck
deck = shuffle_deck(deck)
display_shuffled_deck = []
for card in deck:
    display_shuffled_deck.append(card['display'])
print('shuffled deck = ' + str(display_shuffled_deck))
print ''
print 'card count of shuffled deck = ' + str(len(display_shuffled_deck))
print ''




#instantiate the 4 players
#need to set points to 10k in the very first game only (do in game_state)
Player1 = Player(1, deal_hand(deck,13))
Player2 = Player(2, deal_hand(deck,13))
Player3 = Player(3, deal_hand(deck,13))
Player4 = Player(4, deal_hand(deck,13))

#sort then print all players' hands
print "Player 1's Hand"
Player1.sort_hand()
Player1.show_hand()
pp_card(Player1.Hand)
print_hidden_cards(Player1.Hand)
print ''

print "Player 2's Hand"
Player2.sort_hand()
Player2.show_hand()
pp_card(Player2.Hand)
print_hidden_cards(Player2.Hand)
print ''

print "Player 3's Hand"
Player3.sort_hand()
Player3.show_hand()
pp_card(Player3.Hand)
print_hidden_cards(Player3.Hand)
print ''

print "Player 4's Hand"
Player4.sort_hand()
Player4.show_hand()
pp_card(Player4.Hand)
print_hidden_cards(Player4.Hand)
print ''


#TEST HANDS FOR INSTANT WIN CONDITIONS
#four_twos_hand = ['3H', '4C', '4H', '6S', '8C', '9C', 'QS', 'QC', 'QD', '2D', '2C', '2S', '2H']
#print Player2.Hand
#four_twos_test = [{'display': 'QH', 'name': 'Queen', 'value': 40, 'suit': 'Hearts'}, {'display': 'KS', 'name': 'King', 'value': 41, 'suit': 'Spades'}, {'display': 'KC', 'name': 'King', 'value': 42, 'suit': 'Clubs'}, {'display': 'KD', 'name': 'King', 'value': 43, 'suit': 'Diamonds'}, {'display': 'KH', 'name': 'King', 'value': 44, 'suit': 'Hearts'}, {'display': 'AS', 'name': 'Ace', 'value': 45, 'suit': 'Spades'}, {'display': 'AC', 'name': 'Ace', 'value': 46, 'suit': 'Clubs'}, {'display': 'AD', 'name': 'Ace', 'value': 47, 'suit': 'Diamonds'}, {'display': 'AH', 'name': 'Ace', 'value': 48, 'suit': 'Hearts'}, {'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}, {'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clubs'}, {'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'}, {'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'}]
#Player2.Hand = four_twos_test
#print "Four 2's Test Hand"
#Player2.show_hand()
#print ''
#six_pairs_test = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clubs'}, {'display': '3D', 'name': '3', 'value': 3, 'suit': 'Diamonds'}, {'display': '3H', 'name': '3', 'value': 4, 'suit': 'Hearts'}, {'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '4D', 'name': '4', 'value': 7, 'suit': 'Diamonds'}, {'display': '4H', 'name': '4', 'value': 8, 'suit': 'Hearts'}, {'display': '5S', 'name': '5', 'value': 9, 'suit': 'Spades'}, {'display': '5C', 'name': '5', 'value': 10, 'suit': 'Clubs'}, {'display': '5D', 'name': '5', 'value': 11, 'suit': 'Diamonds'}, {'display': '5H', 'name': '5', 'value': 12, 'suit': 'Hearts'}, {'display': '6S', 'name': '6', 'value': 13, 'suit': 'Spades'}]
#Player3.Hand = six_pairs_test
#print ''
#Player3.show_hand()
#dragon_test = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'},{'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '5H', 'name': '5', 'value': 12, 'suit': 'Hearts'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'},{'display': '7S', 'name': '7', 'value': 17, 'suit': 'Spades'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '9D', 'name': '9', 'value': 27, 'suit': 'Diamonds'}, {'display': '10S', 'name': '10', 'value': 29, 'suit': 'Spades'}, {'display': 'JD', 'name': 'Jack', 'value': 35, 'suit': 'Diamonds'}, {'display': 'QC', 'name': 'Queen', 'value': 38, 'suit': 'Clubs'}, {'display': 'KD', 'name': 'King', 'value': 43, 'suit': 'Diamonds'}, {'display': 'AC', 'name': 'Ace', 'value': 46, 'suit': 'Clubs'}, {'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'}]
#Player1.Hand = dragon_test

#make a list of players for later use
list_of_players = [Player1, Player2, Player3, Player4]


#check_for_instant_win(list_of_players)
player_going_first = Player
index_of_player = int

check1,player_that_won,two_count = check_for_four_twos_instant_win(list_of_players)
check2 = check_for_six_pairs_instant_win(list_of_players)
check3 = check_for_dragon_instant_win(list_of_players)
print check1, check2, check3

if check1 or check2 or check3:
    print 'Instant win.'
else:
    player_going_first, index_of_player = find_first_player(list_of_players)

print player_going_first
print index_of_player
print type(index_of_player)
#print ''
#print player_going_first


#set the gamestate
#player going first
#player order = player turn +1

#instantiate the 'first game' gamestate
is_first_game = True
#new_board = []
#got to instantiate all variables separately
very_first_game = game_state()
very_first_game.first_game = is_first_game #it is first game
very_first_game.game_is_over = False
very_first_game.round_is_won = False
very_first_game.Turn = player_going_first
very_first_game.current_board = [] #new board
very_first_game.list_of_players = list_of_players
very_first_game.player_index = index_of_player


#print turn of first player
while very_first_game.game_is_over == False:
    print_turn(player_going_first,very_first_game)

if very_first_game.game_is_over == True:
    #update points
    #start new game
    new_game = game_state()
