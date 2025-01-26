from utils.fonctions.gameVar import menu, dimension, screenSize, grille, playerConfig, screen, classInStr, state, resetState
from utils.fonctions.gameAction import placeBlock
from utils.fonctions.interfaces import *
from utils.fonctions.solde import *
import subprocess

divisedDimension = dimension//2

def changeState() -> None:
    """Est executé quand un clic gauche est effectué. Permet de détécter l'élément sur lequel le joueur clique, le cas échéant, la fonction effectue une action (ouvre un menu, exécute un bouton, place un bloc).
       Si les coordonnées sont dans l'invervalle de la barre des tâche et dans celui d'un menu, elle l'exécute.
       Si un Menu est ouvert et qu'un bouton est cliqué, elle assigne l'élément séléctionné et ferme le menu.
       Si les coordonnées sont sur la carte de jeu, elle peut : placer un bloc, acheter un terrain.
    """
    if menu[-1] == "game":
        coords = pygame.mouse.get_pos()
        
        # Barre des tâches
        
        # Menu Blocs
        if coords[0] >=0 and coords[0] < divisedDimension*4 and coords[1] >=0 and coords[1] < divisedDimension*2: 
            selection = Menu("bloc")
            if selection != None:
                buttonAction([selection[0], selection[1]], True, Bloc)
            
        # Menu Machines
        elif coords[0] >=screenSize[0]-divisedDimension*6 and coords[0] < screenSize[0]-divisedDimension*2 and coords[1] >=0 and coords[1] < divisedDimension*2:
            selection = Menu("machine")
            if selection != None:
                # Menu Convoyeurs
                if selection[1] == "convoyeur":
                    selection = Menu("convoyeur")
                buttonAction([selection[0], selection[1]], True, classInStr[selection[1]])

        # Bouton fermeture  
        elif coords[0] >=screenSize[0]-divisedDimension*2 and coords[0] <= screenSize[0] and coords[1] >=0 and coords[1] < divisedDimension*2:
            closeButton()

        # Menu Achat de Terrain
        elif coords[0] >= divisedDimension*4 and coords[0] < divisedDimension*6 and coords[1] >=0 and coords[1] < divisedDimension*2:
            selection = Menu("buyField", playerConfig=playerConfig)
            if selection != None:
                resetState()
                if selection == "yes":
                    state["buy"] = True
                state["selectionned"] = True

        elif coords[0] >= divisedDimension*6 and coords[0] < divisedDimension*8 and coords[1] >=0 and coords[1] < divisedDimension*2:
            subprocess.call(["python", "miniGames/Snake/main.py"])
            


        # Si le clic est effectué sur un bloc de la map :
        else:
            if state["selectionned"]: 
                blocKey = f"{(coords[0]//dimension)*dimension},{(coords[1]//dimension)*dimension}"
                if grille[0].get(blocKey) != None: 
                    bloc:Bloc = grille[0].get(blocKey) # On difinit notre Bloc selon les coordonnées
                    
                    if bloc.getTexture() != state["args"]["texture"] and bloc.getBlocked() == False and state["buy"] == False: 
                        placeBlock(coords, bloc)
          
                    else:
                        if bloc.getBlocked() == True and state["buy"] == True and playerConfig["field"]*1.2 <= playerConfig["solde"]:
                            bloc.unblock(screen)
                            playerConfig["field"]*=1.15
                            updateSolde(0-playerConfig["field"])
                            showSolde()
                            
                            
def params() -> None:
    """Est effectuée lors d'un Clic Droit. Si le clic est effecuté sur une Machine, le Menu d'amélioration de celle-ci est ouverte, l'amélioration esst gérée selon l'action effectuée."""
    if menu[-1] == "game":
        coords = pygame.mouse.get_pos()
        blocKey = f"{(coords[0]//dimension)*dimension},{(coords[1]//dimension)*dimension}"
        if grille[0].get(blocKey) != None:
            bloc:Bloc = grille[0].get(blocKey)
            if issubclass(type(bloc), Machine):
                
                selection = Menu("upgrade", bloc.getLevel())
                price=0
                bloc:Machine = bloc
                
                if selection == "stock":
                    if bloc.getLevel()["stock"] < 5:
                        price = priceConfig["machines"]["stock"][str(bloc.getLevel()["stock"]+1)]
                        if price <= playerConfig["solde"]:
                            bloc.upgradeStock()
                            
                elif selection == "speed":
                    if bloc.getLevel()["speed"] < 5:
                        price = priceConfig["machines"]["speed"][str(bloc.getLevel()["speed"]+1)]
                        if price <= playerConfig["solde"]:
                            bloc.upgradeSpeed()
                    
                elif selection == "ressource":
                    if bloc.getLevel()["ressource"] < 5:
                        price = priceConfig["machines"]["ressource"][str(bloc.getLevel()["ressource"]+1)]
                        if price <= playerConfig["solde"]:
                            bloc.upgradeRessource()
                            
                updateSolde(-price)
                showSolde()