import pygame

player = pygame.image.load("sprites/bomberman/bomberman.png")
player = pygame.transform.scale(player, (60, 60))

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([60, 60])
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.image.set_colorkey((255, 0, 255))
        self.image.blit(player, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        # Changes the speed of the character if needed left or right
        self.rect.x += self.change_x
        # Checks for collision on the walls when walking left or right
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        # Changes the speed of the character if needed up or down
        self.rect.y += self.change_y
        # Checks for collision on the walls when walking up or down
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


