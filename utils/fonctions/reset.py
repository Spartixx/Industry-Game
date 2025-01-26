import json

def writeData(file:str, data:dict):

    """
    Ecris des données dans un fichier spécifique. Ecrase les données s'il y en a.

    Args:
        file (str): Le chemin vers le fichier de configuration.
        data (dict): Les données à écrire.
    """

    with open(file, "w") as f:
        json.dump(data, f)

def resetDatas():
    """
    Rénitialise les données de la map.
    """
    writeData("configs/map.json", {})
    writeData("configs/player.json", {"name": "username", "solde": 340, "field": 100})

if __name__ == "__main__":
    print("Rénitialisation des données effectuées avec succès !")
    resetDatas()