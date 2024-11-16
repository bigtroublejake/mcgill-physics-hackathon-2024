import pygame
from pygame.locals import *
from parameters import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

TEXT = my_font.render('You must survive 5 nights at freddy fivebears. Press F to do stuff.', True, WHITE)
LEVELS=[]
for i in range(3):
    LEVELS.append(my_font.render('Level '+str(i+1), True, WHITE))

def SETTEXT(text, color):
    return my_font.render(text, True, color)

LENSINSTRUCTIONS = my_font.render('Use T and Y to adjust diameter of lens', True, WHITE)