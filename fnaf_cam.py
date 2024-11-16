import pygame, sys
from pygame.locals import *

class Fnaf_cam(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect()
        self.shown = 0

    def show(self):
        self.shown = 1

    def hide(self):
        self.shown = 0
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)