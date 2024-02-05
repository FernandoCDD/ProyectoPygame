import math
import time
import pygame
from config import *


class SpriteSheet:

    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.health = 10
        self.oxygen = False
        self._layer = PLAYER_LAYER
        self.diamonds = 0
        self.bombs = 0
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.walk_animate()

        self.rect.x += self.x_change
        self.check_wall_collide('x')
        self.check_item_collide('x')
        self.check_water_collide('x')

        self.rect.y += self.y_change
        self.check_wall_collide('y')
        self.check_item_collide('y')
        self.check_water_collide('y')

        if self.diamonds == 10:
            self.win_screen()

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
            # WALK_SOUND.play()

        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
            # WALK_SOUND.play()

        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            # WALK_SOUND.play()

        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            # WALK_SOUND.play()

    def check_wall_collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

                HIT_SOUND.play()
                time.sleep(0.2)
                self.health -= 1

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

                time.sleep(0.2)
                self.health -= 1

        if self.health == 0:
            self.kill()
            self.game.playing = False

    def check_item_collide(self, direction):
        if direction == "x":

            diamond_hits = pygame.sprite.spritecollide(self, self.game.diamond, True)
            for diamond_hit in diamond_hits:
                self.diamonds += 1
                ITEM_COLLECT_SOUND.play()

            bomb_hits = pygame.sprite.spritecollide(self, self.game.bomb, True)
            for bomb_hit in bomb_hits:
                self.bombs += 1
                ITEM_COLLECT_SOUND.play()

            potion_hits = pygame.sprite.spritecollide(self, self.game.potion, True)
            for potion_hit in potion_hits:
                self.health += 5
                POTION_SOUND.play()

            o2_tank_hits = pygame.sprite.spritecollide(self, self.game.o2_tank, True)
            for o2_tank_hit in o2_tank_hits:
                self.oxygen = True
                ITEM_COLLECT_SOUND.play()

        if direction == "y":
            diamond_hits = pygame.sprite.spritecollide(self, self.game.diamond, True)
            for diamond_hit in diamond_hits:
                self.diamonds += 1

            bomb_hits = pygame.sprite.spritecollide(self, self.game.bomb, True)
            for bomb_hit in bomb_hits:
                self.bombs += 1

            potion_hits = pygame.sprite.spritecollide(self, self.game.potion, True)
            for potion_hit in potion_hits:
                self.health += 5

            o2_tank_hits = pygame.sprite.spritecollide(self, self.game.o2_tank, True)
            for o2_tank_hit in o2_tank_hits:
                self.oxygen = True

    def check_water_collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.water, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    if not self.oxygen:
                        HIT_SOUND.play()
                        time.sleep(0.2)
                        self.health -= 3
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    if not self.oxygen:
                        HIT_SOUND.play()
                        time.sleep(0.2)
                        self.health -= 3

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.water, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    if not self.oxygen:
                        HIT_SOUND.play()
                        time.sleep(0.2)
                        self.health -= 3
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    if not self.oxygen:
                        HIT_SOUND.play()
                        time.sleep(0.2)
                        self.health -= 3

        if self.health == 0:
            self.kill()
            self.game.playing = False

    def walk_animate(self):

        up_animations = [self.game.character_spritesheet.get_sprite(20, 16, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def win_screen(self):
        win_text = self.game.font.render(' You Win! ', True, WHITE)
        win_text_rect = win_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.game.screen.blit(win_text, win_text_rect)
        pygame.display.flip()
