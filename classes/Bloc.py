import pygame
import itertools
from classes.Item import *


class Bloc():
    """
    Classe Bloc. Elle est l'une des superClasse la plus haute de la hiérarchie. Toutes les autres classes Blocs (plaçable) descendent de celle ci.
    Elle représente un bloc de la carte.

    Args:
        texture (str): Le chemin vers le fichier de configuration.
        price (int): Le prix du bloc.
        name (str): Le nom du bloc.
        x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        size (int): La taille du bloc, sa dimension.
        blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
    """
    
    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False, **kwargs) -> None:
        """
        Initialisation de la classe Bloc.

        Args:
            texture (str): Le chemin vers le fichier de configuration.
            price (int): Le prix du bloc.
            name (str): Le nom du bloc.
            x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            size (int): La taille du bloc, sa dimension.
            blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
            args (dict): stock tout les arguments de la classe dans un dictionnaire.
        """
        self.size = size
        self.name = name
        self.price = price
        self.texture = texture
        self.x = x
        self.y = y
        self.blocked = blocked
        self.args = {"coords": self.getStrKey(), "texture": self.texture, "price": self.price, "name": self.name, "x": self.x, "y": self.y, "size": self.size, "blocked": self.blocked}


    def changeTexture(self, texture:str) -> None:
        """
        Permet de changer la texture du Bloc.

        Args:
            texture (str): chemin vers la nouvelle texture.
        """
        self.texture = texture


    def getArgs(self) -> dict:
        """
        Renvoie les arguments du Bloc.

        Returns:
            dict: Le dictionaire contenant tout les arguments du Bloc.
        """

        self.args["blocked"] = self.blocked
        return self.args    
    
    def getX(self) -> list:
        """
        Renvoie les coordonnées X du Bloc.

        Returns:
            list: les coordonnées X du Bloc. Sous forme d'intervalle, les plus petits coordonnées X du bloc, puis les plus grandes.
        """
        return self.x
    
    def getY(self) -> list:
        """
        Renvoie les coordonnées Y du Bloc.

        Returns:
            list: les coordonnées Y du Bloc. Sous forme d'intervalle, les plus petits coordonnées Y du bloc, puis les plus grandes.
        """
        return self.y
    
    def getPrice(self) -> int:
        """
        Renvoie le prix du Bloc.

        Returns:
            int: Renvoie le prix du Bloc sous la forme d'un entier.
        """
        return self.price
    
    def getTexture(self) -> str:
        """
        Renvoie la texture du bloc. Il s'agit de son chemin.

        Returns:
            str: Le chemin de la texture du bloc.
        """
        return self.texture
    
    def getName(self) -> str:
        """
        Renvoie le nom du Bloc.

        Returns:
            str: Le nom du bloc sous la forme d'une chaîne.
        """
        return self.name
    
    def getSize(self) -> int:
        """
        Renvoie la taille du Bloc. Il s'agit de sa dimension, également du nombre de pixel de sa texture.

        Returns:
            int: La taille du bloc sous forme d'un entier. 
        """
        return self.size
    
    def getBlocked(self) -> bool:
        """
        Renvoie l'état d'accès du Bloc. Permet de savoir si il est bloqué ou non, donc si le terrain est en mode 'achat'.

        Returns:
            bool: Renvoie True si le terrain est en mode achat et donc si il est bloqué. Sinon renvoie False
        """
        return self.blocked
    
    def unblock(self, screen: pygame.Surface) -> None:
        """
        Permet de débloquer un bloc. Il sera ensuite possible d'utiliser cet emplacement.
        """
        self.blocked = False
        screen.blit(pygame.image.load(self.getTexture()), (self.getX()[0], self.getY()[0]))


    def isIn(self, other) -> bool:
        """
        Permet de savoir si un Bloc est dans l'intervalle de coordonnées d'un autre.

        Args:
            other (Bloc): l'instance d'un autre Bloc.

        Returns:
            bool: renvoie True si le bloc est à l'interieur de celui passé en argument. Sinon, renvoie False.
        """
        if self.x[0] >= other.getX()[0] and self.x[1] <= other.getX()[1] and self.y[0] >= other.getY()[0] and self.y[1] <= other.getY()[1]:
            return True
        return False
    
    
    def getStrKey(self) -> str:
        """
        Permet d'obtenir les coordonnées du bloc sous la forme d'une chaine de caractère. La chaîne est du même format que celui des clés de la grille de jeu.

        Returns:
            str: Renvoie les coordonnées du Bloc sous forme d'une chaîne.
        """
        return f"{self.getX()[0]},{self.getY()[0]}"
    
    def __repr__(self) -> str:
        """
        Permet d'obtenir une représentation de la classe sous forme d'une chaîne de caractère

        Returns:
            str: Renvoie une représentation de la classe sous forme d'une chaîne.
        """
        return f"Nom : {self.getName()}   |   Texture : {self.getTexture()}   |   Coordonnées : X :{str(self.getX()[0])}  Y : {str(self.getY()[0])}   |   Blocked : {str(self.getBlocked())}"
    
    def __str__(self) -> str:
        f"""{Bloc.__repr__.__doc__}"""
        return self.__repr__()
   

