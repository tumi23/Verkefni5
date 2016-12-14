import pygame
from random import randint

# -- Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

#Global variables
MAX_NO_OF_BRICKWALLS = 0

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 780

class BlastY(pygame.sprite.Sprite):

    def __init__(self, bomb):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)


        bx = bomb.rect.x
        by = bomb.rect.y
        bi = 0
        bj = 0
        print()
        for i in range(len(coordinates)):
            if (bx, by) in coordinates[i]:
                print(coordinates[i].index((bx, by)))
                bj = coordinates[i].index((bx, by))
                bi = i

        right = coordinates[bi][bj]
        for i in range(4):
            if level[bi][bj + i] == 2 or level[bi][bj + i] == 3:
                break
            right = coordinates[bi][bj + i]

        left = coordinates[bi][bj]
        for i in range(4):
            if level[bi][bj - i] == 2 or level[bi][bj - i] == 3:
                break
            left = coordinates[bi][bj - i]


        print('left right')
        print(right)
        print(left)


        self.image = pygame.Surface([right[0]-left[0]+60, 60])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.time = pygame.time.get_ticks()

        self.rect.x = left[0]
        self.rect.y = left[1]



class BlastX(pygame.sprite.Sprite):

    def __init__(self, bomb):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)


        bx = bomb.rect.x
        by = bomb.rect.y
        bi = 0
        bj = 0
        print()
        for i in range(len(coordinates)):
            if (bx, by) in coordinates[i]:
                print(coordinates[i].index((bx, by)))
                bj = coordinates[i].index((bx, by))
                bi = i

        bottom = coordinates[bi][bj]
        for i in range(4):
            if level[bi + i][bj] == 2 or level[bi + i][bj] == 3:
                break
            bottom = coordinates[bi + i][bj]

        top = coordinates[bi][bj]
        for i in range(4):
            if level[bi - i][bj] == 2 or level[bi - i][bj] == 3:
                break
            top = coordinates[bi - i][bj]

        print('top bottom')
        print(top)
        print(bottom)

        self.image = pygame.Surface([60, bottom[1]-top[1]+60])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.time = pygame.time.get_ticks()

        self.rect.x = top[0]
        self.rect.y = top[1]


class Bomb(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        if player.rect.x % 60 == 0:
            self.rect.x = player.rect.x

            y_mod = player.rect.y % 60
            y_value = min((60 - y_mod), y_mod)
            if y_mod < 30:
                self.rect.y = player.rect.y - y_value
            else:
                self.rect.y = player.rect.y + y_value

        else:
            self.rect.y = player.rect.y

            x_mod = player.rect.x % 60
            x_value = min((60 - x_mod), x_mod)
            if x_mod < 30:
                self.rect.x = player.rect.x - x_value
            else:
                self.rect.x = player.rect.x + x_value

        print()
        print(self.rect.x)
        print(self.rect.y)
        print()
        self.time = pygame.time.get_ticks()

    def detonate(self):

        return [BlastX(self), BlastY(self)]


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([60, 60])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class BrickWall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Test')

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
wall = Wall(0, 0, 60, 780)
wall_list.add(wall)
all_sprite_list.add(wall)

#Top
wall = Wall(10, 0, 900, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

#Right
wall = Wall(SCREEN_WIDTH-60, 0, 60, 780)
wall_list.add(wall)
all_sprite_list.add(wall)

#Bottom
wall = Wall(0, SCREEN_HEIGHT-60, 900, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

#Create all walls in the middle of the board
start = 120
for i in range(6):
    gap = 0
    for j in range(6):
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
    y1 = randint(0,12)
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

all_sprite_list.add(player)

clock = pygame.time.Clock()

carryOnMyWaywardSon = True

while carryOnMyWaywardSon:

    for b in bombs_list:
        if b.time + 3000 < pygame.time.get_ticks():
            blast = b.detonate()
            bombs_list.remove(b)
            all_sprite_list.remove(b)
            blast_list.add(blast)
            all_sprite_list.add(blast)


    for bl in blast_list:
        if bl.time + 1500 < pygame.time.get_ticks():
            blast_list.remove(bl)
            all_sprite_list.remove(bl)

    blast_collision_list = pygame.sprite.spritecollide(player, blast_list, False)
    for p in blast_collision_list:
        print("Yo Dead!")
        # End Of Game
        carryOnMyWaywardSon = False
        break



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_SPACE:
                bomb = Bomb(player)
                all_sprite_list.add(bomb)
                bombs_list.add(bomb)
                last_bomb_time = pygame.time.get_ticks()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)



    all_sprite_list.update()

    screen.fill(BLACK)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()