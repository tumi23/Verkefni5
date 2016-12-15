import pygame

class Blast(pygame.sprite.Sprite):

    def __init__(self, bomb, x_surface, y_surface, x_rect, y_rect, color):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([x_surface, y_surface])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.time = pygame.time.get_ticks()

        self.rect.x = x_rect
        self.rect.y = y_rect


'''
class BlastX(pygame.sprite.Sprite):

    def __init__(self, bomb, x_surface, y_surface, x_rect, y_rect, color):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([x_surface, y_surface])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.time = pygame.time.get_ticks()

        self.rect.x = x_rect
        self.rect.y = y_rect'''
