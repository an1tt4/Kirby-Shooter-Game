# Créé par Jean Gabriel, le 11/10/2022 en Python 3.7

import pygame
import random
class Item:
    """
    On implémente la classe du joueur ici.
    Attention c'est une implémentation partielle.
    """

    def __init__(self, image, position, direction):
        self.image = image
        self.position = position # Attention ici position sera un tuple (x,y)
        self.direction = direction # Indique le mouvement de l'objet

    def deplacement(self):
        (x, y) = self.position
        (delta_x, delta_y) = self.direction
        self.position = (x + delta_x, y + delta_y)

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)