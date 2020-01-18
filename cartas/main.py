import cartas.game as juego


def main():
    """
    funcion principal para la aplicacion
    """
    g = juego.Game()
    print('Baraja: {}'.format(g.baraja))
    print('Jugadas: {}'.format(g.jugadas))
    print('Ganadas por el Jugador 1: {}'.format(g.player_1.won))
    print('Lote del Jugador 1: {}'.format(g.player_1.lot))
    print('Ganadas por el Jugador 2: {}'.format(g.player_2.won))
    print('Lote del Jugador 2: {}'.format(g.player_2.lot))
    print('Ganadas por el Jugador 3: {}'.format(g.player_3.won))
    print('Lote del Jugador 3: {}'.format(g.player_3.lot))
    print('Ganadas por el Jugador 4: {}'.format(g.player_4.won))
    print('Lote del Jugador 4: {}'.format(g.player_4.lot))
    print('Ganadas por el Jugador 5: {}'.format(g.player_5.won))
    print('Lote del Jugador 5: {}'.format(g.player_5.lot))
    g.barajar()
    print('Tras barajar las cartas, la baraja ha quedado así: \n')
    print(g.baraja)
    print('Repartimos las cartas: ')
    g.repartir()

    print('Lote del Jugador 1: {}'.format(g.player_1.lot))
    print('Lote del Jugador 2: {}'.format(g.player_2.lot))
    print('Lote del Jugador 3: {}'.format(g.player_3.lot))
    print('Lote del Jugador 4: {}'.format(g.player_4.lot))
    print('Lote del Jugador 5: {}'.format(g.player_5.lot))

    print('Cartas que sobran: {}'.format(g.baraja))

    print('Ordenamos los lotes de los jugadores: ')

    juego.order(g.player_1.lot)
    juego.order(g.player_2.lot)
    juego.order(g.player_3.lot)
    juego.order(g.player_4.lot)
    juego.order(g.player_5.lot)

    print('Lote del Jugador 1: {}'.format(g.player_1.lot))
    print('Lote del Jugador 2: {}'.format(g.player_2.lot))
    print('Lote del Jugador 3: {}'.format(g.player_3.lot))
    print('Lote del Jugador 4: {}'.format(g.player_4.lot))
    print('Lote del Jugador 5: {}'.format(g.player_5.lot))

    juego.elige_estrategia(g.player_1)
    juego.elige_estrategia(g.player_2)
    juego.elige_estrategia(g.player_3)
    juego.elige_estrategia(g.player_4)
    juego.elige_estrategia(g.player_5)

    print('Estrategia del Jugador 1: {}'.format(g.player_1.election))
    print('Estrategia del Jugador 2: {}'.format(g.player_2.election))
    print('Estrategia del Jugador 3: {}'.format(g.player_3.election))
    print('Estrategia del Jugador 4: {}'.format(g.player_4.election))
    print('Estrategia del Jugador 5: {}'.format(g.player_5.election))


if __name__ == "__main__":
    main()
