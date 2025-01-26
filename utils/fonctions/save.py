from utils.fonctions.conversion import blocToJson
import json

def saveGrille(grille: list) -> None:
    """
    Sauvegarde les données de la carte dans un fichier JSON.

    Args:
        grille (list): La grille du jeu.
    """
    with open('configs/map.json', "w") as f:
        json.dump(blocToJson(grille), f)
       
        
def savePlayer(playerStats: dict) -> None:
    """
    Sauvegarde les données du joueur dans un fichier JSON.

    Args:
        playerStats (dict): Les données du joueur.
    """
    with open('configs/player.json', "w") as f:
        json.dump(playerStats, f)