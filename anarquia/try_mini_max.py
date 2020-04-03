from anarquia.deck import Deck
from anarquia.functions_for_algorythm import MiniMax, choose_strategy, get_points
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

choose_strategy(player1)
choose_strategy(player2)
choose_strategy(player3)
choose_strategy(player4)
choose_strategy(player5)

player1.hand.sort()
player2.hand.sort()
player3.hand.sort()
player4.hand.sort()
player5.hand.sort()

for player in minimax.players:
    for position in range(0, len(player.hand)):
        player.hand[position].position_hand = position

start_time = time.time()
while not minimax.is_end():
    #points, position_card = minimax.max_levels(player1, len(minimax.players[0].hand) - 2)
    points, position_card = minimax.max_levels_prunning(15, player1)
    print(points)
    print(position_card)
    for player in minimax.players:
        number_player = minimax.number_of_player(player)
        print("Player " + str(number_player) + "'s hand: " + str(player.hand))
        print("Player " + str(number_player) + "'s won hand: " + str(player.won_hand))
        print("Player " + str(number_player) + "'s points" + str(player.score))
        if position_card[number_player] == -1:
            position_card[number_player] = 0
        print("Player " + str(number_player) + "plays card " + str(position_card[number_player]))
        minimax.play(player, position_card[number_player])

#points, position_card = minimax.max_cosa(player1)


elapsed_time = time.time() - start_time

print("elapsed time: " + str(elapsed_time) + " seconds")

for player in minimax.players:
    number_player = minimax.number_of_player(player)
    player.score = get_points(player)
    print("Player" + str(number_player) + "'s points: " + str(player.score))
