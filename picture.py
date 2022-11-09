# Créé par houot_j, le 20/10/2022 en Python 3.7
import pygame

class Picture:

    def __init__(self, image, position, taille_extraite, taille_affichee):
        """
        On extrait une partie rectangulaire d'une grande image.
        Les coordonnées du point en haut à gauche est position.
        taille_extraite représente les dimensions extraite de l'image originale.
        taille_affichee représente la déformation de l'image que l'on veut afficher.

        """
        self.image = image
        self.position = position
        self.taille_originale = image.get_size()
        self.taille_extraite = taille_extraite
        self.taille_affichee = taille_affichee

    def obtenir_image(self):
        """
        Cette méthode permet de modifier d'extraite une partie de l'image chargée.
        Puis de la mettre à la taille demandée.
        """
        (x,y) = self.position
        (longueur, largeur) = self.taille_extraite
        # On extrait une sous partie de l'image de départ
        image_extraite = self.image.subsurface((x, y, longueur, largeur))
        image_transformee = pygame.transform.scale(image_extraite, self.taille_affichee)
        transparence = self.image.get_at(self.position)
        image_transformee.set_colorkey(transparence)
        # On étire l'image à la taille voulue
        return image_transformee

    def affichage_image(self, ecran, position_extration, nouvelle_position = (0,0)):
        """
        On change la position d'extraction de l'image de départ.
        On charge ensuite l'image sur la fenêtre écran sur nouvelle_position.
        Pour un fond d'écran, on garde nouvelle_position par défaut (0,0).
        Pour un objet ou un personnage, on change nouvelle_position.
        """
        # On met à jour la position d'extration
        self.position = position_extration
        image = self.obtenir_image()
        # On affiche l'image à la position nouvelle_position.
        ecran.blit(image, nouvelle_position)

    def liste_animation(self, position_depart, longueur, nombre):
        """
        Pour gérer une animation, on extrait de la feuille de sprit une série d'images.

        """
        # On gére la transparence des images
        animation = []
        for i in range(nombre):
            (x,y) = position_depart
            # On définit la position de l'image
            self.position = (x + i * longueur, y)
            # On récupère la bonne image
            image = self.obtenir_image()
            # On l'ajoute à la liste des images
            animation.append(image)
        return animation




