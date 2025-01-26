import pygame
pygame.init()
from fonctions import *
from classes import Snake


dimension = 32
clock = pygame.time.Clock()
running = True
win = None
case = getCase()
screenSize = pygame.display.get_window_size()
font = pygame.font.SysFont('',64) # Font

MOVE = pygame.USEREVENT +1
pygame.time.set_timer(MOVE, 400)

POMME = pygame.USEREVENT +2
pygame.time.set_timer(POMME, 3000)


snake = Snake()
setBar(0)
afficheGrille()

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if win == None:
            if event.__str__().find("'unicode': 'q'") != -1 and event.__str__().find("KeyDown"):
                changeDirection("left")
            if event.__str__().find("'unicode': 'd'") != -1 and event.__str__().find("KeyDown"):
                changeDirection("right")
            if event.__str__().find("'unicode': 's'") != -1 and event.__str__().find("KeyDown"):
                changeDirection("down")
            if event.__str__().find("'unicode': 'z'") != -1 and event.__str__().find("KeyDown"):
                changeDirection("up")
        
            
        if event.type == MOVE and win == None:
            
            if snake.move(getDirection()) or snake.touchQueue():
                win = True
                screen.fill("black")
                texte = font.render(f"Défaite !",True,(255,255,255)) # Texte
                screen.blit(texte, (screenSize[0]//2-100, screenSize[1]//2-48, 128, 64))
            else:
                snake.show()
            
        if event.type == POMME and win == None:
            if snake.addPomme():
                win = False
                screen.fill("black")
                texte = font.render(f"Victoire !",True,(255,255,255)) # Texte
                screen.blit(texte, (screenSize[0]//2-100, screenSize[1]//2-48, 128, 64))


    pygame.display.flip()

    clock.tick(60)  # FPS

pygame.quit()