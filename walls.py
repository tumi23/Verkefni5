import pygame

wallBlock = pygame.image.load("sprites/blocks/wall_block.png")
wallBlock = pygame.transform.scale(wallBlock, (60, 60))
brickBlock = pygame.image.load("sprites/blocks/brick_block.png")
brickBlock = pygame.transform.scale(brickBlock, (60, 60))


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.blit(wallBlock, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class BrickWall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.blit(brickBlock, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
