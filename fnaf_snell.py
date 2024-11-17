import pygame
from pygame.locals import *

from parameters import *
class snell_lens(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/lens.png")

        
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = 0


    def toggle(self):
        print("toggle snell")
        self.shown = not self.shown
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)