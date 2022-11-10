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
        self.image=pygame.image.load('Sprites/Etoile.png')#telecharger l'image du projectile
        self.image =pygame.transform.scale(self.image,(50,50))#redimensionner l'image
       # self.rect=self.image.get_rect()# donner les coordonné exacte du joueur ou essayer plusieur chiffre à x ou y pour que l'objet sorte de sa main
       # self.rect.x = joueur.rect.x +50
       # self.rect.y = joueur.rect.y +50
    def remove(self):
        self.all_projectiles.remove(self)

    def deplacement(self):
        (x, y) = self.position
        delta_x = 5
        delta_y = random.randint(- 5, 5)
        self.position = (x + delta_x, y + delta_y)
         for ennemis in self.check_collision: #verifier si le, projectile rentre en collision avec un ennemis
            self.remove()#supprimer le projectile
            ennemis.damage(self.player.attack)# infliger des degats au monstre impacté par le projectile
        if self.rect.x >800:
            self.remove() #supprimer le projectile

    def affichage(self, surface):
        self.deplacement()
        surface.blit(self.image, self.position)
