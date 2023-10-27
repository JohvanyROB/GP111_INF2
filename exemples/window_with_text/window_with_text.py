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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock() #Pour gerer le nombre de FPS

pygame.init()
screen = pygame.display.set_mode(screen_size)   #creation de la fenetre
pygame.display.set_icon(pygame.image.load(img_folder_path + "/jeux-de-cartes.png")) #Ajout de l'icone
pygame.display.set_caption("GP111 - Fenetre avec du texte")    #Ajout du nom de la fenetre

font_bold = pygame.font.SysFont("Arial", 40, True) #param1: Police du texte, param2: taille, param3: gras ou pas
text_bold = font_bold.render("Premier texte en gras", True, RED)  #Contenu et couleur du texte

font_normal = pygame.font.SysFont("Arial", 40, False) #param1: Police du texte, param2: taille, param3: gras ou pas
text_normal = font_normal.render("Second texte (normal)", True, GREEN)  #Contenu et couleur du texte


running = True  #Indique si on doit fermer ou non la fenetre
while running:  #Tant que l'utilisateur n'a pas ferme la fenetre
    for event in pygame.event.get():    #Gestion des evenements   
        if event.type == pygame.QUIT:   #Si l'utilisateur clique sur le bouton pour fermer la fenetre
            running = False
    
    screen.fill(BG_COLOR)   #D'abord l'arriere plan
    
    screen.blit(text_bold, text_bold.get_rect(center=((screen_size[0]//2, screen_size[1]//2 - 100))))
    screen.blit(text_normal, text_normal.get_rect(center=((screen_size[0]//2, screen_size[1]//2 + 100))))

    pygame.display.update()   #Apres les textes

    clock.tick(5)   #5 FPS

pygame.quit()