class Machine(Bloc):
    """
    Classe Machine. Elle est la superClasse des machines. Elle hérite de la classe Bloc.
    Elle représente une machine qui peut être placée sur la carte. Elle permet de gérer les moyens de productions de ressource

    Args:
        texture (str): Le chemin vers le fichier de configuration.
        price (int): Le prix du bloc.
        name (str): Le nom du bloc.
        x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        size (int): La taille du bloc, sa dimension.
        blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
        stock (int): Désigne le stock de la machine.
        level (dict): Désigne les différents niveau de la machine
    """

    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False, stock:int=0, levels = {}) -> None:
        """
        Initialisation de la classe Machine.

        Args:
            texture (str): Le chemin vers le fichier de configuration.
            price (int): Le prix du bloc.
            name (str): Le nom du bloc.
            x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            size (int): La taille du bloc, sa dimension.
            blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
            stock (int): Désigne le stock de la machine.
            level (dict): Désigne les différents niveau de la machine
            upgrades (dict): Désigne les prochains niveau d'améliorations pour chaque catégorie.
            levels (dict): Désigne les différents niveau de la machine pour chacune de ses catégories.
            speed (int): Représente le temps en demi seconde pour produire une ressource
            state (int): Désigne l'état de production d'une ressource. Quand il est égal à 0, il devient égal à la valeur de 'speed'.
            ressource (Item): Désigne la meilleure ressource que la machine est capable de gérer.
            maxStock (int): Désigne le stock maximum accepté par la machine.
            args (dict): stock tout les arguments de la classe dans un dictionnaire.
        """
        
        super().__init__(texture, price, name, x, y, size, blocked)
        self.upgrades = {"speed": {"1": 10, "2": 8, "3": 6, "4": 4, "5": 3}, "stock": {"1": 3, "2": 4, "3": 6, "4": 9, "5": 15}, "ressource": {"1": Iron(x[0], y[0]),"2": Copper(x[0], y[0]),"3": Gold(x[0], y[0]),"4": Diamond(x[0], y[0]),"5": Ruby(x[0], y[0])}}
        if levels == {}: self.levels = {"speed": 1, "stock": 1, "ressource": 1}
        else: self.levels = levels
        self.maxStock = self.upgrades["stock"][str(self.levels["stock"])]
        self.stock = stock 
        self.speed = self.upgrades["speed"][str(self.levels["speed"])] 
        self.state = self.speed 
        self.args["stock"] = self.stock
        self.ressource = self.upgrades["ressource"][str(self.levels["ressource"])]

    def getArgs(self) -> dict:
        """
        Renvoie les arguments de la Machine.

        Returns:
            dict: Le dictionaire contenant tout les arguments de la Machine.
        """

        self.args["blocked"] = self.blocked
        self.args["stock"] = self.stock
        self.args["levels"] = self.levels
        return self.args

    
    def getMaxStock(self) -> int:
        """
        Renvoie le stock maximum de la Machine.

        Returns:
            int: Le stock maximum de la machine sous la forme d'un entier.
        """

        return self.maxStock
    
    def getStock(self) -> int:
        """
        Renvoie le stock de la Machine.

        Returns:
            int: Le stock de la machine sous la forme d'un entier.
        """

        return self.stock
    
    def getSpeed(self) -> int:
        """
        Renvoie la vitesse de la Machine

        Returns:
            int: La vitesse de la machine sous la forme d'un entier.
        """

        return self.speed
    
    def getLevel(self) -> dict:
        """
        Renvoie tout les niveaux de la Machine (vitesse, stock, ressource)

        Returns:
            dict: Les différents niveaux de la machine (vitesse, stock, ressource).
        """

        return self.levels
    
    
    def updateStock(self, quantity:int) -> None:
        """
        Permet de modifier le stock de la machine selon la valeur donnée en argument.

        Args:
            quantity (int): Le montant à ajouter ou retirer au stock.
        """

        if quantity > self.maxStock-self.stock:
            self.stock = self.maxStock
        else:
            self.stock+=quantity


    def produce(self) -> None:
        """
        Permet de produire une ressource si le temps de production est terminé (si l'état de production est égal à 0), sinon, on décrémente l'état de production. Lorsqu'une ressource est produite, on rénitialise l'état de production.
        """

        if self.state == 0:
            self.state = self.speed+1
            if self.stock < self.maxStock:
                self.stock+=1
        self.state -= 1
        
    def getRessource(self) -> Item:
        """
        Permet d'obtenir la ressource la plus haute que la machine peut gérer.

        Returns:
            Item: Renvoie une instance de la classe Item.
        """

        return self.ressource
    
    def upgradeStock(self) -> None:
        """
        Permet d'améliorer le stock de la machine.
        """

        if self.levels["stock"] < 5:
            self.levels["stock"] +=1
            self.maxStock = self.upgrades["stock"][str(self.levels["stock"])]

    def upgradeSpeed(self) -> None:
        """
        Permet d'améliorer la vitesse de la machine.
        """

        if self.levels["speed"] < 5:
            self.levels["speed"] +=1
            self.speed = self.upgrades["speed"][str(self.levels["speed"])]

    def upgradeRessource(self) -> None:
        """
        Permet d'améliorer la ressource que la machine est capable de gérer.
        """

        if self.levels["ressource"] < 5:
            self.levels["ressource"] +=1
            self.ressource = self.upgrades["ressource"][str(self.levels["ressource"])]
        


