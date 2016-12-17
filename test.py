
import pygame, pygame.mixer
from player import Player
from game_loop import game_loop
from init_level import create_walls, create_random_brick_walls, init_level_board, init_coordinates

# -- Global constants
BLACK = (255,255,255)
WHITE = (0,0,0)
GREEN = (0,150,0)
RED = (150, 0, 0)
BR_GREEN = (0, 255,0)
BR_RED = (255,0,0)
# Global variables
MAX_NO_OF_BRICKWALLS = 30

# Sprites
idleDown = pygame.image.load("sprites/bomberman/bomberman_idle_down.png")
idleDown = pygame.transform.scale(idleDown, (60, 60))
wallBlock = pygame.image.load("sprites/blocks/wall_block.png")
wallBlock = pygame.transform.scale(wallBlock, (60, 60))
brickBlock = pygame.image.load("sprites/blocks/brick_block.png")
brickBlock = pygame.transform.scale(brickBlock, (60, 60))
bomb = pygame.image.load("sprites/bomb/bomb.png")
bomb = pygame.transform.scale(bomb, (60, 60))
background = pygame.image.load("sprites/background/background.jpg")

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 780

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create Background
screen.blit(background, (0, 0))
bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

# Make the brick walls
brickWall_list = pygame.sprite.Group()

# List of all bombs
bombs_list = pygame.sprite.Group()

# List of blasts
blast_list = pygame.sprite.Group()

#Creating level walls that are non-destructable
create_walls(SCREEN_WIDTH, SCREEN_HEIGHT, wall_list, all_sprite_list)

# 2 - is a wall, 1 - are zones not available for brickwall, 0 - are zones available, 3 = brickwall
level = init_level_board()

#Creating coordinates for every slot in the game level
coordinates = init_coordinates()


#Creating random brick walls in empty slots in level
create_random_brick_walls(MAX_NO_OF_BRICKWALLS, wall_list, brickWall_list, all_sprite_list, level)

# Create the player paddle object
player1 = Player(780, 660)
player2 = Player(60, 60)
player1.walls = wall_list
player2.walls = wall_list
all_sprite_list.add(player1)
all_sprite_list.add(player2)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def menu_item_button(message, x_coordinates, y_coordinates, widht, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x_coordinates + widht > mouse[0] > x_coordinates and y_coordinates + height > mouse[1] > y_coordinates:
        pygame.draw.rect(screen, active_color, (x_coordinates, y_coordinates, widht, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color,(x_coordinates, y_coordinates, widht, height))

    text = pygame.font.Font("freesansbold.ttf",20)
    t1, t2 = text_objects(message, text)
    t2.center = ( (x_coordinates + (widht / 2)), (y_coordinates + (height / 2)) )
    screen.blit(t1, t2)

def start_game():
    game_loop(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, player2,
              blast_list)

def quit_game():
    pygame.quit()

def game_menu():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        title = pygame.font.Font('freesansbold.ttf', 115)
        t1, t2 = text_objects("BomberMan", title)
        t2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(t1, t2)

        menu_item_button("1 Player", 150, 450, 100, 50, GREEN, BR_GREEN, start_game)
        menu_item_button("VS Game", 550, 450, 100, 50, RED, BR_RED, quit_game)

        pygame.display.update()
        clock.tick(15)

clock = pygame.time.Clock()

game_menu()

