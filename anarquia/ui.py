import pygame

from deck import Deck
from player import Player
from functions_for_algorythm import MiniMax, choose_strategy

def setup(number_of_cards, deck):
    player1 = Player("player 1", hand=deck.draw(number_of_cards), turn=True, computer=False)
    player2 = Player("player 2", hand=deck.draw(number_of_cards))
    player3 = Player("player 3", hand=deck.draw(number_of_cards))
    player4 = Player("player 4", hand=deck.draw(number_of_cards))
    player5 = Player("player 5", hand=deck.draw(number_of_cards))

    player1.hand.sort()
    player2.hand.sort()
    player3.hand.sort()
    player4.hand.sort()
    player5.hand.sort()

    return [player1, player2, player3, player4, player5]

def main():
    green = (0, 200, 50)
    black = (0, 0, 0)
    white = (255, 255, 255)

    sc_width, sc_height = 1280, 720

    selected_y_pos_player_1 = 330

    font_size = 30
    number_of_cards = 10

    deck = Deck()
    deck.deck_shuffle()

    players = setup(number_of_cards, deck)

    miniMax = MiniMax(deck, players)

    pygame.init()
    screen = pygame.display.set_mode((sc_width, sc_height), pygame.RESIZABLE)


