__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2023, GP111 - Grand Projet Informatique INF2, IPSA 2023"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"


import pygame, os

if os.name == "nt": #si vous etes sur Windows
    screen_resolution_to_fix = False  #Mettre cette variable a True si vous avez des pb d'affichages avec la fenetre graphique
    if screen_resolution_to_fix:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

img_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")    #emplacement du dossier 'img'

screen_size = (640, 480)    #dimensions de la fenetre (largeur et hauteur)
BG_COLOR = (255, 255, 255)  #code RGB pour definir la couleur de l'arriere plan de la fenetre
clock = pygame.time.Clock() #Pour gerer le nombre de FPS

pygame.init()
screen = pygame.display.set_mode(screen_size)   #creation de la fenetre
pygame.display.set_icon(pygame.image.load(img_folder_path + "/jeux-de-cartes.png")) #Ajout de l'icone
pygame.display.set_caption("GP111 - Fenetre avec image")    #Ajout du nom de la fenetre

image = pygame.image.load(img_folder_path + "/img.jpg") #chargement d'une image
w, h = image.get_width(), image.get_height()    #recuperation des dimensions de l'image
scale = 0.2 #facteur permettant de redimensionner l'image
image = pygame.transform.scale(image, (scale*w, scale*h))   #redimensionnement de l'image


running = True  #Indique si on doit fermer ou non la fenetre
while running:  #Tant que l'utilisateur n'a pas ferme la fenetre
    for event in pygame.event.get():    #Gestion des evenements   
        if event.type == pygame.QUIT:   #Si l'utilisateur clique sur le bouton pour fermer la fenetre
            running = False
    
    screen.fill(BG_COLOR)   #D'abord l'arriere plan

    screen.blit(image, image.get_rect(center=(screen_size[0]//2, screen_size[1]//2)))   #image au centre de la fenetre
    
    pygame.display.update()   #Apres l'ajout de l'image

    clock.tick(5)   #5 FPS

pygame.quit()