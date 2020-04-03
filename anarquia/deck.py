from itertools import product
from random import shuffle

from card import Card
from rank import Rank
from suit import Suit


class Deck(object):
    """
    Baraja del juego. Tenemos las cartas que se sacan de la baraja y las cartas sacadas de la baraja.
    Además, tenemos una funcion de sacar cartas, junto con otra de barajado de cartas
    """
    def __init__(self):
        self.cards = [Card(suit, rank, in_deck=True) for suit, rank in product(Suit, Rank)]
        self.removed = []

    def __str__(self):
        return str([str(card) for card in self.cards])

    def draw(self, range=1):
        """
        Sacamos de la baraja el numero de cartas indicado en la función de la baraja
        @param range: numero de cartas a sacar de la baraja
        @return: las cartas sacadas de la baraja
        """
        drawn_cards = self.cards[:range]
        for card in drawn_cards:
            card.in_deck = False
        del self.cards[:range]
        self.removed.append(drawn_cards)
        return drawn_cards

    def deck_shuffle(self):
        shuffle(self.cards)
