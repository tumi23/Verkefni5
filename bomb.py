import pygame, pygame.mixer

from blast import BlastX, BlastY

bomb = pygame.image.load("sprites/bomb/bomb.png")
bomb = pygame.transform.scale(bomb, (60, 60))

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

        self.time = pygame.time.get_ticks()

    def detonate(self, level, brickWall_list, all_sprite_list, player):

        return [BlastX(self, level, brickWall_list, all_sprite_list, player), BlastY(self, level, brickWall_list, all_sprite_list, player)]



