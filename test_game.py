#unittest module for Thirteen game

import unittest
from gameLogic import create_deck,shuffle_deck,deal_hand,find_first_player,print_turn
from checkInstantWin import check_for_four_twos_instant_win,check_for_six_pairs_instant_win,check_for_dragon_instant_win
from collections import Counter
from Player import Player


class test_deck_creation(unittest.TestCase):
    """Test deck creation functionality"""
    def setUp(self):
        """Setup 3 decks for testing"""
        self.deck = create_deck()
        self.display_deck = [card['display'] for card in self.deck]
        self.value_deck = [card['value'] for card in self.deck]
        self.deck = shuffle_deck(self.deck)
        self.display_shuffled_deck = [card['display'] for card in self.deck]
        self.value_shuffled_deck = [card['value'] for card in self.deck]

    def tearDown(self):
        """Nulling the created decks"""
        self.deck = None
        self.display_deck = None
        self.value_deck = None
        self.display_shuffled_deck = None
        self.value_shuffled_deck = None

    def test_deck_length(self):
        """Test if the created deck has 52 cards"""
        self.assertEqual(len(self.deck),52)

    def test_display_deck(self):
        """Test if the deck has the indicated displays values"""
        self.assertEqual(self.display_deck,['3S', '3C', '3D', '3H', '4S', '4C', '4D', '4H', '5S', '5C', '5D', '5H', '6S', '6C', '6D', '6H', '7S', '7C', '7D', '7H', '8S', '8C', '8D', '8H', '9S', '9C', '9D', '9H', '10S', '10C', '10D', '10H', 'JS', 'JC', 'JD', 'JH', 'QS', 'QC', 'QD', 'QH', 'KS', 'KC', 'KD', 'KH', 'AS', 'AC', 'AD', 'AH', '2S', '2C', '2D', '2H'])

    def test_value_deck(self):
        """Test the deck has the indicated card values list"""
        self.assertEqual(self.value_deck,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])

    def test_shuffled_deck(self):
        """Test if the shuffled deck is shuffled by checking if it is the same has orginal deck"""
        self.assertNotEqual(self.display_shuffled_deck,self.display_deck)

    def test_shuffled_deck_size(self):
        """Test if shuffled deck has 52 cards"""
        self.assertEqual(len(self.display_shuffled_deck),52)

    def test_shuffled_deck_by_value(self):
        """Test if deck is shuffled by its card value"""
        self.assertNotEqual(self.value_shuffled_deck,self.value_deck)

