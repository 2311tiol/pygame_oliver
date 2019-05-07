#imports
import pygame
import sys
import random
import time

#initialisering
pygame.mixer.pre_init(44100, -16, 2, 2000)
pygame.mixer.init()
pygame.init()

#oppsett av skjerm parametere (dette er bare å endre på dersom skjermen blir for stor eller for liten)
display_width= 1400
display_height= 800

#definering av farger
white = (255,255,255)
black = (0,0,0)
green = (124,252,0)

pipecolor = (34, 139, 34)
blue = (0,191,255)

#score teller
counter = 0

#oppsett av display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')
clock= pygame.time.Clock()

#oppsett av font
font = pygame.font.SysFont(None, 72)

#definering av funksjoner
def end():
    pygame.display.update()
    clock.tick(60)

x = 575
y = 500

def ball(x,y):
    pygame.draw.circle(gameDisplay, ((black)), [x,y], 35)

x1 = 1500

def drawBarrier(x1):
    pygame.draw.rect(gameDisplay, ((pipecolor)), pygame.Rect(x1, 0, 100, 1750))

x2 = 1650
y1 = random.choice([100, 255, 450, 575, 650])

def drawHole(x1, y1):
    pygame.draw.rect(gameDisplay, ((blue)), pygame.Rect(x1, y1, 100, 200))
y2 = 500

def drawGround():
    pygame.draw.rect(gameDisplay, ((green)), pygame.Rect(0, 895, 1750, 100))

def drawSky():
    pygame.draw.rect(gameDisplay, ((blue)), pygame.Rect(0,0,1750,900))

#oppsett av sjekking quit()
done = False

checker = True

#starten på while loop
while not done: 

    #will avslutte lopp hvis bruxer X failer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #definering av rektangler for kollisjons deteksjon
    ball_rect = pygame.Rect(x, y, 35, 35)

    barrier_rect = pygame.Rect(x1, 0, 100, 1750)

    hole_rect = pygame.Rect(x1, y1, 100, 200)

    topBarrier_rect = pygame.Rect(x1, 0, 100, y1)

    bottomBarrier_rect = pygame.Rect(x1, y1 + 200, 100, 1200)

    invisibleBarrier_rect = pygame.Rect(0, 0, 5, 1275.)

    ground_rect = pygame.Rect(0, 895, 1750, 100)

    text1 = font.render(str(counter/10), True, ((white)))

    #slutter hvis spiller treffer bakken/pipe
    if ball_rect.colliderect(bottomBarrier_rect) or ball_rect.colliderect(topBarrier_rect):
        break

    if ball_rect.colliderect(ground_rect):
        break

    #hvis man kommer gjennom pipa counter + 1
    if ball_rect.colliderect(hole_rect):
        while checker:
            checker = False
        counter = counter + 1
    
    
    pressed = pygame.key.get_pressed()


    #default ball går ned
    y_change = 6

    #hvis space blir blir tastet, ballen går opp
    if pressed[pygame.K_SPACE]:
        y_change = -7

    #skifter y deretter
    y = y_change + y

    #bakgrunn, spiller, bakke, score, hindringer etc
    gameDisplay.fill((white))

    drawSky()

    drawBarrier(x1)

    drawHole(x1, y1)

    x1 = x1 - 13

    #genererer en ny pipe etter den treffer "den usynlige veggen"
    if invisibleBarrier_rect.colliderect(bottomBarrier_rect) or invisibleBarrier_rect.colliderect(topBarrier_rect):
        x1 = 1650
        y1 = random.choice([100, 225, 450, 575, 650])
        drawBarrier(x1)
        drawHole(x1, y1)

    drawGround()

    ball(x,y)

    gameDisplay.blit(text1,
        (610 - text1.get_width() // 2, 50 - text1.get_height() // 2))

    pygame.display.flip()

    end()

text = font.render("Du tapte! Poengsummen er " + str(counter/10), True, ((black)))

#end skjerm
while not done: 
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            done = True

    gameDisplay.fill((white))

    gameDisplay.blit(text,
        (610 - text.get_width() // 2, 500 - text.get_height() // 2))
    pygame.display.flip()

    end()

pygame.quit()
quit()
