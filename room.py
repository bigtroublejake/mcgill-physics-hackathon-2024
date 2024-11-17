import pygame
from pygame.locals import *

class Room(pygame.sprite.Sprite): 
    def __init__(self, color, width, height, posx, posy): 
        super().__init__() 
        self.image = pygame.Surface([width, height])
        self.floor = pygame.image.load("Sprites/room_floor.png")
        self.camera = pygame.image.load("Sprites/camera.png")
        self.camera = pygame.transform.scale_by(self.camera,1.5)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.frect = self.floor.get_rect()
        self.frect.center = (posx,posy)
        self.crect = self.camera.get_rect()
        self.crect.center = (1152,48)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.floor, self.frect)
        surface.blit(self.camera, self.crect)