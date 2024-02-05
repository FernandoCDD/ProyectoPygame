import pygame.image
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

WIN_WIDTH = 1245
WIN_HEIGHT = 673
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 5
ITEM_LAYER = 4
WALL_LAYER = 3
WATER_LAYER = 2
FLOOR_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

BOMB_SPRITE = pygame.image.load("images/bomb.png")
POTION_SPRITE = pygame.image.load("./images/potion.png")
DIAMOND_SPRITE = pygame.image.load("./images/diamante.png")
AMULET_SPRITE = pygame.image.load("./images/amulet.png")

BOMB_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - 8- bit explosion sound effect ['
    'SFX] (128 kbps).mp3')

POTION_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - Undertale Sound Effect - Heal ('
    '128 kbps).mp3')

WALK_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - Single Footstep In Grass (128 '
    'kbps).mp3')

ITEM_COLLECT_SOUND = pygame.mixer.Sound(
    'sounds/tomp3.cc - Item collect  Sound Effect.mp3')

WIN_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - Win sound effect no copyright ('
    '128 kbps).mp3')

HIT_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - Punch Sound Effect - Gaming SFX (128 kbps).mp3')

GAME_SOUND = pygame.mixer.Sound(
    'sounds/Y2meta.app - Mega Man 2 Medley 8-Bit (NES) (128 kbps).mp3')
