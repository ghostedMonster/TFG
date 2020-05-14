from deck import Deck
from functions_for_algorythm import MiniMax, choose_strategy, get_points
from player import Player
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
    #points, position_card = minimax.max_levels(player1, len(minimax.players[0].hand) - 1)
    results = minimax.max_levels_prunning_v2(5, -1000, 1000, player1, player1)
    sum_points_1 = results[0]
    card_1 = results[1]
    results = minimax.max_levels_prunning_v2(5, -1000, 1000, player1, player2)
    sum_points_2 = results[0]
    card_2 = results[1]
    results = minimax.max_levels_prunning_v2(5, -1000, 1000, player1, player3)
    sum_points_3 = results[0]
    card_3 = results[1]
    results = minimax.max_levels_prunning_v2(5, -1000, 1000, player1, player4)
    sum_points_4 = results[0]
    card_4 = results[1]
    results = minimax.max_levels_prunning_v2(5, -1000, 1000, player1, player5)
    sum_points_5 = results[0]
    card_5 = results[1]
    #points, position_card = minimax.max_levels_prunning(10, player1, len(player1.hand))
    print(sum_points_1)
    print(card_1)

    print(sum_points_2)
    print(card_2)

    print(sum_points_3)
    print(card_3)

    print(sum_points_4)
    print(card_4)

    print(sum_points_5)
    print(card_5)

    for player in minimax.players:
        number_player = minimax.number_of_player(player) + 1
        hand = ''
        won_hand = ''
        for card in player.hand:
            hand += str(card) + ', '
        for card in player.won_hand:
            won_hand += str(card) + ', '

        print("Player " + str(number_player) + "'s hand: " + hand)
        print("Player " + str(number_player) + "'s won hand: " + won_hand)
        print("Player " + str(number_player) + "'s strategy: " + str(player.choice))
        print("Player " + str(number_player) + "'s points: " + str(player.score))
        if card_1 == -1:
            card_1 = 0

        if card_2 == -1:
            card_2 = 0

        if card_3 == -1:
            card_3 = 0

        if card_4 == -1:
            card_4 = 0

        if card_5 == -1:
            card_5 = 0
        cards = [card_1, card_2, card_3, card_4, card_5]
        print("Player " + str(number_player) + "plays card " + str(cards[number_player - 1]))
        minimax.play(player, cards[number_player - 1])
    max_hearts, max_diamonds, max_clubs, max_spades = minimax.get_max_card_each_suit()
    minimax.put_won_cards_in_its_place(max_hearts, max_diamonds, max_clubs, max_clubs)

#points, position_card = minimax.max_cosa(player1)


elapsed_time = time.time() - start_time

print("elapsed time: " + str(elapsed_time) + " seconds")

for player in minimax.players:
    number_player = minimax.number_of_player(player)
    player.score = get_points(player)
    print("Player" + str(number_player) + "'s points: " + str(player.score))
