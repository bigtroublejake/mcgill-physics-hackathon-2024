import pygame
from pygame.locals import *

from parameters import *
from equations import *


class snell_lens(pygame.sprite.Sprite):
    def __init__(self, wavelength):
        super().__init__() 
        self.image = pygame.image.load("Sprites/lens.png")
        
        self.wavelength = wavelength
        print(self.wavelength)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = 0
        self.laserAngle = 0

    def toggle(self):
        print("toggle snell")
        self.shown = not self.shown
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_k]:
            if self.laserAngle + 1 < 90:
                self.laserAngle += 1
        if pressed_keys[K_l]:
            if self.laserAngle - 1 > -90:
                self.laserAngle -= 1
        
        self.refractedAngle = refractAngleGlass(1.470, self.laserAngle)

