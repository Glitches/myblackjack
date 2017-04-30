#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BlackJack Game!
from random import randint

play_deck = ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Otto', 'Nove', 'Dieci', 'Jack', 'Donna', 'Re',\
'Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Otto', 'Nove', 'Dieci', 'Jack', 'Donna', 'Re',\
'Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Otto', 'Nove', 'Dieci', 'Jack', 'Donna', 'Re',\
'Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Otto', 'Nove', 'Dieci', 'Jack', 'Donna', 'Re']


class Player(object):
    '''Define object player with its inital bankroll,
    Take account

    Input:
    bankroll: player's money
    name: player's name
    '''
    def __init__(self, bankroll=100, name='Player'):
        self.name = name
        self.bankroll = bankroll
        self.hand = ['','']

    def add_bankroll(self, win):
        self.bankroll += win

    def bet(self, bet):
        self.bankroll -= bet

class Game(object):
    '''Define the game '''

    def __init__(self):
        self.player = Player()
        self.deck = play_deck
        self.bank = ['','']

    def first_draw(self):
        i = 0
        while i < 4:
            c = randint(0,54)
            if self.deck[c] != '' and self.player.hand[0] == '':
                self.player.hand[0] = self.deck[c]
                self.deck[c] = ''
                i += 1
                continue
            elif self.deck[c] != '' and self.bank[0] == '':
                self.bank[0] = self.deck[c]
                self.deck[c] = ''
                i += 1
                continue
            elif self.deck[c] != '' and self.player.hand[1] == '':
                self.player.hand[1] = self.deck[c]
                self.deck[c] = ''
                i += 1
                continue
            elif self.deck[c] != '' and self.bank[1] == '':
                self.bank[1] = self.deck[c]
                self.deck[c] = ''
                print(self.player.hand)
                i += 1
                continue
            elif self.deck[c] != '' and self.bank[1] == '':
                self.bank[1] = self.deck[c]

        # print(self.player.hand, self.bank, self.deck) debug print

    def compare_points(self):
        bank_points = 0
        player_points = 0
        points_dict = {'Asso':1, 'Due':2, 'Tre':3, 'Quattro':4, 'Cinque':5, 'Sei':6, 'Sette':7, 'Otto':8, 'Nove':9, 'Dieci':10, 'Jack':10, 'Donna':10, 'Re':10}
        for elem in self.bank:
            bank_points += int(points_dict[elem])
            # print(points_dict[elem])
            # print(elem)
        print('Bank points are: %s' %(bank_points))
        for elem in self.player.hand:
            player_points += int(points_dict[elem])
            # print(points_dict[elem])
            # print(elem)
        print('Player points are: %s' %(player_points))
andrea = Player()
game = Game()

game.first_draw()
game.compare_points()
