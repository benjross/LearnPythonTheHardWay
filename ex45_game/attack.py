from random import random
class Attack(object):

    def __init__(self, damage, prob):
        self.prob = prob
        self.damage = damage

    def attack(self):
        if random() < self.prob:
            return self.damage
        else:
            return 0