class Foreuse(Machine):
    """
    Classe Foreuse. Elle hérite de la classe Machine.
    Elle représente une Foreuse qui peut être placée sur la carte.

    Args:
        texture (str): Le chemin vers le fichier de configuration.
        price (int): Le prix du bloc.
        name (str): Le nom du bloc.
        x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        size (int): La taille du bloc, sa dimension.
        blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
        stock (int): Désigne le stock de la machine.
        level (dict): Désigne les différents niveau de la machine
    """

    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False, stock:int=0, levels:dict = {}) -> None:
        f"""{Machine.__doc__}"""
        
        super().__init__(texture, price, name, x, y, size, blocked, stock, levels)

        

class Fonderie(Machine):
    """
    Classe Fonderie. Elle hérite de la classe Machine.
    Elle représente une fonderie qui peut être placée sur la carte.

    Args:
        texture (str): Le chemin vers le fichier de configuration.
        price (int): Le prix du bloc.
        name (str): Le nom du bloc.
        x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        size (int): La taille du bloc, sa dimension.
        blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
        stock (int): Désigne le stock de la machine.
        level (dict): Désigne les différents niveau de la machine
    """
    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False, stock:int=0, levels:dict = {}, ressourceFile:list = []) -> None:
        f"""
        {Machine.__init__.__doc__}
            classInStr (dict): permet d'associer une classe à une clé sous forme d'une chaîne de caractère.
            rawStock (int): Désigne le stock d'item non cuit de la machine.
            maxRawStock (int): Désigne le sotck maximum d'item non cuit de la machine.
            rawRessourceFile (list): Représente une file. Ses valeurs sont des instances de la classe Item (avec l'attribut smelt en False).
            acceptedRessource (list): Liste des ressources acceptées par la machines. Ses ressources sont de la classe Item.
            RessourceFile (list): Représente une file. Ses valeurs sont des instances de la classe Item (avec l'attribut smelt en True).
        """
        
        super().__init__(texture, price, name, x, y, size, blocked, stock, levels)
        classInStr = {"iron": Iron, "copper": Copper, "gold": Gold, "diamond": Diamond, "ruby": Ruby}
        self.rawStock = 0 
        self.maxRawStock = 5 
        self.rawRessourceFile = []
        self.acceptedRessource = [type(self.upgrades["ressource"][str(i)]) for i in range(1,self.levels["ressource"]+1)]
        if ressourceFile == []:
            self.ressourceFile = []
        else:
            self.ressourceFile = [classInStr[i["name"]](*list(itertools.islice(i.values(), 0, len(i.values())-1))) for i in ressourceFile if type(i) == dict]
        
    def getArgs(self) -> dict:
        f"""{Machine.getArgs.__doc__}"""
        
        self.args["blocked"] = self.blocked
        self.args["stock"] = self.stock
        self.args["levels"] = self.levels
        if len(self.ressourceFile) > 0:
            self.args["ressourceFile"] = [i.getArgs() for i in self.ressourceFile]
        return self.args


    def getAcceptedRessource(self) -> list:
        """
        Renvoie la liste des ressources acceptées par la Machine.

        Returns:
            list: La liste des ressources acceptées par la machine.
        """
        
        return self.acceptedRessource
    

    def getRawStock(self) -> int:
        """
        Renvoie le stock d'Item non cuit de la Machine.

        Returns:
            int: Le stock d'item non cuit de la machine sous forme d'un entier.
        """

        return self.rawStock
    
    def getMaxRawStock(self) -> int:
        """
        Renvoie le stock maximum d'Item non cuit de la Machine.

        Returns:
            int: Le stock maximum d'item non cuit de la machine sous forme d'un entier.
        """
        
        return self.maxRawStock
    

    def updateStock(self, item) -> None:
        """
        Ajoute un Item à la file d'Item cuit de la machine. Si Item vaut -1, on retire le dernier élément.

        Args:
            item (int) || (Item): Une instance de la classe Item a ajouté à la File d'Item cuit. Sinon, la valeur: -1 pour supprimer le dernière élément de cette File.
        """
        
        if item == -1:
            self.ressourceFile.pop(0)
            self.stock-=1
        else:
            self.ressourceFile.append(item)
            self.stock+=1

    
    def updateRawStock(self, item) -> None:
        """
        Ajoute un Item à la file d'Item non cuit de la machine. Si Item vaut -1, on retire le dernier élément.

        Args:
            item (int) || (Item): Une instance de la classe Item a ajouté à la File d'Item non cuit. Sinon, la valeur: -1 pour supprimer le dernière élément de cette File.
        """
        
        if item == -1 and len(self.rawRessourceFile) > 0:
            self.rawStock-=1
            self.rawRessourceFile.pop(0)
        else:
            if type(item) == Diamond or type(item) == Ruby:
                if self.getStock() < self.getMaxStock():
                    self.ressourceFile.append(item)
                    self.stock+=1
            else:
                self.rawRessourceFile.append(item)
                self.rawStock+=1
    
    
    def produce(self) -> None:
        f"""{Machine.produce.__doc__}"""
        
        if self.state == 0:
            self.state = self.speed+1
            if self.stock < self.maxStock and self.rawStock > 0:
                self.stock+=1 
                ressource = type(self.rawRessourceFile.pop(0))(self.getX()[0], self.getY()[0], True)
                self.ressourceFile.append(ressource)
                self.rawStock -=1 
        self.state -= 1

    def getRawRessource(self) -> Item:
        """
        Renvoie le dernier Item non cuit de la file de la Machine.

        Returns:
            Item: Le dernier élément de la file. Il est de la clase Item.
        """
        
        return self.rawRessourceFile[0]
    
    def getRessource(self) -> Item:
        """
        Renvoie le dernier Item cuit de la file de la Machine.

        Returns:
            Item: Le dernier élément de la file. Il est de la clase Item.
        """
        
        return self.ressourceFile[0]
    
    def upgradeStock(self) -> None:
        """
        Permet d'améliorer le stock de la machine.
        """
        
        if self.levels["stock"] < 5:
            self.levels["stock"] +=1
            self.maxStock = self.upgrades["stock"][str(self.levels["stock"])]
            self.maxRawStock = self.maxStock
    
    def upgradeRessource(self) -> None:
        f"""{Machine.upgradeRessource.__doc__}"""
        
        if self.levels["ressource"] < 5:
            self.levels["ressource"] +=1
            self.ressource = self.upgrades["ressource"][str(self.levels["ressource"])]
        self.acceptedRessource.append(type(self.ressource))
    


