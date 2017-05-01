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

    points_dict = {'Asso':1, 'Due':2, 'Tre':3, 'Quattro':4, 'Cinque':5, 'Sei':6, 'Sette':7, 'Otto':8, 'Nove':9, 'Dieci':10, 'Jack':10, 'Donna':10, 'Re':10}
    bank_points = 0
    player_points = 0

    def __init__(self, bet=1):
        self.player = Player()
        self.deck = play_deck
        self.bank = ['','']
        self.bet = bet

    def first_draw(self):
        i = 0
        while i < 4:
            c = randint(0,51)
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
                self.deck[c] = ''

        # print(self.player.hand, self.bank, self.deck) debug print

    def compare_points(self):

        # points_dict = {'Asso':1, 'Due':2, 'Tre':3, 'Quattro':4, 'Cinque':5, 'Sei':6, 'Sette':7, 'Otto':8, 'Nove':9, 'Dieci':10, 'Jack':10, 'Donna':10, 'Re':10}
        for elem in self.bank:
            self.bank_points += int(self.points_dict[elem])
            print(self.points_dict[elem]) # debug
            print(elem) # debug
        print('Bank points are: %s' %(self.bank_points))
        for elem in self.player.hand:
            self.player_points += int(self.points_dict[elem])
            # print(points_dict[elem])
            # print(elem)
        print('Player points are: %s' %(self.player_points))

    def banker(self):
        '''attenzione che due funzioni contapunti raddoppiano il punteggio
        attenzione che va in loop perenne'''

        c = randint(0,51)
        '''for elem in self.player.hand:
            self.player_points += int(self.points_dict[elem])
        for elem in self.bank:
            self.bank_points += int(self.points_dict[elem])'''
        while self.bank_points < self.player_points and self.bank_points < 21:
            c = randint(0,51)
            # print(self.deck) # debug
            if self.deck[c] != '':
                self.bank.append(self.deck[c])

    def draw_card(self):
            c = randint(0,51)
            # print(self.deck) # debug
            while self.deck[c] == '':
                c = randint(0,51)
            self.player.hand.append(self.deck[c])
            print(self.player.hand)
            self.stand_hit()


    def stand_hit(self):
        st_hit = ' '
        while st_hit[0] != 'h' and st_hit[0] != 's':
            st_hit = input('Type \'Hit\' if you want another card , or \'Stand\' if you are already ok! -> ').lower()
        if st_hit[0] == 'h':
            self.draw_card() # chiedi carta
        else:
            self.banker()





    #def hit(self):
    #def double(self):
    '''def bet(self):
        while self.bet != '1' and self.bet != '5' and self.bet != '10':
            self.bet = input('How much do you want bet? 1/5/10')'''



print('''Welcome to my project BlackJack!
It's pretty easy to play''')
end = 'y'
while end[0] == 'y':
    bet = input('how much you want to bet? ')
    andrea = Player()
    game = Game(bet)
    #game.bet()
    game.first_draw()
    game.stand_hit()
    # game.banker()
    game.compare_points()
    end = input('Do you want play again? Y/N ').lower()
print('Thank you for playing!')
