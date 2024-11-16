import pygame
from pygame.locals import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

TEXT = my_font.render('You must survive 5 nights at freddy fivebears. Press F to do stuff.', True, (0, 0, 0))
LEVEL1 = my_font.render('Level 1', True, (0, 0, 0))
LEVEL2 = my_font.render('Level 2', True, (0, 0, 0))
LEVEL3 = my_font.render('Level 3', True, (0, 0, 0))