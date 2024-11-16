import pygame
from pygame.locals import *

class Room(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)