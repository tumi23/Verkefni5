import pygame, pygame.mixer
from random import randint

# -- Global constants

#Global variables
MAX_NO_OF_BRICKWALLS = 30

#Sprites
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
            if level[bi][bj + i] == 2:
                break
            if level[bi][bj + i] == 3:
                ts = str(coordinates[bi][bj + i])
                ts = ts[1:-1]
                ts = ts.split(',')
                for brick in brickWall_list:
                    if brick.rect.x == int(ts[0]) and brick.rect.y == int(ts[1][1:]):
                        all_sprite_list.remove(brick)
                        player1.walls.remove(brick)
                        level[bi][bj + i] = 0
                break
            right = coordinates[bi][bj + i]

        left = coordinates[bi][bj]
        for i in range(4):
            if level[bi][bj - i] == 2:
                break
            if level[bi][bj - i] == 3:
                ts = str(coordinates[bi][bj - 1])
                ts = ts[1:-1]
                ts = ts.split(',')
                for brick in brickWall_list:
                    if brick.rect.x == int(ts[0]) and brick.rect.y == int(ts[1][1:]):
                        all_sprite_list.remove(brick)
                        player1.walls.remove(brick)
                        level[bi][bj - i] = 0
                break
            left = coordinates[bi][bj - i]


        print('left right')
        print(right)
        print(left)


        self.image = pygame.Surface([right[0]-left[0]+60, 60])
        blastY = pygame.image.load("sprites/bomb/blastY.png")
        blastY = pygame.transform.scale(blastY, ([right[0]-left[0]+60, 60]))
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(blastY, (0, 0))
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
            if level[bi + i][bj] == 2:
                break
            if level[bi + i][bj] == 3:
                ts = str(coordinates[bi + i][bj])
                ts = ts[1:-1]
                ts = ts.split(',')
                for brick in brickWall_list:
                    if brick.rect.x == int(ts[0]) and brick.rect.y == int(ts[1][1:]):
                        all_sprite_list.remove(brick)
                        player1.walls.remove(brick)
                        level[bi + i][bj] = 0
                break
            bottom = coordinates[bi + i][bj]

        top = coordinates[bi][bj]
        for i in range(4):
            if level[bi - i][bj] == 2:
                break
            if level[bi - i][bj] == 3:
                ts = str(coordinates[bi - i][bj])
                ts = ts[1:-1]
                ts = ts.split(',')
                for brick in brickWall_list:
                    if brick.rect.x == int(ts[0]) and brick.rect.y == int(ts[1][1:]):
                        all_sprite_list.remove(brick)
                        player1.walls.remove(brick)
                        level[bi - i][bj] = 0
                break
            top = coordinates[bi - i][bj]

        print('top bottom')
        print(top)
        print(bottom)

        self.image = pygame.Surface([60, bottom[1]-top[1]+60])
        blastX = pygame.image.load("sprites/bomb/blastX.png")
        blastX = pygame.transform.scale(blastX, ([60, bottom[1]-top[1]+60]))
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(blastX, (0, 0))
        self.rect = self.image.get_rect()
        self.time = pygame.time.get_ticks()

        self.rect.x = top[0]
        self.rect.y = top[1]

class Bomb(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        bomb = pygame.image.load("sprites/bomb/bomb.png")
        bomb = pygame.transform.scale(bomb, (60, 60))
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(bomb, (0, 0))
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
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(idleDown, (0, 0))

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
        self.image.blit(wallBlock, (0, 0))

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
        self.image.blit(brickBlock, (0, 0))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# Call this function so the Pygame library can initialize itself
pygame.init()
while (True):
    class GameMenu():
        def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                        font_color=(255, 255, 255)):
            self.screen = screen
            self.scr_width = self.screen.get_rect().width
            self.scr_height = self.screen.get_rect().height
     
            self.bg_color = bg_color
            self.clock = pygame.time.Clock()
     
            self.items = items
            self.font = pygame.font.SysFont(font, font_size)
            self.font_color = font_color
     
            self.items = []
            for index, item in enumerate(items):
                label = self.font.render(item, 1, font_color)
     
                width = label.get_rect().width
                height = label.get_rect().height
     
                posx = (self.scr_width / 2) - (width / 2)
                # t_h: total height of text block
                t_h = len(items) * height
                posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
     
                self.items.append([item, label, (width, height), (posx, posy)])
     
        def run(self):
            mainloop = True
            while mainloop:
                # Limit frame speed to 50 FPS
                self.clock.tick(50)
     
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mainloop = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            mainloop = False
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            
                            break
                # Redraw the background
                self.screen.fill(self.bg_color)
                screen.blit(background, (0, 0))
     
                for name, label, (width, height), (posx, posy) in self.items:
                    self.screen.blit(label, (posx, posy))
     
                pygame.display.flip()
     
     
    if __name__ == "__main__":
        # Creating the screen
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], 0, 32)
     
        menu_items = ('Press Space to start', 'Press Esc to Quit')
     
        pygame.display.set_caption('Game Menu')
        gm = GameMenu(screen, menu_items)
        gm.run()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Create Background
    screen.blit(background,(0,0))
    bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))


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
    player1 = Player(780, 660)
    player2 = Player(60,60)
    player1.walls = wall_list
    player2.walls = wall_list
    all_sprite_list.add(player1)
    all_sprite_list.add(player2)

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
            if bl.time + 500 < pygame.time.get_ticks():
                blast_list.remove(bl)
                all_sprite_list.remove(bl)

        blast_collision_list = pygame.sprite.spritecollide(player1, blast_list, False)
        for p in blast_collision_list:
            print(p)
            print("Yo player 1, yu Dead!")
            # End Of Game
            carryOnMyWaywardSon = False
            break
        blast_collision_list = pygame.sprite.spritecollide(player2, blast_list, False)
        for p in blast_collision_list:
            print(p)
            print("Yo player 2, yu  Dead!")
            # End Of Game
            carryOnMyWaywardSon = False
            mainloop = True
            break



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                #TODO functionize
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

pygame.quit()
