import pygame, sys
from pygame.locals import *


from parameters import *
from fnaf_cam import Fnaf_cam, ballBoy, diffpattmystery, colordiff
from roombuilder import roomBuidler
from room import Room
from textbox import *
import equations
from fnaf_snell import *

pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")
 
lens = Fnaf_cam()
lensLight = ballBoy()
mysterydiff = diffpattmystery()
colorsdiff = colordiff()

# Create rooms 
builder = roomBuidler()
roomWidth = SCREEN_WIDTH
roomHeight = 1200

rooms = []
for i in range(3):
    rooms.append(Room(builder.cbroomColorRGB[i],roomWidth,roomHeight,SCREEN_WIDTH/2,0))
wall1=(SCREEN_WIDTH-roomWidth)/2
wall2=SCREEN_WIDTH-(SCREEN_WIDTH-roomWidth)/2
wallThick=10




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/Player.png")
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.shown = 1
        self.current_room=0
        self.state = "room"
        # self.laserAngle = 90

        self.laserAngle = 90
        self.colorsname = ["red","orange","yellow","green","blue","indigo","violet"]
        self.colorposition =0
    def colorchange(self,key) -> str:
        if key == K_RIGHT:
            self.colorposition+=1
            if self.colorposition == len(self.colorsname):
                self.colorposition = 0
            return self.colorsname[self.colorposition]
        if key == K_LEFT:
            self.colorposition-=1
        if self.colorposition < 0:
            self.colorposition = len(self.colorsname)-1
        return self.colorsname[self.colorposition]
    
    def update(self):

        #inWallx = (self.rect.centerx>wall1-wallThick and self.rect.centerx<wall1+wallThick) or (self.rect.centerx>wall2-wallThick and self.rect.centerx<wall2+wallThick)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]and self.rect.centery<SCREEN_HEIGHT:
            self.rect.move_ip(0,5)
        if pressed_keys[K_a] and self.rect.centerx>0:
            self.rect.move_ip(-5, 0)
            #if inWallx:
            #    self.rect.move_ip(7,0)
        if pressed_keys[K_d] and self.rect.centerx<SCREEN_WIDTH:
            self.rect.move_ip(5,0)
            #if inWallx:
            #    self.rect.move_ip(-7,0)

        if self.rect.centery==0 and self.current_room<=4:
            self.rect.centery=SCREEN_HEIGHT
            self.current_room+=1
            print('Room#: ', self.current_room)

        if self.state == "snell":
            if pressed_keys[K_o]:
                self.laserAngle += 1
            elif pressed_keys[K_p]:
                self.laserAngle -= 1
            

        '''
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        '''  

    def state_toggle(self, popup, key):
        self.shown = not self.shown

        if popup == "lens":
            lens.toggle()
            if self.current_room == 1:
                lensLight.toggle()
            self.state = "lens" if self.state == "room" else "room"
        if popup == "diffraction":
            if self.current_room == 2:
                mysterydiff.toggle()
            self.state = "diffraction" if self.state == "room" else "room"
        if popup == "diffchange":
            if mysterydiff.shown == True and self.current_room == 1:
                colorsdiff.imgchange(self.colorchange(key))
                if colorsdiff.shown == False:
                    colorsdiff.toggle()
            self.state = "diffchange" if self.state == "room" else "room"


            
 
    def draw(self, surface):
        if self.shown == 1:
            surface.blit(self.image, self.rect)  

P1 = Player()
snellLens = snell_lens(builder.wavelengths[2])

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        ### USE THIS FOR ONE TIME KEY PRESSES ###
        elif event.type == KEYDOWN: # Detect single key presses
                
                if event.key == K_f:
                    P1.state_toggle("lens")
                    # print("f was pressed")
                if event.key == K_g:
                    P1.state_toggle("diffraction", K_g)
                if event.key == K_RIGHT:
                    P1.state_toggle("diffchange", K_RIGHT)
                if event.key == K_LEFT:
                    P1.state_toggle("diffchange", K_LEFT)


    P1.update()

    DISPLAYSURF.fill(GRAY)

    if P1.current_room >0 and P1.current_room<=3:
        rooms[P1.current_room-1].draw(DISPLAYSURF)

    P1.draw(DISPLAYSURF)

    if P1.state == "room":
        if P1.current_room==0:
            for i in range(len(TEXT)):
                DISPLAYSURF.blit(TEXT[i], (100,500+25*i))
        elif P1.current_room >0 and P1.current_room<=3:
            DISPLAYSURF.blit(LEVELS[P1.current_room-1],(10,10))
        elif P1.current_room==4:
            for i in range(len(TEXTEND)):
                DISPLAYSURF.blit(TEXTEND[i], (100, 500+25*i))

    lensLight.draw(DISPLAYSURF)
    lensLight.update()
    lens.draw(DISPLAYSURF)
    mysterydiff.draw(DISPLAYSURF)
    colorsdiff.draw(DISPLAYSURF)
    if lens.shown==1:
        DISPLAYSURF.blit(SETTEXT(str(lensLight.blur_amount), WHITE), (SCREEN_WIDTH/2, SCREEN_HEIGHT-80))
        DISPLAYSURF.blit(LENSINSTRUCTIONS, LENSINSTRUCTIONSRECT)

    snellLens.update()
    snellLens.draw(DISPLAYSURF)


    pygame.display.update()
    FramePerSec.tick(FPS)
