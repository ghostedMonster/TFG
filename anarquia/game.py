import pygame

from choice import Choice
from deck import Deck
import functions_for_game as f
from functions_for_algorythm import MiniMax, choose_strategy
from player import Player

pygame.init()
class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.deck_shuffle()

        self.green = (0, 200, 50)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.sc_width, self.sc_height = 1920, 1080

        self.selected_y_pos_player_1 = 330

        self.font_size = 30

        self.number_of_cards = 10

        self.player1 = Player("player 1", hand=self.deck.draw(self.number_of_cards), turn=True, computer=False)
        self.player2 = Player("player 2", hand=self.deck.draw(self.number_of_cards))
        self.player3 = Player("player 3", hand=self.deck.draw(self.number_of_cards))
        self.player4 = Player("player 4", hand=self.deck.draw(self.number_of_cards))
        self.player5 = Player("player 5", hand=self.deck.draw(self.number_of_cards))

        for player in [self.player1, self.player2, self.player3, self.player4, self.player5]:
            for card in player.hand:
                card.owner = player

        self.player1.hand.sort()
        self.player2.hand.sort()
        self.player3.hand.sort()
        self.player4.hand.sort()
        self.player5.hand.sort()

        self.player1.hand.sort()
        self.player2.hand.sort()
        self.player3.hand.sort()
        self.player4.hand.sort()
        self.player5.hand.sort()

        self.miniMax = MiniMax(self.deck, [self.player1, self.player2, self.player3, self.player4, self.player5])

        self.my_font = pygame.font.SysFont('Times New Roman', self.font_size)
        self.text_button_hearts = self.my_font.render('Hearts', True, self.black, self.white)
        self.text_button_spades = self.my_font.render('Spades', True, self.black, self.white)
        self.text_button_diamonds = self.my_font.render('Diamonds', True, self.black, self.white)
        self.text_button_clubs = self.my_font.render('Clubs', True, self.black, self.white)
        self.text_button_no_suit = self.my_font.render('No suit', True, self.black, self.white)
        self.text_button_misere = self.my_font.render('Misêre', True, self.black, self.white)

        self.button_hearts = self.text_button_hearts.get_rect()
        self.button_spades = self.text_button_spades.get_rect()
        self.button_diamonds = self.text_button_diamonds.get_rect()
        self.button_clubs = self.text_button_clubs.get_rect()
        self.button_no_suit = self.text_button_no_suit.get_rect()
        self.button_misere = self.text_button_misere.get_rect()

        self.strategy_player_2 = None
        self.strategy_player_3 = None
        self.strategy_player_4 = None
        self.strategy_player_5 = None

        self.strategy_player_2_rect = None
        self.strategy_player_3_rect = None
        self.strategy_player_4_rect = None
        self.strategy_player_5_rect = None

    def phase_loading(self):
        card_width = 175
        card_height = 250

        f.load_card_images(self.player1, card_width, card_height)
        f.load_card_images(self.player2, card_width, card_height)
        f.load_card_images(self.player3, card_width, card_height)
        f.load_card_images(self.player4, card_width, card_height)
        f.load_card_images(self.player5, card_width, card_height)

        pygame.font.init()

        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        self.strategy_player_2 = self.my_font.render('Player 2 strategy: ' + self.player2.choice.name.lower(), True,
                                                self.black,
                                                self.green)
        self.strategy_player_3 = self.my_font.render('Player 3 strategy: ' + self.player3.choice.name.lower(), True,
                                                self.black,
                                                self.green)
        self.strategy_player_4 = self.my_font.render('Player 4 strategy: ' + self.player4.choice.name.lower(), True,
                                                self.black,
                                                self.green)
        self.strategy_player_5 = self.my_font.render('Player 5 strategy: ' + self.player5.choice.name.lower(), True,
                                                self.black,
                                                self.green)

        self.strategy_player_2_rect = self.strategy_player_2.get_rect()
        self.strategy_player_3_rect = self.strategy_player_3.get_rect()
        self.strategy_player_4_rect = self.strategy_player_4.get_rect()
        self.strategy_player_5_rect = self.strategy_player_5.get_rect()

        self.strategy_player_2_rect.center = (150, 165)
        self.strategy_player_3_rect.center = (630, 165)
        self.strategy_player_4_rect.center = (1110, 165)
        self.strategy_player_5_rect.center = (1590, 165)

        self.button_hearts.center = (1590, 680)
        self.button_spades.center = (1780, 680)
        self.button_diamonds.center = (1590, 780)
        self.button_clubs.center = (1780, 780)
        self.button_no_suit.center = (1590, 880)
        self.button_misere.center = (1780, 880)

    def phase_1(self, mouse_pos, screen):
        if mouse_pos is not None:
            if self.button_clubs.collidepoint(mouse_pos):
                self.player1.choice = Choice.CLUBS
            if self.button_hearts.collidepoint(mouse_pos):
                self.player1.choice = Choice.HEARTS
            if self.button_diamonds.collidepoint(mouse_pos):
                self.player1.choice = Choice.DIAMONDS
            if self.button_spades.collidepoint(mouse_pos):
                self.player1.choice = Choice.SPADES
            if self.button_no_suit.collidepoint(mouse_pos):
                self.player1.choice = Choice.NO_SUIT
            if self.button_misere.collidepoint(mouse_pos):
                self.player1.choice = Choice.MISERE

        screen.blit(self.text_button_hearts, self.button_hearts)
        screen.blit(self.text_button_clubs, self.button_clubs)
        screen.blit(self.text_button_diamonds, self.button_diamonds)
        screen.blit(self.text_button_spades, self.button_spades)
        screen.blit(self.text_button_no_suit, self.button_no_suit)
        screen.blit(self.text_button_misere, self.button_misere)

    def not_phase_1(self, screen):
        strategy_player_1 = self.my_font.render('Player 1 strategy: ' + self.player1.choice.name.lower(), True, self.black, self.green)
        strategy_player_1_rect = strategy_player_1.get_rect()
        strategy_player_1_rect.center = (150, 700)

        screen.blit(strategy_player_1, strategy_player_1_rect)
        screen.blit(self.strategy_player_2, self.strategy_player_2_rect)
        screen.blit(self.strategy_player_3, self.strategy_player_3_rect)
        screen.blit(self.strategy_player_4, self.strategy_player_4_rect)
        screen.blit(self.strategy_player_5, self.strategy_player_5_rect)

    def get_max_card_suit(self, card, player):
        max_card = None
        for carta in player.hand:
            if carta.suit == card.suit:
                if max_card is None:
                    max_card = carta
                elif max_card.rank.value < carta.rank.value:
                    max_card = carta
        return max_card

    def phase_2(self, screen):
        self.not_phase_1(screen)
        if self.deck.cards[0].image is None:
            for card in self.deck.cards:
                image = pygame.image.load("cartas/" + str(card) + ".png")
                card.image = pygame.transform.scale(image, (175, 250))
                width, height = card.image.get_size()
                card.horizontal_dimension = width
                card.vertical_dimension = height

        carta = self.deck.draw()
        carta_sola = carta[0]



        screen.blit(carta_sola.image, (960, 540))

        winner_card = None

        for player in [self.player1, self.player2, self.player3, self.player4, self.player5]:
            max_card = self.get_max_card_suit(carta_sola, player)
            if max_card is not None:
                screen.blit(max_card.image, (max_card.position_x, max_card.position_y + 100))

            if winner_card is None:
                winner_card = max_card
            elif max_card.rank.value > winner_card.rank.value:
                winner_card = max_card
        print(str(winner_card))
        winner = winner_card.owner
        winner.won_hand.append(carta_sola)

    def phase_3(self, mouse_x, mouse_y, screen):
        if not self.miniMax.played_cards:
            points, position_cards = self.miniMax.max_levels_prunning(10, self.player1)
            self.miniMax.play(self.player2, position_cards[1])
            pygame.time.delay(200)
            self.miniMax.play(self.player3, position_cards[2])
            pygame.time.delay(200)
            self.miniMax.play(self.player4, position_cards[3])
            pygame.time.delay(200)
            self.miniMax.play(self.player5, position_cards[4])
            pygame.time.delay(200)

            for card in self.miniMax.played_cards:
                card.position_y += 50


        f.turn(self.player1, mouse_x, mouse_y, self.selected_y_pos_player_1)
        if self.player1.selected_card:
            self.player1.turn = False
