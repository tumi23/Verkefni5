import pygame, pygame.mixer
from random import randint
import math

from bomb import Bomb
from player import Player
from walls import BrickWall, Wall
from enemy import Enemy

# -- Global constants

#Global variables
MAX_NO_OF_BRICKWALLS = 30

#Sprites
background = pygame.image.load("sprites/background/background.jpg")

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 780


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create Background
screen.blit(background,(0,0))
bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption('BomberMan')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

#Make the brick walls
brickWall_list = pygame.sprite.Group()

#List of all bombs
bombs_list = pygame.sprite.Group()

#List of blasts
blast_list = pygame.sprite.Group()


#Left
tY = 0
while tY < 780:
    wall = Wall(0, tY, 60, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    tY += 60

#Top
tX = 60
while tX < 900:
    wall = Wall(tX, 0, 60, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    tX += 60

#Right
tY = 0
while tY < 780:
    wall = Wall(SCREEN_WIDTH-60, tY, 60, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    tY += 60

#Bottom
tX = 60
while tX < 900:
    wall = Wall(tX, SCREEN_HEIGHT-60, 60, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    tX += 60

#Create all walls in the middle of the board
start = 120
for i in range(6):
    gap = 0
    for j in range(5):
        wall = Wall(start, 120+gap, 60, 60)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        gap += 120
    start += 120

# 2 - is a wall, 1 - are zones not available for brickwall, 0 - are zones available, 3 = brickwall
level = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
    [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
    [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], ]

x, y = 0, 0
coordinates = []
for i in range(13):
    sub = []
    x = 0
    for j in range(15):
        sub.append((x,y))
        x += 60
    coordinates.append(sub)
    y += 60

for i in coordinates:
    print(i)

#Creating random brick walls in empty slots
numberOfBrickWalls = 0
while numberOfBrickWalls < MAX_NO_OF_BRICKWALLS:
    x1 = randint(0, 14)
    y1 = randint(0, 12)
    if level[y1][x1] == 0:
        level[y1][x1] = 3
        brickWall = BrickWall(60*x1, 60*y1, 60, 60)
        brickWall_list.add(brickWall)
        wall_list.add(brickWall)
        all_sprite_list.add(brickWall)
        numberOfBrickWalls += 1


# Create the player paddle object
player = Player(60, 60)
player.walls = wall_list


#Create Enemy
enemy = Enemy(60,60)
enemy.walls = wall_list

all_sprite_list.add(enemy)


all_sprite_list.add(player)

clock = pygame.time.Clock()

carryOnMyWaywardSon = True

while carryOnMyWaywardSon:

    for b in bombs_list:
        if b.time + 3000 < pygame.time.get_ticks():
            blast = b.detonate(level, brickWall_list, all_sprite_list, player)
            bombs_list.remove(b)
            all_sprite_list.remove(b)
            blast_list.add(blast)
            all_sprite_list.add(blast)


    for bl in blast_list:
        if bl.time + 500 < pygame.time.get_ticks():
            blast_list.remove(bl)
            all_sprite_list.remove(bl)

    blast_collision_list = pygame.sprite.spritecollide(player, blast_list, False)
    for p in blast_collision_list:
        print("Yo Dead!")
        # End Of Game
        carryOnMyWaywardSon = False
        break

    for b in bombs_list:
        bomb_blast_list = pygame.sprite.spritecollide(b, blast_list, False)
        for p in blast_collision_list:
            print("Yo Dead!")
            p.detonte()
            # End Of Game
            carryOnMyWaywardSon = False
            break



    #enemy.move_towards_player(player)

    for event in pygame.event.get():
        print()
        print ('for event loop')

        if event.type == pygame.QUIT:
            carryOnMyWaywardSon = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print()
                print('down-left')
                player.changespeed(-3, 0,'LL')
            elif event.key == pygame.K_RIGHT:
                print()
                print('down-right')
                player.changespeed(3, 0,'RR')
            elif event.key == pygame.K_UP:
                print()
                print('down-up')
                player.changespeed(0, -3,'UU')
            elif event.key == pygame.K_DOWN:
                print()
                print('down-down')
                player.changespeed(0, 3, 'DD')
            elif event.key == pygame.K_SPACE:
                bomb = Bomb(player)
                all_sprite_list.add(bomb)
                bombs_list.add(bomb)
                last_bomb_time = pygame.time.get_ticks()
            elif event.key == pygame.K_ESCAPE:
                carryOnMyWaywardSon = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print()
                print('up-left')
                player.changespeed(3, 0,'')
            elif event.key == pygame.K_RIGHT:
                print()
                print('up-right')
                player.changespeed(-3, 0,'')
            elif event.key == pygame.K_UP:
                print()
                print('up-up')
                player.changespeed(0, 3,'')
            elif event.key == pygame.K_DOWN:
                print()
                print('up-down')
                player.changespeed(0, -3,'')
            elif event.key == pygame.K_ESCAPE:
                carryOnMyWaywardSon = False

    screen.blit(background, (0, 0))
    all_sprite_list.update()

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()