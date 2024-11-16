import pygame
from pygame.locals import *

class Fnaf_cam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/lens.png")
        self.rect = self.image.get_rect()
        self.shown = 0

    def toggle(self):
        print("toggle lens")
        if (self.shown==1):
            self.shown=0
        elif (self.shown==0):
            self.shown=1
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)