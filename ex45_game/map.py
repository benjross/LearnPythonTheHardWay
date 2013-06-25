import sys
from time import sleep
from attack import Attack

class Map(object):

    def __init__(self, player1, player2, players):
        '''Initializes a Map.  player1 and player2 are the players names.
        players a dictionary mapping player names to a dictionary of attacks'''
        self.players = players
        self.player2 = player2
        self.player1 = player1
        self.name_bar = self.player1
        self.name_bar += self.draw_spaces(self.player1, self.player2)
        self.name_bar += self.player2 
        self.bottom_bar = "_" * 80

    def draw_spaces(self, former, latter):
        '''Returns a string of spaces to evenly divde former and latter on an 80
        character screen.'''
        return " " * (80 - len(former) - len(latter))

    def print_health(self, health1, health2):
        '''Prints each character's health on the screen.  health1 and healt2 are
        player 1's and player2's health'''
        health1 = 'health %d / 100' % health1
        health2 = 'health %d / 100' % health2
        print health1 + self.draw_spaces(health1, health2) + health2

    def print_screen(self, pos1, pos2, message):
        '''Prints the characters on screen at pos1 and pos2 with message
        displayed in the middle of the screen'''
        print "\n" * 3
        print " " * (40 - len(message)/2),
        print "%s\n\n" % message
        self.print_body("_0_", pos1, pos2)
        self.print_body(" | ", pos1, pos2)
        self.print_body("/ \\", pos1, pos2)

    def print_body(self, part, pos1, pos2):
        '''A helper method for print_screen().  Prints a component of the
        players' bodies'''
        bar = " " * pos1 + part + " " * (74 - pos1 - pos2) + part
        print bar

    def draw_bottom(self):
        '''Prints the players moves and the bottom of the screen'''
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

    def print_death(self, message, spaces):
        '''Prints the death screen with message in the middle.  spaces is a
        boolean for if the player should be printed in the air or not.'''
        print "\n" * 3
        print " " * (40 - len(message)/2),
        if not spaces:
            print "%s\n" % message
        else:
            print "%s" % message
        print " " * 37 + "_0_"
        print " " * 37 + " | "
        print " " * 37 + "/ \\"
        if spaces:
            print ""
        print " " * 37 + ">+o"

    def draw(self, health1, health2, pos1, pos2, message):
        '''Draws the screen.  health1 and health2 are player 1's and player 2's
        health. pos1 and pos2 are their position relative to the edge with
        distance increasing towards the middle.'''
        print self.name_bar
        self.print_health(health1, health2)
        self.print_screen(pos1, pos2, message)
        print self.bottom_bar
        self.draw_bottom()
        print "\n"

    def draw_death(self, health1, health2, message, spaces):
        '''Draws the death screen with message displayed in the middle of the
        screen.  health1 and health2 are player 1's and player 2's health.
        spaces is a boolean to denote the player should be jumping on the
        oppenents body'''
        print self.name_bar
        self.print_health(health1, health2)
        self.print_death(message, spaces)
        print self.bottom_bar
        print "\n"

class Drawer(object):
    '''This is a class for animating the map'''

    def __init__(self, map):
        '''Initializes the Drawer object with a Map object named map.'''
        self.map = map

    
    def start_fight(self):
        '''Draws the beginning of the fight.'''
        for i in range(35):
            self.map.draw(100, 100, i, i, "Begin Fight!")
            sleep(.1)

    def player1_hit(self, health1, health2, damage, move):
        '''Draws player 1 hitting player 2.  health1 and health2 are the players
        health.  damage is how much damage the attack does.  move is the name of
        the attack; it gets displayed on the middle of the screen.'''
        for i in range(34, 40):
            self.map.draw(health1, health2, i, 34, move)
            sleep(.1)

        for i in range(40, 34, -1):
            self.map.draw(health1, health2 - damage, i, 34, "")
            sleep(.1)

    def player2_hit(self, health1, health2, damage, move):
        '''Draws player 2 hitting player 1.  health1 and health2 are the players
        health.  damage is how much damage the attack does.  move is the name of
        the attack; it gets displayed on the middle of the screen.'''
        for i in range(34, 40):
            self.map.draw(health1, health2, 34, i, move)
            sleep(.1)

        for i in range(40, 34, -1):
            self.map.draw(health1 - damage, health2, 34, i, "")
            sleep(.1)

    def death_player1(self, health):
        '''Draws player 2 winning and player 1 dead. health is player 2's final
        health (player 1's final health is 0 because he is dead.'''
        for i in range(10):
            self.map.draw_death(0, health, "Player 2 wins!", i % 2)
            sleep(.1)
        self.map.draw_death(0, health, "Play Again?", 0)


    def death_player2(self, health):
        '''Draws player 1 winning and player 2 dead. health is player 1's final
        health (player 2's final health is 0 because he is dead.'''
        for i in range(10):
            self.map.draw_death(health, 0,  "Player 1 wins!", i % 2)
            sleep(.1)
        self.map.draw_death(0, health, "Play Again?", 0)
