from anarquia.choice import Choice
from anarquia.deck import Deck
from anarquia.player import Player


value_suits = [2, 1, 0]

value_no_suit = [0.75, 0.5, 0]

value_misere = [1, 0.5, 0]

value_tie_breaker = [2, 1, 0.5]


def is_valid(card, player):
    """
    Función para ver si una jugada es válida o no. Una jugada será válida si la carta está en la mano del jugador.
    @param card: Carta a analizar.
    @param player: Jugador a analizar.
    @return: Un boolean indicando si la carta pertenece al jugador o no
    """
    if card in player.hand:
        return True
    else:
        return False


def sum_counts(card, suit, count, count_type):
    """
    Función que se usa en la decisión de estrategia en la analizamos carta a carta para darle una puntuación a la
    estrategia dada.
    @param card: Carta a analizar.
    @param suit: Palo que queremos analizar si es viable o no.
    @param count: Contador a usar por la función para guardar la viabilidad de la estrategia.
    @param count_type: Tipo de puntuación que usaremos para hacer los sumatorios de puntuación para ver la viabilidad
    de la estrategia.
    @return: El contador tras hacer la suma para averiguar la viabilidad de la estrategia.
    """
    number = card.rank.value
    sum_count = 0
    if suit == card.suit.name:
        if number > 10:
            sum_count = count_type[0]
        elif 5 <= number <= 10:
            sum_count = count_type[1]
        elif number < 5:
            sum_count = count_type[2]
        count += sum_count
    elif suit == 'NO_SUIT':
        if number > 10:
            sum_count = count_type[0]
        elif 5 <= number <= 10:
            sum_count = count_type[1]
        elif number < 5:
            sum_count = count_type[2]
        count += sum_count
    elif suit == 'MISERE':
        if 7 <= number < 10:
            sum_count = count_type[0]
        if 5 <= number <= 6:
            sum_count = count_type[1]
        if number < 5:
            sum_count = count_type[2]
        count += sum_count

    return count


def choose_strategy(player):
    """
    Función utilizada para la decisión de la estrategia de cada uno de los jugadores controlados por la máquina.
    @param player: Jugador al que se le va a dedicar la decisión.
    """
    cards = player.hand
    count_clubs = 0
    count_hearts = 0
    count_diamonds = 0
    count_spades = 0

    count_no_suit = 0
    count_misere = 0

    for card in cards:
        count_clubs = sum_counts(card, 'CLUBS', count_clubs, value_suits)
        count_hearts = sum_counts(card, 'HEARTS', count_hearts, value_suits)
        count_diamonds = sum_counts(card, 'DIAMONDS', count_diamonds, value_suits)
        count_spades = sum_counts(card, 'SPADES', count_spades, value_suits)

        count_no_suit = sum_counts(card, 'NO_SUIT', count_no_suit, value_no_suit)
        count_misere = sum_counts(card, 'MISERE', count_misere, value_misere)

    res = max(count_clubs, count_hearts, count_diamonds, count_spades, count_no_suit, count_misere)

    choice = Choice.MISERE
    if count_misere == res:
        choice = Choice.MISERE
    if count_no_suit == res:
        choice = Choice.NO_SUIT
    if count_clubs == res:
        choice = Choice.CLUBS
    if count_hearts == res:
        choice = Choice.HEARTS
    if count_spades == res:
        choice = Choice.SPADES
    if count_diamonds == res:
        choice = Choice.DIAMONDS

    player.choice = choice


def get_points(player):
    """
    Calcula los puntos del jugador sleccionado
    @param player: Jugador al que se le calcularán los puntos
    @return: Los puntos calculados
    """
    points = 0

    strategy = player.choice.name

    for card in player.hand:
        if strategy == card.suit.name:
            points += 2
        if strategy == 'NO_SUIT':
            points += 1
        if strategy == 'MISERE' and card.rank.value <= 10:
            points += 1

    return points


class MiniMax(object):
    """
    Clase encargada de la inteligencia del ordenador a la hora de jugar cartas en el juego
    """
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.played_cards = []

    def is_end(self):
        """
        Con esta función, vemos si el juego ha finalizado o no. 
        @return: True si no hay jugadores con cartas, False en caso contrario
        """
        check = 0
        for player in self.players:
            if len(player.hand) == 0:
                check += 1
        if check == len(self.players):
            return True
        return False

    def winner(self):
        """
        Averigua el jugador con más puntos
        @return: el jugador con mayor puntuación
        """
        res = []

        for player in self.players:
            res.append(player.score)

        max_score = max(res)

        winner = None
        for player in self.players:
            if player.score == max_score:
                winner = player

        return winner

    def number_of_player(self, player):
        """
        Cuenta el numero de jugador en la partida
        @param player: Jugador
        @return: El número de jugador en la partida
        """
        res = None
        for i in range(0, len(self.players)):
            if player == self.players[i]:
                res = i
        return res

    def play(self, player, card):
        """
        Juega la carta elegida del jugador elegido
        @param player: Jugador elegido
        @param card: Carta elegida
        """
        pass



    def min(self, player):
        """
        Función min del algoritmo minimax.  
        @param player:
        """
        pass

    def max(self, player):
        end = self.is_end()

        number_of_player = self.number_of_player(player)

        next_number_of_player = number_of_player + 1
        if next_number_of_player == len(self.players):
            next_number_of_player = 0



        points = get_points(player)

        max_points = 0

        if end:
            return self.winner()

        for card in player.hand:
            self.play(card, player)
            if self.players[next_number_of_player].computer:
                points = self.max(self.players[next_number_of_player])
            else:
                self.min(self.players[next_number_of_player])

        return points

