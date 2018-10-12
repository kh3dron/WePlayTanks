from Tank import *
from Map import *
from Round import *
from Wall import *
import pygame
import numpy
import sys
from pygame.locals import *
pygame.init()

#Some easy colors
BLACK = (  0,   0,   0)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
level1 = Map('./level2')

def drawWall(Wall, screen):
    pygame.draw.rect(screen, BLUE, [Wall.getX(), Wall.getY(), 80, 80])

def drawTank(map, Tank, color, screen):
    pygame.draw.rect(screen, color, [Tank.getX()-15, Tank.getY()-15, 30, 30])

def drawAllWalls(map, screen):
    for wall in map.getWalls():
        drawWall(wall, screen)

def drawCrosshairs(mouse, screen):
    x, y = mouse
    pygame.draw.circle(screen, RED, mouse, 15, 3)
    pygame.draw.line(screen, RED, (x, y-20), (x, y+20), 3)
    pygame.draw.line(screen, RED, (x-20, y), (x+20, y), 3)

def drawRound(round, screen):
    pygame.draw.circle(screen, WHITE, round.getCoords(), 8)

#Buggy, works ~90% of the time
def bounceRoundsX(round, map, screen):
    for wall in map.getWalls():
        if (wall.getY() < round.getY() < wall.getY()+80):
            if 0 <= abs(wall.getX() - round.getX()) <= 4 and not round.isDead():
                round.bounceX()
            if 0 <= abs(wall.getX()+80 - round.getX()) <= 4 and not round.isDead():
                round.bounceX()

def bounceRoundsY(round, map, screen):
    for wall in map.getWalls():
        if (wall.getX() < round.getX() < wall.getX()+80) :
            if 0 <= abs(wall.getY() - round.getY()) <= 4 and not round.isDead():
                round.bounceY()
            if 0 <= abs(wall.getY()+80 - round.getY()) <= 4 and not round.isDead():
                round.bounceY()

#these aren't perfect, but they're good enough to work right now
#They're a frame too slow, will need to add in a predictive method of sorts
def tankHitsLeft(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getY()-15 <= tank.getY() <= wall.getY()+95):
            if 0 <= abs(wall.getX()+80 - tank.getX()+15) <= 2:
                return True
def tankHitsRight(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getY()-15 <= tank.getY() <= wall.getY()+95):
            if 0 <= abs(wall.getX() - tank.getX()-15) <= 2:
                return True
def tankHitsUp(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-15 <= tank.getX() <= wall.getX()+95):
            if 0 <= abs(wall.getY()+80 - tank.getY()+15) <= 2:
                return True
def tankHitsDown(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-15 <= tank.getX() <= wall.getX()+95):
            if 0 <= abs(wall.getY() - tank.getY()-15) <= 2:
                return True

def roundHitsTank(round, tank):
    if (abs(tank.getX()-round.getX())<15 and abs(tank.getY()-round.getY())<15):
        return True
    else:
        return False

def Run():

    windowSize = (1280, 720)
    screen = pygame.display.set_mode(windowSize)
    clock = pygame.time.Clock()
    shots = []
    enemyTanks = level1.getEnemyTanks()
    playerTank = level1.getPlayerTank()

    while True:

        clock.tick(30)
        mousePosition = pygame.mouse.get_pos()
        x, y = mousePosition

        #kews that are hit once
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if len(shots)<5:
                    shots.append(level1.getPlayerTank().fire(mousePosition, 10))

        #Keys that are being HELD DOWN, handle player moves
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if not tankHitsUp(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveUp()
        if keys[pygame.K_s]:
            if not tankHitsDown(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveDown()
        if keys[pygame.K_a]:
            if not tankHitsLeft(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveLeft()
        if keys[pygame.K_d]:
            if not tankHitsRight(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveRight()

        screen.fill(GREY)
        drawAllWalls(level1, screen)
        drawCrosshairs(mousePosition, screen)
        for n in shots:
            if (n.getX() > 1280 or n.getX() < 0 or n.getY() > 720 or n.getY() < 0):
                shots.remove(n)
                break
            if n.isDead():
                shots.remove(n)
                break
            for e in enemyTanks:
                if roundHitsTank(n, e):
                    enemyTanks.remove(e)
                    shots.remove(n)
            bounceRoundsX(n, level1, screen)
            bounceRoundsY(n, level1, screen)
            n.updatePosition()
            drawRound(n, screen)
        for e in enemyTanks:
            drawTank(level1, e, RED, screen)
        drawTank(level1, playerTank, GREEN, screen)
        #Always run this
        pygame.display.update()

Run()
