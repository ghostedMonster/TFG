import pygame

from deck import Deck
from functions_for_algorythm import MiniMax
from game import Game
from player import Player
import functions_for_game as f


def main():
    game = Game()

    pygame.init()
    screen = pygame.display.set_mode((game.sc_width, game.sc_height), pygame.RESIZABLE)

    game.phase_loading()

    game_is_running = True

    while game_is_running:
        screen.fill(game.green)

        mouse_x, mouse_y = None, None
        mouse_pos = None

        events = pygame.event.get()

        phase_1 = True

        # Aqui vemos si el usuario hace algo, y si lo hace, lo guardamos
        for event in events:
            if event.type == pygame.QUIT:
                game_is_running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                mouse_pos = event.pos
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Siempre mostramos las cartas nuestras y la de los demás
        f.show_hand(screen, game.player1)
        f.show_covered_hand(screen, [game.player2, game.player3, game.player4, game.player5])

        if game.player1.choice is None:
            game.phase_1(mouse_pos, screen)

        if game.player1.choice is not None and game.deck != []:
            game.phase_2(screen)
        if game.player1.choice is not None and game.deck == [] and game.player1.turn:
            game.phase_3(mouse_x, mouse_y, screen)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