class Convoyeur(Bloc):
    """
    Classe Convoyeur. Elle hérite de la classe Bloc.
    Elle représente un convoyeur (tapis roulant) qui peut être placée sur la carte.

    Args:
        texture (str): Le chemin vers le fichier de configuration.
        price (int): Le prix du bloc.
        name (str): Le nom du bloc.
        x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
        size (int): La taille du bloc, sa dimension.
        blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
        item (Item) | (dict): Désigne l'item présent sur le convoyeur. Il est un dictionnaire uniquement lorsque le convoyeur est chargé à l'initialisation du jeu.
        has (bool): True si le convoyeur possède une ressource. Sinon, False
    """

    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False, item:dict=None, has:bool=False) -> None:
        """
        Initialisation de la classe Convoyeur.

        Args:
            texture (str): Le chemin vers le fichier de configuration.
            price (int): Le prix du bloc.
            name (str): Le nom du bloc.
            x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            size (int): La taille du bloc, sa dimension.
            blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
            item (Item) | (dict): Désigne l'item présent sur le convoyeur. Il est un dictionnaire uniquement lorsque le convoyeur est chargé à l'initialisation du jeu.
            has (bool): True si le convoyeur possède une ressource. Sinon, False
            sens (list): une liste comportant 2 valeurs : X,Y. Représente la direction du convoyeur, X positif à droite, à l'inverse à gauche. Y positif en bas, à l'inverse en haut.
            next (str): Une chaîne désignant le prochain Bloc selon le sens du Convoyeur. La chaîne est au format des clés de la grille de jeu.
            args (dict): stock tout les arguments de la classe dans un dictionnaire.
        """
        
        super().__init__(texture, price, name, x, y, size, blocked)
        classInStr = {"iron": Iron, "copper": Copper, "gold": Gold, "diamond": Diamond, "ruby": Ruby}
        self.has = has
        self.sens = None
        self.setSens(texture)
        if type(item) == dict:
            self.item = classInStr[item["name"]](item["x"], item["y"], item["smelt"])
        else:
            self.item = item
        self.args["item"] = self.item
        self.args["has"] = self.has
        self.next = f"{self.getX()[0]+self.sens[0]},{self.getY()[0]+self.sens[1]}"
        


    # Permet de définir le sens du convoyeur
    def setSens(self, sens:str) -> None:
        """Permet d'assigner le sens du convoyeur selon les coordonnées X et Y a ajouter à ses coordonnées pour atteindre le prochain Bloc. X positif = vers la droite etc...

        Args:
            sens (str): Le sens du convoyeur sous forme d'une chaîne (gauche, droite, haut, bas).
        """
        if sens.find("gauche") != -1: self.sens = [-self.size, 0]
        elif sens.find("droite") != -1: self.sens = [self.size, 0]
        elif sens.find("haut") != -1: self.sens = [0, -self.size]
        elif sens.find("bas") != -1: self.sens = [0, self.size]
        


    def getArgs(self) -> dict:
        f"""{Bloc.getArgs.__doc__}"""
        
        if self.item != None:
            self.args["item"] = {"x": self.item.getX(), "y": self.item.getY(), "smelt": self.item.getSmelt(), "name": self.item.getName()}
        else:
            self.args["item"] = None
        self.args["has"] = self.has
        return self.args
        


    # Getters, ils sont explicites
    def getHas(self) -> bool:
        """Permet de savoir si un Convoyeur possède une ressource.

        Returns:
            bool: Vrai si le Convoyeur possède une ressource. Sinon, retourne Faux.
        """
        return self.has
    
    def getSens(self) -> list:
        """Renvoie le sens du Convoyeur sous forme d'une liste.

        Returns:
            list: renvoie le nombre de pixels X et Y à ajouter aux coordonénes du Convoyeur pour atteindre le prochain Bloc. Cette liste correspond à un sens.
        """
        return self.sens
    
    def getItem(self) -> Item:
        """Permet d'obtenir la ressource du Convoyeur. Il s'agit d'une instance de la classe Item.

        Returns:
            Item: Renvoie une instance de la classe Item.
        """
        return self.item

    
    def updateHas(self, item=False) -> None:
        """Permet de mettre à jour la possession d'Item. 

        Args:
            item (bool, optional): True si le convoyeur possède un Item. False sinon. Defaults to False.
        """
        
        if self.has == False:
            self.has = True
        if item != False:
            self.item = item

    
    def transport(self) -> None:
        """Permet de retirer une ressource d'un Convoyeur. l'attribut item passe en 'None'."""
        self.has = False
        self.item = None


