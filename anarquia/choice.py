from enum import Enum


class Choice(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES, NO_SUIT, MISERE = range(1, 7)
