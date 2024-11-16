import pygame
from pygame.locals import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

TEXT = my_font.render('You must survive 5 nights at freddy fivebears. Press F to do stuff.', True, (0, 0, 0))
LEVELS=[]
for i in range(3):
    LEVELS.append(my_font.render('Level '+str(i+1), True, (0, 0, 0)))