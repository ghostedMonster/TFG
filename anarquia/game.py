import pygame

from anarquia.deck import Deck
import anarquia.functions_for_game as f
from anarquia.player import Player


def main():
    green = (0, 200, 50)
    sc_width, sc_height = 1920, 1080

    selected_y_pos_player_1 = 330
    selected_y_pos_player_2 = 230

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

    pygame.init()
    screen = pygame.display.set_mode((sc_width, sc_height))

    card_width = 175
    card_height = 250

    f.load_card_images(player1, card_width, card_height)
    f.load_card_images(player2, card_width, card_height)
    f.load_card_images(player3, card_width, card_height)
    f.load_card_images(player4, card_width, card_height)
    f.load_card_images(player5, card_width, card_height)

    pygame.font.init()
    my_font = pygame.font.SysFont('Times New Roman', font_size)

    game_is_running = True

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

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
