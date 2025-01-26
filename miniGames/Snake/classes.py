import copy
from fonctions import *
import random

class Snake():
    
    def __init__(self):
        self.tete = [64, 32]
        self.queue = [[32, 32]]
        self.last = [blocs["herbe"], self.queue[0]]
        self.pomme = [[160, 160]]
        self.score = 0
        self.grille = {f"{x*getDimension()},{y*getDimension()}": (x*getDimension(), y*getDimension()) for y in range(getCase()) for x in range(getCase())}
        blitBloc(blocs["tete"], self.pomme[0][0], self.pomme[0][1])
        
    def getTete(self):
        return self.tete
    
    def getQueue(self):
        return self.queue
    
    def getPos(self):
        pos = [self.queue]
        pos.insert(0, self.tete)
        return pos

    def move(self, direction):
        copieTete = copy.deepcopy(self.tete)
        if direction == "left":
            self.tete = [self.tete[0]-32, self.tete[1]]
            
        if direction == "right":
            self.tete = [self.tete[0]+32, self.tete[1]]
          
        if direction == "up":
            self.tete = [self.tete[0], self.tete[1]-32]  
            
        if direction == "down":
            self.tete = [self.tete[0], self.tete[1]+32]
            
        if self.isOut(getCase(), getDimension()):
            return True
            
        copieQueue = copy.deepcopy(self.queue)
        self.queue[0] = copieTete
        for i in range(1,len(self.queue)):
            self.queue[i] = copieQueue[i-1]
        self.last[1] = copieQueue[-1]
        if self.eatPomme():
            self.queue.append(copieQueue[-1])
            self.score+=1
            setBar(self.score)

            
        
            
    def show(self):
        blitBloc(self.last[0], self.last[1][0], self.last[1][1])
        blitBloc(blocs["tete"], self.tete[0], self.tete[1])
        for i in self.queue:
            blitBloc(blocs["queue"], i[0], i[1])
        
        
    def addPomme(self):
        goodCases = copy.deepcopy(self.grille)
        for i in self.queue + [self.tete]:
            goodCases.pop(f"{i[0]},{i[1]}")
        if goodCases == {}:
            return True
        else:
            pomme = random.choice(tuple(goodCases.values()))
            self.pomme.append([pomme[0],pomme[1]])
            blitBloc(blocs["tete"], pomme[0], pomme[1])
        
    def eatPomme(self):
        if self.tete in self.pomme:
            return True
        return False
    
    def isOut(self, case, dimension):
        if self.tete[0] < 0 or self.tete[0] > case*dimension or self.tete[1] < 0 or self.tete[1] > case*dimension:
            return True
        return False
    
    def touchQueue(self):
        if self.tete in self.queue:
            return True
        return False
        
        
        
            