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
        for numero in range(1, 14):
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


# valor_...[0] == puntos para cartas mayores o iguales a 10
# valor_...[1] == puntos para cartas entre el 5 y el 10
# valor_...[0] == puntos para cartas menores o iguales a 4
valor_palos = [2, 1, 0]

valor_no_suit = [0.75, 0.5, 0]

valor_miseria = [1, 0.5, 0]
# valor_desempate[0] == puntos a los que se multiplica si palo
# valor_desempate[1] == puntos a los que se multiplica si no suit
# valor_desempate[2] == puntos a los que se multiplica si miseria
valor_desempate = [2, 1, 0.5]


def elige_estrategia(jugador):
    """
    Función para elegir estrategia de juego
    @param jugador: Jugador que elige la estrategia
    """
    cartas = jugador.lot

    contador_picas = 0
    contador_corazones = 0
    contador_treboles = 0
    contador_rombos = 0
    contador_no_suit = 0
    contador_miseria = 0

    for carta in cartas:
        contador_picas = suma_contador(carta, 'P', contador_picas, valor_palos)
        contador_corazones = suma_contador(carta, 'C', contador_corazones, valor_palos)
        contador_treboles = suma_contador(carta, 'T', contador_treboles, valor_palos)
        contador_rombos = suma_contador(carta, 'R', contador_rombos, valor_palos)
        contador_no_suit = suma_contador(carta, 'N', contador_no_suit, valor_no_suit)
        contador_miseria = suma_contador(carta, 'M', contador_miseria, valor_miseria)

    res = max(contador_picas, contador_corazones, contador_treboles, contador_rombos, contador_no_suit,
              contador_miseria)

    string_res = 'M'
    if contador_miseria == res:
        string_res = 'M'
    if contador_no_suit == res:
        string_res = 'N'
    if contador_picas == res:
        string_res = 'P'
    if contador_corazones == res:
        string_res = 'C'
    if contador_treboles == res:
        string_res = 'T'
    if contador_rombos == res:
        string_res = 'R'

    jugador.election = string_res

    return string_res


def suma_contador(carta, palo, contador, tipo_contador):
    """
    Suma en el contador el numero d la carta
    @param tipo_contador: el valor qu le daremos a la carta
    @param carta: carta a examinar
    @param palo: palo a comprobar
    @param contador: contador a sumar
    @return: el contador sumado
    """
    if palo in carta:
        numero = numero_carta(carta)
        suma = 0
        if numero > 10:
            suma = tipo_contador[0]
        if 5 <= numero < 10:
            suma = tipo_contador[1]
        if numero < 5:
            suma = tipo_contador[2]
        contador += suma

    elif palo == 'N':
        numero = numero_carta(carta)
        suma = 0
        if numero > 10:
            suma = tipo_contador[0]
        if 5 <= numero < 10:
            suma = tipo_contador[1]
        if numero < 5:
            suma = tipo_contador[2]
        contador += suma

    elif palo == 'M':
        numero = numero_carta(carta)
        suma = 0
        if 7 <= numero < 10:
            suma = tipo_contador[0]
        if 5 <= numero <= 6:
            suma = tipo_contador[1]
        if numero < 5:
            suma = tipo_contador[2]
        contador += suma

    return contador


def numero_carta(carta):
    """
    Te da el número de la carta
    @param carta: string qu designa la carta qu se está mirando. Ej: Si se tiene "A02", el valor de la carta será 2
    @return: Número decimal del 2 (mínimo) al 14 (el valor del ás, máximo)
    """
    numero_carta_array = [int(s) for s in carta if s.isdigit()]
    numeroTotal = (numero_carta_array[0] * 10) + numero_carta_array[1]

    return numeroTotal


def choose_strategy_random(player):
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
        card_number = (numero_carta_array[0] * 10) + numero_carta_array[1]

        if card_number >= 10:
            c_sin_palo += 1
        if i != 0 and i % 2 != 0 and card_number < 10 and \
                [int(s) for s in player_lot[i - 1] if s.isdigit()][0] < 10:
            c_miseria += 1

    suma_todo = c_miseria + c_sin_palo + c_treboles + c_picas + c_rombos + c_corazones
    array_probabilidad = [c_corazones / suma_todo, c_rombos / suma_todo, c_picas / suma_todo,
                          c_treboles / suma_todo,
                          c_sin_palo / suma_todo, c_miseria / suma_todo]
    election = choice(["C", "R", "P", "T", "S", "M"], 1, p=array_probabilidad)
    player.election = election
    return election


