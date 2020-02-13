import enum


class Rank(enum.Enum):
    """Enumerado en el que se definen los valores que tendrán las cartas"""
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(2, 15)
