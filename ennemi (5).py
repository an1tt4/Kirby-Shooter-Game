# Créé par meliani_n, le 11/10/2022 en Python 3.7

import pygame
import random
from picture import picture

#creation de la classe Ennemi
class Ennemi:

    def __init__(self, name):
        self.nom = nom #le nom de l'ennemi
        self.pv = 1 #l'ennemi n'a qu'un seul pv
        self.pv_max = 1 #l'ennemi meurt en une seule attaque
        self.att = 5 #inflige un degat de 5
        self.image = image #mettre le chemin pour trouver l'image de l'ennemi
        self.rect = self.image.get_rect() #redimensionner l'image del'ennemi
        self.rect.x = 800 + random.randint(0, 500) #positionnement de l'ennemi de droite à gauche
        self.rect.y = 500 #positionnement de l'ennemi de haut en bas
        self.vitesse = random.randint(1, 3) #vittesse aléatoire, les ennemi n"ont pastous la même vitesse

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)

    def deplacement(self):
        (x, y) = self.position
        delta_x = random.randint(- self.vitesse, self.vitesse)
        delta_y = random.randint(- self.vitesse, self.vitesse)
        self.position = (x + delta_x, y + delta_y)

    def foward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec le joueur
        if not self.check_collision(self, self.joueur):
            self.rect.x -= self.vitesse

    def dommage(self, amount): #lui retirer le montant des degats infligés
        #infliger les degats
        self.pv -= amount
        # verifier ses points point de vie : si ils sont infeerieur ou égal à 0, l'ennemi meurt
        if self.pv <= 0:
            #faire reaparaitre comme un nouveau ennemi
            self.rect.x = 800 + random.randint(0,500)
            self.vitesse = random.randint(1, 3)
            self.pv = self.pv_max



