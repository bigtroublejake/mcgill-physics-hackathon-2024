import pygame
from pygame.locals import *
from parameters import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

TEXT = []
TEXT.append(my_font.render('Hello Spy, you must sneak through the facility by blending in.', True, WHITE))
TEXT.append(my_font.render('However, you have a type of color blindness so figure out the color using gadgets', True, WHITE))
TEXT.append(my_font.render('', True, WHITE))
TEXT.append(my_font.render('Press F to bring up lens to observe an source and find its wavelength.', True, WHITE))
TEXT.append(my_font.render('Press G to bring up a mystery diffraction gratting whcih you can compare', True, WHITE))
TEXT.append(my_font.render('Press H to bring up refraction stuff', True, WHITE))

TEXTLEVEL1=my_font.render('You see a light at the end of the room. Maybe you have something to focus on it.', True, WHITE)

TEXTLEVEL2=my_font.render('Theres a plane with a grating, the light shines through it.', True, WHITE)

TEXTLEVEL3=my_font.render('Theres pieces of glass.', True, WHITE)

TEXTEND=[]
TEXTEND.append(my_font.render('You made it to the end! With the information you have gathered you must determine', True, WHITE))
TEXTEND.append(my_font.render('which type of colourblindness you have.', True, WHITE))

LEVELS=[]
for i in range(3):
    LEVELS.append(my_font.render('Level '+str(i+1), True, WHITE))

def SETTEXT(text, color):
    return my_font.render(text, True, color)

LENSINSTRUCTIONS = my_font.render('(Use T and Y to adjust diameter of lens)', True, WHITE)
LENSINSTRUCTIONSRECT = LENSINSTRUCTIONS.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-30))