class vendingMachine(Bloc):
    """Classe vendingMachine. Elle représente une boutique. Elle hérite de la classe Bloc et peut donc être placée sur la carte.
       Elle permet de gérer la vente des ressources données par les convoyeurs.

    Args:
        Bloc (_type_): _description_
    """
    
    def __init__(self, texture:str, price:int, name:str, x:list, y:list, size:int, blocked:bool=False) -> None:
        """
        Initialisation de la classe vendingMachine.

        Args:
            texture (str): Le chemin vers le fichier de configuration.
            price (int): Le prix du bloc.
            name (str): Le nom du bloc.
            x (list): Les coordonnées X du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            y (list): Les coordonnées Y du bloc, il s'agit de l'intervalle de coordonnées dans lequel le bloc est.
            size (int): La taille du bloc, sa dimension.
            blocked (bool): Désigne l'état d'accès du bloc, si il est bloqué ou non.
            args (dict): stock tout les arguments de la classe dans un dictionnaire.
        """
        
        super().__init__(texture, price, name, x, y, size, blocked)
        self.monney = 0

    def updateSolde(self, other: Item) -> None:
        """Permet d'actualiser le solde du joueur selon le prix de la ressource en paramètre.

        Args:
            other (Item): Une instance de la classe Item.
        """
        self.monney += other.getPrice()

    def getMoney(self, reset: bool=True) -> int:
        """Renvoie le solde de la boutique sous forme d'un entier.

        Args:
            reset (bool, optional): True si le solde de la machine doit être rénitialisé. False, sinon. Defaults to True.

        Returns:
            int: Le solde de la machine.
        """
        copieMonney = self.monney
        if reset: self.monney = 0
        return copieMonney