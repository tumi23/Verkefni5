import pygame, pygame.mixer, time
from player import Player
from bomb import Bomb
from init_level import create_walls, create_random_brick_walls, init_level_board, init_coordinates, create_random_enemies
from input_box import *
from tinydb import TinyDB, where

db = TinyDB('db/db.json')
#db.purge_table('HighScore')
table = db.table('HighScore')
#table.insert({'value': 1000, 'Name': 'MyName'})
#print(table.all())

# -- Global constants
BLACK = (255,255,255)
WHITE = (0,0,0)
GREEN = (0,150,0)
RED = (150, 0, 0)
BR_GREEN = (0, 255,0)
BR_RED = (255,0,0)
# Global variables
MAX_NO_OF_BRICKWALLS = 30
NUMBER_OF_ENEMIES_BEGINNING = 1
current_score = 0

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
pygame.display.set_caption('Bomberman')

pygame.mixer.music.load('music/32-main-theme.mp3')
pygame.mixer.music.play(-1)

def display_message(string):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(string, largeText)
    TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    pygame.time.wait(5000)



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

def start_game_two_player_game():
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

    # Creating level walls that are non-destructable
    create_walls(SCREEN_WIDTH, SCREEN_HEIGHT, wall_list, all_sprite_list)

    # 2 - is a wall, 1 - are zones not available for brickwall, 0 - are zones available, 3 = brickwall
    level = init_level_board()

    # Creating coordinates for every slot in the game level
    coordinates = init_coordinates()

    # Creating random brick walls in empty slots in level
    create_random_brick_walls(MAX_NO_OF_BRICKWALLS, wall_list, brickWall_list, all_sprite_list, level)

    # Create the player paddle object
    player1 = Player(780, 660)
    player2 = Player(60, 60)
    player1.walls = wall_list
    player2.walls = wall_list
    all_sprite_list.add(player1)
    all_sprite_list.add(player2)

    game_loop_two_player(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, player2,
              blast_list)

def start_game_one_player_game():
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

    # Creating level walls that are non-destructable
    create_walls(SCREEN_WIDTH, SCREEN_HEIGHT, wall_list, all_sprite_list)

    # 2 - is a wall, 1 - are zones not available for brickwall, 0 - are zones available, 3 = brickwall
    level = init_level_board()

    # Creating coordinates for every slot in the game level
    coordinates = init_coordinates()

    # Creating random brick walls in empty slots in level
    create_random_brick_walls(MAX_NO_OF_BRICKWALLS, wall_list, brickWall_list, all_sprite_list, level)

    # Create the player paddle object
    player1 = Player(60, 60)
    player2 = None
    player1.walls = wall_list
    all_sprite_list.add(player1)

    #Create random enemies
    enemies_list = pygame.sprite.Group()
    create_random_enemies(NUMBER_OF_ENEMIES_BEGINNING, wall_list, enemies_list, all_sprite_list, level)

    game_loop_one_player(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, enemies_list,
              blast_list, NUMBER_OF_ENEMIES_BEGINNING)

def high_score_screen():
    global table
    r = []
    for i in table.all():
        print(i['value'])
        print(i['Name'])
        r.append((i['Name'], i['value']))
    l = table.all()
    print (r)
    p = sorted(r, key=lambda x: (-x[1], x[0]))
    print(p)



    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(WHITE)
        title = pygame.font.Font('freesansbold.ttf', 115)
        t1, t2 = text_objects("Highscores", title)
        t2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 300)
        screen.blit(t1, t2)

        for i in range(10):
            try:
                string = str(p[i][0]) + ' - ' + str(p[i][1])
                score = pygame.font.Font('freesansbold.ttf', 30)
                t1, t2 = text_objects(string, score)
                t2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT) - 550 + i * 35)
                screen.blit(t1, t2)
            except:
                continue

        menu_item_button("Back", (SCREEN_WIDTH / 2) - 50, (SCREEN_HEIGHT / 2) + 300, 100, 50, RED, BR_RED, game_menu)

        pygame.display.update()
        clock.tick(15)

def quit_game():
    pygame.quit()

def game_menu():
    global  NUMBER_OF_ENEMIES_BEGINNING
    NUMBER_OF_ENEMIES_BEGINNING += 2
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        title = pygame.font.Font('freesansbold.ttf', 115)
        t1, t2 = text_objects("BomberMan", title)
        t2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)-150)
        screen.blit(t1, t2)

        #TODO one player og highscore
        menu_item_button("1 Player", (SCREEN_WIDTH / 2 )-50, (SCREEN_HEIGHT / 2)-75, 130, 50, GREEN, BR_GREEN, start_game_one_player_game)
        menu_item_button("2 Player", (SCREEN_WIDTH / 2 )-50, (SCREEN_HEIGHT / 2), 130, 50, GREEN, BR_GREEN, start_game_two_player_game)
        menu_item_button("Highscores", (SCREEN_WIDTH / 2)-50, (SCREEN_HEIGHT / 2)+75, 130, 50, GREEN, BR_GREEN, high_score_screen)
        menu_item_button("Quit", (SCREEN_WIDTH / 2)-50, (SCREEN_HEIGHT / 2)+150, 130, 50, RED, BR_RED, quit_game)


        pygame.display.update()
        clock.tick(15)



