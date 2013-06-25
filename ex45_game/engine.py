'''Running this module starts the game.'''

from attack import Attack
from map import Map, Drawer
from random import choice

class Engine(object):
    '''The engine that runs the game'''

    # A player is a dictionary of attacks
    players = {
            'bob': {
                'punch': Attack(10, 1),
                'kick': Attack(25, .5),
                'cool guy punch': Attack(45, .125)
                },
            'sue': {
                'punch': Attack(15, .95),
                'kick': Attack(25, .5),
                'cool gal punch': Attack(45, .125)
                },
            'ben': {
                'punch': Attack(100, 1),
                'kick': Attack(100, .5),
                'kill': Attack(100, .125)
                }
            }

    def play(self):
        '''Starts a game'''
        print "Welcome to ASCII Kombat"
        self.player = self.choose_player()
        map = Map(self.player, self.opponent, Engine.players)
        drawer = Drawer(map)
        drawer.start_fight()
        health = 100
        oppHealth = 100
        while health > 0 and oppHealth > 0:
            oppDamage = 0
            damage = 0
            attack = raw_input("attack> ")
            hit = Engine.players.get(self.player).get(attack)
            if hit:
                oppDamage = hit.attack()
                if oppDamage > oppHealth:
                    oppDamage = oppHealth
                drawer.player1_hit(health, oppHealth, oppDamage, attack)
                oppHealth -= oppDamage
                if oppHealth <= 0:
                    oppHealth = 0
                    break
            
            oppAttack = choice(Engine.players.get(self.opponent).keys())
            damage =  Engine.players.get(self.opponent).get(oppAttack).attack()
            if damage > health:
                 damage = health
            drawer.player2_hit(health, oppHealth, damage, oppAttack)
            health -= damage

        if (health > 0):
            drawer.death_player2(health)
        else:
            drawer.death_player1(oppHealth)
        answer = raw_input("> ")
        if answer == "yes":
            self.play()
        else:
            print "GAME OVER"
            
    def choose_player(self):
        '''Helper method for play().  Lets the user choose a player and randomly
        picks an opponent.'''
        print "Choose a player"
        for key in Engine.players.keys():
            print key
        player = raw_input("selection> ")
        availPlayers = Engine.players.keys()
        availPlayers.remove(player)
        self.opponent = choice(availPlayers)
        return player


game = Engine()
game.play()
