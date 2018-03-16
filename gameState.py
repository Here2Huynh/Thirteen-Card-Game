#game_state module
# this module will hold:
#   -current round and its moves
#   -which player is locked out
#   -which player is choked out / do it in player moduel??
#   -player's move

# might need a executor file to execute the calls

class game_state:

    def __init__(self):
        self.Turn = int #current player that is going
        self.player_index = int
        self.current_board = [] #current move on the board / in play
        self.list_of_players = [] #list of players playing
        self.first_game = bool #keeps track if the game is a first game or not
        self.round_winner = ''
        self.round_is_won = bool #false continues round, true ends round
        self.game_winner = '' #when hand count = 0
        self.game_is_over = bool #False continues the game, True ends the game
        self.previous_hand = [] #stores previous played hand for comparison and move validation
        self.players_done = 0 # if == 4 ends the game
        #needs a Player state
        self.first_place = int #index of first place winner
        self.second_place = int #index of second place game_winner
        self.third_place = int
        self.fourth_place = int
        
    def get_turn(self):
        return self.Turn

    def get_current_board(self):
        return self.current_board

    def get_list_of_players(self):
        return self.list_of_players

    def first_game(self):
        """bool that starts of as True and get
        changed at the end of the first game"""
        return self.first_game

    def it_is_first_game(self):
        """sets first game bool to True"""
        self.first_game == True

    def not_first_game(self):
        """sets first game bool to False"""
        self.first_game == False

    def next_player(self):
        """sets the next player when it is called
        and then cycles back to 0. 0->1 1->2 2->3 3->4"""
        #print type(self.player_index)
        print 'current player index: ' + str(self.player_index)
        if self.player_index == 3:
            self.player_index = 0
            print self.player_index
        else:
            self.player_index += 1
            print self.player_index

    def current_player(self):
        """ """
        return self.list_of_players[player_index]
    """
    def lock_out_player(self, player):
        return
    """

    def start_game(self):
        """ """
        if self.first_game == True:
            #takes player input / move
            print 'Player ' + self.Turn+ ' please enter the card(s) you want to play: '
            #remove that card(s) in that hand
            #print that new hand

    def get_number_of_players_done(self):
        """returns number of players with empty hand
        if equals to 4 then it will end the game by
        changing game_is_over to True"""
        return self.players_done
