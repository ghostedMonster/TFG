from enum import Enum


class Suit(Enum):
    """Enumerado en el que se definen los palos de las cartas"""
    CLUBS, DIAMONDS, HEARTS, SPADES = range(1, 5)
