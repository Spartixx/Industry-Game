from utils.fonctions.files import loadConfig
from utils.fonctions.gameVar import *
import pygame

def updateSolde(montant:int) -> None:
    """Met à jour le solde en fonction d'un montant à ajouter.

    Args:
        montant (int): Montant à ajouter au solde du joueur.
    """
    playerConfig["solde"] += montant


def strSolde(solde:int) -> str:

    """
    Renvoie un solde transformé avec une lettre pour chaque unité (M: Million, K: Millier etc...).

    Args:
        solde (int): Le montant du solde à convertir.

    Returns:
        str: Le solde convertit en une chaîne de caractère adaptée au jeu.
    """

    if solde == "End": return "End"
    chaine = ""
    if solde >= 1000:
        if solde >= 100_000_000_000_0:
            chaine = f"{round(solde/100_000_000_000_0, 3)}T"
        elif solde >= 100_000_000_0 and solde < 100_000_000_000_0:
            chaine = f"{round(solde/100_000_000_0, 3)}Md"
        elif solde >= 100_000_0 and solde < 100_000_000_0:
            chaine = f"{round(solde/100_000_0, 3)}M"
        elif solde >= 1000 and solde < 100_000_0:
            chaine = f"{round(solde/1000, 3)}K"
    else:
        chaine = str(solde)
    return chaine


def showSolde() -> None:
    """Permet d'afficher / actualiser le solde du joueur sur la barre des tâches"""
    font = pygame.font.SysFont('',64) # Font
    solde = font.render(f"Solde : {strSolde(playerConfig['solde'])}",True,(255,255,255)) # Texte
    pygame.draw.rect(pygame.display.get_surface(), (188, 143, 75), (dimension*6, 0, screenSize[0]-dimension*11, 64)) # Rectangler pour cacher l'ancien Solde
    screen.blit(solde, (screenSize[0]//2-64, 10, 128, 64))