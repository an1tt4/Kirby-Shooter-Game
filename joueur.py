# Créé par Jean Gabriel, le 11/10/2022 en Python 3.7
import pygame
from picture import Picture

class Joueur:
    """
    On implémente la classe du joueur ici.
    Attention c'est une implémentation partielle.
    """

    def __init__(self, image, position):
        self.position = position # Attention ici position sera un tuple (x,y)
        self.vie = 100
        self.vie_max = 100
        self.attaque = 10
        self.defense = 5
        self.vitesse = 4
        self.image = image

    def deplacement(self, vecteur):
        (x, y) = self.position
        (dx, dy) = vecteur
        self.position = (x + dx * self.vitesse, y + dy * self.vitesse)

    def affichage_joueur(self, surface, vecteur, frame = 0):
        # Création d'une instance Picture pour gérer l'affichage
        image_joueur = Picture(self.image, (8, 468), (34,34), (100, 100))
        self.deplacement(vecteur)
        # Utilisation de la méthode affiche_image
        image_joueur.affichage_image(surface, (8+frame*38, 468), self.position)










