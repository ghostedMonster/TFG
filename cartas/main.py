from cartas.juego import Juego


def main():
    g = Juego()
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

    g.ordenar(g.player_1.lot)
    g.ordenar(g.player_2.lot)
    g.ordenar(g.player_3.lot)
    g.ordenar(g.player_4.lot)
    g.ordenar(g.player_5.lot)

    print('Lote del Jugador 1: {}'.format(g.player_1.lot))
    print('Lote del Jugador 2: {}'.format(g.player_2.lot))
    print('Lote del Jugador 3: {}'.format(g.player_3.lot))
    print('Lote del Jugador 4: {}'.format(g.player_4.lot))
    print('Lote del Jugador 5: {}'.format(g.player_5.lot))

    g.elegir_estrategia(g.player_1)
    g.elegir_estrategia(g.player_2)
    g.elegir_estrategia(g.player_3)
    g.elegir_estrategia(g.player_4)
    g.elegir_estrategia(g.player_5)

    print('Estrategia del Jugador 1: {}'.format(g.player_1.election))
    print('Estrategia del Jugador 2: {}'.format(g.player_2.election))
    print('Estrategia del Jugador 3: {}'.format(g.player_3.election))
    print('Estrategia del Jugador 4: {}'.format(g.player_4.election))
    print('Estrategia del Jugador 5: {}'.format(g.player_5.election))


if __name__ == "__main__":
    main()
