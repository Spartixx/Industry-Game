import pygame
from classes.Bloc import *
from classes.Industry import Industry
from utils.fonctions.files import loadConfig


dataConfig = loadConfig('configs/config.json')
mapConfig = loadConfig('configs/map.json')
blocConfig = loadConfig('configs/blocs.json')
playerConfig = loadConfig('configs/player.json')
itemConfig = loadConfig('configs/items.json')
priceConfig = loadConfig("configs/price.json")

dimension = 64
screen = pygame.display.set_mode(((pygame.display.get_desktop_sizes()[0][0]), (pygame.display.get_desktop_sizes()[0][1])))
screenSize = pygame.display.get_window_size()
state = {"selectionned": False, "args": {"texture": "", "name": ""}, "classe": Bloc, "buy": False}
grille = []
menu = ["game"]
classInStr = {"foreuse": Foreuse, "grass": Bloc, "dirt": Bloc, "convoyeur": Convoyeur, "fonderie": Fonderie, "vendingMachine": vendingMachine}
foreuses = {}
convoyeurs = {}
fonderies = {}
activeConvoyeurs = {}
vendingMachineList = {}
ListInStr = {"foreuse": foreuses, "convoyeur": convoyeurs, "fonderie": fonderies, "vendingMachine": vendingMachineList}
industry = Industry()

def getPassive() -> int:
    """renvoie le revenu passif de l'industrie"""
    return industry

def getScreen() -> pygame.Surface:
    """
    Renvoie la fenêtre de jeu.

    Returns:
        Surface: l'objet de la surface du jeu.
    """
    return screen

def getScreenSize() -> tuple:
    """
    Renvoie les coordonnées X et Y de la fenêtre de jeu.

    Returns:
        tuple: Renvoie un tuple incluant les coordonnées X et Y de la fenêtre de jeu.
    """
    return screen

def getDimension() -> int:
    """Permet d'obtenir la dimension sur laquelle le jeu est crée. Soit la largeur d'un Bloc
    
    Returns:
        int: La dimension du jeu.
    """
    return dimension


def getState() -> dict:
    """
    Renvoie l'état de séléction.

    Returns:
        dict: Un dictionaire comportant toutes les informations de séléctions :
            -selectionned (bool): Si un bloc est séléctionné.
            -args (dict): Les paramètres du blocs:
                -texture (str): La texture du bloc
                -name (str): le nom du bloc
            -classe (Bloc): la Classe du bloc. Est une instance de la classe Bloc.
            -buy (bool): Si vrai, le joueur peut débloquer un terrain

    """
    return state


def getGrille() -> list:
    """
    Renvoie la grille du jeu. Il d'un dictionnaire dans une liste. Les clés sont les coordonnées des blocs, et les valeurs, les objets représentant les blcos.

    Returns:
        list: La grille du jeu. Un dictionnaire dans une liste.
    """
    return grille


def getMenu() -> list:
    """Renvoie une liste contenant l'historique de Menu. Le dernier est le plus récent

    Returns:
        list: File de Menu, le dernier est le plus récent.
    """
    return menu


def getMachines() -> dict:
    """Renvoie chacun des dictionaires de machine dans un dictionaire.

    Returns:
        dict: Un dictionaire comprenant tout les dictionaires de machines :
            - "fonderie": dictionaire fonderies.
            - "convoyeur": dictionaire convoyeurs.
            - "foreuses": dictionaires foreuses.
            - "vendingMachine": dictionaure vendingMachine
    """
    return ListInStr

def getActiveConvoyeurs() -> dict:
    """Renvoie tout les convoyeurs possèdant une ressource du jeu.

    Returns:
        dict: Renvoie un dictionaire de Convoyeurs.
    """
    return activeConvoyeurs

def getListInStr() -> dict:
    """Renvoie un dictionaire avec pour clé une chaîne correspondant à une classe Bloc et pour valeur le dictionaire correspondant à cette classe.. Par exemple, 'foreuse' est associé au dictionaire des foreuses.

    Returns:
        dict: Un dictionaire associant un dictionaire de machines (valeur) à une chaîne (clé).
    """
    return ListInStr


def getClassInStr() -> dict:
    """Renvoie un dictionaire avec pour clé une chaîne correspondant à une classe Bloc. Par exemple, 'foreuse' est associé à la classe Foreuse.

    Returns:
        dict: Un dictionaire associant une classe (valeur) à une chaîne (clé).
    """
    return classInStr


def getForeuse() -> list:
    """Renvoie toute les foreuses du jeu. Il s'agit d'instances de la classe Foreuse.

    Returns:
        list: Une liste de toute les foreuses. (dict_values).
    """
    return foreuses.values()


def getFonderies() -> list:
    """Renvoie toute les fonderies du jeu. Il s'agit d'instances de la classe Fonderie.

    Returns:
        list: Une liste de toute les fonderies. (dict_values).
    """
    return fonderies.values()


# Obtenir tout les convoyeurs du jeu
def getConvoyeur() -> list:
    """Renvoie tout les convoyeurs du jeu. Il s'agit d'instances de la classe Convoyeur.

    Returns:
        list: Une liste de tout les convoyeurs. (dict_values).
    """
    return convoyeurs.values()

def getVendingMachine() -> list:
    """Renvoie toute les boutiques du jeu. Il s'agit d'instances de la classe vendingMachine.

    Returns:
        list: Une liste de toutes les boutiques. (dict_values).
    """
    return vendingMachineList.values()

def resetState() -> None:
    """Remet à 0 l'état de la variable state"""
    global state
    state = {"selectionned": False, "args": {"texture": "", "name": ""}, "classe": Bloc, "buy": False}
