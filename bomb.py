import pygame
from blast import Blast
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

class Bomb(pygame.sprite.Sprite):

    def __init__(self, player, color):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(color)
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

    def detonate(self, level, color):
        #Blast Y
        bx = self.rect.x
        by = self.rect.y
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

        x_surface_y = right[0] - left[0] + 60
        y_surface_y = 60
        x_rect_y = left[0]
        y_rect_y = left[1]

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

        x_surface_x = 60
        y_surface_x = bottom[1] - top[1] + 60
        x_rect_x = top[0]
        y_rect_x = top[1]

        return [Blast(self, x_surface_x, y_surface_x, x_rect_x, y_rect_x, color),
                Blast(self, x_surface_y, y_surface_y, x_rect_y, y_rect_y, color)]