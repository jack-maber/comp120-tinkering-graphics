import pygame, sys, time
from pygame.locals import *

pygame.init()
img = pygame.image.load('Meme.jpg')
Height =600
Width =600

window = pygame.display.set_mode((Width, Height), 0, 24)
pygame.display.set_caption('Meme Generator')
window.blit(img,(0,0))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
