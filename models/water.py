import pygame
from config import *

class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WATER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.water_spritesheet.get_sprite(920, 160, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y