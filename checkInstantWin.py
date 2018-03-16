#check for instant module
# there are 3 conditions for instant win
# 1. 4 2's
# 2. dragon
# 3. 6 pairs and a single card

import sys
from collections import Counter

def check_for_four_twos_instant_win(list_of_players):
    """ """
    #4 2's
    #check for the presence of 4 2's and different suits
    #check for all 13 cards are still in hand
    #all cards have different values
    for player in list_of_players:
        #player.show_hand()
        #print len(list_of_players)
        four_twos_counter = 0
        for card in player.Hand:
            #print card
            #print four_twos_counter and if there is 13 cards in your hand
            if card['display'] == '2S' and card['value'] == 49 and len(player.Hand) == 13:
                four_twos_counter += 1
            elif card['display'] == '2C' and card['value'] == 50 and len(player.Hand) == 13:
                four_twos_counter += 1
            elif card['display'] == '2D' and card['value'] == 51 and len(player.Hand) == 13:
                four_twos_counter += 1
            elif card['display'] == '2H' and card['value'] == 52 and len(player.Hand) == 13:
                four_twos_counter += 1
            #print four_twos_counter
        if four_twos_counter == 4:
            print 'Player ' + str(player.get_ID())+ " got an instant win with four 2's!"
            #set next game's first player to this player
            #add and subtract points
            #restart game
            #player.sort_hand()
            player.show_hand()
            return True
            sys.exit()

def check_for_six_pairs_instant_win(list_of_players):
    """ """
    # 6 pairs
    #check if there is 13 cards in card FIRST
    for player in list_of_players:
        if len(player.Hand) == 13:
            pair_count = 0
            pair_list = []
            for card in player.Hand:
                pair_list.append(card['display'][0])
            #print '6_doubles_pair_list= ' + str(pair_list)
            #print 'Counter(pair_list) = ' + str(Counter(pair_list))
            counter_list = Counter(pair_list).items()
            #print 'counter_list = ' + str(counter_list)
            for item in counter_list:
                #print item[1]
                if item[1] == 2:
                    pair_count += 1
                elif item[1] == 3:
                    pair_count += 1
                elif item[1] == 4:
                    pair_count += 2
            #print 'pair_count = ' + str(pair_count)
            #print ''
            if pair_count == 6:
                print 'Player ' + str(player.get_ID()) + ' got an instant win with 6 pairs!'
                player.show_hand()
                #set next game's first player to this player
                #add and subtract points
                #restart game
                return True
                sys.exit()

def check_for_dragon_instant_win(list_of_players):
    """ """
    #dragon
    #check if there is 13 cards first
    dragon_list = ['3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']
    for player in list_of_players:
        if len(player.Hand) == 13:
            pair_list = []
            for card in player.Hand:
                pair_list.append(card['display'][0])
            print 'dragon_compare_list= ' + str(pair_list)
            print ''
            if set(dragon_list).issubset(pair_list) == True:
                print 'Player ' + str(player.get_ID()) + ' got an instant win with a dragon!'
                return True
                sys.exit()
