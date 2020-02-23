from anarquia.deck import Deck
from anarquia.functions_for_algorythm import MiniMax, choose_strategy
from anarquia.player import Player
import time

deck = Deck()
deck.deck_shuffle()

player1 = Player("player 1", hand=deck.draw(10), turn=True)
player2 = Player("player 2", hand=deck.draw(10))
player3 = Player("player 3", hand=deck.draw(10))
player4 = Player("player 4", hand=deck.draw(10))
player5 = Player("player 5", hand=deck.draw(10))

minimax = MiniMax(deck, [player1, player2, player3, player4, player5])
for player in minimax.players:
    for position in range(0, len(player.hand)):
        player.hand[position].position_hand = position
choose_strategy(player1)
choose_strategy(player2)
choose_strategy(player3)
choose_strategy(player4)
choose_strategy(player5)

start_time = time.time()
points, p_card = minimax.max(player1)
print(points)
print(p_card)
elapsed_time = time.time() - start_time

print("elapsed time: " + str(elapsed_time) + " seconds")
