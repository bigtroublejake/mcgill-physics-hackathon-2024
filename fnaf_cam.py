import pygame
from pygame.locals import *

from parameters import *
class Fnaf_cam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/lens.png")

        
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = 0

    def toggle(self):
        print("toggle lens")
        self.shown = not self.shown
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)

class ballBoy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Sprites/BallLight.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)

        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = 0
    

    def draw(self, surface):
        if self.shown == 1:
            surface.blit(self.image, self.rect)

    def toggle(self):
        print("toggle light")
        self.shown = not self.shown
