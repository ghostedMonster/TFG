import pygame

green = (0, 200, 50)

def show_covered_hand(screen, players):
    x, y, space_between_cards = 5, 10, 3
    image = pygame.image.load("cartas/" + "zzzz_red_back.png")
    scaled_image = pygame.transform.scale(image, (40, 58))
    for player in range(0, len(players)):
        for card in players[player].hand:
            card.position_x, card.position_y = x, y
            screen.blit(scaled_image, (x, y))
            x += 40 + space_between_cards
        x = (player + 1) * 480

def show_hand(screen, player):
    x, y, space_between_cards = 5, 780, 5
    for card in player.hand:
        card.position_x, card.position_y = x, y
        screen.blit(card.image, (x, y))
        x += card.horizontal_dimension + space_between_cards

def select_card(player, mouse_x, mouse_y):
    if mouse_x:
        for card in player.hand:
            lower_x, upper_x = (card.position_x, card.position_x + card.horizontal_dimension)
            lower_y, upper_y = (card.position_y, card.position_y + card.vertical_dimension)

            if mouse_x > lower_x and mouse_x < upper_x:
                if mouse_y > lower_y and mouse_y < upper_y:
                    player.selected_card = card

def load_card_images(player, width, height):
    for card in player.hand:
        image = pygame.image.load("cartas/" + str(card) + ".png")
        card.image = pygame.transform.scale(image, (width, height))
        width, height = card.image.get_size()
        card.horizontal_dimension = width
        card.vertical_dimension = height

def play_selected_card(screen, player):
    x = player.selected_card.position_x = 220
    y = player.selected_card.position_y
    screen.blit(player.selected_card.image, (x, y))

def update_selected_card_position(player, new_y_position):
    if player.selected_card:
        player.selected_card.position_y = new_y_position

def flip_turns(player1, player2):
    player1.turn = not player1.turn
    player2.turn = not player2.turn

def turn(player, mouse_x, mouse_y, new_y_position):
    select_card(player, mouse_x, mouse_y)
    player.remove_from_hand(player.selected_card)
    update_selected_card_position(player, new_y_position)