import pygame, sys, time
from pygame.locals import *

pygame.init()

Height = 800
Width = 800

window = pygame.display.set_mode((Width, Height), 0, 24)
pygame.display.set_caption('Meme Generator')




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