def game_loop_two_player(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, player2, blast_list):
    carryOnMyWaywardSon = True
    while carryOnMyWaywardSon:

        for b in bombs_list:
            if b.time + 3000 < pygame.time.get_ticks():
                blast = b.detonate(level, brickWall_list, all_sprite_list, player1)
                bombs_list.remove(b)
                all_sprite_list.remove(b)
                blast_list.add(blast)
                all_sprite_list.add(blast)

        for bl in blast_list:
            if bl.time + 500 < pygame.time.get_ticks():
                blast_list.remove(bl)
                all_sprite_list.remove(bl)

        blast_collision_list = pygame.sprite.spritecollide(player1, blast_list, False)
        for p in blast_collision_list:
            print("Yo player 1, yu  Dead!")
            carryOnMyWaywardSon = False
            break

        blast_collision_list = pygame.sprite.spritecollide(player2, blast_list, False)
        for p in blast_collision_list:
            print("Yo player 2, yu  Dead!")
            carryOnMyWaywardSon = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                # TODO functionize
                if event.key == pygame.K_LEFT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_SPACE:
                    bomb = Bomb(player1)
                    all_sprite_list.add(bomb)
                    bombs_list.add(bomb)
                    last_bomb_time = pygame.time.get_ticks()

                elif event.key == pygame.K_a:
                    player2.changespeed(-3, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(3, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, -3)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, 3)
                elif event.key == pygame.K_q:
                    bomb = Bomb(player2)
                    all_sprite_list.add(bomb)
                    bombs_list.add(bomb)
                    last_bomb_time = pygame.time.get_ticks()

                elif event.key == pygame.K_ESCAPE:
                    carryOnMyWaywardSon = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, -3)

                elif event.key == pygame.K_a:
                    player2.changespeed(3, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(-3, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, 3)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, -3)


        screen.blit(background, (0, 0))
        all_sprite_list.update()

        all_sprite_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)



def game_loop_one_player(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, enemies_list, blast_list, no_enemies_in_game):
    global current_score, table
    carryOnMyWaywardSon = True
    won_game = False
    no_enemies = no_enemies_in_game
    while carryOnMyWaywardSon:

        for b in bombs_list:
            if b.time + 3000 < pygame.time.get_ticks():
                blast = b.detonate(level, brickWall_list, all_sprite_list, player1)
                bombs_list.remove(b)
                all_sprite_list.remove(b)
                blast_list.add(blast)
                all_sprite_list.add(blast)

        for bl in blast_list:
            if bl.time + 500 < pygame.time.get_ticks():
                blast_list.remove(bl)
                all_sprite_list.remove(bl)

        blast_collision_list = pygame.sprite.spritecollide(player1, blast_list, False)
        for p in blast_collision_list:
            print("Yo player 1, yu  Dead!")
            carryOnMyWaywardSon = False
            break

        for blast in blast_list:
            blast_collision_enemies_list = pygame.sprite.spritecollide(blast, enemies_list, False)
            for p in blast_collision_enemies_list:
                print('ENEMY GOT HIT')
                current_score += 100
                no_enemies -= 1
                enemies_list.remove(p)
                all_sprite_list.remove(p)
                if no_enemies == 0:
                    won_game = True
                    carryOnMyWaywardSon = False

        player_enemy_collission_list = pygame.sprite.spritecollide(player1, enemies_list, False)
        for p in player_enemy_collission_list:
            print('you dead')
            carryOnMyWaywardSon = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                # TODO functionize
                if event.key == pygame.K_LEFT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_SPACE:
                    bomb = Bomb(player1)
                    all_sprite_list.add(bomb)
                    bombs_list.add(bomb)
                    last_bomb_time = pygame.time.get_ticks()
                elif event.key == pygame.K_ESCAPE:
                    carryOnMyWaywardSon = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, -3)


        screen.blit(background, (0, 0))
        all_sprite_list.update()

        all_sprite_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

        if not carryOnMyWaywardSon and not won_game:
            name_of_player = ask(screen, 'What is your name?')
            print(name_of_player)
            table.insert({'value': current_score, 'Name': name_of_player})
            current_score = 0



clock = pygame.time.Clock()

game_menu()

