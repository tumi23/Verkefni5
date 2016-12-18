import pygame, pygame.mixer

from walls import BrickWall
from player import Player

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


class BlastY(pygame.sprite.Sprite):

    def __init__(self, bomb, level, brickWall_list, all_sprite_list, player):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)


        bx = bomb.rect.x
        by = bomb.rect.y
        bi = 0
        bj = 0
        for i in range(len(coordinates)):
            if (bx, by) in coordinates[i]:
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
                        player.walls.remove(brick)
                        level[bi][bj + i] = 0
                break
            right = coordinates[bi][bj + i]

        left = coordinates[bi][bj]
        for i in range(4):
            if level[bi][bj - i] == 2:
                break
            if level[bi][bj - i] == 3:
                ts = str(coordinates[bi][bj - i])
                ts = ts[1:-1]
                ts = ts.split(',')
                for brick in brickWall_list:
                    if brick.rect.x == int(ts[0]) and brick.rect.y == int(ts[1][1:]):
                        all_sprite_list.remove(brick)
                        player.walls.remove(brick)
                        level[bi][bj - i] = 0
                break
            left = coordinates[bi][bj - i]

        print('left')
        print (left)
        print('right')
        print(right)

        print(coordinates)

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

    def __init__(self, bomb, level, brickWall_list, all_sprite_list, player):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)


        bx = bomb.rect.x
        by = bomb.rect.y
        bi = 0
        bj = 0
        for i in range(len(coordinates)):
            if (bx, by) in coordinates[i]:
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
                        player.walls.remove(brick)
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
                        player.walls.remove(brick)
                        level[bi - i][bj] = 0
                break
            top = coordinates[bi - i][bj]

        print('top')
        print(top)
        print('bottom')
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
