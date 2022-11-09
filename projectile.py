# Créé par Jean Gabriel, le 11/10/2022 en Python 3.7
import pygame
import random
class Projectile:
    """
    On implémente la classe du joueur ici.
    Attention c'est une implémentation partielle.
    """

    def __init__(self, image, position):
        self.image = image
        self.position = position # Attention ici position sera un tuple (x,y)
        self.vitesse = 5
        self.degat = 10

    def deplacement(self):
        (x, y) = self.position
        delta_x = 5
        delta_y = random.randint(- 5, 5)
        self.position = (x + delta_x, y + delta_y)

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)