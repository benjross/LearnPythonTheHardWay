from attack import Attack
	
class Player(object):
    attacks = {
              'punch': Attack(0, 0),
              'kick': Attack(0, 0)
              }
    def attack(self, move):
        Player.attacks.get(move).attack()

class Bob(Player):
    Player.attacks['punch'] = Attack(15, .25)
    Player.attacks['kick'] = Attack(25, .185)
    Player.attacks['cool guy punch'] = Attack(45, .1)

class Sue(Player):
    Player.attacks['punch'] = Attack(15, .25)
    Player.attacks['kick'] = Attack(25, .185)
    Player.attacks['cool guy punch'] = Attack(45, .1)
