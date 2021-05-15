import pygame
import sys
import random
from time import sleep

Black = (0, 0, 0)
padWidth = 480
padHeight = 640
rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png', 'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png', 'rock11.png',
'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png', 'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png', 'rock21.png', 'rock22.png', 'rock23.png',
'rock24.png', 'rock25.png', 'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def initGame():
    global gamePad, clock, background, flight, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load("background.png")
    flight = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    clock = pygame.time.Clock()

def runGame():
    global gapdPad, Clock, background, flight, missile

    #전투기 사이즈 : 여기서 flightsize라는 변수가 global로 선언 안해줘도 영상에서는 되는데 나는 왜 안되지?..
    flightSize = flight.get_rect().size
    flightWidth = flightSize[0]
    flightHeight = flightSize[1]

    #전투기 처음 위치!
    x = padWidth * 0.45
    y = padHeight * 0.9
    flightX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rocksize[0]
    rockHeight = rocksize[1]

    rockX = random.randrage(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 4

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:     #왼쪽으로 이동
                    flightX -= 5

                elif event.key == pygame.K_RIGHT:     #오른 으로 이동
                    flightX += 5

                elif event.type == pygame.K_SPACE:
                    missileX = x + flightWidth/2 #미사일 발사시 전투기 중간에서 나가게
                    missileY = y - flightHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:     # 멈춤(방향키 뗌)
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    flightX = 0

        drawObject(background, 0, 0)

        #전투기 위치 재조정(왼쪽 or 오른쪽 화면밖으로 못가게)
        x += flightX
        if x < 0 :
            x = 0
        elif x > padWidth - flightWidth:
            x = padWidth - flightWidth

        drawObject(flight, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


initGame()
runGame()
