import pygame, sys

pygame.init()

windowsSize = (500, 400)


windows = pygame.display.set_mode(windowsSize)
pygame.display.set_caption('MovingObject on window')

name = pygame.font.SysFont("Gabriola ",30)
#pygame.windows.opacity("MovingName")
#name = pygame.font.SysFont("Informal Roman", 30).render("Hey welcome to game", 1, (255, 0, 0), (0, 255, 255))
paintName = name.render("Hey welcome to game", 1, (255, 0, 0), (0, 255, 255))

x,y=0,0
directionX,directionY = 1,1

#background = pygame.image.load("p.jpg")

objectSize = paintName.get_size()
frameSpeed = pygame.time.Clock()
while True:
    frameSpeed.tick(30)
    windows.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    windows.blit(paintName, (x,y))
    #windows.blit(background,(0,0))

    x += 5 * directionX
    y += 5 * directionY

    if x + objectSize[0] > 500 or x<=0:
        directionX *= -1
    if y + objectSize[1] > 400 or y<=0:
        directionY *= -1

    pygame.display.update()