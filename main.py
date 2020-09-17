import pygame
import random
from pygame import mixer
# intialize the pygame
pygame.init()
# create a screen
screen = pygame.display.set_mode((800, 600))
backgraund = pygame.image.load('backpackbig.png')
mixer.music.load('Eminem - Rap God (Explicit) [Official Video].wav')

# title and icon
pygame.display.set_caption("M.I war")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# caracterse
player1 = pygame.image.load('man64.png')
playerimg = player1
playerX = 370
playerY = 500
playerX_change = 0
playerBoost = 0
skin = playerimg


def Player(x, y, skin):
    screen.blit(skin, (x, y))


# enemy ['binary-code.png','the-sum-of-mathematical-symbol.png']
enemy1 = pygame.image.load('binary-code.png')
enemy2 = pygame.image.load('the-sum-of-mathematical-symbol.png')
enemy3 = pygame.image.load('f(x).png')
enemy4 = pygame.image.load('data.png')
enemy5 = pygame.image.load('css.png')
enemy6 = pygame.image.load('infinite-mathematical-symbol.png')
enemy7 = pygame.image.load('code.png')
enemy8 = pygame.image.load('calculature.png')
enemyimg = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
z = random.randint(0, 7)
enemyX = random.randint(20, 736)
enemyY = -100
enemy_change = 0
defc = 0.5


def Enemy(x, y, z, w):
    screen.blit(enemyimg[z], (x, y))
    return y + w


# score
score = 0
font = pygame.font.Font('Australove.ttf', 40)

textX = 10
testY = 10


def show_score(x, y, score, scoreMAX):
    score = font.render("Score : " + str(score), True, (0, 0, 0))
    scoreMAX = font.render("Best Score : " + str(scoreMAX), True, (255, 255, 255))
    screen.blit(score, (x, y))
    screen.blit(scoreMAX, (x, y + 40))


# game loop
left = False
right = False

running = True
gameON = False
while running:
    # rad green blue
    screen.fill((175, 155, 155))
    screen.blit(backgraund, (280, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.play()
                gameON = True
            # if keystroke is pressed check whether its right or left
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -2
                left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 2
                right = True
            # if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # playerX_change = 0
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_KP0:
                if playerX_change <= -1:
                    playerBoost = -3
                else:
                    playerBoost = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_KP0:
                playerBoost = 0
            # if (event.key == pygame.K_a or event.key == pygame.K_LEFT ) and right == False or ( event.key == pygame.K_d or event.key == pygame.K_RIGHT) and left == False:
            # playerX_change = 0
            if event.key == pygame.K_a and right == False or event.key == pygame.K_d and left == False:
                playerX_change = 0
    left = False
    right = False
    if gameON == True:

        playerX = playerX + playerBoost + playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        if enemyY >= 500:
            if enemyX >= playerX - 100 and enemyX <= playerX + 100:
                if defc < 2:
                    defc += 0.05
                else:
                    defc += 0.01
                score += 1
            else:
                gameON = False
                mixer.music.pause()
                print(score)
                if score > int(scoreMAX):
                    scoreMAXfile = open('scoreMAX.txt', 'w')
                    scoreMAXfile.write(str(score))
                    scoreMAXfile.close()

                score = 0
                defc = 0.5
            enemyY = -100
            enemyX = random.randint(20, 736)
            z = random.randint(0, 7)
        enemyY = Enemy(enemyX, enemyY, z, defc)
        Player(playerX, playerY, skin)
        scoreMAXfile = open('scoreMAX.txt', 'r')
        scoreMAX = scoreMAXfile.read()
        show_score(textX, testY, score, scoreMAX)

    pygame.display.update()
