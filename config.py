import pygame
import time

pygame.init()

#set up the colors
RIVER = (175, 238, 238)
LAND  = (139,  69,  19)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
PINK  = (255, 192, 203)

#font
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf',10)
#Text
text = font.render('START', True, BLACK, LAND)
textRect = text.get_rect()
textRect.center = (50,30)
texty = font.render('END', True,BLACK,LAND)
textrecty = texty.get_rect()
textrecty.center = (30,870)
texta = font1.render('0 to QUIT',True,BLACK,LAND)
textrecta = texta.get_rect()
textrecta.center = (870,860)
textb = font1.render('1 to PlayAgain',True,BLACK,LAND)
textrectb = textb.get_rect()
textrectb.center = (860,880)



