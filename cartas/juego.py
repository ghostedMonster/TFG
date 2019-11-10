import time
import random
from cartas.jugador import Player


def inicia_tablero():
    res = []

    for palo in range(0, 4):
        for numero in range(0, 13):
            numero_real = numero + 1
            if palo == 0:
                if numero_real < 10:
                    txt = "C0{}".format(numero_real)
                    res.append(txt)
                else:
                    txt = "C{}".format(numero_real)
                    res.append(txt)
            elif palo == 1:
                if numero_real < 10:
                    txt = "R0{}".format(numero_real)
                    res.append(txt)
                else:
                    txt = "R{}".format(numero_real)
                    res.append(txt)
            elif palo == 2:
                if numero_real < 10:
                    txt = "P0{}".format(numero_real)
                    res.append(txt)
                else:
                    txt = "P{}".format(numero_real)
                    res.append(txt)
            elif palo == 3:
                if numero_real < 10:
                    txt = "T0{}".format(numero_real)
                    res.append(txt)
                else:
                    txt = "T{}".format(numero_real)
                    res.append(txt)

    return res


class Juego:
    def __init__(self):
        self.baraja = inicia_tablero()
        self.jugadas = []
        self.player_1 = Player()

        self.player_2 = Player()

        self.player_3 = Player()

        self.player_4 = Player()

        self.player_5 = Player()

    def barajar(self):
        return random.shuffle(self.baraja)

    def repartir(self):
        for carta in range(0, 10):
            carta_a_repartir_1 = self.baraja.pop()
            carta_a_repartir_2 = self.baraja.pop()
            carta_a_repartir_3 = self.baraja.pop()
            carta_a_repartir_4 = self.baraja.pop()
            carta_a_repartir_5 = self.baraja.pop()
            self.player_1.lot.append(carta_a_repartir_1)
            self.player_2.lot.append(carta_a_repartir_2)
            self.player_3.lot.append(carta_a_repartir_3)
            self.player_4.lot.append(carta_a_repartir_4)
            self.player_5.lot.append(carta_a_repartir_5)

    def ordenar(self, baraja):
        return baraja.sort()
