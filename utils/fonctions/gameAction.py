from utils.fonctions.save import saveGrille, savePlayer
from utils.fonctions.gameVar import *
from utils.fonctions.solde import *
from utils.fonctions.show import blitBloc

def closeGame() -> None:
    """Permet de sauvegarder les données de la partie (Les données joueur et les données de la carte)."""
    saveGrille(grille)
    savePlayer(playerConfig)
    
    
def placeBlock(coords:tuple, bloc:Bloc) -> None:
    """Permet de placer un bloc sur la carte. Ajoute ou retire si nécessaire les blocs de leur dictionaires attitrés.

    Args:
        coords (tuple): Les coordonnées X et Y du curseur lors du Clic.
        bloc (Bloc): Une instance de la classe Bloc. Il s'agit du bloc situé aux coordonnées du Clic.
    """
    if playerConfig["solde"] >= blocConfig[state["args"]["name"]]["price"]: 
        
        xDimension = (coords[0]//dimension)*dimension 
        yDimension = (coords[1]//dimension)*dimension 
        newBloc:Bloc = state["classe"](state["args"]["texture"], blocConfig[state["args"]["name"]]["price"], blocConfig[state["args"]["name"]]["name"], (xDimension, xDimension+dimension-1), (yDimension, yDimension+dimension-1), dimension)
        grille[0][f'{xDimension},{yDimension}'] = newBloc 
        
        if ListInStr.get(bloc.getStrKey()) != None:
            if ListInStr[bloc.getName()].get(newBloc.getStrKey()) != None:
                ListInStr[bloc.getName()].pop(bloc.getStrKey())

        if state["classe"] in classInStr.values() and issubclass(state["classe"], Machine) or state["classe"] == vendingMachine or state["classe"] == Convoyeur:
            ListInStr[list(itertools.islice(classInStr.keys(), len(classInStr.keys())))[list(itertools.islice(classInStr.values(), len(classInStr.values()))).index(state["classe"])]][newBloc.getStrKey()] = newBloc

        bloc.changeTexture(state["args"]["texture"])
        blitBloc(bloc)
        updateSolde(0-newBloc.getPrice())
        showSolde()