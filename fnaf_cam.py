import pygame
from pygame.locals import *

from parameters import *
class Fnaf_cam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Sprites/lens.png")

        
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = 0

    def toggle(self):
        print("toggle lens")
        self.shown = not self.shown
 
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)

class ballBoy(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.image.load("Sprites/BallLight.png")
        self.scale_amount = 0.2
        self.original_image = pygame.transform.scale_by(self.original_image, self.scale_amount)

        self.rect = self.original_image.get_rect()

        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = False

        # Create blurred image
        self.blur_amount = 0  # Adjust this value to control blur amount
        
        size = self.original_image.get_size()
        smaller_img = self.original_image
        self.blurred_image = pygame.transform.smoothscale(smaller_img, size)
        self.blurAdd(0)

    

    def draw(self, surface):
        if self.shown == True:

            surface.blit(self.blurred_image, self.rect)

    def toggle(self):
        print("toggle light")
        self.shown = not self.shown

    def blurAdd(self, amount):

        self.blur_amount += amount

        size = self.original_image.get_size()

        if 0.6 < self.scale_amount + amount < 0.8:
            self.scale_amount += amount / 100
            self.blurred_image = pygame.transform.scale_by(self.blurred_image, self.scale_amount)


        if self.blur_amount == 0:
            self.blurred_image = self.original_image
        elif abs(self.blur_amount) > 60:
            # cancels out whatever it tried to blur as
            self.blur_amount -= amount
        else:
            smaller_img = pygame.transform.smoothscale(self.original_image, (int(size[0]/abs(self.blur_amount)), int(size[1]/abs(self.blur_amount))))
            self.blurred_image = pygame.transform.smoothscale(smaller_img, size)

        self.rect = self.blurred_image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
    
    '''
    def update(self):
        if self.shown == True:
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_t]:
                self.blurAdd(2)
            if pressed_keys[K_y]:
                self.blurAdd(-2)
        
            # print(self.scale_amount)
            # print(self.blurred_image.get_rect())
    '''
    
class diffpattmystery(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("diffimg/mysterywavelength.png")

        self.image.convert_alpha
        self.image.set_alpha(90)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = False


    def toggle(self):
        print("toggle mystery pattern")
        self.shown = not self.shown
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)
class colordiff(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("diffimg/red.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shown = False
    def imgchange(self, color):
        self.image = pygame.image.load("diffimg/"+color+".png")
        self.image.convert_alpha
        self.image.set_alpha(80)
    def toggle(self):
        print("toggle color patterns")
        self.shown = not self.shown
    def draw(self, surface):
        if (self.shown == 1):
            surface.blit(self.image, self.rect)
        
