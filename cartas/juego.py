import random
from cartas.jugador import Player
from numpy.random import choice


def inicia_tablero():
    """
    Hace la baraja que se usará para el juego.
    :return: La nueva baraja sin barajar.
    """
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
    """
    Clase que define las acciones que se pueden hacer en el juego
    """
    def __init__(self):
        self.baraja = inicia_tablero()
        self.jugadas = []
        self.player_1 = Player()

        self.player_2 = Player()

        self.player_3 = Player()

        self.player_4 = Player()

        self.player_5 = Player()

    def barajar(self):
        """
        Baraja las cartas
        :return: las cartas de la baraja barajadas
        """
        return random.shuffle(self.baraja)

    def repartir(self):
        """
        Reparte equitativamente todas las cartas de la baraja que se pueden repartir.
        """
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

    def elegir_estrategia(self, player):
        """
        Esta funcion, dado un jugador, dependiendo de sus cartas, te devolverá la posible estrategia a jugar durante
        esta mano. Los posibles valores que puede tomar son: \n
            * "C": El jugador buscará coger el mayor número posible de corazones.\n
            * "R": El jugador buscará coger el mayor número posible de rombos.\n
            * "P": El jugador buscará coger el mayor número posible de picas.\n
            * "T": El jugador buscará coger el mayor número posible de tréboles.\n
            * "S": El jugador buscará coger el mayor número posible de cartas, sin importar el palo.\n
            * "M": El jugador buscará coger el mayor número posible de cartas menores a 10, sin importar el palo.\n
        La forma de decidir esto es la siguiente: \n
            Cada decisión tiene un contador. Se va contando las cartas que se tiene de cada tipo, y al final se escoge
            un valor aleatoriamente, pero con peso. Estos pesos serán estos contadores. \n
        A parte, cada decisión tiene una forma de contar: \n
            * Para las decisiones de palo, se cuenta el numero de cartas que hay de cada palo. \n
            * Para la decisión sin palo, se cuenta todas las cartas mayores o iguales a 10, sin importar el palo. \n
            * Para la decisión de misria, se mira cada dos cartas, y si la carta que se está mirando y la anterior son
              menores a 10, se cuenta uno. Esto se ha hecho así porque hay muchas más cartas menores a 10 que mayores
              o iguales a 10.
        \n
        :param player: El jugador que va a elegir la posible estrategia para el juego.
        :return: Un string con la decisión que se ha tenido al final.
        """
        player_lot = player.lot
        c_corazones = 0
        c_rombos = 0
        c_picas = 0
        c_treboles = 0
        c_sin_palo = 0
        c_miseria = 0

        for i in range(0, len(player_lot)):
            if "C" in player_lot[i]:
                c_corazones += 1
            if "R" in player_lot[i]:
                c_rombos += 1
            if "P" in player_lot[i]:
                c_picas += 1
            if "T" in player_lot[i]:
                c_treboles += 1

            numero_carta_array = [int(s) for s in player_lot[i] if s.isdigit()]
            numero_carta = (numero_carta_array[0] * 10) + numero_carta_array[1]

            if numero_carta >= 10:
                c_sin_palo += 1
            if i != 0 and i % 2 != 0 and numero_carta < 10 and \
                    [int(s) for s in player_lot[i - 1] if s.isdigit()][0] < 10:
                c_miseria += 1

        suma_todo = c_miseria + c_sin_palo + c_treboles + c_picas + c_rombos + c_corazones
        array_probabilidad = [c_corazones/suma_todo, c_rombos/suma_todo, c_picas/suma_todo, c_treboles/suma_todo,
                              c_sin_palo/suma_todo, c_miseria/suma_todo]
        election = choice(["C", "R", "P", "T", "S", "M"], 1, p=array_probabilidad)
        player.election = election
        return election

    def ordenar(self, baraja):
        """
        Ordena las cartas del array "baraja".
        :param baraja: Array con las cartas a ordenar. Normalmente se usaría con las cartas de los jugadores, pero si
        se quiere, se puede volver a ordenar la baraja de cartas del juego.
        :return: la baraja dada ordenada.
        """
        return baraja.sort()

    def is_valid(self, carta, jugador):
        """
        Define cuales son las jugadas permitidas para un jugador. En esencia, cada jugador podrá poner cualquier carta
        que tenga en su mano n juego.
        :param carta: Carta en juego
        :param jugador: Jugador que quiere poner en juego la carta
        :return: Un boolean diciendo si se puede poner o no la carta en juego
        """
        if carta in jugador.lot:
            return True
        else:
            return False

    def is_end(self):
        """
        Con esta funcion vemos si hemos terminado de jugar. Para que una partida haya terminado, se necesita que todos
        los usuarios hayan hechado todas sus cartas, a la vez que en la sección de cartas jugadas no quede ninguna,
        significando que todas las cartas han sido jugadas y todos han ganado todas sus cartas.
        :return:
        """
        if len(self.player_1.lot) == 0 and len(self.player_2.lot) == 0 and len(self.player_3.lot) == 0 and \
                len(self.player_4.lot) == 0 and len(self.player_5.lot) == 0:
            if len(self.jugadas) == 0:
                return True
        else:
            return False
