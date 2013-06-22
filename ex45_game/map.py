import sys
from time import sleep
class Map(object):

    def __init__(self, players):
        self.players = players
        names = self.players.keys()
        player2 = names.pop()
        player1 = names.pop()
        self.name_bar = player1 + self.draw_spaces(player1, player2) + player2
        self.bottom_bar = "_" * 80

    def draw_spaces(self, former, latter):
        return " " * (80 - len(former) - len(latter))

    def print_health(self, health1, health2):
        health1 = 'health %d / 100' % health1
        health2 = 'health %d / 100' % health2
        print health1 + self.draw_spaces(health1, health2) + health2

    def draw(self, health1, health2, pos1, pos2):
        print self.name_bar
        self.print_health(health1, health2)
        self.print_screen(pos1, pos2)
        print self.bottom_bar

    def print_screen(self, pos1, pos2):
        print "\n" * 6
        self.print_body("_0_", pos1, pos2)
        self.print_body(" | ", pos1, pos2)
        self.print_body("/ \\", pos1, pos2)

    def print_body(self, part, pos1, pos2):
        bar = " " * pos1 + part + " " * (74 - pos1 - pos2) + part + " " * pos2
        print bar
        

    # player1 and player2 are names
    #def draw(self, player1, player2):
    #    
    #    print player1,
    #    for i in range(80 - len(player1) - len(player2)):
    #        print "",
    #    print player2
    #
    #    health1 = 'health %d / 100' % 100
    #    health2 = 'health %d / 100' % 100
    #    print health1,
    #    for i in range(80 - len(health1) - len(health2)):
    #        print "",
    #    print health2

    #    for i in range(7):
    #        print ""

    #    print "_0_",
    #    for i in range(74):
    #        print "",
    #    print "_0_"

    #    print " | ",
    #    for i in range(74):
    #        print "",
    #    print " | "

    #    print "/ \\",
    #    for i in range(74):
    #        print "",
    #    print "/ \\"

    #    for i in range(80):
    #        sys.stdout.write('_')
    #    
    #    sys.stdout.flush()
    #    print ""

map = Map({'bob': 'hello', 'sue': 'goodbye'})
for i in range(38):
    map.draw(100, 100, i, i)
    sleep(.1)
print "-" * 80
