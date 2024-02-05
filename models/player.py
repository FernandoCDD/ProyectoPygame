import datetime
import math
import time
import pygame
from config import *
from models import tile


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
        self.t_pressed = False
        self.amulet_suit = False
        self.game = game
        self.health = 10
        self.amulet = False
        self._layer = PLAYER_LAYER
        self.diamonds = 0
        self.bombs = 0
        self.end_time = None
        self.start_time = datetime.datetime.now()
        self.score = 0
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
        self.throw_bomb()
        self.change_suit()

        if self.amulet_suit:
            self.walk_animate_with_amulet()
        else:
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
            self.end_time = datetime.datetime.now()
            time = self.end_time - self.start_time
            self.score = (10 * 1000) - (time.total_seconds() * 10) + (self.health * 50)
            self.save_score()
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
        all_wall_sprites = pygame.sprite.Group()
        all_wall_sprites.add(self.game.wall, self.game.breakable_wall)

        if direction == "x":
            hits = pygame.sprite.spritecollide(self, all_wall_sprites, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

                HIT_SOUND.play()
                time.sleep(0.2)
                self.health -= 1

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, all_wall_sprites, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

                HIT_SOUND.play()
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

            amulet_hits = pygame.sprite.spritecollide(self, self.game.amulet, True)
            for amulet_hit in amulet_hits:
                self.amulet = True
                ITEM_COLLECT_SOUND.play()

        if direction == "y":
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

            amulet_hits = pygame.sprite.spritecollide(self, self.game.amulet, True)
            for amulet_hit in amulet_hits:
                self.amulet = True
                ITEM_COLLECT_SOUND.play()
                ITEM_COLLECT_SOUND.play()

    def check_water_collide(self, direction):
        if not self.amulet:
            next_rect = self.rect.copy()

            if direction == "x":
                next_rect.x += self.x_change
            elif direction == "y":
                next_rect.y += self.y_change

            water_hits = pygame.sprite.spritecollide(self, self.game.water, False)

            for water_hit in water_hits:
                if water_hit.rect.colliderect(next_rect):
                    time.sleep(0.1)
                    self.health -= 3

                    if self.health <= 0:
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

    def walk_animate_with_amulet(self):

            up_animations = [self.game.character_with_amulet_spritesheet.get_sprite(20, 16, self.width, self.height),
                             self.game.character_with_amulet_spritesheet.get_sprite(35, 34, self.width, self.height),
                             self.game.character_with_amulet_spritesheet.get_sprite(68, 34, self.width, self.height)]

            down_animations = [self.game.character_with_amulet_spritesheet.get_sprite(3, 2, self.width, self.height),
                               self.game.character_with_amulet_spritesheet.get_sprite(35, 2, self.width, self.height),
                               self.game.character_with_amulet_spritesheet.get_sprite(68, 2, self.width, self.height)]

            left_animations = [self.game.character_with_amulet_spritesheet.get_sprite(3, 98, self.width, self.height),
                               self.game.character_with_amulet_spritesheet.get_sprite(35, 98, self.width, self.height),
                               self.game.character_with_amulet_spritesheet.get_sprite(68, 98, self.width, self.height)]

            right_animations = [self.game.character_with_amulet_spritesheet.get_sprite(3, 66, self.width, self.height),
                                self.game.character_with_amulet_spritesheet.get_sprite(35, 66, self.width, self.height),
                                self.game.character_with_amulet_spritesheet.get_sprite(68, 66, self.width, self.height)]

            if self.facing == "down":
                if self.y_change == 0:
                    self.image = self.game.character_with_amulet_spritesheet.get_sprite(3, 2, self.width, self.height)
                else:
                    self.image = down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

            if self.facing == "up":
                if self.y_change == 0:
                    self.image = self.game.character_with_amulet_spritesheet.get_sprite(3, 34, self.width, self.height)
                else:
                    self.image = up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

            if self.facing == "left":
                if self.x_change == 0:
                    self.image = self.game.character_with_amulet_spritesheet.get_sprite(3, 98, self.width, self.height)
                else:
                    self.image = left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop >= 3:
                        self.animation_loop = 1

            if self.facing == "right":
                if self.x_change == 0:
                    self.image = self.game.character_with_amulet_spritesheet.get_sprite(3, 66, self.width, self.height)
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

    def throw_bomb(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_b] and self.bombs >= 1:
            explosion = TILESIZE * 2
            self.bombs -= 1

            for sprite in self.game.all_sprites:
                if isinstance(sprite, tile.Breakable_wall):
                    x_position = sprite.rect.x
                    y_position = sprite.rect.y
                    distance = pygame.math.Vector2(x_position - self.rect.x, y_position - self.rect.y).length()

                    if distance <= explosion:
                        sprite.kill()
                        BOMB_SOUND.play()

            pygame.time.delay(200)

    def change_suit(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and not self.t_pressed and self.amulet:
            self.amulet_suit = not self.amulet_suit
            self.t_pressed = True

        elif not keys[pygame.K_t]:
            self.t_pressed = False

    def save_score(self):
        with open("score.txt", "a") as file:
            file.write(f"{self.score}\n")
