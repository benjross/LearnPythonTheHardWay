import sys
from time import sleep
from attack import Attack
class Map(object):

    def __init__(self, players):
        self.players = players
        names = self.players.keys()
        self.player2 = names.pop()
        self.player1 = names.pop()
        self.name_bar = self.player1
        self.name_bar += self.draw_spaces(self.player1, self.player2)
        self.name_bar += self.player2 
        self.bottom_bar = "_" * 80

    def draw_spaces(self, former, latter):
        return " " * (80 - len(former) - len(latter))

    def print_health(self, health1, health2):
        health1 = 'health %d / 100' % health1
        health2 = 'health %d / 100' % health2
        print health1 + self.draw_spaces(health1, health2) + health2

    def print_screen(self, pos1, pos2):
        print "\n" * 6
        self.print_body("_0_", pos1, pos2)
        self.print_body(" | ", pos1, pos2)
        self.print_body("/ \\", pos1, pos2)

    def print_body(self, part, pos1, pos2):
        bar = " " * pos1 + part + " " * (74 - pos1 - pos2) + part
        print bar

    def draw_bottom(self):
        player1 =  self.player1 + "'s moves:"
        player2 =  self.player2 + "'s moves:"
        print player1 + " "*(40 + (20 - len(player1))) + player2
        print "-"*20 + " "*40 + "-"*20
        print "|" + " "*18 + "|" + " "*40 +"|" + " "*18 + "|"
        moves1 = self.players.get(self.player1).keys()
        moves2 = self.players.get(self.player2).keys()
        for move1, move2 in zip(moves1, moves2):
            a = "|" + move1 + " "*(18 - len(move1)) +"|" + " "*40 + "|"
            a += move2 + " "*(18 - len(move2)) +"|"
            print a

        print "|" + " "*18 + "|" + " "*40 +"|" + " "*18 + "|"
        print "-"*20 + " "*40 + "-"*20


    def draw(self, health1, health2, pos1, pos2):
        print self.name_bar
        self.print_health(health1, health2)
        self.print_screen(pos1, pos2)
        print self.bottom_bar
        map.draw_bottom()
        print "\n"

class Drawer(object):

    def __init__(self, map):
        self.map = map

    def start_fight(self):
        for i in range(35):
            self.map.draw(100, 100, i, i)
            sleep(.1)

    def player1_hit(self, health1, health2, damage):
        for i in range(34, 40):
            self.map.draw(health1, health2, i, 34)
            sleep(.1)

        for i in range(40, 34, -1):
            self.map.draw(health1, health2 - damage, i, 34)
            sleep(.1)

    def player2_hit(self, health1, health2, damage):
        for i in range(34, 40):
            self.map.draw(health1, health2, 34, i)
            sleep(.1)

        for i in range(40, 34, -1):
            self.map.draw(health1 - damage, health2, 34, i)
            sleep(.1)

players = {                                                                 
        'bob': {                                                            
            'punch': Attack(15, .25),                                       
            'kick': Attack(25, .185),                                       
            'cool guy punch': Attack(45, .125)                              
            },                                                              
        'sue': {                                                            
            'punch': Attack(15, .25),                                       
            'kick': Attack(25, .185),                                       
            'cool gal punch': Attack(45, .125)                              
            }                                                               
        }
map = Map(players)
#for i in range(35):
#    map.draw(100, 100, i, i)
#    sleep(.1)
#drawer = Drawer(map)
#drawer.start_fight()
#drawer.player1_hit(100, 100, 25)
#drawer.player2_hit(100, 75, 25)
