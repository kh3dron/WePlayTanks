from Tank import *
from Map import *
from Round import *
from Wall import *
import pygame
from pygame.locals import *
import sys
BLACK = (  0,   0,   0)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
pygame.init()



level1 = Map('./level1')
def drawWall(Wall, screen):
    pygame.draw.rect(screen, BLUE, [Wall.getX(), Wall.getY(), 80, 80])

def drawPlayerTank(Tank, screen):
    pygame.draw.rect(screen, GREEN, [Tank.getX(), Tank.getY(), 30, 30])


def drawAllWalls(map, screen):
    for wall in map.getWalls():
        drawWall(wall, screen)
    drawPlayerTank(map.getPlayerTank(), screen)

def loadCourse(Map):
    course = Map.getCourse()

    for n in range(0, 9):
        for m in range(0, 16):
            if course[n][m] == "X":
                print(4)



def Run():

    windowSize = (1280, 720)
    screen = pygame.display.set_mode(windowSize)
    clock = pygame.time.Clock()


    while True:

        clock.tick(30)
        mousePosition = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_w]:
            level1.getPlayerTank().moveUp()
        if keys[pygame.K_s]:
            level1.getPlayerTank().moveDown()
        if keys[pygame.K_a]:
            level1.getPlayerTank().moveLeft()
        if keys[pygame.K_d]:
            level1.getPlayerTank().moveRight()




        screen.fill(GREY)
        x, y = mousePosition
        drawAllWalls(level1, screen)
        #Always run this
        pygame.display.update()

Run()
