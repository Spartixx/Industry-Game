import pygame
import json



dimension = 32
case = None
case = 10
screen = pygame.display.set_mode((case*32, case*32))

direction = ["right"]

def loadFile(file):
    with open(file, "r") as f:
        return json.load(f)
    
blocs = loadFile("miniGames/Snake/config.json")


def createGrille():
    grille = {f"{x*dimension},{y*dimension}":blocs["herbe"] for y in range(case) for x in range(case)}
    grille["64,32"] = blocs["tete"]
    grille["32,32"] = blocs["queue"]
    return grille

grille = createGrille()

def getScreen():
    return screen

def getCase():
    return case


def blitBloc(texture, x, y):
    screen.blit(pygame.image.load(texture), (x, y))
    
def afficheGrille():
    for i, j in grille.items():
        blitBloc(j, int(i.split(",")[0]), int(i.split(",")[1]))

def setBar(piece):
    pygame.display.set_caption(f"Pieces : {piece},  Revenu Total : Pas dispo")
        
def changeDirection(newD):
    direction.append(newD)
        
def getDirection():
    return direction[-1]
    
def getDimension():
    return dimension