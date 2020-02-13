import pygame

from anarquia.choice import Choice
from anarquia.deck import Deck
import anarquia.functions_for_game as f
from anarquia.functions_for_algorythm import MiniMax, choose_strategy
from anarquia.player import Player


def main():
    """
    Funcion principal del juego
    """
    green = (0, 200, 50)
    black = (0, 0, 0)
    white = (255, 255, 255)
    sc_width, sc_height = 1920, 1080

    selected_y_pos_player_1 = 330

    font_size = 30
    delay_time_ms = 1000
    number_of_cards = 10

    turn = 1

    deck = Deck()
    deck.deck_shuffle()

    player1 = Player("player 1", hand=deck.draw(number_of_cards), turn=True, computer=False)
    player2 = Player("player 2", hand=deck.draw(number_of_cards))
    player3 = Player("player 3", hand=deck.draw(number_of_cards))
    player4 = Player("player 4", hand=deck.draw(number_of_cards))
    player5 = Player("player 5", hand=deck.draw(number_of_cards))

    miniMax = MiniMax(deck, [player1, player2, player3, player4, player5])

    pygame.init()
    screen = pygame.display.set_mode((sc_width, sc_height), pygame.RESIZABLE)

    card_width = 175
    card_height = 250

    f.load_card_images(player1, card_width, card_height)
    f.load_card_images(player2, card_width, card_height)
    f.load_card_images(player3, card_width, card_height)
    f.load_card_images(player4, card_width, card_height)
    f.load_card_images(player5, card_width, card_height)

    pygame.font.init()
    my_font = pygame.font.SysFont('Times New Roman', font_size)

    choose_strategy(player2)
    choose_strategy(player3)
    choose_strategy(player4)
    choose_strategy(player5)

    strategy_player_2 = my_font.render('Player 2 strategy: ' + player2.choice.name.lower(), True, black, green)
    strategy_player_3 = my_font.render('Player 3 strategy: ' + player3.choice.name.lower(), True, black, green)
    strategy_player_4 = my_font.render('Player 4 strategy: ' + player4.choice.name.lower(), True, black, green)
    strategy_player_5 = my_font.render('Player 5 strategy: ' + player5.choice.name.lower(), True, black, green)

    strategy_player_2_rect = strategy_player_2.get_rect()
    strategy_player_3_rect = strategy_player_3.get_rect()
    strategy_player_4_rect = strategy_player_4.get_rect()
    strategy_player_5_rect = strategy_player_5.get_rect()

    strategy_player_2_rect.center = (150, 165)
    strategy_player_3_rect.center = (630, 165)
    strategy_player_4_rect.center = (1110, 165)
    strategy_player_5_rect.center = (1590, 165)

    game_is_running = True

    text_button_hearts = my_font.render('Hearts', True, black, white)
    text_button_spades = my_font.render('Spades', True, black, white)
    text_button_diamonds = my_font.render('Diamonds', True, black, white)
    text_button_clubs = my_font.render('Clubs', True, black, white)
    text_button_no_suit = my_font.render('No suit', True, black, white)
    text_button_misere = my_font.render('Misêre', True, black, white)

    button_hearts = text_button_hearts.get_rect()
    button_spades = text_button_spades.get_rect()
    button_diamonds = text_button_diamonds.get_rect()
    button_clubs = text_button_clubs.get_rect()
    button_no_suit = text_button_no_suit.get_rect()
    button_misere = text_button_misere.get_rect()

    button_hearts.center = (1590, 680)
    button_spades.center = (1780, 680)
    button_diamonds.center = (1590, 780)
    button_clubs.center = (1780, 780)
    button_no_suit.center = (1590, 880)
    button_misere.center = (1780, 880)

    # main game loop
    while game_is_running:
        screen.fill(green)

        mouse_x, mouse_y = None, None
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game_is_running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                mouse_pos = event.pos

                if button_clubs.collidepoint(mouse_pos):
                    player1.choice = Choice.CLUBS
                if button_hearts.collidepoint(mouse_pos):
                    player1.choice = Choice.HEARTS
                if button_diamonds.collidepoint(mouse_pos):
                    player1.choice = Choice.DIAMONDS
                if button_spades.collidepoint(mouse_pos):
                    player1.choice = Choice.SPADES
                if button_no_suit.collidepoint(mouse_pos):
                    player1.choice = Choice.NO_SUIT
                if button_misere.collidepoint(mouse_pos):
                    player1.choice = Choice.MISERE

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        f.show_hand(screen, player1)
        f.show_covered_hand(screen, [player2, player3, player4, player5])
        if player1.turn:
            f.turn(player1, mouse_x, mouse_y, selected_y_pos_player_1)
            if player1.selected_card:
                f.flip_turns(player1, player2)

        if player1.selected_card:
            f.play_selected_card(screen, player1)
        if player2.selected_card:
            f.play_selected_card(screen, player2)

        if player1.choice is not None:
            strategy_player_1 = my_font.render('Player 1 strategy: ' + player1.choice.name.lower(), True, black, green)
            strategy_player_1_rect = strategy_player_1.get_rect()
            strategy_player_1_rect.center = (150, 700)

            screen.blit(strategy_player_1, strategy_player_1_rect)
            screen.blit(strategy_player_2, strategy_player_2_rect)
            screen.blit(strategy_player_3, strategy_player_3_rect)
            screen.blit(strategy_player_4, strategy_player_4_rect)
            screen.blit(strategy_player_5, strategy_player_5_rect)
        else:
            screen.blit(text_button_hearts, button_hearts)
            screen.blit(text_button_clubs, button_clubs)
            screen.blit(text_button_diamonds, button_diamonds)
            screen.blit(text_button_spades, button_spades)
            screen.blit(text_button_no_suit, button_no_suit)
            screen.blit(text_button_misere, button_misere)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
