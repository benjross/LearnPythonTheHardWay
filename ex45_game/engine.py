from attack import Attack
from map import Map, Drawer
from random import choice

class Engine(object):

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

    def __init__(self):
        self.availPlayers = Engine.players.keys()        
        self.map = Map(Engine.players)
        self.drawer = Drawer(self.map)

    def play(self):
        print "Welcome to ASCII Kombat"
        self.player = self.choose_player()
        self.drawer.start_fight()
        #print Engine.players.get(self.player)
        #print Engine.players.get(self.opponent)
        health = 100
        oppHealth = 100
        while health > 0 and oppHealth > 0:
            attack = raw_input("attack> ")
            oppDamage = Engine.players.get(self.player).get(attack).attack()
            oppAttack = choice(Engine.players.get(self.opponent).keys())
            damage =  Engine.players.get(self.opponent).get(oppAttack).attack()
            self.drawer.player1_hit(health, oppHealth, oppDamage, attack)
            oppHealth -= oppDamage
            if oppHealth <= 0:
                oppHealth = 0
                break
            self.drawer.player2_hit(health, oppHealth, damage, oppAttack)
            health -= damage
        if (health > 0):
            drawer.death_player2()
        else:
            drawer.death_player1()
            

    def choose_player(self):
        print "Choose a player"
        for key in Engine.players.keys():
            print key
        player = raw_input("selection> ")
        self.availPlayers.remove(player)
        self.opponent = choice(self.availPlayers)
        return player


game = Engine()
game.play()
