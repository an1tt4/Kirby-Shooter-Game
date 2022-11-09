# Créé par Jean Gabriel, le 11/10/2022 en Python 3.7
"""
Exemple de squelette d'un jeu sous pygame.
Il y aura 4 classes: Joueur, Ennemi, Projectile et Item.
Dans le fichier principale on implémentera une classe Game qui contrôle
la boucle de jeu.
"""

import pygame
import random
from joueur import Joueur
from ennemi import Ennemi
from projectile import Projectile
from item import Item
from picture import Picture

pygame.init()

# Règlage de la taille de l'écran
LARGEUR = 800
HAUTEUR = 700

# Création d'un fenêtre de jeu
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Kirby")

# Charger les images
# images de fond
background = pygame.image.load('background/Fond1.png').convert()
taille = (8000, 500)
background = pygame.transform.scale(background, taille)

# images des personnages et ennemis
image_joueur = pygame.image.load('Sprites/kirbysprite2.png').convert()
image_ennemi = pygame.image.load('Sprites/Waddle_Dee.png').convert()

# gravité du personnage
joueur_gravity = 0

# images des projectiles
etoile = pygame.image.load('sprites/Etoile.png').convert()
mes_projectiles = [etoile]

# images des items
##item1 = pygame.image.load('sprites/item1.jpg').convert()
##item2 = pygame.image.load('sprites/item2.jpg').convert()
##mes_items = [item1, item2]



# image par seconde dans le module pygame et initialisation de l'horloge
FPS = 30
clock = pygame.time.Clock()

personnage = Joueur(image_joueur, (50, 350))
monstre = Ennemi(image_ennemi, (700, 350))



# On définit une boucle de jeux
def game_loop():

    running = True
    mouvement = 0
    vecteur = (0,0)
    frame_joueur = 0

    liste_projectiles = []

    liste_items = []
    timer_item = 0

    while running:

        # bloc d'arret du jeux en fermant avec la croix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    vecteur = (0, -1)
                    joueur_gravity = -10
                elif event.key == pygame.K_DOWN:
                    vecteur = (0, 1)
                elif event.key == pygame.K_LEFT:
                    vecteur = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    vecteur = (1, 0)
                elif event.key == pygame.K_SPACE:
                    # Tire d'un projectile
                    image_etoile = random.choice(mes_projectiles)
                    nouvelle_etoile = Projectile(image_etoile, personnage.position)
                    if len(liste_projectiles) >= 100:
                        liste_projectiles.pop(0)
                    liste_projectiles.append(nouvelle_etoile)

            if event.type == pygame.KEYUP:
                vecteur = (0,0)

        # Dessin de la fenetre graphique
        mouvement -= 2
        ecran.blit(background, (mouvement, 0))

        # Dessin du personnage et des ennemis
        frame_joueur = (frame_joueur+1)%10
        personnage.affichage_joueur(ecran, vecteur, frame_joueur)
        monstre.affichage(ecran)

        # Dessin des projectiles
        for etoile in liste_projectiles:
            etoile.affichage(ecran)

##        # Ajout d'un item
##        timer_item += 1
##        if timer_item == 30:
##            timer_item = 0
##            image_item = random.choice(mes_items)
##            position = (random.randint(200, 600), random.randint(100, 500))
##            direction = (random.randint(-5,5), random.randint(-5, 5))
##            nouvel_item = Item(image_item, position, direction)
##
##            # Pas plus de 5 items à la fois
##            if len(liste_items) >= 5:
##                liste_items.pop(0)
##            liste_items.append(nouvel_item)
##
##        # Dessin d'un item
##        for objet in liste_items:
##            objet.affichage(ecran)


        # mise à jour de la fenêtre graphique
        pygame.display.update()
        clock.tick(FPS)

# lancement du jeux
game_loop()