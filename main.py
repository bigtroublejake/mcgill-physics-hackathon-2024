import pygame, sys
from pygame.locals import *
from fnaf_cam import Fnaf_cam
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
 
# Screen information
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")
 
lens = Fnaf_cam()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/Player.png")
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5,0)
        if pressed_keys[K_f]:
            lens.toggle()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)  
 
         
P1 = Player()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
     
    DISPLAYSURF.fill(GRAY)
    P1.draw(DISPLAYSURF)
    lens.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)