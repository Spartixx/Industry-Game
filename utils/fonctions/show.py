from utils.fonctions.gameVar import *
from utils.fonctions.solde import *


divisedDimension = dimension//2

def blitBloc(bloc:Bloc) -> None:
    """
    Affiche l'image d'un bloc en fonction de ses propres paramètres (texture, coordonnées, bloqué).

    Args:
        bloc (Bloc): un objet étant une instance de la classe Bloc.
    """
    screen.blit(pygame.image.load(bloc.getTexture()), (bloc.getX()[0], bloc.getY()[0]))
    if bloc.getBlocked():
        screen.blit(pygame.image.load("textures/blocked.png"), (bloc.getX()[0], bloc.getY()[0]))


def afficheGrille() -> None:
    """Permet d'afficher la totalité de la carte (Bloc et Item)."""
    for i in grille[0].values():
        blitBloc(i)
    afficheItems()


def afficheItems() -> None:
    """Permet d'afficher toutes les ressource du jeu sur les Convoyeurs."""
    for i in convoyeurs.values():
        if i.getHas():
            blitItem(i.getItem().getTexture(), i)



def blitButtons() -> None:
    """Permet d'afficher tout les boutons sur la barre des Menus."""
    showSolde()
    screen.blit(pygame.image.load(dataConfig["BLOCS_BUTTON"]), (0,0))
    screen.blit(pygame.image.load(dataConfig["CADENAS"]), (divisedDimension*4,0))
    screen.blit(pygame.image.load(dataConfig["SNAKE"]), (divisedDimension*6,0))
    screen.blit(pygame.image.load(dataConfig["MACHINES_BUTTON"]), (screenSize[0]-divisedDimension*6,0))
    screen.blit(pygame.image.load(dataConfig["CLOSE"]), (screenSize[0]-divisedDimension*2,0))
    


def blitItem(item: Item, convoyeur: Convoyeur) -> None:
    """Permet d'afficher un Item sur un Convoyeur. Il prend une instance de la classe Item en paramètre ainsi qu'une instance de la classe Convoyeur.

    Args:
        item (Item): Instance de la classe Item. Elle est la ressource à afficher sur le Convoyeur.
        convoyeur (Convoyeur): Instance de la classe Convoyeur. Il est le bloc sur lequel la ressource doit être affichée.
    """
    screen.blit(pygame.image.load(item), (convoyeur.getX()[0], convoyeur.getY()[0]))