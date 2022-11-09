# Créé par Jean Gabriel, le 11/10/2022 en Python 3.7
import pygame
import random
class Ennemi:
    """
    On implémente la classe du joueur ici.
    Attention c'est une implémentation partielle.
    """

    def __init__(self, image, position):
        self.image = image
        self.position = position # Attention ici position sera un tuple (x,y)
        self.vie = 100
        self.vie_max = 100
        self.attaque = 10
        self.defense = 5
        self.vitesse = 5


    def deplacement(self):
        (x, y) = self.position
        delta_x = random.randint(- self.vitesse, self.vitesse)
        delta_y = random.randint(- self.vitesse, self.vitesse)
        self.position = (x + delta_x, y + delta_y)

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)