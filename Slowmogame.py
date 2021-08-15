#!/usr/bin/python3.4
# Setup Game ----------------------------------------------- #
import pygame, sys, time
from data.Scripts.Player import Player
from pygame.locals import *
pygame.init()

def main(): 
    # Setup pygame/window ---------------------------------------- #
    starttime = time.time()
    mainClock = pygame.time.Clock()
    pygame.display.set_caption('game base')
    screen = pygame.Surface((240, 135))
    display = pygame.display.set_mode((1280, 720),0,32)
    Level = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[11,10,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,4,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,11,10,10,10,10,10,10,10,12,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,5,4,4,4,4,4,4,4,6,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    last_time = time.time()
    tiles = {"center": pygame.image.load("data\Assets\Tiles\Ground\Center.png"),
             "topleft": pygame.image.load("data\Assets\Tiles\Ground\TopLeft.png"),
             "topright": pygame.image.load("data\Assets\Tiles\Ground\TopRight.png"),
             "top": pygame.image.load("data\Assets\Tiles\Ground\Top.png"),
             "right": pygame.image.load("data\Assets\Tiles\Ground\Right.png"),
             "bottomright": pygame.image.load("data\Assets\Tiles\Ground\BottomRight.png"),
             "left": pygame.image.load("data\Assets\Tiles\Ground\Left.png"),
             "bottomleft": pygame.image.load("data\Assets\Tiles\Ground\BottomLeft.png"),
             "bottom": pygame.image.load("data\Assets\Tiles\Ground\Bottom.png")}
    pimg = pygame.image.load("data\Assets/Animations/player_idle/img_0.png").convert()
    pimg.set_colorkey((0, 255, 0))
    player = Player(pimg, 50, 50)
    platforms = []
    # Loop ------------------------------------------------------- #
    while True:
     
        dt = time.time() - last_time
        dt *= 30
        last_time = time.time()
        
        # Background --------------------------------------------- #
        screen.fill((0,0,0))
     
        
        # Update ------------------------------------------------ #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        player.update(dt, platforms)
        # Draw ------------------------------------------------- #
        y = 0
        platforms = []
        for level in Level:
            x = 0
            for tile in level:
                if tile == 11:
                    screen.blit(tiles["topleft"], (x* 12 - 1, y* 12 - 1))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                if tile == 10:
                    screen.blit(tiles["top"], (x* 12, y* 12 - 1))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                if tile == 12:
                    screen.blit(tiles["topright"], (x* 12, y* 12 - 1))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                if tile == 5:
                    screen.blit(tiles["bottomleft"], (x* 12 - 1, y* 12))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                if tile == 4:
                    screen.blit(tiles["bottom"], (x* 12, y* 12))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                if tile == 6:
                    screen.blit(tiles["bottomright"], (x* 12 , y* 12))
                    platforms.append(pygame.Rect(x, y, 12, 12))
                
                x += 1
            y += 1
        player.draw(screen)
        display.blit(pygame.transform.scale(screen, (1280, 720)), (0, 0))
        pygame.display.update()
main()
