from Tank import *
from Map import *
from Round import *
from Wall import *
import pygame
pygame.init()


map = Map()
round = Round(10)
wall  = Wall()



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

        screen.fill((0, 0, 0))
        x, y = mousePosition

        #Always run this
        pygame.display.update()

Run()
