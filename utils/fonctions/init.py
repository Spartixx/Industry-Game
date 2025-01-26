from utils.fonctions.gameVar import *

def getBlocInit(blocs: list) -> None:
    """Permet d'ajouter tout les blocs passés en paramètre dans la liste blocs dans leur dictionnaire. Permet de remplir les dictionaires de chacuns de leurs blocs assignés avec les blocs de la carte. (ajoute toute les fonderies dans le dictionaires fonderies par exemple).

    Args:
        blocs (list): Liste de noms de Blocs (foreuse, fonderie etc...) (str). Il s'agit des blocs pour lesquels il faut créer un dictionaire dans lequel on y ajoute chacun des blocs correspondant.
    """
    for i in grille[0].values(): 
        if i.getName() in blocs: 
            ListInStr[i.getName()][i.getStrKey()] = i