"""
player class
player class structure:
ID
Hand
Points

class Player:
    def __init__(self,ID,Hand):
        self.ID = ID
        self.Hand = Hand
    def getID(self):
        return self.ID
    def getHand(self):
        return self.Hand
    def showHand(self):
        print self.Hand

Points are in increments of thousands:
1st place gets 2000 (+2000),
2nd place gets 1000 (-1000),
3rd place pays 2nd place 1000 (-1000),
4th palce pays 1st place 2000 (-2000)
Everyone starts of at 10,000
"""

class Player(object):
    """
    4 players in total
    attributes:
    ID: int
    Hand: list
    Points: int
    turn_lock_out:
    shut_down_status:
    Turn?
    """

    def __init__(self, ID, Hand = []):
        self.ID = ID #int
        self.Hand = Hand
        self.status = True #true = in  / false = locked out
        self.shut_down = False #true = is shutdown / false = is not
        self.locked_out = False
        self.hand_empty = False

    def set_points(self, Points = 10000):
        """set player's starting balance to 10k"""
        self.Points = Points

    def get_ID(self):
        """Returns player's ID"""
        return self.ID

    def get_points(self):
        """Returns player's points"""
        return self.Points

    def get_hand(self):
        """Returns entire hand and card attributes"""
        return self.Hand

    def show_hand(self):
        """Pretty prints hand for display, ONLY PRINTS, returns no value"""
        print [card['display'] for card in self.Hand]

    def list_hand(self):
        """Returns list of the hand as a list obj for validation purposes"""
        return [card['display'] for card in self.Hand]

    def list_hand_value(self):
        """Returns list of card values of that player's hand"""
        return [card['value'] for card in self.Hand]

    def show_points(self):
        """Print out points"""
        print str(self.Points) + ' Points'

    def sort_hand(self):
        """ sort player's hand in the order of Thirteen's rule"""
        sorted_hand = sorted(self.Hand, key=lambda card: card['value'])
        self.Hand = sorted_hand
