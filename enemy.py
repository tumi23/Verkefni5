import pygame, math, pygame.mixer

idleDown = pygame.image.load("sprites/bomberman/bomberman_idle_down.png")
idleDown = pygame.transform.scale(idleDown, (60, 60))

class Enemy(pygame.sprite.Sprite):
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

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed