from utils.fonctions.gameVar import state, menu
from classes.Bloc import *
from menus import execMenu
import pygame

def buttonAction(args:list, selection:bool, classe:Bloc) -> None: 
    """Permet de créer des boutons. Il s'agit d'un constructeur de bouton. Il ajoute le bloc séléctionné en tant que Bloc à placer quand un clic est effectué sur la carte.

    Args:
        args (list): Une liste de 2 valeurs : 
            -texture (str): L'image du Bloc
            -name (str): Le nom du Bloc
        selection (bool): Définis si un Bloc est séléctionné ou non. True si séléctionné, False sinon.
        classe (Bloc): Classe correspondant au bloc séléctionné
    """
    state["args"] = {"texture": args[0], "name": args[1]}
    state["selectionned"] = selection
    state["classe"] = classe
    state["buy"] = False
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    
def closeButton() -> None:
    """Bouton permettant de fermer le jeu. Il ajoute l'événement QUIT à la file d'événement."""
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    
def Menu(menuName:str, level:dict=None, playerConfig:dict = None):
    """Permet d'exécuter un menu en fonction du nom qui lui est assigné. les paramètres autre que menuName ne sont uniquement utilisé pour certains menus.

    Args:
        menuName (str): Le nom du menu à exécuter.
        level (dict, optional): Le niveau d'une machine s'il s'agit du menu d'amélioration. Defaults to None.
        playerConfig (dict, optional): Les données du joueur si le Menu le nécéssite. Defaults to None.

    Returns:
        list or str: Renvoie l'élément séléctionné par le joueur. s'il s'agit d'une liste, elle contient la texture d'un bloc puis son nom.
    """
    menu[-1] = menuName 
    selection = execMenu(menuName, level=level, playerConfig=playerConfig) 
    menu[-1] = "game"
    return selection