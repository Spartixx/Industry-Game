import pygame

pygame.init() # J'initialise au début, car j'importe des fonctions qui en auront besoins
from utils.fonctions.gameVar import *
from utils.fonctions.show import afficheGrille, blitButtons
from utils.fonctions.gameAction import closeGame
from utils.fonctions.files import writeData
from utils.fonctions.userAction import params, changeState
from utils.fonctions.transfer import nextConvoyeur
from utils.fonctions.machineTransfer import checkConvoyeur
from utils.fonctions.solde import updateSolde, showSolde
from utils.fonctions.connect import firstConnection


# Démarrage de Pygame ( taille de l'écran etc... )
clock = pygame.time.Clock()
running = True



# Définition d'événements personnalisés 
CHECK_MACHINES = pygame.USEREVENT + 1
CHECK_VENDING_MACHINE = pygame.USEREVENT + 2
CHECK_TRANSPORT = pygame.USEREVENT + 3
CHECK_PASSIVE = pygame.USEREVENT + 4 


# Initialisation du Jeu
screen.fill((188, 143, 75))
firstConnection()
afficheGrille()
blitButtons()

# On ajoute un timer sur les événements définis plus tôt
pygame.time.set_timer(CHECK_MACHINES, 500)
pygame.time.set_timer(CHECK_TRANSPORT, 400)
pygame.time.set_timer(CHECK_VENDING_MACHINE, 500)
pygame.time.set_timer(CHECK_PASSIVE, 3*100**2)


# Boucle de jeu
while running:
    
    # Récupérer les événements
    for event in pygame.event.get():
        # Quitte le jeu
        if event.type == pygame.QUIT:
            closeGame()
            running = False
            
         # Si un bouton de la souris est pressé 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Gauche
            if pygame.mouse.get_pressed()[0]:
                changeState()
            # Droite
            elif pygame.mouse.get_pressed()[2]:
                params()

        if event.type == CHECK_MACHINES:
            # Pour chaque Foreuse de la map
            for i in getForeuse():
                # On produit une ressource
                i.produce()
                # On l'a met sur un convoyeur si possible                
                if i.getStock() > 0:
                    checkConvoyeur(i)

            for i in getFonderies():        
                i.produce()           
                if i.getStock() < i.getMaxStock():
                    checkConvoyeur(i, "take")
                checkConvoyeur(i)

        # Gérer le transport de ressource
        if event.type == CHECK_TRANSPORT:
            # Pour tout les convoyeurs de la map
            for i in [i for i in getConvoyeur() if i.getHas()]:
                # Je cherche un convoyeur autour, je lui transmet la ressource, sinon je la garde
                nextConvoyeur(i)

        # Récupérer l'argent gagné par les boutiques.
        if event.type == CHECK_VENDING_MACHINE:
            for i in getVendingMachine():
                updateSolde(i.getMoney())
                showSolde()

        # Actualiser le revenu passif de l'industrie
        if event.type == CHECK_VENDING_MACHINE:
            industry.reset()

                

    

    pygame.display.flip() # Afficher les éléments
    clock.tick(60) # FPS

pygame.quit()