class test_players_hand(unittest.TestCase):
    """Test Player class module"""
    def setUp(self):
        """Calls before every test case"""
        self.deck = create_deck()
        self.Player1 = Player(1, deal_hand(self.deck,13))
        self.Player2 = Player(2, deal_hand(self.deck,13))
        self.Player3 = Player(3, deal_hand(self.deck,13))
        self.Player4 = Player(4, deal_hand(self.deck,13))
        self.deck_to_be_shuffled = create_deck()
        self.shuffled_deck = shuffle_deck(self.deck_to_be_shuffled)
        self.Player1_shuffled = Player(1, deal_hand(self.shuffled_deck,13))
        self.Player2_shuffled = Player(2, deal_hand(self.shuffled_deck,13))
        self.Player3_shuffled = Player(3, deal_hand(self.shuffled_deck,13))
        self.Player4_shuffled = Player(4, deal_hand(self.shuffled_deck,13))

    def tearDown(self):
        """Calls after every test case"""
        self.deck = None
        self.Player1 = None
        self.Player2 = None
        self.Player3 = None
        self.Player4 = None
        self.deck_to_be_shuffled = None
        self.shuffled_deck = None
        self.Player1_shuffled = None
        self.Player2_shuffled = None
        self.Player3_shuffled = None
        self.Player4_shuffled = None

    def test_shuffled_Player1_hand(self):
        """Test if Player1's dealt hand is shuffled"""
        self.assertNotEqual(self.Player1_shuffled.list_hand(),self.Player1.list_hand())

    def test_shuffled_Player2_hand(self):
        """Test if Player2's dealt hand is shuffled"""
        self.assertNotEqual(self.Player2_shuffled.list_hand(),self.Player2.list_hand())

    def test_shuffled_Player3_hand(self):
        """Test if Player3's dealt hand is shuffed"""
        self.assertNotEqual(self.Player3_shuffled.list_hand(),self.Player3.list_hand())

    def test_shuffled_Player4_hand(self):
        """Test if Player4's dealt hand is shuffled"""
        self.assertNotEqual(self.Player4_shuffled.list_hand(),self.Player4.list_hand())

    def test_static_Player1_hand(self):
        """Test if Player1's static hand is static"""
        self.assertEqual(self.Player1.list_hand(),['2H', '2D', '2C', '2S', 'AH', 'AD', 'AC', 'AS', 'KH', 'KD', 'KC', 'KS', 'QH'])

    def test_static_Player2_hand(self):
        """Test if Player2's static hand is static"""
        self.assertEqual(self.Player2.list_hand(),['QD', 'QC', 'QS', 'JH', 'JD', 'JC', 'JS', '10H', '10D', '10C', '10S', '9H', '9D'])

    def test_static_Player3_hand(self):
        """Test if Player3's static hand is static"""
        self.assertEqual(self.Player3.list_hand(),['9C', '9S', '8H', '8D', '8C', '8S', '7H', '7D', '7C', '7S', '6H', '6D', '6C'])

    def test_static_Player4_hand(self):
        """Test if Player4's static hand is static"""
        self.assertEqual(self.Player4.list_hand(),['6S', '5H', '5D', '5C', '5S', '4H', '4D', '4C', '4S', '3H', '3D', '3C', '3S'])

    def test_total_hand_size(self):
        """Test if the four dealt hands adds up to 52 cards"""
        self.assertEqual(len(self.Player1.Hand)+len(self.Player2.Hand)+len(self.Player3.Hand)+len(self.Player4.Hand),52)

    def test_Player1_hand_size(self):
        """Test if player 1 was dealt 13 cards"""
        self.assertEqual(len(self.Player1.Hand),13)

    def test_Player2_hand_size(self):
        """Test if player 2 was dealt 13 cards"""
        self.assertEqual(len(self.Player2.Hand),13)

    def test_Player3_hand_size(self):
        """Test if player 3 was dealt 13 cards"""
        self.assertEqual(len(self.Player3.Hand),13)

    def test_Player4_hand_size(self):
        """Test if player 4 was dealth 13 cards"""
        self.assertEqual(len(self.Player4.Hand),13)

    def test_Player1_sorted_static_hand(self):
        """Test if player 1 static hand is sorted correctly"""
        self.Player1.sort_hand()
        self.assertEqual(self.Player1.list_hand(),['QH', 'KS', 'KC', 'KD', 'KH', 'AS', 'AC', 'AD', 'AH', '2S', '2C', '2D', '2H'])

    def test_Player2_sorted_static_hand(self):
        """Test if player 2 static hand is sorted correctly"""
        self.Player2.sort_hand()
        self.assertEqual(self.Player2.list_hand(),['9D', '9H', '10S', '10C', '10D', '10H', 'JS', 'JC', 'JD', 'JH', 'QS', 'QC', 'QD'])

    def test_Player3_sorted_static_hand(self):
        """Test if player 3 static hand is sorted correctly"""
        self.Player3.sort_hand()
        self.assertEqual(self.Player3.list_hand(),['6C', '6D', '6H', '7S', '7C', '7D', '7H', '8S', '8C', '8D', '8H', '9S', '9C'])

    def test_Player4_sorted_static_hand(self):
        """Test if player4 static hand is sorted correctly"""
        self.Player4.sort_hand()
        self.assertEqual(self.Player4.list_hand(),['3S', '3C', '3D', '3H', '4S', '4C', '4D', '4H', '5S', '5C', '5D', '5H', '6S'])

