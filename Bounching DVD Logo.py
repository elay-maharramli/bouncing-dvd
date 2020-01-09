import pygame
from pygame.locals import *
import random

pygame.init()


width = 156
height = 70
win_width = 900
win_height = 600
x = 350
y = 10
#wall_width = 60
#wall_height = 140
#wall_x = 500
#wall_y = 200
velx = 0.5
vely = 0.5
#wall_vel = 0.5
win = pygame.display.set_mode((win_width,win_height))
dvd = pygame.image.load('DVDLogo.png').convert_alpha()
dvd = pygame.transform.scale(dvd, (width,height))
#wall = pygame.image.load('Wall.png').convert_alpha()
#wall = pygame.transform.scale(wall, (wall_width,wall_height))
while True:
    win.fill((0,0,0))
    win.blit(dvd, (x,y))
    #win.blit(wall, (wall_x,wall_y))


    x = x + velx
    y = y + vely

    #print(x)

    if x + width >= 900:
        velx = -velx

    if x <= 0 or x <= 0:
       velx = -velx

    if y + height >= 600:
        vely = -vely

    if y <= 0:
        vely = -vely



    pygame.display.update()
