import pygame, sys
import time
from pygame.locals import *
from config import *

pygame.init()

FPS = 50
fpsClock = pygame.time.Clock()
crashed = False
def Player(x,y):
    DISPLAYSURF.blit(PLAYERX, (x,y))
x = 0
y = 0


DISPLAYSURF = pygame.display.set_mode((900,900), 0, 32)
pygame.display.set_caption('The Scary River')


ROCK = pygame.image.load('rock.png')
PLAYER = pygame.image.load('player.resized.png')
PLAYER1 = pygame.image.load('player1.resized.png')
PLAYERX = PLAYER
score = 0
score1 = 0
SHIP = pygame.image.load('ship.png')
BOAT = pygame.image.load('boat.png')
ship1x = 0
ship2x = 200
ship3x = 600
boat1x = 400
boat2x = 700
direction1 = 'right'
direction2 = 'right'
direction3 = 'left'
direction4 = 'right'
direction5 = 'left'
c1 = 0
c2 = 0
sp = 2
sp1 = 2
t0= time.time()


pixObj= pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
k = 1
# run the game loop
while not crashed and k>= 1:

    DISPLAYSURF.fill(RIVER)

    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0, 0), (900,  0), (900,  50),(  0,  50)))
    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0,170), (900, 170), (900, 220),(  0, 220)))
    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0,340), (900, 340), (900, 390),(  0, 390)))
    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0,510), (900, 510), (900, 560),(  0, 560)))
    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0,680), (900, 680), (900, 730),(  0, 730)))
    pygame.draw.polygon(DISPLAYSURF, LAND, ((  0,850), (900, 850), (900, 900),(  0, 900)))

    DISPLAYSURF.blit(ROCK, (20, 130))
    DISPLAYSURF.blit(ROCK, (300, 320))
    DISPLAYSURF.blit(ROCK, (300, 660))
    DISPLAYSURF.blit(ROCK, (800, 480))
    DISPLAYSURF.blit(ROCK, (600, 320))
    DISPLAYSURF.blit(ROCK, (100, 480))
    DISPLAYSURF.blit(ROCK, (600, 660))
    DISPLAYSURF.blit(ROCK, (560, 130))
    DISPLAYSURF.blit(text, textRect)
    DISPLAYSURF.blit(texty, textrecty)
    DISPLAYSURF.blit(texta, textrecta)
    DISPLAYSURF.blit(textb, textrectb)
    text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)

    textrect = text1.get_rect()
    textrect.center = (500,30)
    text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)

    textrect1 = text2.get_rect()
    textrect1.center = (500,870)

    t1 = time.time()
    dt = t1-t0
    textx = font.render('TIME:' + str(dt),True, BLACK,LAND)
    textrectx = textx.get_rect()
    textrectx.center = (899,30)
    DISPLAYSURF.blit(textx, textrectx)



    if direction1 == 'right':
        ship1x += 2
        if ship1x == 850:
            direction1 = 'left'
    elif direction1 == 'left':
        ship1x -= 2
        if ship1x == 10:
            direction1 = 'right'
    DISPLAYSURF.blit(SHIP, (ship1x, 50))


    if direction2 == 'right':
        ship2x += 2
        if ship2x == 850:
            direction2 = 'left'
    elif direction2 == 'left':
        ship2x -= 2
        if ship2x == 10:
            direction2 = 'right'
    DISPLAYSURF.blit(SHIP, (ship2x, 220))

    if direction3 == 'right':
        boat1x += 2
        if boat1x == 850:
            direction3 = 'left'
    elif direction3 == 'left':
        boat1x -= 2
        if boat1x == 10:
            direction3 = 'right'
    DISPLAYSURF.blit(BOAT, (boat1x, 400))

    if direction4 == 'right':
        ship3x += 2
        if ship3x == 850:
            direction4 = 'left'
    elif direction4 == 'left':
        ship3x -= 2
        if ship3x == 10:
            direction4 = 'right'
    DISPLAYSURF.blit(SHIP, (ship3x, 560))

    if direction5 == 'right':
        boat2x += 2
        if boat2x == 850:
            direction5 = 'left'
    elif direction5 == 'left':
        boat2x -= 2
        if boat2x == 10:
            direction5 = 'right'
    DISPLAYSURF.blit(BOAT, (boat2x, 730))
    




    for event in pygame.event.get():
        if event.type == QUIT:
              crashed = True

        #########################
    keys = pygame.key.get_pressed()
    if PLAYERX == PLAYER:
        if keys[pygame.K_LEFT] and x>=5:
            x-=sp

        if keys[pygame.K_RIGHT] and x<850:
            x+=sp

        if keys[pygame.K_UP] and y>=5:
            y-=sp

        if keys[pygame.K_DOWN] and y<850:
            y+=sp
            
    if PLAYERX == PLAYER1:
        if keys[pygame.K_LEFT] and x>=5: 
            x-=sp1

        if keys[pygame.K_RIGHT] and x<850:
            x+=sp1

        if keys[pygame.K_UP] and y>=5:
            y-=sp1

        if keys[pygame.K_DOWN] and y<850:
            y+=sp1

    

       ##
    if x > ship1x-35 and x < ship1x+55 and y> 10 and y < 100: 
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 840
            y = 840
        else :
            c2 = 1
            PLAYERX = PLAYER
            x = 10
            y = 10



    elif x > ship2x-35 and x < ship2x+55 and y > 190 and y < 260:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 840
            y = 840
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10



    elif x > ship3x-35 and x < ship3x+55 and y > 530 and y < 610:
        c1 = 1
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 840
            y = 840
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10

    elif x > boat1x-35 and x < boat1x+55 and y > 370 and y < 450:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            c2 = 1
            PLAYERX = PLAYER
            x = 10
            y = 10


    elif x > boat2x-35 and x < boat2x+50 and y > 700 and y < 780:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            c2 = 1
            PLAYERX = PLAYER
            x = 10
            y = 10

    

    elif x >= 0 and x < 100 and y > 100 and y < 180:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10


    elif x > 270 and x < 370 and y > 290 and y < 370:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10

    elif x > 270 and x < 370 and y > 630 and y < 710:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10


    elif x > 770 and x < 870 and y > 450 and y < 530:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10

    elif x > 570 and x < 670 and y > 290 and y < 370:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10
    elif x > 530 and x < 670 and y > 100 and y < 180:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10

    elif x > 570 and x < 670 and y > 630 and y < 710:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10
    elif x > 70  and x < 170 and y > 450 and y < 630:
        if PLAYERX == PLAYER:
            c1 = 1
            PLAYERX = PLAYER1
            x = 850
            y = 850
        else :
            PLAYERX = PLAYER
            c2 = 1
            x = 10
            y = 10
    text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
    DISPLAYSURF.blit(text1, textrect)
    if PLAYERX == PLAYER:

       if y > 170 and y < 220:
           if score < 10:
               score += 10
           FPS += 10
           fpsClock.tick(FPS)
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)

           DISPLAYSURF.blit(text1, textrect)
       if y > 220 and y < 340 :
           if score < 20:
               score += 10
           FPS += 10
           fpsClock.tick(FPS)

           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)

       if y > 340 and y < 390 :
           if score < 30:
               score += 10
           FPS += 10
           fpsClock.tick(FPS) 

           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
           fpsClock.tick(FPS)
       if y > 390 and y < 510  :
           if score < 40:
               score += 10
           FPS += 10
           fpsClock.tick(FPS) 
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
       if y > 510 and y < 560 :
           if score < 50:
               score += 10
           FPS += 10
           fpsClock.tick(FPS) 
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
       if y > 560 and y < 680 :
           if score < 60:
               score += 10
           FPS += 10
           fpsClock.tick(FPS) 
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
       if y > 680 and y < 730 :
           if score < 70:
               score += 10
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
       if y > 730 and y < 850 :
           if score < 80:
               score += 10
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)
       if y >= 850:
           if score < 90:
               score += 10
           PLAYERX = PLAYER1
           text1 = font.render('PLAYER1 SCORE:' + str(score), True, BLACK, LAND)
           DISPLAYSURF.blit(text1, textrect)

    if PLAYERX == PLAYER1:

       if y <= 730 and y > 680:
           if score1 < 10:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)

           DISPLAYSURF.blit(text2, textrect1)
       if y <= 680 and y > 560 :
           if score1 < 20:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)

       if y <= 560 and y > 510 :
           if score1 < 30:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 510 and y > 390  :
           if score1 < 40:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 390 and y > 340 :
           if score1 < 50:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 340 and y > 220 :
           if score1 < 60:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 220 and y > 170 :
           if score1 < 70:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 170 and y > 50 :
           if score1 < 80:
               score1 += 10
           FPS += 10
           fpsClock.tick(FPS)

           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
       if y <= 50:
           if score1 < 90:
               score1 += 10
           FPS = 60
           fpsClock.tick(FPS)
           PLAYERX = PLAYER1
           text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
           DISPLAYSURF.blit(text2, textrect1)
    text2 = font.render('PLAYER2 SCORE:' + str(score1), True, BLACK, LAND)
    DISPLAYSURF.blit(text2, textrect1)

    Player(x,y)

    if score == 90:
        c1 = 2
    if score1 == 90:
        c2 = 2
    if c1 == 2 and c2 == 2:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)

        text4=font.render('GAME OVER',True,WHITE,BLACK)

        text3=font.render('Match Tied', True, LAND, BLACK) 
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)
        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)

        DISPLAYSURF.blit(text6, textrect5)
        DISPLAYSURF.blit(textk, textrectk)


        DISPLAYSURF.blit(text4, textrect3)
        DISPLAYSURF.blit(text5, textrect4)


        DISPLAYSURF.blit(text3, textrect2)
    if c1 == 2 and c2 == 1:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)

        text4=font.render('GAME OVER',True,WHITE,BLACK)

        text3=font.render('PLAYER1 WON THE GAME', True, WHITE, BLACK)
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)
        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)

        DISPLAYSURF.blit(text6, textrect5)
        DISPLAYSURF.blit(textk, textrectk)


        DISPLAYSURF.blit(text4, textrect3)

        DISPLAYSURF.blit(text5, textrect4)

        DISPLAYSURF.blit(text3, textrect2)
    if c2 == 2 and c1 == 1:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)

        text4=font.render('GAME OVER',True,WHITE,BLACK)

        text3=font.render('PLAYER2 WON THE GAME', True, WHITE, BLACK)
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)
        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)
        DISPLAYSURF.blit(textk, textrectk)

        DISPLAYSURF.blit(text6, textrect5)


        DISPLAYSURF.blit(text4, textrect3)


        DISPLAYSURF.blit(text3, textrect2)
        DISPLAYSURF.blit(text5, textrect4)

    if c1 == 1 and c2 == 1 and score > score1:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)

        text4=font.render('GAME OVER',True,WHITE,BLACK)

        text3=font.render('PLAYER1 WON THE GAME',True,WHITE,BLACK)
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)
        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)
        DISPLAYSURF.blit(textk, textrectk)

        DISPLAYSURF.blit(text6, textrect5)


        DISPLAYSURF.blit(text4, textrect3)


        DISPLAYSURF.blit(text3, textrect2)
        DISPLAYSURF.blit(text5, textrect4)

    if c1 == 1 and c2 == 1 and score < score1:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)

        text4=font.render('GAME OVER',True,WHITE,BLACK)
        text3=font.render('PLAYER2 WON THE GAME',True,WHITE,BLACK)
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)
        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)

        DISPLAYSURF.blit(text6, textrect5)
        DISPLAYSURF.blit(textk, textrectk)


        DISPLAYSURF.blit(text4, textrect3)
        DISPLAYSURF.blit(text3, textrect2)
        DISPLAYSURF.blit(text5, textrect4)
    if c1 == 1 and c2 == 1 and score == score1:
        DISPLAYSURF.fill(BLACK)
        texth = font1.render('PLAYER1 SCORE:'+ str(score),True,WHITE,BLACK)
        textrecth = texth.get_rect()
        textrecth.center=(250,250)
        DISPLAYSURF.blit(texth,textrecth)
        textl = font1.render('PLAYER2 SCORE:'+ str(score1),True,WHITE,BLACK)
        textrectl = textl.get_rect()
        textrectl.center=(250,300)
        DISPLAYSURF.blit(textl,textrectl)


        text4=font.render('GAME OVER',True,WHITE,BLACK)

        text3=font.render('MATCH TIED',True,WHITE,BLACK)
        textrect2 = text3.get_rect()
        textrect2.center = (400,400)
        textrect3 = text4.get_rect()
        textrect3.center = (400,200)
        text5=font.render('Press 1 to Play Again', True, RIVER, BLACK)

        textrect4 = text5.get_rect()
        textrect4.center = (400,800)
        text6=font.render('Press 0 to END game',True,WHITE,BLACK)
        textrect5 = text6.get_rect()
        textrect5.center = (400,850)
        textk=font.render('Press 2 to go to NEXT level',True,WHITE,BLACK)
        textrectk = textk.get_rect()
        textrectk.center = (400,750)
        DISPLAYSURF.blit(textk, textrectk)

        DISPLAYSURF.blit(text6, textrect5)
        DISPLAYSURF.blit(text4, textrect3)


        DISPLAYSURF.blit(text3, textrect2)
        DISPLAYSURF.blit(text5, textrect4)

    if keys[pygame.K_1]:
        score = 0
        score1 = 0
        x = 10
        y = 10
        FPS = 60
        k += 1
        c1 = 0
        c2 = 0
        t1 = 0
        PLAYERX = PLAYER
        t0 = time.time()
    if keys[pygame.K_2]:
        if c1 == 2 and c2 == 1:
            sp += 5
        if c1 == 1 and c2 == 2:
            sp1 += 5
        if c1 == 2 and c2 == 2:
            sp += 5
            sp1 += 5
        score = 0
        score1 = 0
        x = 10
        y = 10
        FPS = 60
        k += 1
        PLAYERX = PLAYER
        c1 = 0
        c2 = 0
        t1 = 0
        t0 = time.time()


    if keys[pygame.K_0]:
        k = -100
    if keys[pygame.K_0] and k < 0:
        DISPLAYSURF.fill(PINK)
        text7=font.render('GAME END',True,BLACK,PINK)
        textrect6 = text7.get_rect()
        textrect6.center = (400,400)
        DISPLAYSURF.blit(text7,textrect6)

 
   

    pygame.display.update()

pygame.quit()
sys.exit()
fpsClock.tick(FPS)

