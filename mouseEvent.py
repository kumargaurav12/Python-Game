import pygame, sys

pygame.init()

pygame.mixer.init()  #mixer help us to init the sound
windowsSize = (500, 400)
windows = pygame.display.set_mode(windowsSize)

paintName = pygame.image.load("img.png")
myMusic = pygame.mixer.music.load("t.mp3")
#myMusic = pygame.mixer.Sound("t.ogg")


directionX,directionY = 1,1
objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()

myMusic = pygame.mixer.music.play()

while True:
    frameSpeed.tick(30)
    windows.fill((0,0,0))

    mouseCoordinates = pygame.mouse.get_pos()

    x = mouseCoordinates[0]
    y = mouseCoordinates[1]

    if x + objectSize[0] >=500:
        x= 500 -objectSize[0]
        '''
        myMusic.stop()
        myMusic.play()
        '''

    if y + objectSize[1]>400:
        y =y - objectSize[1]
        '''
        myMusic.stop()
        myMusic.play()
        '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    windows.blit(paintName, (x,y))
    '''
    x += 5 * directionX
    y += 5 * directionY
    '''


    pygame.display.update()