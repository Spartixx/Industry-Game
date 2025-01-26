from utils.fonctions.gameVar import activeConvoyeurs, grille, dimension
from utils.fonctions.show import blitBloc, blitItem
from classes.Bloc import *
from classes.Item import *

def checkConvoyeur(machine:Machine, mode:str="set") -> None:
        """Permet de déposer une ressource sur un Convoyeur ou de prendre une ressource depuis un Convoyeur s'il y en a. Ceci, selon une machine et un mode (prise de ressource (take) ou dépôt de ressource (set)).
        

        Args:
            machine (Machine): Une instance de la classe Machine. Il s'agit de la machine qui récupérera ou déposera une ressource si elle le peut.
            mode (str, optional): Il s'agit du mode de transfert de ressource de la machine. "set" pour déposer, "take" pour récupérer. Defaults to "set".
        """
        cases = [[0,-dimension],[0,dimension],[-dimension,0],[dimension,0]]
        for xy in cases:
                caseKey = f"{machine.getX()[0]+xy[0]},{machine.getY()[0]+xy[1]}"
                if grille[0].get(caseKey) != None:
                    case = grille[0][caseKey] 
                    if type(case) == Convoyeur: 
                        case:Convoyeur = case
                        
                        if mode=="set":  
                            if machine.getStock() > 0: 
                                if not case.getHas():
                                    if f"{case.getX()[0] + case.getSens()[0]},{case.getY()[0] + case.getSens()[1]}" != machine.getStrKey(): # si le convoyeur ne pointe pas vers la Machine
                                        case.updateHas(machine.getRessource())
                                        blitItem(machine.getRessource().getTexture(), case)
                                        machine.updateStock(-1)
                                        activeConvoyeurs[case.getStrKey()] = case   
                            else:
                                break # Eviter de boucler, cette condition ne sera pas remplie.
                            
                        elif mode=="take":
                            machine: Fonderie = machine
                            if machine.getRawStock() < machine.getMaxRawStock():
                                if case.getHas():

                                    if f"{case.getX()[0] + case.getSens()[0]},{case.getY()[0] + case.getSens()[1]}" == machine.getStrKey():
                                        if type(case.getItem()) in machine.getAcceptedRessource():
                                            if case.getItem().getSmelt() == False:
                                                machine.updateRawStock(case.getItem())
                                                case.transport()
                                                blitBloc(case)
                                                activeConvoyeurs.pop(case.getStrKey())
                                            else:
                                                if machine.getStock() < machine.getMaxStock():
                                                    machine.updateStock(case.getItem())    
                                                    case.transport()
                                                    blitBloc(case)
                                                    activeConvoyeurs.pop(case.getStrKey())   
                            else:
                                break