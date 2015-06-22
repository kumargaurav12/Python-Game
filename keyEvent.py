import pygame, sys

pygame.init()
pygame.mixer.init()  #mixer help us to init the sound

windowsSize = (500, 400)
windows = pygame.display.set_mode(windowsSize)

paintName = pygame.image.load("img.png")

#myMusic = pygame.mixer.Sound("t.ogg")

myMusic = pygame.mixer.music.load("t.mp3")
directionX,directionY = 1,1

objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()
myMusic = pygame.mixer.music.play()



x= 500 - objectSize[0]
y= 400 - objectSize[1]


while True:
    frameSpeed.tick(30)
    windows.fill((0,0,0))
    windows.blit(paintName, (x,y))

    for event in pygame.event.get():

         #---- Key down or up
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x -=25
            elif event.key ==pygame.K_RIGHT:
                x +=25
            elif event.key == pygame.K_UP:
                y -=25
            elif event.key ==pygame.K_DOWN:
                y += 25

    if x + objectSize[0] >500:
        x= 500 -objectSize[0]
        #myMusic.stop()
        #myMusic.play()

    if y + objectSize[1] > 400:
        y = 400 - objectSize[1]
        #myMusic.stop()
        #myMusic.play()

    if x <= 0 or y <=0:
        x + objectSize[0]
        #myMusic.play()


    pygame.display.update()