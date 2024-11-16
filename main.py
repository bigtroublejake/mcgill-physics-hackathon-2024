import pygame, sys
from pygame.locals import *
from PIL import Image, ImageFilter


from parameters import *
from fnaf_cam import Fnaf_cam, ballBoy


pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 

 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")
 
lens = Fnaf_cam()
lensLight = ballBoy()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/Player.png")
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.shown = 1

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
        # if pressed_keys[K_f]:
        #     lens.toggle()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    

    def state_toggle(self):
        self.shown = not self.shown
        lens.toggle()
        lensLight.toggle()
 
    def draw(self, surface):
        if self.shown == 1:
            surface.blit(self.image, self.rect)  
 
         
P1 = Player()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        ### USE THIS FOR ONE TIME KEY PRESSES ###
        elif event.type == KEYDOWN: # Detect single key presses
                
                if event.key == K_f:
                    P1.state_toggle()
                    # print("f was pressed")





    P1.update()
     
    DISPLAYSURF.fill(GRAY)
    P1.draw(DISPLAYSURF)
    lens.draw(DISPLAYSURF)
    lensLight.draw(DISPLAYSURF)


    pygame.display.update()
    FramePerSec.tick(FPS)