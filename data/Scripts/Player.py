import pygame
from pygame.locals import *
class Player:
    def __init__(self, img, x, y):
        self.image = img
        self.x = x
        self.y = y
        self.xvel = 0
        self.speed = 2
    def update(self, dt, platforms):
        keys = pygame.key.get_pressed()
        xvel = int(keys[K_d]) - int(keys[K_a])
        self.x += (xvel * self.speed) * dt
        for platform in platforms:
            rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
            while rect.colliderect(platform):
                if xvel > 0:
                    self.x -= .1
                    rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
                if xvel < 0:
                    self.x += .1
                    rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

                            
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
        
        
