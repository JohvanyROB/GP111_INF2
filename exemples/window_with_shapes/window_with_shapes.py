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

BG_COLOR = (0, 127, 255)  #code RGB pour definir la couleur de l'arriere plan de la fenetre
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)

clock = pygame.time.Clock() #Pour gerer le nombre de FPS

pygame.init()
screen = pygame.display.set_mode(screen_size)   #creation de la fenetre
pygame.display.set_icon(pygame.image.load(img_folder_path + "/jeux-de-cartes.png")) #Ajout de l'icone
pygame.display.set_caption("GP111 - Fenetre avec des formes")    #Ajout du nom de la fenetre

running = True  #Indique si on doit fermer ou non la fenetre
while running:  #Tant que l'utilisateur n'a pas ferme la fenetre
    for event in pygame.event.get():    #Gestion des evenements   
        if event.type == pygame.QUIT:   #Si l'utilisateur clique sur le bouton pour fermer la fenetre
            running = False
    
    screen.fill(BG_COLOR)   #D'abord l'arriere plan

    pygame.draw.line(screen, YELLOW, (15, 20), (15, 400), width=3)  #param3: coordonnees du point de depart (X, Y), param4: coordonnees d'arrivee
    pygame.draw.rect(screen, GREEN, (400, 100, 100, 300), width=0)  #param3: x, y, width, height, param4: width=0: fill, width>0: border only colored
    pygame.draw.circle(screen, RED, (320, 240), 25) #param3: coordonnees du centre du cercle, param4: rayon
    pygame.draw.lines(screen, ORANGE, False, [(50, 50), (600, 50), (600, 400)], width=4)    #param3: ferme ou ouvert, param4: liste des points a relier
    
    pygame.display.update()   #Apres tous les dessins
    
    clock.tick(5)   #5 FPS    

pygame.quit()