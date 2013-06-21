import attack
	
class Player(object):
    def __init__(self, attack):
        self.attack = attack

    attacks = {
              'punch': self.attack.punch(0, 0),
              'kick': self.attack.kick(0, 0)
              }
    def attack(self, move):
        Player.attacks.get(move)

class Bob(Player):
    attacks['punch'] = self.attack.punch(15, .25)
    attacks['kick'] = self.attack.special(25, .185)
    attacks['cool guy punch'] = self.attack.special(45, .1)