def order(baraja):
    """
    Ordena las cartas del array "baraja".
    :param baraja: Array con las cartas a ordenar. Normalmente se usaría con las cartas de los jugadores, pero si
    se quiere, se puede volver a ordenar la baraja de cartas del juego.
    :return: la baraja dada ordenada.
    """
    return baraja.sort()


def is_valid(carta, jugador):
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


class Game:
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

        self.players = [self.player_1, self.player_2, self.player_3, self.player_4, self.player_5]

        self.turn = 0

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

    def is_end(self):
        """
        Con esta funcion vemos si hemos terminado de jugar. Para que una partida haya terminado, se necesita que todos
        los usuarios hayan hechado todas sus cartas, a la vez que en la sección de cartas jugadas no quede ninguna,
        significando que todas las cartas han sido jugadas y todos han ganado todas sus cartas.
        :return:
        """
        if len(self.player_1.lot) == 0 and len(self.player_2.lot) == 0 and len(self.player_3.lot) == 0 and \
                len(self.player_4.lot) == 0 and len(self.player_5.lot) == 0:
            if len(self.jugadas) == 0 and (len(self.player_1.won) != 0 or len(self.player_2.won) != 0 or
                                           len(self.player_3.won) != 0 or len(self.player_4.won) != 0 or
                                           len(self.player_5.won) != 0):
                return True
        else:
            return False

    def winner(self):
        """
        Funcion que haya el ganador de la mano.
        :return: El jugador con mayor puntuación.
        """
        return max(self.player_1.points, self.player_2.points, self.player_3.points, self.player_4.points,
                   self.player_5.points)

    def play(self, jugador, carta):
        lot = jugador.lot
        card = lot[carta]

        lot.remove(card)
        jugador.played_card = card
        self.jugadas.append(card)

    def calcula_puntos(self):
        jugadores = self.players

        #Puntos de nuestros jugadores
        puntos = []
        #Cartas de nustros jugadores
        cartas_jugadas = []
        #Estrategias de nuestros jugadores
        estrategias = []

        #Palos de las cartas jugadas en la mesa
        palos_jugadas_mesa = []
        #Valor de las cartas jugadas en la mesa
        valor_jugadas_mesa = []


        for i in jugadores:
            cartas_jugadas.append(i.played_card)
            estrategias.append(i.election)

        for i in self.jugadas:
            palos_jugadas_mesa.append(i[0])
            string = ''.join(x for x in i if x.isdigit())
            valor_jugadas_mesa.append(int(string))

        #Movemos las cartas ganadoras a sus respectivos sitios
        for i in range(0, len(jugadores)):
            #Cartas con el mismo palo que la jugada por el jugador i
            mismo_palo_i = [jugadores[i].played_card]
            for j in range(0, len(self.jugadas)):
                if self.jugadas[j] != cartas_jugadas[i]:
                    if self.jugadas[j][0] == cartas_jugadas[i][0]:
                        mismo_palo_i.append(self.jugadas[j])
            valores_mismo_palo_i = []
            for j in mismo_palo_i:
                valores_mismo_palo_i.append(int(''.join(x for x in j if x.isdigit())))

            if valores_mismo_palo_i[0] == max(valores_mismo_palo_i):
                for k in valores_mismo_palo_i:
                    jugadores[i].won.append(valores_mismo_palo_i[k])
                    self.jugadas.remove(k)

        #Una vez hecho esto, calculamos las puntuaciones y las devolvemos
        for i in range(0, len(jugadores)):
            puntuacion = 0
            for j in jugadores[i].won:
                if estrategias[i] == j[0]:
                    puntuacion += int(''.join(x for x in j if x.isdigit()))
            jugadores[i].points = puntuacion
            puntos.append(puntuacion)

        return puntos




    def max(self, player):
        """
        Función principal de decisión de jugada para un jugador
        @param player:
        @return:
        """
        result = self.is_end()

        current_player = self.players[player]

        valor_maximo = 0
        carta_a_jugar = 0
        if result:
            return self.winner()

        for i in range(0, len(current_player.lot)):
            self.play(current_player, i)
            if player != 5:
                if self.players[player + 1].human:
                    min(player + 1)
                else:
                    max(player + 1)
            else:
                puntos = self.calcula_puntos()
                if puntos[player] > valor_maximo:
                    valor_maximo = puntos[player]
                    carta_a_jugar = i
                #deshacer_jugada
        return valor_maximo, carta_a_jugar



    def min(self, player):
        """

        @param player:
        """
        pass
