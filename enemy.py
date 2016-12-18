import pygame
import pygame.mixer

enemy = pygame.image.load("sprites/bomberman/bomberman_enemy.png")
enemy = pygame.transform.scale(enemy, (60, 60))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Setting the surface of the enemy and blit-ing a sprite on top of it
        self.image = pygame.Surface([60, 60])
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(enemy, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        # Adding the speed of the enemy
        self.change_x = 1
        self.change_y = 1
        self.Down = True
        self.Left = True

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

        if x == 0 or y == 0:
            self.reverse_direction()

    def update(self):
        #Left - Right
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.Left = False
                self.rect.right = block.rect.left
            else:
                self.Left = True
                self.rect.left = block.rect.right

        # Up - Down
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.Down = False
                self.rect.bottom = block.rect.top
            else:
                self.Down = True
                self.rect.top = block.rect.bottom

        if not self.Left:
            self.change_x = -1
        elif not self.Down:
            self.change_y = -1
        elif self.Left:
            self.change_x = 1
        elif self.Down:
            self.change_y = 1

    def reverse_direction(self):
            x = self.change_x
            y = self.change_y
            if x < 0:
                self.change_x = 1
            else:
                self.change_x = -1

            if y < 0:
                self.change_y = 1
            else:
                self.change_y = -1

