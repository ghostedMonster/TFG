import time
import random


def inicia_tablero():
    res = []

    for palo in range(0, 4):
        for numero in range(0, 13):
            numero_real = numero + 1
            if palo == 0:
                txt = "C{}".format(numero_real)
                res.append(txt)
            elif palo == 1:
                txt = "R{}".format(numero_real)
                res.append(txt)
            elif palo == 2:
                txt = "P{}".format(numero_real)
                res.append(txt)
            elif palo == 3:
                txt = "T{}".format(numero_real)
                res.append(txt)

    return res


class Juego:
    def __init__(self):
        self.baraja = inicia_tablero()
        self.jugadas = []
        self.player_1_won = []
        self.player_1_lot = []
        self.player_2_won = []
        self.player_2_lot = []
        self.player_3_won = []
        self.player_3_lot = []
        self.player_4_won = []
        self.player_4_lot = []
        self.player_5_won = []
        self.player_5_lot = []

    def barajar(self):
        return random.shuffle(self.baraja)

    def repartir(self):
        longitud = len(self.baraja)
        for carta in range(0, 10):
            carta_a_repartir_1 = self.baraja.pop()
            carta_a_repartir_2 = self.baraja.pop()
            carta_a_repartir_3 = self.baraja.pop()
            carta_a_repartir_4 = self.baraja.pop()
            carta_a_repartir_5 = self.baraja.pop()
            self.player_1_lot.append(carta_a_repartir_1)
            self.player_2_lot.append(carta_a_repartir_2)
            self.player_3_lot.append(carta_a_repartir_3)
            self.player_4_lot.append(carta_a_repartir_4)
            self.player_5_lot.append(carta_a_repartir_5)

    def ordenar(self, baraja):
        return baraja.sort()


def main():
    g = Juego()
    print('Baraja: {}'.format(g.baraja))
    print('Jugadas: {}'.format(g.jugadas))
    print('Ganadas por el Jugador 1: {}'.format(g.player_1_won))
    print('Lote del Jugador 1: {}'.format(g.player_1_lot))
    print('Ganadas por el Jugador 2: {}'.format(g.player_2_won))
    print('Lote del Jugador 2: {}'.format(g.player_2_lot))
    print('Ganadas por el Jugador 3: {}'.format(g.player_3_won))
    print('Lote del Jugador 3: {}'.format(g.player_3_lot))
    print('Ganadas por el Jugador 4: {}'.format(g.player_4_won))
    print('Lote del Jugador 4: {}'.format(g.player_4_lot))
    print('Ganadas por el Jugador 5: {}'.format(g.player_5_won))
    print('Lote del Jugador 5: {}'.format(g.player_5_lot))
    g.barajar()
    print('Tras barajar las cartas, la baraja ha quedado así: \n')
    print(g.baraja)
    print('Repartimos las cartas: ')
    g.repartir()

    print('Lote del Jugador 1: {}'.format(g.player_1_lot))
    print('Lote del Jugador 2: {}'.format(g.player_2_lot))
    print('Lote del Jugador 3: {}'.format(g.player_3_lot))
    print('Lote del Jugador 4: {}'.format(g.player_4_lot))
    print('Lote del Jugador 5: {}'.format(g.player_5_lot))

    print('Cartas que sobran: {}'.format(g.baraja))

    print('Ordenamos los lotes de los jugadores: ')

    g.ordenar(g.player_1_lot)
    g.ordenar(g.player_2_lot)
    g.ordenar(g.player_3_lot)
    g.ordenar(g.player_4_lot)
    g.ordenar(g.player_5_lot)

    print('Lote del Jugador 1: {}'.format(g.player_1_lot))
    print('Lote del Jugador 2: {}'.format(g.player_2_lot))
    print('Lote del Jugador 3: {}'.format(g.player_3_lot))
    print('Lote del Jugador 4: {}'.format(g.player_4_lot))
    print('Lote del Jugador 5: {}'.format(g.player_5_lot))


if __name__ == "__main__":
    main()