class test_instant_win(unittest.TestCase):
    """Test checkInstantWin module"""
    def setUp(self):
        """ """
        self.shuffled_deck = shuffle_deck(create_deck())
        self.Player1 = Player(1, deal_hand(self.shuffled_deck,13))
        self.Player2 = Player(2, deal_hand(self.shuffled_deck,13))
        self.Player3 = Player(3, deal_hand(self.shuffled_deck,13))
        self.Player4 = Player(4, deal_hand(self.shuffled_deck,13))
        self.list_of_players = [self.Player1, self.Player2, self.Player3, self.Player4]

    def tearDown(self):
        """ """
        self.shuffled_deck = None
        self.Player1 = None
        self.Player2 = None
        self.Player3 = None
        self.Player4 = None
        self.list_of_players = None

    def test_four_twos_by_rng(self):
        """Test will fail if a hand with four 2's is generated"""
        self.check_four_twos = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos, "Instant win by four 2's!!!")

    def test_six_pairs_by_rng(self):
        """Test will fail if a hand with six pairs is generated"""
        self.check_for_six_pairs = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_six_pairs, "Instant win by 6 pairs!!!")

    def test_dragon_by_rng(self):
        """Test will fail if a hand with a dragon generated"""
        self.check_for_dragon = check_for_dragon_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_dragon, "Instant win by dragon!!!")

    def test_four_two_by_test_Player1(self):
        """Test if four 2's algorithm works for Player1"""
        self.Player1.Hand = [{'display': '9H', 'name': '9', 'value': 28, 'suit': 'Hearts'}, {'display': '7S', 'name': '7', 'value': 17, 'suit': 'Spades'}, {'display': '8S', 'name': '8', 'value': 21, 'suit': 'Spades'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'}, {'display': 'JH', 'name': 'Jack', 'value': 36, 'suit': 'Hearts'}, {'display': '10S', 'name': '10', 'value': 29, 'suit': 'Spades'}, {'display': '8D', 'name': '8', 'value': 23, 'suit': 'Diamonds'}, {'display': '4D', 'name': '4', 'value': 7, 'suit': 'Diamonds'}, {'display': 'QD', 'name': 'Queen', 'value': 39, 'suit': 'Diamonds'}]
        self.assertEqual(len(self.Player1.Hand),9)
        self.Player1.Hand += [{'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'},{'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'},{'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clovers'},{'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}]
        self.assertEqual(len(self.Player1.Hand),13)
        self.check_four_twos_player1 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertTrue(self.check_four_twos_player1)
        self.Player1.Hand.pop(0)         #test if the alogrithm check if the player has 13 cards
        self.assertEqual(len(self.Player1.Hand),12)
        self.check_four_twos_player1 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player1)

    def test_four_two_by_test_Player2(self):
        """Test if four 2's algorithm works for Player2"""
        self.Player2.Hand = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'}, {'display': '9S', 'name': '9', 'value': 25, 'suit': 'Spades'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clovers'}, {'display': '6S', 'name': '6', 'value': 13, 'suit': 'Spades'}, {'display': 'QD', 'name': 'Queen', 'value': 39, 'suit': 'Diamonds'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '9H', 'name': '9', 'value': 28, 'suit': 'Hearts'}, {'display': '6H', 'name': '6', 'value': 16, 'suit': 'Hearts'},{'display': 'JC', 'name': 'Jack', 'value': 34, 'suit': 'Clubs'}]
        self.assertEqual(len(self.Player2.Hand),9)
        self.Player2.Hand += [{'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'},{'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'},{'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clovers'},{'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}]
        self.assertEqual(len(self.Player2.Hand),13)
        self.check_four_twos_player2 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertTrue(self.check_four_twos_player2)
        self.Player2.Hand.pop(0)         #test if the alogrithm check if the player has 13 cards
        self.assertEqual(len(self.Player2.Hand),12)
        self.check_four_twos_player2 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player2)
        self.Player2.Hand.append({'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clovers'}) #test if algorithm does not pass 3 2's
        self.Player2.Hand.pop(10)
        self.Player2.Hand.append({'display': '3D', 'name': '3', 'value': 3, 'suit': 'Diamonds'})
        self.assertEqual(len(self.Player2.Hand),13)
        self.check_four_twos_player2 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player2)

    def test_four_two_by_test_Player3(self):
        """Test if four 2's alogrithm works for Player3"""
        self.Player3.Hand = [{'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '3H', 'name': '3', 'value': 4, 'suit': 'Hearts'}, {'display': '8D', 'name': '8', 'value': 23, 'suit': 'Diamonds'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clubs'}, {'display': '5D', 'name': '5', 'value': 11, 'suit': 'Diamonds'}, {'display': 'AC', 'name': 'Ace', 'value': 46, 'suit': 'Clubs'}, {'display': 'QS', 'name': 'Queen', 'value': 37, 'suit': 'Spades'}, {'display': '9H', 'name': '9', 'value': 28, 'suit': 'Hearts'}, {'display': '3D', 'name': '3', 'value': 3, 'suit': 'Diamonds'}]
        self.assertEqual(len(self.Player3.Hand),9)
        self.Player3.Hand += [{'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'},{'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'},{'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clovers'},{'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}]
        self.assertEqual(len(self.Player3.Hand),13)
        self.check_four_twos_player3 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertTrue(self.check_four_twos_player3)
        self.Player3.Hand.pop(0)         #test if the alogrithm check if the player has 13 cards
        self.assertEqual(len(self.Player3.Hand),12)
        self.check_four_twos_player3 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player3)
        self.Player3.Hand.append({'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clovers'}) #test if algorithm does not pass 3 2's
        self.Player3.Hand.pop(10)
        self.Player3.Hand.append({'display': '3D', 'name': '3', 'value': 3, 'suit': 'Diamonds'})
        self.assertEqual(len(self.Player3.Hand),13)
        self.check_four_twos_player3 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player3)

    def test_four_two_by_test_Player4(self):
        """Test if four 2's algorithm works for Player4"""
        self.Player4.Hand = [{'display': 'KH', 'name': 'King', 'value': 44, 'suit': 'Hearts'}, {'display': 'QS', 'name': 'Queen', 'value': 37, 'suit': 'Spades'}, {'display': '7C', 'name': '7', 'value': 18, 'suit': 'Clubs'}, {'display': 'QH', 'name': 'Queen', 'value': 40, 'suit': 'Hearts'}, {'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '10D', 'name': '10', 'value': 31, 'suit': 'Diamonds'}, {'display': 'QC', 'name': 'Queen', 'value': 38, 'suit': 'Clubs'}, {'display': '8S', 'name': '8', 'value': 21, 'suit': 'Spades'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clubs'}]
        self.assertEqual(len(self.Player4.Hand),9)
        self.Player4.Hand += [{'display': '2H', 'name': '2', 'value': 52, 'suit': 'Hearts'},{'display': '2D', 'name': '2', 'value': 51, 'suit': 'Diamonds'},{'display': '2C', 'name': '2', 'value': 50, 'suit': 'Clovers'},{'display': '2S', 'name': '2', 'value': 49, 'suit': 'Spades'}]
        self.assertEqual(len(self.Player4.Hand),13)
        self.check_four_twos_player4 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertTrue(self.check_four_twos_player4)
        self.Player4.Hand.pop(0)         #test if the alogrithm check if the player has 13 cards
        self.assertEqual(len(self.Player4.Hand),12)
        self.check_four_twos_player4 = check_for_four_twos_instant_win(self.list_of_players)
        self.assertFalse(self.check_four_twos_player4)

    def test_six_pairs_by_test_player1(self):
        """Test if six pairs algorithm works for Player1"""
        self.Player1.Hand = [{'display': '3S', 'name': '3', 'value': 1, 'suit': 'Spades'}, {'display': '3C', 'name': '3', 'value': 2, 'suit': 'Clubs'}, {'display': '6S', 'name': '6', 'value': 13,'suit': 'Spades'}, {'display': '9C', 'name': '9', 'value': 26, 'suit': 'Clubs'}, {'display': '9D', 'name': '9', 'value': 27, 'suit': 'Diamonds'}, {'display': '9H', 'name': '9', 'value': 28, 'suit': 'Hearts'}, {'display': 'JS', 'name': 'Jack', 'value': 33, 'suit': 'Spades'}, {'display': 'JH', 'name': 'Jack', 'value': 36, 'suit': 'Hearts'}, {'display': 'KC', 'name': 'King', 'value': 42, 'suit': 'Clubs'}, {'display': 'KD', 'name': 'King', 'value': 43, 'suit': 'Diamonds'}, {'display': 'AC', 'name': 'Ace','value': 46, 'suit': 'Clubs'}, {'display': 'AD', 'name': 'Ace', 'value': 47, 'suit': 'Diamonds'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'}]
        self.assertEqual(len(self.Player1.Hand),13)
        self.Player1.sort_hand()
        self.check_for_six_pairs_for_player1 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertTrue(self.check_for_six_pairs_for_player1)
        self.Player1.Hand.pop()
        self.check_for_six_pairs_for_player1 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_six_pairs_for_player1)
        self.Player1.Hand.append({'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'})
        self.check_for_six_pairs_for_player1 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_six_pairs_for_player1)

    def test_six_pairs_by_test_player2(self):
        """Test if six pairs algorithm works for Player2"""
        self.Player2.Hand = [{'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '4D', 'name': '4', 'value': 7, 'suit': 'Diamonds'}, {'display': '6C', 'name': '6', 'value': 14, 'suit': 'Clubs'}, {'display': '6H', 'name': '6', 'value': 16, 'suit': 'Hearts'}, {'display': '7D', 'name': '7', 'value': 19, 'suit': 'Diamonds'}, {'display': '7H', 'name': '7', 'value': 20, 'suit': 'Hearts'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '8H', 'name': '8', 'value': 24, 'suit': 'Hearts'}, {'display': '9D', 'name': '9', 'value': 27, 'suit': 'Diamonds'}, {'display': 'QH', 'name': 'Queen', 'value': 40, 'suit': 'Hearts'}, {'display': 'QS', 'name':'Queen', 'value': 37, 'suit': 'Spades'}, {'display': 'QC', 'name': 'Queen', 'value': 38, 'suit': 'Clubs'}, {'display': 'QD', 'name': 'Queen', 'value': 39, 'suit': 'Diamonds'}]
        self.assertEqual(len(self.Player2.Hand),13)
        self.Player2.sort_hand()
        self.check_for_six_pairs_for_player2 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertTrue(self.check_for_six_pairs_for_player2)
        self.Player2.Hand.pop()
        self.check_for_six_pairs_for_player2 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_six_pairs_for_player2)
        self.Player2.Hand.append({'display': '10D', 'name': '10', 'value': 31, 'suit': 'Diamonds'})
        self.check_for_six_pairs_for_player2 = check_for_six_pairs_instant_win(self.list_of_players)
        self.assertFalse(self.check_for_six_pairs_for_player2)

    def test_six_pairs_by_test_player3(self):
        """Test if six pairs algorithm works for Player3"""
        self.Player3.Hand = [{'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '5C', 'name': '5', 'value': 10, 'suit': 'Clubs'}, {'display': '5D', 'name': '5', 'value': 11, 'suit': 'Diamonds'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'}, {'display': '6H', 'name': '6', 'value': 16, 'suit': 'Hearts'}, {'display': '7D', 'name': '7', 'value': 19, 'suit': 'Diamonds'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '8H', 'name': '8', 'value': 24, 'suit': 'Hearts'}, {'display': '10C', 'name': '10', 'value': 30, 'suit': 'Clubs'}, {'display': '10H', 'name': '10', 'value': 32, 'suit': 'Hearts'}, {'display': 'JS', 'name': 'Jack', 'value': 33, 'suit': 'Spades'}, {'display': 'KS', 'name': 'King', 'value': 41, 'suit': 'Spades'}]
        self.assertEqual(len(self.Player3.Hand),13)
        self.Player3.sort_hand()
        self.check_for_six_pairs_for_player3 = check_for_dragon_instant_win(self.list_of_players)

        """
        print self.Player1.sort_hand()
        print self.Player1.show_hand()
        print self.Player1.Hand
        print self.Player2.sort_hand()
        print self.Player2.show_hand()
        print self.Player2.Hand
        print self.Player3.sort_hand()
        print self.Player3.show_hand()
        print self.Player3.Hand
        print self.Player4.sort_hand()
        print self.Player4.show_hand()
        print self.Player4.Hand"""

"""
['4S', '4C', '5C', '5D', '6D', '6H', '7D', '8C', '8H', '10C', '10H', 'JS', 'KS']

[{'display': '4S', 'name': '4', 'value': 5, 'suit': 'Spades'}, {'display': '4C', 'name': '4', 'value': 6, 'suit': 'Clubs'}, {'display': '5C', 'name': '5', 'value': 10, 'suit': 'Clubs'}, {'display': '5D', 'name': '5', 'value': 11, 'suit': 'Diamonds'}, {'display': '6D', 'name': '6', 'value': 15, 'suit': 'Diamonds'}, {'display': '6H', 'name': '6', 'value': 16, 'suit': 'Hearts'}, {'display': '7D', 'name': '7', 'value': 19, 'suit': 'Diamonds'}, {'display': '8C', 'name': '8', 'value': 22, 'suit': 'Clubs'}, {'display': '8H', 'name': '8', 'value': 24, 'suit': 'Hearts'}, {'display': '10C', 'name': '10', 'value': 30, 'suit': 'Clubs'}, {'display': '10H', 'name': '10', 'value': 32, 'suit': 'Hearts'}, {'display': 'JS', 'name': 'Jack', 'value': 33, 'suit': 'Spades'}, {'display': 'KS', 'name': 'King', 'value': 41, 'suit': 'Spades'}]




"""


if __name__ == '__main__':
    #run all tests
    unittest.main()
