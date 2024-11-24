import pygame
from pygame.locals import *
from time import*

pygame.init
screen=pygame.display.set_mode((600,600))
player_x = 200
player_y = 200
keys = [False, False, False, False]
player = pygame.image.load("Cat.jpg")
background = pygame.image.load("mouse.jpg")

while player_y < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key ==K_UP:
                Keys[0]=True
            if event.key ==K_LEFT:
                Keys[1]=True
            if event.key ==K_DOWN:
                Keys[2]=True
            if event.key ==K_RIGHT:
                Keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_UP:
                Keys[0]=False
            elif event.key ==pygame.K_LEFT:
                Keys[1]=False
            elif event.key ==pygame.K_DOWN:
                Keys[2]=False
            elif event.key ==pygame.K_RIGHT:
                Keys[3]=False
            
            
