import pygame
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, layer, groups, spritesheet, sprite_coords):
        self.game = game
        self._layer = layer
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.image = spritesheet.get_sprite(*sprite_coords, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Floor(Tile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, FLOOR_LAYER, game.all_sprites, game.floor_spritesheet, (254, 352))


class Wall(Tile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, WALL_LAYER, (game.all_sprites, game.wall), game.wall_spritesheet, (960, 448))


class Breakable_wall(Tile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, WALL_LAYER, (game.all_sprites, game.breakable_wall), game.wall_spritesheet,
                         (990, 542))


class Water(Tile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, WATER_LAYER, game.all_sprites, game.water_spritesheet, (920, 160))
