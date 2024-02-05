import pygame
from config import *

import pygame
from config import *


class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y, layer, groups, spritesheet, sprite_coords):
        self.game = game
        self._layer = layer
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Diamond(Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, ITEM_LAYER, (game.all_sprites, game.diamond), DIAMOND_SPRITE, (0, 0))
        image_to_load = pygame.transform.scale(DIAMOND_SPRITE, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))
class WaterPotion(Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, ITEM_LAYER, (game.all_sprites, game.potion), POTION_SPRITE, (0, 0))
        image_to_load = pygame.transform.scale(POTION_SPRITE, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))


class Bomb(Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, ITEM_LAYER, (game.all_sprites, game.bomb), BOMB_SPRITE, (0, 0))
        image_to_load = pygame.transform.scale(BOMB_SPRITE, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))


class Amulet(Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, ITEM_LAYER, (game.all_sprites, game.amulet), AMULET_SPRITE, (0, 0))
        image_to_load = pygame.transform.scale(AMULET_SPRITE, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))
