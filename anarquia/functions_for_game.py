import pygame

green = (0, 200, 50)


def show_covered_hand(screen, players):
    """
    Muestra la mano de un jugador controlado por el ordenador. Como se supone que no podemos ver las cartas de este
    jugador,  las mostraremos tapadas
    @param screen: pantalla en la que se mostrará
    @param players: Jugadores que queremos que s muestren las cartas cubiertas
    """
    x, y, space_between_cards = 5, 10, -10
    image = pygame.image.load("cartas/" + "zzzz_red_back.png")
    scaled_image = pygame.transform.scale(image, (90, 125))
    for player in range(0, len(players)):
        for card in players[player].hand:
            card.position_x, card.position_y = x, y
            screen.blit(scaled_image, (x, y))
            x += 40 + space_between_cards
        x = (player + 1) * 480


def show_hand(screen, player):
    """
    Muestra las cartas del jugador elegido
    @param screen: Pantalla del programa en la que aparecerá
    @param player: Jugador que queremos ver
    """
    x, y, space_between_cards = 5, 760, -50
    for card in player.hand:
        card.position_x, card.position_y = x, y
        screen.blit(card.image, (x, y))
        x += card.horizontal_dimension + space_between_cards


def select_card(player, mouse_x, mouse_y):
    """
    Selecciona una carta para jugar
    @param player: Jugador que queremos usar
    @param mouse_x: Posicion del raton en el eje x
    @param mouse_y: Posicion del raton en el eje y
    """
    if mouse_x:
        for card in player.hand:
            lower_x, upper_x = (card.position_x, card.position_x + card.horizontal_dimension)
            lower_y, upper_y = (card.position_y, card.position_y + card.vertical_dimension)

            if lower_x < mouse_x < upper_x:
                if lower_y < mouse_y < upper_y:
                    player.selected_card = card


def load_card_images(player, width, height):
    """
    Carga las imágenes de las cartas que queremos mostrar
    @param player: Jugador que tiene las cartas que queremos cargar
    @param width: Ancho por carta en pixeles
    @param height: Altura por carta en pixeles
    """
    for card in player.hand:
        image = pygame.image.load("cartas/" + str(card) + ".png")
        card.image = pygame.transform.scale(image, (width, height))
        width, height = card.image.get_size()
        card.horizontal_dimension = width
        card.vertical_dimension = height


def play_selected_card(screen, player):
    """
    Ponemos la carta elegida en posicion de jugar
    @param screen: pantalla donde se actualizará la posición de la carta
    @param player: Jugador dueño de la carta a jugar
    """
    x = player.selected_card.position_x = 220
    y = player.selected_card.position_y
    screen.blit(player.selected_card.image, (x, y))


def update_selected_card_position(player, new_y_position):
    """
    Actualiza la posición de la carta seleccionada
    @param player: Jugador dueño de la carta a jugar
    @param new_y_position: Posición a donde se pondrá la carta en el eje y
    """
    if player.selected_card:
        player.selected_card.position_y = new_y_position


def flip_turns(player1, player2):
    """
    Cambia el estado de el turno de un jugador a otro
    @param player1:
    @param player2:
    """
    player1.turn = not player1.turn
    player2.turn = not player2.turn


def turn(player, mouse_x, mouse_y, new_y_position):
    """
    Función que define qué es lo que hay que hacer para jugar una carta
    @param player: Jugador que va a jugar la carta
    @param mouse_x: Posición en el eje x del ratón
    @param mouse_y: Posición en el eje y del ratón
    @param new_y_position: Nueva posición de la carta en la mesa
    """
    select_card(player, mouse_x, mouse_y)
    player.remove_from_hand(player.selected_card)
    update_selected_card_position(player, new_y_position)
