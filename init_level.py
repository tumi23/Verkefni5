from walls import BrickWall, Wall

from random import randint
from enemy import Enemy


def create_walls(SCREEN_WIDTH, SCREEN_HEIGHT, wall_list, all_sprite_list):
    # Creating boundary walls

    # Left
    tY = 0
    while tY < 780:
        wall = Wall(0, tY, 60, 60)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        tY += 60

    # Top
    tX = 60
    while tX < 900:
        wall = Wall(tX, 0, 60, 60)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        tX += 60

    # Right
    tY = 0
    while tY < 780:
        wall = Wall(SCREEN_WIDTH - 60, tY, 60, 60)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        tY += 60

    # Bottom
    tX = 60
    while tX < 900:
        wall = Wall(tX, SCREEN_HEIGHT - 60, 60, 60)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        tX += 60

    # Create all walls in the middle of the board
    start = 120
    for i in range(6):
        gap = 0
        for j in range(5):
            wall = Wall(start, 120 + gap, 60, 60)
            wall_list.add(wall)
            all_sprite_list.add(wall)
            gap += 120
        start += 120


# Creating random brick walls in empty slots
def create_random_brick_walls(MAX_NO_OF_BRICKWALLS, wall_list, brickWall_list, all_sprite_list, level):

    numberOfBrickWalls = 0
    while numberOfBrickWalls < MAX_NO_OF_BRICKWALLS:
        x1 = randint(0, 14)
        y1 = randint(0, 12)
        if level[y1][x1] == 0:
            level[y1][x1] = 3
            brickWall = BrickWall(60 * x1, 60 * y1, 60, 60)
            brickWall_list.add(brickWall)
            wall_list.add(brickWall)
            all_sprite_list.add(brickWall)
            numberOfBrickWalls += 1


def init_level_board():
    return ([
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
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], ])


def init_coordinates():
    x, y = 0, 0
    coordinates = []
    for i in range(13):
        sub = []
        x = 0
        for j in range(15):
            sub.append((x, y))
            x += 60
        coordinates.append(sub)
        y += 60
    return coordinates


def create_random_enemies(Number_of_enemies, wall_list, enemies_list, all_sprite_list, level):

    numberOfEnemies = 0
    while numberOfEnemies < Number_of_enemies:
        x1 = randint(0, 14)
        y1 = randint(0, 12)
        if level[y1][x1] == 0:
            level[y1][x1] = 3
            enemy = Enemy(60 * x1, 60 * y1)
            enemies_list.add(enemy)
            enemy.walls = wall_list
            all_sprite_list.add(enemy)
            numberOfEnemies += 1

