import pygame
from config import *
from models.player import *
from models.tile import *
from models.button import *
from models.items import *
import random
import sys


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(
            './fonts/8-bit-hud.ttf', 20)

        self.character_spritesheet = SpriteSheet('images/character.png')
        self.character_with_amulet_spritesheet = SpriteSheet('images/character_with_amulet.png')
        self.floor_spritesheet = SpriteSheet('images/tileset.png')
        self.water_spritesheet = SpriteSheet('images/tileset.png')
        self.wall_spritesheet = SpriteSheet('images/tileset.png')
        self.breakable_wall_spritesheet = SpriteSheet('images/tileset.png')
        self.potion_spritesheet = SpriteSheet('images/potion.png')
        self.bomb_spritesheet = SpriteSheet('images/bomb.png')
        self.diamond_spritesheet = SpriteSheet('images/diamante.png')
        self.intro_background = pygame.image.load('images/introbackground.png')
        self.death_background = pygame.image.load('images/gameover.png')

    map_file = 'mapa.txt'

    def load_map(self):
        with open('mapa.txt', 'r') as mapFile:
            itemList = mapFile.readline().strip().split(', ')
            itemListMap = {item.split(':')[0]: int(item.split(':')[1]) for item in itemList}
            result = [line.strip() for line in mapFile]
            # itemListMap = '{}'
            # for item in itemList:
            #     parts = item.split(':')
            #     if len(parts) == 2:
            #         itemListMap[parts[0]] = int(parts[1])

        return itemListMap, result

    game_items, game_map = load_map(map_file)
    print(game_items)

    def create_map(self):
        for i, row in enumerate(self.game_map):
            for j, column in enumerate(row):
                Floor(self, j, i)
                if column == "M":
                    Wall(self, j, i)
                if column == "W":
                    Water(self, j, i)
                if column == "C":
                    Player(self, j, i)
                if column == "X":
                    Breakable_wall(self, j, i)

    def load_items(self):
        for key, value in self.game_items.items():
            for randomValues in range(value):
                x = random.randint(0, len(self.game_map[0]) - 1)
                y = random.randint(0, len(self.game_map) - 1)

                while self.game_map[y][x] != ' ':
                    x = random.randint(0, len(self.game_map[0]) - 1)
                    y = random.randint(0, len(self.game_map) - 1)

                if key == "B":
                    Bomb(self, x, y)
                if key == "P":
                    WaterPotion(self, x, y)
                if key == "D":
                    Diamond(self, x, y)
                if key == "A":
                    Amulet(self, x, y)

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.wall = pygame.sprite.LayeredUpdates()
        self.breakable_wall = pygame.sprite.LayeredUpdates()
        self.water = pygame.sprite.LayeredUpdates()
        self.potion = pygame.sprite.LayeredUpdates()
        self.diamond = pygame.sprite.LayeredUpdates()
        self.bomb = pygame.sprite.LayeredUpdates()
        self.amulet = pygame.sprite.LayeredUpdates()

        self.create_map()
        self.load_items()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                health_text = f'Health: {sprite.health}'
                health = self.font.render(health_text, True, WHITE)
                self.screen.blit(health, (30, 5))

                diamonds_text = f'Diamonds: {sprite.diamonds}'
                diamonds = self.font.render(diamonds_text, True, WHITE)
                self.screen.blit(diamonds, (330, 5))

                bomb_text = f'Bombs: {sprite.bombs}'
                bomb = self.font.render(bomb_text, True, WHITE)
                self.screen.blit(bomb, (680, 5))

                oxygen_text = f'Amulet: {"ON" if sprite.amulet else "OFF"}'
                oxygen_tank = self.font.render(oxygen_text, True, WHITE)
                self.screen.blit(oxygen_tank, (920, 5))

        self.clock.tick(FPS)
        pygame.display.update()

    def events(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                self.show_exit_message()

    def death_screen(self):
        death_text = self.font.render('''You're Dead''', True, WHITE)
        death_text_rect = death_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        continue_button = Button(WIN_WIDTH / 2 - 75, WIN_HEIGHT / 2 + 50, 250, 80,
                                 WHITE, BLACK, 'Continue?', 20)

        self.all_sprites.empty()

        while self.running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if continue_button.isPressed(mouse_position, mouse_pressed):
                self.new()
                self.main()

            self.screen.fill(BLACK)
            self.screen.blit(death_text, death_text_rect)
            self.screen.blit(continue_button.image, continue_button.rect)

            pygame.display.flip()
            self.clock.tick(FPS)
            pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def intro_screen(self):
        intro = True

        title = self.font.render('Proyecto Pygame', True, BLACK)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        play_button = Button(520, 400, 200, 50, WHITE, BLACK, 'PLAY', 28)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.isPressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def show_exit_message(self):
        self.screen.fill(BLACK)

        font = pygame.font.Font(None, 30)
        text = font.render("¿Estás seguro?", True, WHITE)  # Texto blanco
        text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        self.screen.blit(text, text_rect)

        yes_text = font.render("Sí (Q)", True, WHITE)
        yes_rect = yes_text.get_rect(center=(WIN_WIDTH // 2 - 50, WIN_HEIGHT // 2 + 30))
        self.screen.blit(yes_text, yes_rect)

        no_text = font.render("No (N)", True, WHITE)
        no_rect = no_text.get_rect(center=(WIN_WIDTH // 2 + 50, WIN_HEIGHT // 2 + 30))
        self.screen.blit(no_text, no_rect)

        pygame.display.flip()

        waiting_for_confirmation = True
        while waiting_for_confirmation:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    waiting_for_confirmation = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        waiting_for_confirmation = False
                    elif event.key == pygame.K_n:
                        waiting_for_confirmation = False


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.death_screen()

pygame.quit()
sys.exit()
