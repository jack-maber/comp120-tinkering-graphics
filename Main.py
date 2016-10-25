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


label = myfont.render("CJ?", 18, (0,0,0)) #Defines Bottom Text
text_rect = label.get_rect(center=(Width/2, 550)) #Automatically Centers Text
window.blit(label, text_rect) #blits text to window
pxarray = pygame.PixelArray(window) #Creates a pixel array on the existing image

def greyscale():
    for Y in xrange(Height):
        for X in xrange(Width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            grey = (Red + Green + Blue)/3

            pxarray[X, Y] = (grey, grey, grey)



def thedevil():
    for Y in xrange(Height):
        for X in xrange(Width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            spook = (Red + Green + Blue)/4
            if Red > 25 and Green > 25 and Blue > 25:
                pxarray[X, Y] = (255, spook, spook)

def sepiatone():
    for Y in xrange(Height): #greyscales image
        for X in xrange(Width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            grey = (Red + Green + Blue)/3

            pxarray[X, Y] = (grey, grey, grey)







while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_g:
            greyscale()
        if event.type == KEYDOWN and event.key == K_h:
            thedevil()
    pygame.display.update()
