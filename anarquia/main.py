# coding=utf-8
from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

from choice import Choice
from deck import Deck
from functions_for_algorythm import choose_strategy, MiniMax, get_points
from player import Player

from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')


class FirstScreen(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    carta = None
    minimax = None

    def on_release(self):
        cartas_player1_layout = self.parent
        player1_layout = cartas_player1_layout.parent
        screen = player1_layout.parent
        for child in screen.children:
            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = True

        count_strategies = 0
        mi_carta = None

        carta_completa_player1 = None
        carta_completa_player2 = None
        carta_completa_player3 = None
        carta_completa_player4 = None
        carta_completa_player5 = None

        for card in range(0, len(self.minimax.players[0].hand)):
            if self.minimax.players[0].hand[card].image == self.carta.image:
                mi_carta = card
        for player in self.minimax.players:
            if player.choice is not None:
                count_strategies += 1
        if count_strategies == 5:
            if len(self.minimax.players[1].hand) <= 5:
                results_2 = self.minimax.max_levels_prunning_v2(10, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[1])
                results_3 = self.minimax.max_levels_prunning_v2(10, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[2])
                results_4 = self.minimax.max_levels_prunning_v2(10, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[3])
                results_5 = self.minimax.max_levels_prunning_v2(10, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[4])
            else:
                results_2 = self.minimax.max_levels_prunning_v2(5, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[1])
                results_3 = self.minimax.max_levels_prunning_v2(5, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[2])
                results_4 = self.minimax.max_levels_prunning_v2(5, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[3])
                results_5 = self.minimax.max_levels_prunning_v2(5, -1000, 1000, self.minimax.players[0],
                                                                self.minimax.players[4])

            carta_completa_player1 = self.minimax.players[0].hand[mi_carta]
            carta_completa_player2 = self.minimax.players[1].hand[results_2[1]]
            carta_completa_player3 = self.minimax.players[2].hand[results_3[1]]
            carta_completa_player4 = self.minimax.players[3].hand[results_4[1]]
            carta_completa_player5 = self.minimax.players[4].hand[results_5[1]]
            # points, positions = self.minimax.max_levels(self.minimax.players[0], len(self.minimax.players[0].hand) - 1)
            self.minimax.play(self.minimax.players[0], mi_carta)
            self.minimax.play(self.minimax.players[1], results_2[1])
            self.minimax.play(self.minimax.players[2], results_3[1])
            self.minimax.play(self.minimax.players[3], results_4[1])
            self.minimax.play(self.minimax.players[4], results_5[1])

        cartas_player1_layout = self.parent
        player1_layout = cartas_player1_layout.parent
        screen = player1_layout.parent
        for child in screen.children:

            if child.name == 'players':

                for child1 in child.children:
                    if child1.name == 'player2':
                        for child2 in child1.children:
                            if child2.name == 'cards':
                                child2.remove_widget(child2.children[0])
                    if child1.name == 'player3':
                        for child2 in child1.children:
                            if child2.name == 'cards':
                                child2.remove_widget(child2.children[0])
                    if child1.name == 'player4':
                        for child2 in child1.children:
                            if child2.name == 'cards':
                                child2.remove_widget(child2.children[0])
                    if child1.name == 'player5':
                        for child2 in child1.children:
                            if child2.name == 'cards':
                                child2.remove_widget(child2.children[0])

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'cards':
                        imagen_mi_carta = carta_completa_player1.image
                        for child2 in child1.children:
                            child2.disabled = True
                            if child2.source == imagen_mi_carta:
                                child1.remove_widget(child2)

            if child.name == 'board':
                carta_player1 = Image(source=carta_completa_player1.image, size_hint=(.1, .15),
                                      pos=(0.5 * child.size[0], 0))
                carta_player2 = Image(source=carta_completa_player2.image, size_hint=(.1, .15),
                                      pos=(0, 0.9 * child.size[1]))
                carta_player3 = Image(source=carta_completa_player3.image, size_hint=(.1, .15),
                                      pos=(0.25 * child.size[0], 0.9 * child.size[1]))
                carta_player4 = Image(source=carta_completa_player4.image, size_hint=(.1, .15),
                                      pos=(0.5 * child.size[0], 0.9 * child.size[1]))
                carta_player5 = Image(source=carta_completa_player5.image, size_hint=(.1, .15),
                                      pos=(0.75 * child.size[0], 0.9 * child.size[1]))

                child.add_widget(carta_player1)
                child.add_widget(carta_player2)
                child.add_widget(carta_player3)
                child.add_widget(carta_player4)
                child.add_widget(carta_player5)

                animation_1 = Animation(pos=(child.size[0] * 0.5, child.size[1] * 0.35), duration=2,
                                        transition='out_bounce')
                animation_2 = Animation(pos=(child.size[0] * 0.120, child.size[1] * 0.55), duration=2,
                                        transition='out_bounce')
                animation_3 = Animation(pos=(child.size[0] * 0.35, child.size[1] * 0.55), duration=2,
                                        transition='out_bounce')
                animation_4 = Animation(pos=(child.size[0] * 0.55, child.size[1] * 0.55), duration=2,
                                        transition='out_bounce')
                animation_5 = Animation(pos=(child.size[0] * 0.8, child.size[1] * 0.55), duration=2,
                                        transition='out_bounce')

                animation_1.start(carta_player1)
                animation_2.start(carta_player2)
                animation_3.start(carta_player3)
                animation_4.start(carta_player4)
                animation_5.start(carta_player5)

                next_button = Button(text='Next turn', pos=(0, child.size[1] * 0.2), size_hint=(1, 0.05),
                                     on_release=screen.next_round)
                child.add_widget(next_button)

class FinishScreen(Screen):
    def on_pre_enter(self, *args):
        minimax = self.manager.get_screen('game').minimax
        for i in self.children:
            if i.name == 'all':
                for j in i.children:
                    if j.name == 'player1':
                        player1 = minimax.players[0]
                        player1.score = get_points(player1)
                        j.text += str(player1.score)
                    if j.name == 'player2':
                        player2 = minimax.players[1]
                        player2.score = get_points(player2)
                        j.text += str(player2.score)
                    if j.name == 'player3':
                        player3 = minimax.players[2]
                        player3.score = get_points(player3)
                        j.text += str(player3.score)
                    if j.name == 'player4':
                        player4 = minimax.players[3]
                        player4.score = get_points(player4)
                        j.text += str(player4.score)
                    if j.name == 'player5':
                        player5 = minimax.players[4]
                        player5.score = get_points(player5)
                        j.text += str(player5.score)

class SecondScreen(Screen):
    deck = None
    player1 = None
    player2 = None
    player3 = None
    player4 = None
    player5 = None
    minimax = None

    def update_won_cards(self, cards_to_update):
        card_images = []
        for card in cards_to_update:
            card_images.append(card.image)
        for child in self.children:
            if child.name == "board":
                board = child
                for child1 in board.children:
                    cards_for_player_1 = []
                    cards_for_player_2 = []
                    cards_for_player_3 = []
                    cards_for_player_4 = []
                    cards_for_player_5 = []

                    if child1.source in card_images:
                        carta = child1
                        anim = Animation()
                        for i in cards_to_update:
                            if carta.source == i.image:
                                if i.won_by == self.minimax.players[0]:
                                    anim = Animation(pos=(self.size[0] * 0.5, self.size[1] * 0.2), size=(50, 75),
                                                     duration=0.5, t='out_elastic')

                                elif i.won_by == self.minimax.players[1]:
                                    anim = Animation(pos=(self.size[0] * 0.15, self.size[1] * 0.7), size=(50, 75),
                                                     duration=0.5, t='out_elastic')

                                elif i.won_by == self.minimax.players[2]:
                                    anim = Animation(pos=(self.size[0] * 0.35, self.size[1] * 0.7), size=(50, 75),
                                                     duration=0.5, t='out_elastic')

                                elif i.won_by == self.minimax.players[3]:
                                    anim = Animation(pos=(self.size[0] * 0.65, self.size[1] * 0.7), size=(50, 75),
                                                     duration=0.5, t='out_elastic')

                                elif i.won_by == self.minimax.players[4]:
                                    anim = Animation(pos=(self.size[0] * 0.85, self.size[1] * 0.7), size=(50, 75),
                                                     duration=0.5, t='out_elastic')
                        anim.bind(on_complete=self.give_won_card)
                        anim.start(carta)

    def give_won_card(self, animation, widget):
        for i in self.children:
            if i.name == "board":
                board = i
                board.remove_widget(widget)
            if i.name == "players":
                players = i
                for j in players.children:
                    if j.name == "player2":
                        player2 = j
                        for k in player2.children:
                            if k.name == "won_cards":
                                for card in self.minimax.players[1].won_hand:
                                    if card.image == widget.source:
                                        won_cards = k
                                        carta = Image(source=widget.source, size_hint=widget.size_hint,
                                                      allow_stretch=True)
                                        won_cards.add_widget(carta)
                    if j.name == "player3":
                        player3 = j
                        for k in player3.children:
                            if k.name == "won_cards":
                                for card in self.minimax.players[2].won_hand:
                                    if card.image == widget.source:
                                        won_cards = k
                                        carta = Image(source=widget.source, size_hint=widget.size_hint,
                                                      allow_stretch=True)
                                        won_cards.add_widget(carta)
                    if j.name == "player4":
                        player4 = j
                        for k in player4.children:
                            if k.name == "won_cards":
                                for card in self.minimax.players[3].won_hand:
                                    if card.image == widget.source:
                                        won_cards = k
                                        carta = Image(source=widget.source, size_hint=widget.size_hint,
                                                      allow_stretch=True)
                                        won_cards.add_widget(carta)
                    if j.name == "player5":
                        player5 = j
                        for k in player5.children:
                            if k.name == "won_cards":
                                for card in self.minimax.players[4].won_hand:
                                    if card.image == widget.source:
                                        won_cards = k
                                        carta = Image(source=widget.source, size_hint=widget.size_hint,
                                                      allow_stretch=True)
                                        won_cards.add_widget(carta)
            if i.name == "player1":
                player1 = i
                for j in player1.children:
                    if j.name == "won_cards":
                        for card in self.minimax.players[0].won_hand:
                            if card.image == widget.source:
                                won_cards = j
                                carta = Image(source=widget.source, size_hint=widget.size_hint, allow_stretch=True)
                                won_cards.add_widget(carta)

    def next_round(self, *largs):
        if self.minimax.is_end():
            self.manager.current = 'finish'

        for i in self.children:
            if i.name == "board":
                board = i
                for j in board.children:
                    if isinstance(j, Button):
                        board.remove_widget(j)
            if i.name == "player1":
                player1 = i
                for j in player1.children:
                    if j.name == "cards":
                        cards = j
                        for card in cards.children:
                            card.disabled = False

        cards_to_update = self.minimax.played_cards
        max_hearts, max_diamonds, max_clubs, max_spades = self.minimax.get_max_card_each_suit()
        self.minimax.put_won_cards_in_its_place(max_hearts, max_diamonds, max_clubs, max_spades)
        self.update_won_cards(cards_to_update)

    def give_player(self, player, x, y, offset):
        for card in range(offset, len(player.hand) + offset):
            for child in self.children:
                if child.name == 'board':
                    anim = Animation(x=x, y=y, duration=0.4, t='out_elastic')
                    if player == self.player1:
                        anim.bind(on_complete=self.show_cards_player1)
                    if player == self.player2:
                        anim.bind(on_complete=self.show_cards_player2)
                    if player == self.player3:
                        anim.bind(on_complete=self.show_cards_player3)
                    if player == self.player4:
                        anim.bind(on_complete=self.show_cards_player4)
                    if player == self.player5:
                        anim.bind(on_complete=self.show_cards_player5)

                    widget = child.children[offset]
                    anim.start(widget)

    def remove_from_board(self):
        for child in self.children:
            if child.name == 'board':
                child.remove_widget(child.children[0])

    def choose_hearts(self, *args):
        self.player1.choice = Choice.HEARTS
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: Corazones'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def choose_diamonds(self, *args):
        self.player1.choice = Choice.DIAMONDS
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: Diamantes'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def choose_clubs(self, *args):
        self.player1.choice = Choice.CLUBS
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: Tréboles'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def choose_spades(self, *args):
        self.player1.choice = Choice.SPADES
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: Picas'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def choose_no_suit(self, *args):
        self.player1.choice = Choice.NO_SUIT
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: No suit'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def choose_misere(self, *args):
        self.player1.choice = Choice.MISERE
        choose_strategy(self.player2)
        choose_strategy(self.player3)
        choose_strategy(self.player4)
        choose_strategy(self.player5)

        for child in self.children:
            if child.name == 'players':
                for child1 in child.children:
                    if child1.name == 'player2':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player2.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player3':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player3.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player4':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player4.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))
                    if child1.name == 'player5':
                        child1.add_widget(Label(name='strategy', text='Estrategia: ' + str(self.player5.choice),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.05}))

            if child.name == 'player1':
                for child1 in child.children:
                    if child1.name == 'buttons':
                        child1.clear_widgets()
                        child1.add_widget(Label(name='strategy', text='Estrategia: Misère'))
                    if child1.name == 'cards':
                        for child2 in child1.children:
                            child2.disabled = False

    def show_cards_player1(self, animation, widget):
        self.remove_from_board()
        for card in self.player1.hand:
            for child in self.children:
                if child.name == 'player1':
                    for child1 in child.children:
                        if child1.name == 'buttons':
                            player = child1
                            if len(player.children) < 6:
                                player.add_widget(Button(text='Corazones', on_release=self.choose_hearts))
                                player.add_widget(Button(text='Diamantes', on_release=self.choose_diamonds))
                                player.add_widget(Button(text='Tréboles', on_release=self.choose_clubs))
                                player.add_widget(Button(text='Picas', on_release=self.choose_spades))
                                player.add_widget(Button(text='No Suit', on_release=self.choose_no_suit))
                                player.add_widget(Button(text='Misère', on_release=self.choose_misere))
                        if child1.name == 'cards':
                            player = child1

                            if len(player.children) < 10:
                                carta = ImageButton(
                                    source=card.image, size_hint=(0.2, 1),
                                    allow_stretch=True, disabled=True
                                )
                                carta.carta = card
                                carta.minimax = self.minimax
                                player.add_widget(carta)

    def show_cards_player2(self, animation, widget):
        self.remove_from_board()
        for card in self.player2.hand:
            for child in self.children:
                if child.name == 'players':
                    for child1 in child.children:
                        if child1.name == 'player2':
                            for child2 in child1.children:
                                if child2.name == 'cards':
                                    player = child2
                                    if len(player.children) < 10:
                                        player.add_widget(Image(
                                            source='cartas/zzzz_red_back.png', size_hint=(0.1, 0.2),
                                            allow_stretch=True
                                        ))

    def show_cards_player3(self, animation, widget):
        self.remove_from_board()
        for card in self.player3.hand:
            for child in self.children:
                if child.name == 'players':
                    for child1 in child.children:
                        if child1.name == 'player3':
                            for child2 in child1.children:
                                if child2.name == 'cards':
                                    player = child2
                                    if len(player.children) < 10:
                                        player.add_widget(Image(
                                            source='cartas/zzzz_red_back.png', size_hint=(0.1, 0.2),
                                            allow_stretch=True
                                        ))

    def show_cards_player4(self, animation, widget):
        self.remove_from_board()
        for card in self.player4.hand:
            for child in self.children:
                if child.name == 'players':
                    for child1 in child.children:
                        if child1.name == 'player4':
                            for child2 in child1.children:
                                if child2.name == 'cards':
                                    player = child2
                                    if len(player.children) < 10:
                                        player.add_widget(Image(
                                            source='cartas/zzzz_red_back.png', size_hint=(0.1, 0.2),
                                            allow_stretch=True
                                        ))

    def show_cards_player5(self, animation, widget):
        self.remove_from_board()
        for card in self.player5.hand:
            for child in self.children:
                if child.name == 'players':
                    for child1 in child.children:
                        if child1.name == 'player5':
                            for child2 in child1.children:
                                if child2.name == 'cards':
                                    player = child2
                                    if len(player.children) < 10:
                                        player.add_widget(Image(
                                            source='cartas/zzzz_red_back.png', size_hint=(0.1, 0.2),
                                            allow_stretch=True
                                        ))

    def begin(self, *args):
        self.deck = Deck()
        self.deck.deck_shuffle()

        cartas = []
        for card in self.deck.cards:
            card.image = "cartas/" + str(card) + ".png"
            for child in self.children:
                if child.name == 'board':
                    imagen = Image(
                        source='cartas/zzzz_red_back.png',
                        size_hint=(0.1, 0.2),
                        allow_stretch=True,
                        pos=(0.9 * self.size[0], 0.5 * self.size[1])
                    )
                    child.add_widget(imagen)

        self.player1 = Player("player 1", hand=self.deck.draw(10), turn=True)
        self.give_player(self.player1, 0.1 * self.size[0], 0.075 * self.size[1], 0)
        self.player1.hand.sort()

        self.player2 = Player("player 2", hand=self.deck.draw(10))
        self.give_player(self.player2, 0.125 * self.size[0], 0.8 * self.size[1], 10)
        self.player2.hand.sort()

        self.player3 = Player("player 3", hand=self.deck.draw(10))
        self.give_player(self.player3, 0.375 * self.size[0], 0.8 * self.size[1], 20)
        self.player3.hand.sort()

        self.player4 = Player("player 4", hand=self.deck.draw(10))
        self.give_player(self.player4, 0.625 * self.size[0], 0.8 * self.size[1], 30)
        self.player4.hand.sort()

        self.player5 = Player("player 5", hand=self.deck.draw(10))
        self.give_player(self.player5, 0.875 * self.size[0], 0.8 * self.size[1], 40)
        self.player5.hand.sort()

        self.minimax = MiniMax(self.deck, [self.player1, self.player2, self.player3, self.player4, self.player5])

        for child in self.children:
            if child.name == 'buttons':
                for child1 in child.children:
                    if child1.name == 'start_btn':
                        child1.disabled = True


class MyScreenManager(ScreenManager):
    pass


root_widget = Builder.load_file('card.kv')


class CardApp(App):
    def build(self):
        return root_widget


if __name__ == "__main__":
    CardApp().run()
