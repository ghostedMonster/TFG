import numpy

from choice import Choice
from deck import Deck
from player import Player
from suit import Suit

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

        return winner.score

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

    def undo(self, player, card):
        """
        Deshace la jugada hecha por el jugador
        @param position: Posición en la que estaba la carta
        @param card: Carta que quieres que vuelva a la mano
        @param player: Jugador a realizar el deshecho
        """
        for i in self.players:
            for j in i.won_hand:
                if j.owner == player:
                    if j.turn == card.turn:
                        card_to_remove = j
                        i.won_hand.remove(card_to_remove)
                        player.hand.append(card_to_remove)
                        player.hand.sort()

    def get_max_card_each_suit(self):
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
        return max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades

    def put_won_cards_in_its_place(self, max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades):
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

    def is_finish(self):
        res = []
        count = 0
        for player in self.players:
            if len(player.hand) == 0:
                count += 1
        if count == len(self.players):
            for player in self.players:
                res.append(get_points(player))
            return res
        else:
            return res

    def getPlayedCards(self):
        res = []
        for player in self.players:
            for card in player.won_hand:
                res.append(card)
        return res

    def finished(self, player, played_cards, objective):
        res = False
        check = 0
        for player in self.players:
            if len(player.hand) == 0:
                check += 1
        if check == len(self.players):
            res = True
        elif played_cards >= 10 - objective:
            res = True

        return res

    def max_levels(self, player, objective):
        played_cards = self.getPlayedCards()
        max_cards = [-1, -1, -1, -1, -1]
        max_position = [-1, -1, -1, -1, -1]

        number_player = self.number_of_player(player)
        next_number_of_player = number_player + 1

        if next_number_of_player == len(self.players):
            next_number_of_player = 0

        if next_number_of_player == 1:
            self.turn += 1

            max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades = self.get_max_card_each_suit()
            self.put_won_cards_in_its_place(max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades)

        number_played_cards = 10 - len(self.players[number_player].hand)

        end = self.finished(number_player, number_played_cards, objective)

        if end:
            return [get_points(self.players[0]), get_points(self.players[1]), get_points(self.players[2]),
                    get_points(self.players[3]), get_points(self.players[4])], [-1, -1, -1, -1, -1]

        for card in range(0, len(player.hand)):
            all_card = player.hand[card]
            self.play(player, card)
            points, position = self.max_levels(self.players[next_number_of_player], objective)
            for i in range(0, len(self.players)):
                if points[i] > max_cards[i]:
                    max_cards[i] = points[i]
                    max_position[i] = position[i]

            self.undo(player, all_card)
        return max_cards, max_position


    def max_levels_prunning_v2(self, depth, alpha, beta, curr_player, first_player):
        end = self.is_end()

        number_curr_player = self.number_of_player(curr_player)
        next_number_of_player = number_curr_player + 1
        number_first_player = self.number_of_player(first_player)

        if next_number_of_player == len(self.players):
            next_number_of_player = 0

        if next_number_of_player == 1:
            self.turn += 1

            max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades = self.get_max_card_each_suit()
            self.put_won_cards_in_its_place(max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades)

        if end or depth == 0:
            sum_points = 0
            for player in self.players:
                points = get_points(player)
                sum_points += points
            return sum_points, -1
        used_card = -1
        for card in range(0, len(curr_player.hand)):
            all_card = curr_player.hand[card]
            self.play(curr_player, card)

            if number_curr_player == number_first_player:
                alpha = max(alpha, self.max_levels_prunning_v2(depth - 1, alpha, beta,
                                                               self.players[next_number_of_player], first_player)[0])
                self.undo(curr_player, all_card)
                if beta <= alpha:
                    break
                else:
                    used_card = card
            else:
                beta = min(beta, self.max_levels_prunning_v2(depth - 1, alpha, beta,
                                                             self.players[next_number_of_player], first_player)[0])
                self.undo(curr_player, all_card)
                if beta <= alpha:
                    break
                else:
                    used_card = card
        if number_first_player == number_curr_player:
            return alpha, used_card
        else:
            return beta, used_card

    def max_levels_prunning(self, depth, player, started_cards):
        max_cards = [-1, -1, -1, -1, -1]
        max_position = [-1, -1, -1, -1, -1]

        end = self.is_end()

        number_player = self.number_of_player(player)
        next_number_of_player = number_player + 1

        if next_number_of_player == len(self.players):
            next_number_of_player = 0

        if next_number_of_player == 1:
            self.turn += 1

            max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades = self.get_max_card_each_suit()
            self.put_won_cards_in_its_place(max_card_hearts, max_card_diamonds, max_card_clubs, max_card_spades)

        if end or depth == 0:
            return [get_points(self.players[0]), get_points(self.players[1]), get_points(self.players[2]),
                    get_points(self.players[3]), get_points(self.players[4])], [-1, -1, -1, -1, -1]
        for card in range(0, len(player.hand)):
            all_card = player.hand[card]
            self.play(player, card)
            points, position = self.max_levels_prunning(depth - 1, self.players[next_number_of_player], started_cards)
            self.undo(player, all_card)

            sum_max_points = 0
            for point in max_cards:
                sum_max_points += point

            sum_points = 0
            for point in points:
                sum_points += point
#            if points[number_player] <= max_cards[number_player]:

            if sum_max_points > sum_points:
                break

            for i in range(0, len(self.players)):
                if i == number_player:
                    if points[i] > max_cards[i]:
                        max_cards[i] = points[i]
                        max_position[i] = card
                elif points[i] > max_cards[i]:
                    max_cards[i] = points[i]
                    max_position[i] = position[i]

        return max_cards, max_position
