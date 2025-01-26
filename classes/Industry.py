import copy

class Industry():
    """Classe représentant l'industrie. Elle permet de gérer le revenu passif de celle ci."""

    def __init__(self) -> None:
        """Initialisation de la classe Industry. 
        
            Attributes:
                passive: le revenu passif de l'industrie sur 30 secondes
                newPassive: le revenu passif de l'industrie entrain d'être incrémenté jusqu'à 30 seconde.
                
        """
        self.passive = 0
        self.newPassive = 0

    def updateNewPassive(self, montant:int) -> None:
        """Permet d'incrémenter le revenu passif actuel selon le montant en paramètre
        
            Args:
                montant (int): Montant à ajouter au revenu passif
        """
        self.newPassive += montant

    def reset(self) -> None:
        """Permet d'associer au revenu passif, le revenu passif qui vient d'être calculé sur les 30 dernières secondes. Le précédent est écrasé. On démarre un nouveau compteur de 30 secondes dans lequel on recalcule le nouveau revenu passif associé à newPassive."""
        self.passive = copy.deepcopy(self.newPassive)
        self.newPassive = 0

    def getPassive(self) -> int:
        """Renvoie le revenu passif de l'industrie sur 30 secondes"""
        return self.passive