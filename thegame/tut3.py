# Code by jay kumar follow on twitter and linkedin..
import pygame
import random

pygame.init()
# creating a window screen
screen = pygame.display.set_mode((700,600))
#creating the icon title and background
pygame.display.set_caption("Space invades")
icon = pygame.image.load("../../sanke the game/snake game/backgroundpic.jpg")
pygame.display.set_icon(icon)
#player bg image adding
playerImg = pygame.image.load("space-invaders.png")
playerX = 350
playerY = 480
playerX_change = 0
# make the enemy or monster boundaring and adding the image
monsterImg = pygame.image.load("monster.png")
monsterX = random.randint(0,800)
monsterY = random.randint(50,150)
monsterX_change = 0.3
monsterY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y ))
def monster(x,y):
    screen.blit(monsterImg,(x,y ))

# we created the exit button working on while loop
running = True
while running:

    # RGB = R - RED AND G - GREEN AND B - BLUE
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystrokes is pressed so check weather it's left or right ..
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.K_UP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerX_change = 0

# player boundary algorithm
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 640:
        playerX = 640

    # enemy movement
# checking for boundaries for enemy that's enemy can't go any where from the boundaries
    monsterX += monsterX_change
    if monsterX <= 0:
        monsterX = 0.3
    elif monsterX >= 640:
        monsterX = -0.3




    player(playerX, playerY)
    monster(monsterX, monsterY)
    pygame.display.update()
