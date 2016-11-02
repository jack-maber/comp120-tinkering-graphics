import pygame, sys, time, math, random
from pygame.locals import *

pygame.init()  #  Initiates Pygame
img1 = pygame.image.load('BigSmoke.jpg')
img2 = pygame.image.load('Harambe.jpg')
img3 = pygame.image.load('Doge.jpg')
img4 = pygame.image.load('YeaBoi.jpg')
img5 = pygame.image.load('Dio.jpg')
img6 = pygame.image.load('Jaguars.jpg')
img7 = pygame.image.load('Issac.jpg')
myfont = pygame.font.SysFont("comic", 100) #Imports text font
HEIGHT =800 #Sets dimensions of window
WIDTH =800

imagelist = [img1, img2, img3, img4,img5, img6, img7] #Picks random from loaded images
imagelistRan = (random.choice(imagelist))

window = pygame.display.set_mode((WIDTH, HEIGHT)) #Creates window
pygame.display.set_caption('Meme Generator 3000') #Sets caption for game window
window.blit(imagelistRan,(0, 0)) #Blits image to created window

textlist = ["CJ?","Are you OK?","Excuse me Young Man!","WHEN YOU MEME"]
textlist1 = ["Ohhhhhhhhhh","Big Smoke, It's me!","Boiiiiiiiiiiiiiiiiiiiiiiiii","It was me, Dio!","JAGUARS","BOTTOM TEXT"]#Picks random text snippet from list
textlistRan = (random.choice(textlist))
textlistRan1 =(random.choice(textlist1))

def greyscale():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b

            grey = (Red + Green + Blue)/3

            pxarray[x, y] = (grey, grey, grey)

def redblack():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b

            spook = (Red + Green + Blue)/4
            if Red > 25 and Green > 25 and Blue > 25:
                pxarray[x, y] = (255, spook, spook)

def invert(window):
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b
            pxarray[x, y] = (255 - Red, 255 - Green, 255 - Blue)

def nightvision(window):
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b
            pxarray[x, y] = (255 - Red, Green, 255 - Blue)

def ganggreen(window):
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b
            pxarray[x, y] = (Red,255 - Green, Blue)

def bluebell(window):
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            Red = window.get_at((x, y)).r
            Green = window.get_at((x, y)).g
            Blue = window.get_at((x, y)).b
            pxarray[x, y] = (Red, Green, 255 - Blue)



while True:

    pxarray = pygame.PixelArray(window)  # Creates a pixel array on the existing image

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_g:
            greyscale()
        if event.type == KEYDOWN and event.key == K_h:
            redblack()
        if event.type == KEYDOWN and event.key == K_j:
            invert(window)
        if event.type == KEYDOWN and event.key == K_k:
            nightvision(window)
        if event.type == KEYDOWN and event.key == K_f:
            ganggreen(window)
        if event.type == KEYDOWN and event.key == K_d:
            bluebell(window)
        


    del pxarray #Deletes PixelArray so that the text is not affected by the colour doesn't change

    label = myfont.render(textlistRan, 18, (255, 255, 255))  # Defines Top Text
    text_rect = label.get_rect(center=(WIDTH / 2, 50))  # Automatically Centers Text
    window.blit(label, text_rect)  # blits text to window

    label = myfont.render(textlistRan1, 18, (255, 255, 255))  # Defines Bottom Text
    text_rect = label.get_rect(center=(WIDTH / 2, 750))  # Automatically Centers Text
    window.blit(label, text_rect)  # blits text to window

    pygame.display.update()
