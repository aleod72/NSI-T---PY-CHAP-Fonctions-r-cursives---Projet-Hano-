import random

class Setup:
    def __init__(self, taille):
        self.taille = taille
        self.couleur = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def __str__(self):
        return str(self.taille)