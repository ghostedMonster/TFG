class Player(object):
    """
    Jugador de la partida
    """
    def __init__(self, name, hand=None, score=0, turn=False, computer=True):
        self.name = name
        self.hand = hand
        self.score = score
        self.turn = turn
        self.selected_card = None
        self.computer = computer
        self.choice = None
        self.won_hand = []

    def __str__(self):
        return str(self.name)

    def remove_from_hand(self, card):
        """
        Quita una carta de la mano del jugador
        @param card: Carta que queremos quitar de la mano
        @return: Esa misma carta que hemos eliminado de la mano
        """
        if card and card in self.hand:
            position = self.hand.index(card)
            del self.hand[position]
            return card
        return None
