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
1 = Spadeswe
2 = Clovers
3 = Diamonds
4 = Hearts

#Need to rename functions to _ convention

#sortHand is a function that sorts that hand based on 13's rules
#2 are highes 3 are lowest, S<C<D<H

"""

import sys
from collections import Counter
from PrettyPrintCards import pp_card, print_hidden_cards,join_lines
from random import shuffle
#not using this module anymore
#from sortHand import sort_hand
#from game_state import GameState
from Player import Player
from checkInstantWin import check_for_four_twos_instant_win,check_for_six_pairs_instant_win,check_for_dragon_instant_win
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
            #card_dict['value'] = (card_list.index(card)+1)
            card_dict['value'] = card[0]
            #assign special 'value' for 10
            #if card[0] == '1':
                #card_dict['value'] = '10'
            #assign 'display' value for the card
            card_dict['display'] = (card[0] + suit[0])
            #assign special 'display' for 10
            if card[0] == '1':
                card_dict['display'] = (card + suit[0])
            deck.append(card_dict)
    for card in deck:
        card['value'] = (deck.index(card)+1)
    return deck

#test_deck = create_deck()
#print test_deck

#print display_deck

#to sort, assign each card a spefic value and sort by that value

def shuffle_deck(deck):
    shuffle(deck)
    return deck
#test_deck = create_deck()
#test_deck = shuffle_deck(test_deck)
#pretty_deck = []
#for card in test_deck:
#    pretty_deck.append(card['value'])
#print pretty_deck
#print len(pretty_deck)

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
                return player, list_of_players.index(player)
            #else:

#########################################################################################

#dictionary of key and values to be used to validation straights
card_num_value ={'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'1':8,'J':9,'Q':10,'K':11,'A':12,'2':13}

def check_move_played(moves,player_hand):
    """check move made in validation, to avoid repeating code"""
    #ensure player does not in put same card twice
    move_is_in_player_hand = set(moves) < set(player_hand)
    doubles_check = len(moves) == 2 and moves[0][0] == moves[1][0]
    triples_check = len(moves) == 3 and moves[0][0] == moves[1][0] == moves[2][0]
    quads_check = len(moves) == 4 and moves[0][0] == moves[1][0] == moves [2][0] == moves[3][0]
    #need to make list comprehension to count for 3 pairs and 4 pairs
    three_consecutive_bomb_check = len(moves) == 6 and move_is_in_player_hand
    three_consecutive_bomb_last_move_check = len(moves) == 6 and moves == player_hand
    four_consecutive_bomb_check = len(moves) == 8 and move_is_in_player_hand
    four_consecutive_bomb_last_move_check = len(moves) == 6 and moves == player_hand
    straights_check = len(moves) >= 3 and len(moves) == len(set(moves))
    straights_last_move_check = straights_check and moves == player_hand
    if [k for k,v in Counter(moves).items() if v > 1] != []:
        print "You can't play the same card twice."
        print 'Returning False'
        return False
    elif len(moves) == 1 and move_is_in_player_hand or (len(moves) == 1 and moves == player_hand):
        print 'Valid single card move, returning True'
        print ''
        return True
    #validate doubles
    elif doubles_check and move_is_in_player_hand or (doubles_check and moves[0] in player_hand and moves[1] in player_hand):
        print 'Valid doubles move, returning True'
        print ''
        return True
    #validate triples
    elif triples_check and move_is_in_player_hand or (triples_check and moves[0] in player_hand and moves[1] in player_hand and moves[2] in player_hand):
        print 'Valid triples move, returning True'
        print ''
        return True
    #validate 4 of a kind
    elif quads_check and move_is_in_player_hand or (quads_check and moves[0] in player_hand and moves[1] in player_hand and moves[2] in player_hand and moves[3] in player_hand):
        print 'Valid 4 of a kind move, returning True'
        print ''
        return True
    #FOR first move on first game only, bombs with 3S included are valid
    #this includes 3 consecutive pairs & 4 consecutive pairs
    #might need to split the 4 consecutive pair bomb in a different clause
    elif three_consecutive_bomb_check or four_consecutive_bomb_check or three_consecutive_bomb_last_move_check or four_consecutive_bomb_last_move_check:
        #['JS', 'JD', 'QS', 'QC', 'KS', 'KC']
        #three_consecutive_bomb = ['3','3','4','4','5','5']
        three_consecutive_bomb = [] #list in value form
        three_consecutive_bomb = [card_num_value[moves[0][0]]] * 2  #[1,1]
        #three_consecutive_bomb += card_num_value[str(int(moves[0][0]) + 1)] * 2 #[1,1,2,2]
        three_consecutive_bomb += [card_num_value[moves[0][0]] + 1] * 2
        #three_consecutive_bomb += card_num_value[str(int(moves[0][0]) + 2)] * 2 #[1,1,2,2,3,3]
        three_consecutive_bomb += [card_num_value[moves[0][0]] + 2] * 2
        #four_consecutive_bomb ['3','3','4','4','5','5','6','6']
        four_consecutive_bomb = []
        four_consecutive_bomb = three_consecutive_bomb + [card_num_value[moves[0][0]] + 3] * 2
        #four_consecutive_bomb = three_consecutive_bomb + card_num_value[str(int(moves[0][0]) + 3)] * 2 #[1,1,2,2,3,3,4,4]
        print 'three_consecutive_bomb: ' + str(three_consecutive_bomb)
        print 'four_consecutive_bomb: ' + str(four_consecutive_bomb)
        bomb_compare_list = []
        for card in moves:
            bomb_compare_list.append(card[0]) #[3,3,4,4,5,5]
        print 'bomb_compare_list: ' + str(bomb_compare_list)
        #convert card number list to value list
        value_of_bomb_compare_list = []
        for item in bomb_compare_list:
            value_of_bomb_compare_list.append(card_num_value[item]) #[1,1,2,2,3,3]
        print 'value_of_bomb_compare_list: ' + str(value_of_bomb_compare_list)
        if (set(value_of_bomb_compare_list) < set(three_consecutive_bomb)) and 13 not in value_of_bomb_compare_list:
            print ''
            print 'Valid 3 consecutive pair bomb, returning True'
            print ''
            return True
        elif (set(value_of_bomb_compare_list) < set(four_consecutive_bomb)) and 13 not in value_of_bomb_compare_list:
            print ''
            print 'Valid 4 consecutive pair bomb, returning True'
            print ''
            return True
        else:
            print ''
            print 'Invalid bomb played. Please try again.'
            print ''
            return False
    #validate straights:: at least 3 cards long, consecutive, high card decides rank
    elif straights_check and move_is_in_player_hand or straights_last_move_check :
        print 'in straights validation'
        #validate_straights(moves)
        card_num_list = []
        value_list = []
        #moves = ['3S', '5D', '6C']
        for card in moves:
            card_num_list.append(card[0])
            #['3','5','6']
        for num in card_num_list:
            value_list.append(card_num_value[num])
            #[1,3,4]
        print 'value list ' + str(value_list)
        compare_list = []
        for n in range(len(value_list)):
            compare_list += [value_list[0] + n ]
        print 'compare list ' + str(compare_list)
        #ensure 2 can not be in straights
        #compare_list = sorted(card_num_value.values())
        #print compare_list[len(value_list)]
        if compare_list == sorted(value_list) and 13 not in value_list and 13 not in compare_list:
            print ''
            print 'Valid Straight, returning True'
            print ''
            return True
        else:
            print ''
            print 'Invalid Straight, returning False'
            print ''
            return False


def validate_move(Player, moves, game_state):
    """
    Player:: Player object, player that is making the move
    moves:: list of cards, move that this Player is making
    current_board:: list of cards, current board that player has to be beat,
    is being used to against Player's move to be validated
    """
    #check highest suit beats this suit
    #check value singles
    #check value doubles
    #check value in straights
    #check value in triples
    #bombs
    #check for valid move
        #beats the current board
        #if first move has to include 3S
        #match len of current board
    """ special rule for 4 consecutive pairs bomb:
    they can bomb anytime and best 4 of a kind and 3 consecutive pairs
    """
    #check card count is the same
    #if Player.status is True and Player.shut_down is False and len(moves) == len(current_board):
        #return 'True'
    #else:
        #return 'False'
    #first turn validation
    #check if very first turn, and 3S has been played
    first_game = game_state.first_game
    #print 1
    #print moves
    #Player.show_hand()
    player_hand = Player.list_hand()
    #print 2
    #print player_hand
    if first_game is True and '3S' not in moves:
        print 'It is the very first game. Please play something with a 3 of Spades (3S).'
        return False
    elif first_game is True and '3S' in moves: #validating move if it is the game
        return check_move_played(moves,player_hand)
    #when player plays their last move before getting an empty hand
    elif first_game is False and len(Player.Hand) == len(moves) and check_move_played(moves,player_hand) is True:
        print 'here 1'
        print 'You have finished your hand.'
        #if check_move_played(moves,player_hand) is True:
            #print 'here 2'
        #change hand empty to true
        game_state.list_of_players[game_state.player_index].hand_empty = True
        #update player_done count
        game_state.players_done += 1
        #assign the index of the winner to their placing
        if game_state.players_done == 1:
            game_state.first_place = game_state.player_index
        elif game_state.players_done == 2:
            game_state.second_place = game_state.player_index
        elif game_state.players_done == 3:
            game_state.third_place = game_state.player_index
        elif game_state.players_done == 4:
            game_state.fourth_place = game_state.player_index
        return check_move_played(moves,player_hand)
        #game_state.next_player()
    #when it is not first move of the first game anymore
    elif first_game is False:
        return check_move_played(moves,player_hand)
    else:
        print 'INVALID MOVE, returning False'
        return False

def post_move(Player,player_hand):
    """prints the player that just went hand in hidden mode
    and tells them to pass it to the next player """
    print 'inside post move: ' + str(Player.hand_empty)
    if Player.hand_empty is False:
        print 'Player ' + str(Player.ID) + ' has ' + str(len(player_hand)) + ' cards left:'
        print_hidden_cards(player_hand)
    else:
        print 'Player ' + str(Player.ID) + ' finshed their hand. '
    #print current_board
    response = None
    #change the to next player id for printing purposes
    printed_ID = Player.ID
    if printed_ID == 4:
        printed_ID = 1
    else:
        printed_ID += 1
    while response not in {'ok'}:
        print "It is the next player's turn. Please pass it to them."
        response = raw_input('Player ' + str(printed_ID) + ' ready to go? ')
        if response in {'k','ok'}:
            return True
        elif response in {'exit'}:
            sys.exit()
        else:
            print 'Please enter ok or k. '

def print_current_board(moves):
    """this function takes list of moves and convert it to list of cards
    so it can be used to be pretty printed"""
    deck = create_deck()
    #print deck

    #[d for d in a if d['name'] == 'pluto']
    #[card for card in deck if deck['display'] == move]
    #to_be_printed = [card for card in deck if deck['display'] == moves]
    to_be_printed = []
    for move in moves:
        to_be_printed += [card for card in deck if card['display'] == move]
    print 'This is the current board: '
    return pp_card(to_be_printed)


def print_turn(Player,game_state):
    print '=============================================================================='
    print 'It is Player '+str(Player.ID)+' turn.'
    print 'Player_hand_empty: ' + str(Player.hand_empty)
    print '# of Players done: ' + str(game_state.get_number_of_players_done())
    if game_state.players_done == 4:
        print 'The game is done.'
        game_state.game_is_over = True
        return
    if Player.hand_empty is True:
        #need to check for the case where all hands are empty
        print print_current_board(game_state.current_board)
        game_state.next_player()
        next_player_obj = game_state.list_of_players[game_state.player_index]
        print_turn(next_player_obj,game_state)
    print pp_card(Player.Hand)
    move_validated = False
    while move_validated is False:
        moves = raw_input("\nPlease enter your move : ").upper().split(',')
        str(moves)
        moves = filter(None, moves)
        moves = [move.strip() for move in moves]
        print 'this is the move made: ' +  str(moves)
        print ''
    #validate the move first then change
        if moves == []:
            print 'Plese enter a valid move, Player ' + str(Player.ID)+ '.'
            print pp_card(Player.Hand)
            continue
        elif moves[0] == 'EXIT':
            sys.exit()
        #allows player to pass
        # ^ this function is not working properly
        elif moves[0] == 'PASS':
            check_for_3s = [card for card in Player.Hand if card['display'] == '3S']
            #print Player.Hand
            #check
            #print check_for_3s
            #print check_for_3s[0]['display']
            #if statement to check if player has 3s and current_board is empty
            if check_for_3s == []:
                print print_current_board(game_state.current_board)
                game_state.next_player()
                next_player_obj = game_state.list_of_players[game_state.player_index]
                print_turn(next_player_obj,game_state)
            elif '3S' == check_for_3s[0]['display'] and game_state.current_board == []:
                print "You can't pass. You are the player going first. "
                print pp_card(Player.Hand)
            else:
                print print_current_board(game_state.current_board)
                game_state.next_player()
                next_player_obj = game_state.list_of_players[game_state.player_index]
                print_turn(next_player_obj,game_state)
        elif validate_move(Player, moves, game_state) is True:
            #game_state.current_board
            #needs a function to convert list of moves to acutal list of cards
            #so the cards can be printed
            game_state.current_board = moves
            print print_current_board(game_state.current_board)
            #take out the cards played
            Player.Hand = [card for card in Player.Hand if card['display'] not in moves]
            #print Player.Hand
            #print len(Player.Hand)
            game_state.next_player()
            print 'hand_empty is ' + str(game_state.list_of_players[game_state.player_index].hand_empty)
            #checks if player had already finished their hand
            if game_state.list_of_players[game_state.player_index].hand_empty is True:
                game_state.next_player()
                next_player_obj = game_state.list_of_players[game_state.player_index]
                print_turn(next_player_obj,game_state)
            #????
            #elif len(Player.Hand) == len(moves):
                #game_state.list_of_players[game_state.player_index].hand_empty = True
                #game_state.next_player()
            #print face down hand and ask to next player to get ready
            elif post_move(Player,Player.Hand) is True:
            #update game_state and let next player play
            #next_player_index
            #print next_player_index
            #print type(next_player_index)
            #print game_state.list_of_players
            #change to next player
                next_player_obj = game_state.list_of_players[game_state.player_index]
                game_state.first_game = False
                print_turn(next_player_obj,game_state)
            #move_validated = validate_move(Player, moves, game_state)
        else:
            print 'It is an invalid move. Please try again.'
            print pp_card(Player.Hand)
    #Player.Hand = new_hand
    #print ''

    #game_state.current_board = Player.Hand
    #print game_state.get_current_board()
    #print len(game_state.get_current_board())







""" game engine:
while loop where exit != True
checks for instant wins
if not start
check if very first game
prompt for player move input
validate move input
update board
print updated board
change player
...
...
end game once one player runs out of cards
"""
