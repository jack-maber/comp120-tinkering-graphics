import pygame, sys, time, math
from pygame.locals import *

pygame.init()
img = pygame.image.load('BigSmoke.jpg')  #Imports background image
myfont = pygame.font.SysFont("comic", 100) #Imports text font
Height =600 #Sets dimensions of window
Width =600

window = pygame.display.set_mode((Width, Height), 0, 24) #Creates window
pygame.display.set_caption('Meme Generator') #Sets caption for game window
window.blit(img,(0,0)) #Blits image to created window

label = myfont.render("CJ?", 18, (0,0,0))
text_rect = label.get_rect(center=(Width/2, 550))
window.blit(label, text_rect)

##def blackwhite():



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
