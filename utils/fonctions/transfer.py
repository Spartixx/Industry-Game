from utils.fonctions.gameVar import activeConvoyeurs, grille, industry
from utils.fonctions.show import blitBloc, blitItem
from classes.Bloc import *
from classes.Item import *

def nextConvoyeur(convoyeur:Convoyeur) -> None:
    """Permet de transférer la ressource d'un Convoyeur vers le Convoyeur désigné par son sens. Si le sens du Convoyeur en paramètre pointe vers un Bloc qui n'est pas un Convoyeur, la ressource est perdue.

    Args:
        convoyeur (Convoyeur): Une instance de la classe Convoyeur. Une ressource lui sera retirée puis transférée vers le convoyeur suivant si il y en a un.
    """
    caseKey = f"{convoyeur.getX()[0]+convoyeur.getSens()[0]},{convoyeur.getY()[0]+convoyeur.getSens()[1]}"
    if grille[0].get(caseKey) != None:
        case:Bloc = grille[0][caseKey]
    if case.__class__ == Convoyeur: 
        case:Convoyeur = case
        if not case.getHas(): 
            case.updateHas(convoyeur.getItem()) 
            activeConvoyeurs[case.getStrKey()] = case
            activeConvoyeurs.pop(convoyeur.getStrKey())
            blitItem(convoyeur.getItem().getTexture(), case)
            convoyeur.transport()
            blitBloc(convoyeur)
    else:
        if type(case) == vendingMachine:
            case: vendingMachine = case
            case.updateSolde(convoyeur.getItem())
            industry.updateNewPassive(convoyeur.getItem().getPrice())
        if not isinstance(case, Machine):
            convoyeur.transport()
            blitBloc(convoyeur)
            activeConvoyeurs.pop(convoyeur.getStrKey())