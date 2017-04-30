#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BlackJack Game!
from random import randint

deck = {'Asso':1, 'Due':2, 'Tre':3, 'Quattro':4, 'Cinque':5, 'Sei':6, 'Sette':7, 'Otto':8, 'Nove':9, 'Dieci':10, 'Jack':10, 'Donna':10, 'Re':10}


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

    def add_bankroll(self, win):
        self.bankroll += win

    def bet(self, bet):
        self.bankroll -= bet

class Game(object):
    '''Define the game '''

    def table(self, deck, player):
        
