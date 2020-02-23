from anarquia.choice import Choice
from anarquia.deck import Deck
from anarquia.player import Player
from anarquia.suit import Suit

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

    for card in player.won_hand:
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
        self.turn = 0

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

        return winner.score,

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

    def play(self, player, card_number):
        """
        Juega la carta elegida del jugador elegido
        @param card_number: Numero de la carta a jugar
        @param player: Jugador elegido
        """
        card = player.hand[card_number]
        if card in player.hand:
            card.owner = player
            card.turn = self.turn
            self.played_cards.append(card)
            player.hand.remove(card)

    def undo(self, player, card, position):
        """
        Deshace la jugada hecha por el jugador
        @param position: Posición en la que estaba la carta
        @param card: Carta que quieres que vuelva a la mano
        @param player: Jugador a realizar el deshecho
        """
        for i in self.players:
            for j in i.won_hand:
                if j.owner == player and j == card:
                    i.won_hand.remove(card)
                    player.hand.insert(position, card)

    def max(self, player):
        """
        Función max del algoritmo minimax
        @param player: Jugador que usará la función de max
        @return:
        """
        end = self.is_end()

        number_of_player = self.number_of_player(player)

        next_number_of_player = number_of_player + 1

        if next_number_of_player == 1:
            self.turn += 1
            max_card_hearts = None
            max_card_diamonds = None
            max_card_spades = None
            max_card_clubs = None
            for card in self.played_cards:
                for card_2 in self.played_cards:
                    if card.suit == card_2.suit:
                        if card.suit == Suit.HEARTS:
                            if max_card_hearts is None:
                                max_card_hearts = card
                            if card.rank.value > card_2.rank.value:
                                max_card_hearts = card
                        elif card.suit == Suit.DIAMONDS:
                            if max_card_diamonds is None:
                                max_card_diamonds = card
                            if card.rank.value > card_2.rank.value:
                                max_card_diamonds = card
                        elif card.suit == Suit.SPADES:
                            if max_card_spades is None:
                                max_card_spades = card
                            if card.rank.value > card_2.rank.value:
                                max_card_spades = card
                        elif card.suit == Suit.CLUBS:
                            if max_card_clubs is None:
                                max_card_clubs = card
                            if card.rank.value > card_2.rank.value:
                                max_card_clubs = card

            for card in self.played_cards:
                if max_card_hearts is not None:
                    if card.suit == max_card_hearts.suit:
                        new_owner = max_card_hearts.owner
                        card.won_by = new_owner
                        new_owner.won_hand.append(card)
                if max_card_diamonds is not None:
                    if card.suit == max_card_diamonds.suit:
                        new_owner = max_card_diamonds.owner
                        card.won_by = new_owner
                        new_owner.won_hand.append(card)
                if max_card_spades is not None:
                    if card.suit == max_card_spades.suit:
                        new_owner = max_card_spades.owner
                        card.won_by = new_owner
                        new_owner.won_hand.append(card)
                if max_card_clubs is not None:
                    if card.suit == max_card_clubs.suit:
                        new_owner = max_card_clubs.owner
                        card.won_by = new_owner
                        new_owner.won_hand.append(card)
            self.played_cards = []


        if next_number_of_player == len(self.players):
            next_number_of_player = 0

        points = get_points(player)
        p_card = None
        max_points = 0

        if end:
            return points, -1

        for card in range(0, len(player.hand)):
            all_card = player.hand[card]
            self.play(player, card)
            if self.players[next_number_of_player].computer:
                points, p_card = self.max(self.players[next_number_of_player])
            else:
                points, p_card = self.min(self.players[next_number_of_player])

            if points > max_points:
                max_points = points
                p_card = all_card.position_hand

            self.undo(player, all_card, card)


        print("En la posicion " + str(p_card) + ' consigues ' + str(max_points) + ' puntos')
        return max_points, p_card

    def min(self, player):
        """
        Función min del algoritmo minimax
        @param player: Jugador que hará la función de min
        @return: Puntos recibidos máximos que te darán, si juegas la carta que está en la posición que también devolvemos
        """
        end = self.is_end()

        number_of_player = self.number_of_player(player)

        next_number_of_player = number_of_player + 1
        if next_number_of_player == len(self.players):
            next_number_of_player = 0
            self.turn += 1
            max_card_hearts = None
            max_card_diamonds = None
            max_card_spades = None
            max_card_clubs = None
            for card in self.played_cards:
                for card_2 in self.played_cards:
                    if card.suit == card_2.suit and card.suit == Suit.HEARTS and card.rank.value > card_2.rank.value:
                        max_card_hearts = card
                    if card.suit == card_2.suit and card.suit == Suit.DIAMONDS and card.rank.value > card_2.rank.value:
                        max_card_hearts = card
                    if card.suit == card_2.suit and card.suit == Suit.SPADES and card.rank.value > card_2.rank.value:
                        max_card_hearts = card
                    if card.suit == card_2.suit and card.suit == Suit.CLUBS and card.rank.value > card_2.rank.value:
                        max_card_hearts = card

            max_card_hearts.owner.won_hand.append(max_card_hearts)
            max_card_diamonds.owner.won_hand.append(max_card_diamonds)
            max_card_spades.owner.won_hand.append(max_card_spades)
            max_card_clubs.owner.won_hand.append(max_card_clubs)

            for card in self.played_cards:
                if card.suit == max_card_hearts.suit:
                    new_owner = max_card_hearts.owner
                    card.won_by = new_owner
                    new_owner.won_hand.append(card)
                if card.suit == max_card_diamonds.suit:
                    new_owner = max_card_hearts.owner
                    card.won_by = new_owner
                    new_owner.won_hand.append(card)
                if card.suit == max_card_spades.suit:
                    new_owner = max_card_hearts.owner
                    card.won_by = new_owner
                    new_owner.won_hand.append(card)
                if card.suit == max_card_clubs.suit:
                    new_owner = max_card_hearts.owner
                    card.won_by = new_owner
                    new_owner.won_hand.append(card)

        points = get_points(player)
        p_card = None
        max_points = 1000

        if end:
            return points, -1

        for card in range(0, len(player.hand)):
            all_card = player.hand[card]
            self.play(player, card)
            if self.players[next_number_of_player].computer:
                points, p_card = self.max(self.players[next_number_of_player])
            else:
                points, p_card = self.min(self.players[next_number_of_player])
            if points < max_points:
                max_points = points
                p_card = card

            self.undo(player, all_card, card)


        return points, p_card
