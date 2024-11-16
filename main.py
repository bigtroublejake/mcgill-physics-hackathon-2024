import pygame, sys
from pygame.locals import *
from parameters import *
from fnaf_cam import Fnaf_cam, ballBoy
from roombuilder import roomBuidler
from room import Room

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
        self.current_room=0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]and self.rect.centery<SCREEN_HEIGHT:
            self.rect.move_ip(0,5)
        if pressed_keys[K_a] and self.rect.centerx>0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d] and self.rect.centerx<SCREEN_WIDTH:
            self.rect.move_ip(5,0)

        if self.rect.centery==0:
            self.rect.centery=SCREEN_HEIGHT
            self.current_room+=1
            print(self.current_room)

        '''
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        '''  

    def state_toggle(self):
        self.shown = not self.shown
        lens.toggle()
        lensLight.toggle()
 
    def draw(self, surface):
        if self.shown == 1:
            surface.blit(self.image, self.rect)  
 
# Create rooms 
builder = roomBuidler()
roomSize = [800, 1200]
rooms = []
for i in range(3):
    rooms.append(Room(builder.cbroomColorRGB[i],roomSize[0],roomSize[1],SCREEN_WIDTH/2,0))

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
                if event.key == K_t:
                    lensLight.blurAdd(1)
                if event.key == K_y:
                    lensLight.blurAdd(-1)


    P1.update()
     
    DISPLAYSURF.fill(GRAY)
    
    if P1.current_room!=0:
        rooms[P1.current_room-1].draw(DISPLAYSURF)
    
    P1.draw(DISPLAYSURF)
    lens.draw(DISPLAYSURF)
    lensLight.draw(DISPLAYSURF)


    pygame.display.update()
    FramePerSec.tick(FPS)