from random import random
class Attack(object):

    def __init__(self, prob, damage):
        self.prob = prob
	self.damage = damage
    
    def attack(self):
	if random() < prob:
	    return damage
	else:
	    return 0
