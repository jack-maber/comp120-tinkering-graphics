import pygame, sys, time, math, random
from pygame.locals import *

pygame.init()#Initiates Pygame
img1 = pygame.image.load('BigSmoke.jpg')  #Imports BigSmoke
img2 = pygame.image.load('Harambe.jpg')   #Imports Harambe
img3 = pygame.image.load('Doge.jpg')      #Imports Doge
img4 = pygame.image.load('YeaBoi.jpg')    #Imports Boi
img5 = pygame.image.load('Dio.jpg')       #Imports Dio
img6 = pygame.image.load('Jaguars.jpg')   #Imports Jaguars
myfont = pygame.font.SysFont("comic", 100) #Imports text font
Height =800 #Sets dimensions of window
Width =800

imagelist = [img1, img2, img3, img4,img5, img6] #Picks random from loaded images
imagelistRan = (random.choice(imagelist))

window = pygame.display.set_mode((Width, Height), 0, 24) #Creates window
pygame.display.set_caption('Meme Generator') #Sets caption for game window
window.blit(imagelistRan,(0,0)) #Blits image to created window

textlist = ["CJ?","Are you OK?","Excuse me Young Man!"]
textlist1 = ["Ohhhhhhhhhh","Big Smoke, It's me!","Boiiiiiiiiiiiiiiiiiiiiiiiii", "It was me, Dio!", "JAGUARS" ]#Picks random text snippet from list
textlistRan = (random.choice(textlist))
textlistRan1 =(random.choice(textlist1))

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

def invert(window):
    for Y in xrange(Height):
        for X in xrange(Width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b
            pxarray[X, Y] = (255 - Red, 255 - Green, 255 - Blue)


def nightvision(window):
    for Y in xrange(Height):
        for X in xrange(Width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b
            pxarray[X, Y] = (255 - Red, Green, 255 - Blue)


while True:

    pxarray = pygame.PixelArray(window)  # Creates a pixel array on the existing image

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_g:
            greyscale()
        if event.type == KEYDOWN and event.key == K_h:
            thedevil()
        if event.type == KEYDOWN and event.key == K_j:
            invert(window)
        if event.type == KEYDOWN and event.key == K_k:
            nightvision(window)

    del pxarray #Deletes PixelArray so that the text is not affected

    label = myfont.render(textlistRan, 18, (255, 255, 255))  # Defines Top Text
    text_rect = label.get_rect(center=(Width / 2, 50))  # Automatically Centers Text
    window.blit(label, text_rect)  # blits text to window

    label = myfont.render(textlistRan1, 18, (255, 255, 255))  # Defines Bottom Text
    text_rect = label.get_rect(center=(Width / 2, 750))  # Automatically Centers Text
    window.blit(label, text_rect)  # blits text to window

    pygame.display.update()
