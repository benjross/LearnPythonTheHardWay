import attack
	
class Player(object):
    def __init__(self, attack):
        self.attack = attack

    def attack(self, move):
        pass

class Bob(Player):
    def attack(self, move):
        pass
