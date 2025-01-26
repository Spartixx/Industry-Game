import pygame

class Item():
    """
    Classe Item. Elle est l'une des superClasse la plus haute de la hiérarchie. Toutes les autres classes Ressource descendent de celle ci.
    Elle représente une ressource transportable et productible.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """
    def __init__(self, x:list, y:list, smelt:bool=False) -> None:
        """Initialisation de la classe.

        Args:
            x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
            y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
            smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
        """
        self.x = x
        self.y = y
        self.texture = "textures/raw_iron.png"
        if smelt:
            self.texture = "textures/iron_ingot.png"
        self.smelt = smelt
        self.price = 20
        self.name = "iron"
        self.args = {"x": self.x, "y": self.y, "smelt": self.smelt, "name": self.name}
        

    def getArgs(self) -> dict:
        """
        Renvoie les arguments de l'Item.

        Returns:
            dict: Le dictionaire contenant tout les arguments de l'Item.
        """
        return self.args
    
    def getName(self) -> str:
        """Renvoie le nom de l'Item sous forme d'une chaîne

        Returns:
            str: Le nom de l'Item.
        """
        return self.name

        
    def getTexture(self) -> str:
        """Renvoie la l'image de l'Item sous forme d'une chaîne.

        Returns:
            int: La texture de l'image.
        """
        return self.texture
    
    def getPrice(self) -> int:
        """Renvoie le prix de l'Item selon sa cuisson sous forme d'un entier.

        Returns:
            int: Le prix de l'Item.
        """
        if self.smelt == True:
            return self.price*5
        else:
            return self.price
    
    def getX(self) -> list:
        """
        Renvoie les coordonnées X de l'Item.

        Returns:
            list: les coordonnées X de l'Item. Sous forme d'intervalle, les plus petites coordonnées X du bloc, puis les plus grandes.
        """
        return self.x
    
    def getY(self) -> list:
        """
        Renvoie les coordonnées Y de l'Item.

        Returns:
            list: les coordonnées Y de l'Item. Sous forme d'intervalle, les plus petites coordonnées Y du bloc, puis les plus grandes.
        """
        return self.y
    
    def getSmelt(self) -> bool:
        """Permet de connaître la cuisson de l'Item, si il est cuit ou non cuit.

        Returns:
            bool: True si l'Item est cuit. False sinon.
        """
        return self.smelt
    
class Iron(Item):
    """Classe Iron. Elle hérite de la classe Item. Elle représente une ressource : du Fer.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """

    def __init__(self, x:list, y:list, smelt:bool=False):
        f"""{Item.__init__.__doc__}"""
        super().__init__(x, y, smelt)


class Copper(Item):
    """Classe Copper. Elle hérite de la classe Item. Elle représente une ressource : du Cuivre.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """

    def __init__(self, x:list, y:list, smelt:bool=False):
        f"""{Item.__init__.__doc__}"""
        super().__init__(x, y, smelt)
        self.name = "copper"
        self.price = 50
        self.texture = "textures/raw_copper.png"
        if smelt:
            self.texture = "textures/copper_ingot.png"


class Gold(Item):
    """Classe Gold. Elle hérite de la classe Item. Elle représente une ressource : de l'Or.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """

    def __init__(self, x:list, y:list, smelt:bool=False):
        f"""{Item.__init__.__doc__}"""
        super().__init__(x, y, smelt)
        self.name = "gold"
        self.price = 100
        self.texture = "textures/raw_gold.png"
        if smelt:
            self.texture = "textures/gold_ingot.png"


class Diamond(Item):
    """Classe Diamond. Elle hérite de la classe Item. Elle représente une ressource : du Diamand.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """

    def __init__(self, x:list, y:list, smelt:bool=False):
        f"""{Item.__init__.__doc__}"""
        super().__init__(x, y, smelt)
        self.name = "diamond"
        self.price = 175*5
        self.texture = "textures/diamond.png"


class Ruby(Item):
    """Classe Diamond. Elle hérite de la classe Item. Elle représente une ressource : du Diamand.

    Args:
        x (list): Les coordonnées X de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        y (list): Les coordonnées Y de l'Item, il s'agit de l'intervalle de coordonnées dans lequel l'Item est.
        smelt (bool, optional): Désigne l'état de cuisson de l'Item. True si il est cuit. sinon Faulse. Defaults to False.
    """

    def __init__(self, x:list, y:list, smelt:bool=False):
        f"""{Item.__init__.__doc__}"""
        super().__init__(x, y, smelt)
        self.name = "ruby"
        self.price = 275*5
        self.texture = "textures/ruby.png"    