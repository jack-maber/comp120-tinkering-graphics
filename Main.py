import pygame, sys, time
from pygame.locals import *

pygame.init()
img = pygame.image.load('BigSmoke.jpg')
myfont = pygame.font.SysFont("comic", 100)
Height =600
Width =600

window = pygame.display.set_mode((Width, Height), 0, 24)
pygame.display.set_caption('Meme Generator')
window.blit(img,(0,0))


label = myfont.render("CJ?", 18, (255,255,255))
text_rect = label.get_rect(center=(Width/2, Height/2))
window.blit(label, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
