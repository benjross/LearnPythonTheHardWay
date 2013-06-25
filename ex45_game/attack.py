from random import random

class Attack(object):
    '''A class with data for an attack'''

    def __init__(self, damage, prob):
        '''Initializes an Attack object.  damage is how much damage the attack
        does.  prob is the probability of a succesful attack'''
        self.prob = prob
        self.damage = damage

    def attack(self):
        '''Attemps an attack.  Returns the amount of damage done'''
        if random() < self.prob:
            return self.damage
        else:
            return 0
