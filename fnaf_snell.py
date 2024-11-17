import pygame
from pygame.locals import *

from parameters import *
from equations import *


class snell_lens(pygame.sprite.Sprite):
    def __init__(self, wavelength):
        super().__init__() 
        self.image = pygame.image.load("Sprites/glass.png")
        self.image = pygame.transform.scale_by(self.image, 0.7)
        
        self.protractor = pygame.image.load("Sprites/protractor.png")
        self.protRect = self.protractor.get_rect()
        self.protRect.center = (7+SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        self.wavelength = wavelength
        print(self.wavelength)
        self.refractIndex = 1.2 + (0.01709/(self.wavelength/1000)**4) + (0.000439/(self.wavelength/1000)**5)
        print(self.refractIndex)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/1.3, SCREEN_HEIGHT/2)
        self.shown = True
        self.laserAngle = 0

    def toggle(self):
        print("toggle snell")
        self.shown = not self.shown
 
    def draw(self, surface):
        if (self.shown == True):
            surface.blit(self.image, self.rect)
            surface.blit(self.protractor, self.protRect)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()




        if pressed_keys[K_k]:
            if self.laserAngle + 1 < 90:
                self.laserAngle += 1
        if pressed_keys[K_l]:
            if self.laserAngle - 1 > -90:
                self.laserAngle -= 1
        
        self.refractedAngle = refractAngleGlass(1.470, self.laserAngle)

