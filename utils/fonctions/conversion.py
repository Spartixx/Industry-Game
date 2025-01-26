from utils.fonctions.gameVar import getClassInStr, getMachines, getActiveConvoyeurs
from utils.fonctions.init import getBlocInit
import json
import itertools

def blocToJson(grille:list) -> dict:
    """Convertit la grille sous le format JSON. Convertit les classes ( Bloc ou une de ses instances ) de la grille sous le format JSON afin d'être sauvegardé.

    Args:
        grille (list): Il s'agit de la grille de jeu.

    Returns:
        dict: Renvoie la grille de jeu sous le format JSON
    """
    return {"grille": [i.getArgs() for i in grille[0].values()]}

def jsonToBloc(grille:list) -> None:
    """Convertit la grille de jeu stocké au format JSON sous forme d'une liste avec un dictionaire de clés : 'coordonnées de blocs' et de valeur : 'classe Bloc ou enfant de la classe Bloc'."""
    with open('configs/map.json', "r") as f:
        data = json.load(f)
        grille.append({i["coords"]: getClassInStr()[i["name"]](*list(itertools.islice(i.values(), 1, len(i.values())))) for i in data["grille"]})
        getBlocInit(["foreuse", "convoyeur", "fonderie", "vendingMachine"])
        for i, j in getMachines()["convoyeur"].items():
            if j.getHas():
                getActiveConvoyeurs()[i] = j