import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0,32)
pygame.display.set_caption('Hello World')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # RED, GREEN, BLUE IN 8 BITS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 48)

text = font.render('UltraMemeBoiGenius', True, WHITE, RED)

hello_world_container = text.get_rect()
hello_world_container.centerx = windowSurface.get_rect().centerx
hello_world_container.centery = windowSurface.get_rect().centery

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(windowSurface, RED, hello_world_container)
    windowSurface.blit(text, hello_world_container)
    pygame.draw.circle(windowSurface, BLUE, (250, 250), 20, 0)
    pygame.display.update()



