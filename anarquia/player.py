class Player(object):
    def __init__(self, name, hand=None, score=0, turn=False, computer=True):
        self.name = name
        self.hand = hand
        self.score = score
        self.turn = turn
        self.selected_card = None
        self.computer = computer

    def __str__(self):
        return str(self.name)

    def remove_from_hand(self, card):
        if card and card in self.hand:
            position = self.hand.index(card)
            del self.hand[position]
            return card
        return None
