import pygame
from pygame.locals import *
from parameters import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

TEXT = []
TEXT.append(my_font.render('You must survive 5 nights at freddy fivebears.', True, WHITE))
TEXT.append(my_font.render('Press F to bring up lens.', True, WHITE))
TEXT.append(my_font.render('Press G tp bring up diffraction gratting', True, WHITE))

LEVELS=[]
for i in range(3):
    LEVELS.append(my_font.render('Level '+str(i+1), True, WHITE))

def SETTEXT(text, color):
    return my_font.render(text, True, color)

LENSINSTRUCTIONS = my_font.render('(Use T and Y to adjust diameter of lens)', True, WHITE)
LENSINSTRUCTIONSRECT = LENSINSTRUCTIONS.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-30))