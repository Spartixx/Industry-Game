import json

def loadConfig(file:str) -> dict:

    """
    Renvoie le dictionaire du fichier de configuration prit en paramètre.

    Args:
        file (str): Le chemin vers le fichier de configuration.

    Returns:
        dict: Le dictionaire correspondant.
    """

    with open(file, "r") as f:
        return json.load(f)
    

def writeData(file:str, data:dict):

    """
    Ecris des données dans un fichier spécifique. Ecrase les données s'il y en a.

    Args:
        file (str): Le chemin vers le fichier de configuration.
        data (dict): Les données à écrire.
    """

    with open(file, "w") as f:
        json.dump(data, f)
    

