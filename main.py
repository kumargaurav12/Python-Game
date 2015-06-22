
import pygame,sys,math

pygame.init()

#windowsize =(0,0)
#---------Creating a windows size----------

windowSize =(600,400)

#pygame.display.set_mode(windowSize)
#program.display.set_mode(windowsize.pygame.FULLSCREEN)

window =pygame.display.set_mode(windowSize)

name = pygame.font.SysFont("Courier",20)

paint = name.render("HEY welcom to game",1,(255,0,255),(255,255,255))

#while 1:
while True:
#-------------use for event handle------
    for a in pygame.event.get():
        if a.type==pygame.QUIT:
            sys.exit()
    window.blit(paint,(10,50))     #print the string
    pygame.display.flip()
    pygame.display.update()


'''


import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024,768))
car = pygame.image.load('car.png')
clock = pygame.time.clock()
k_up =k_down =k_left =k_right =0
sped = derectin = 0
position = (100, 100)
TURN_SPEED = 5
ACCELERATION =2
MAX_FORWARD_SPPED =10
MAX_POWER_SPPED =-5
BLACK (0,0,0)

while 1:
    #------------- User Inputs ---------------
    clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event,'key'):
            countinue
            down =event.type ==KEYDOWN       #---- Key down or up
            if event.key == K_RIGHT:
                k_right =down * -5
            elif event.key == K_LEFT:
                k_left =down * 5
            elif event.key == K_UP:
                k_up = down * 2
            elif event.key == K_DOWN:
                k_down =down * -2
            elif event.key ==K_ESCAPE:
                sys.exit(0)      # Quit the game
    screen.fil(BLACK)

    # SIMULATION
    # .. New speed and direction based on acceleration and turn

    speed +=(k_up +k_down)
    if speed > MAX_FORWARD_SPEED:
        speed =MAX_FORWARD_SPPED
    if speed < MAX_REVERSE_SPPED:
        speed = MAX_REVERSE_SPEED
    direction +=(k_right +k_left)


    # new position based on current position, speed and direction
    x, y =position
    rad = direction * math.pi /180
    x+= -speed*math.sin(rad)
    y += -speed*math.cos(rad)
    position =(x,y)

    # RENDERING

    rotated =pygame.transform.rotate(car,direction)
    rect =rotated.get_rect()
    rect.center = position
    screen.blit(rotated,rect)
    pygame.display.flip()
'''