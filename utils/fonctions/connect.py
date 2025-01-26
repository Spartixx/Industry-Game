from utils.fonctions.gameVar import *
from utils.fonctions.conversion import *
from utils.fonctions.save import *
import copy

def firstConnection() -> None:
    """
    S'exécute à l'initialisation. Vérifie si il s'agit de la première connexion du joueur. Si oui, une carte par défaut est crée, sinon on charge les données sauvegardées ( carte, joueur ).
    Détail: On rempli la carte d'herbe bloquée exceptée une zone de 6x6. On y ajoute également une boutique (classe VendingMachine).
    """
    if mapConfig == {}:
        grille.append({f"{x*dimension},{y*dimension}":Bloc(dataConfig["GRASS"], 50, "grass", (x*dimension, x*dimension+dimension-1), (y*dimension, y*dimension+dimension-1), dimension, True) for y in range(1, (screenSize[1]//dimension)+1) for x in range((screenSize[0]//dimension)+1)}) # Création de la grille
        
        xy = [int(((screenSize[0]/2)//dimension)*dimension-dimension*4), int(((screenSize[1]/2)//dimension)*dimension-dimension*4)] # coordonnées du premier bloc de la zone libre à placer.
        xyCopie = copy.deepcopy(xy) 

        for i in range(6): # Hauteur
            for j in range(6): # Largeur
                grille[0][f"{xy[0]},{xy[1]}"].unblock(screen)
                xy[0] += dimension
            xy[0] = xyCopie[0]
            xy[1] += dimension
        xy = xyCopie
        grille[0][f"{xy[0]+dimension*2},{xy[1]+dimension*2}"] = vendingMachine("textures/vendingMachine.png", 1000000, "vendingMachine", [xy[0]+dimension*2,xy[0]-dimension-1], [xy[1]+dimension*2,xy[1]+dimension-1], dimension)

        saveGrille(grille) # On sauvegarde la grille

    else:
        jsonToBloc(grille)

    global playerConfig
    if playerConfig == {}:
            playerConfig = {"name": "username", "solde": 5000, "field": 100}
            savePlayer(playerConfig)