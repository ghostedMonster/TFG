from rank import Rank
from suit import Suit


class Card(object):
    def __init__(self, suit, rank, in_deck=False, image=None):
        if rank in Rank and suit in Suit:
            self.rank = rank
            self.suit = suit
        else:
            self.rank = None
            self.suit = None

        self.in_deck = in_deck
        self.image = image

        self.position_x = 0.0
        self.position_y = 0.0
        self.horizontal_dimension = None
        self.vertical_dimension = None

        self.owner = None
        self.turn = 0
        self.won_by = None
        self.position_hand = 0

    def __str__(self):
        return str(self.rank.name) + " " + str(self.suit.name)

    def __eq__(self, other):
        return True if self.rank == other.rank and self.suit == other.suit else False

    def __gt__(self, other):
        if self.suit == other.suit:
            if self.rank.value > other.rank.value:
                return True
        if self.suit.value > other.suit.value:
            return True
        return False
