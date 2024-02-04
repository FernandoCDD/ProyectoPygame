import pygame.image
pygame.mixer.init()

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

BOMB_SPRITE = pygame.image.load("C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/images/bomb.png")
POTION_SPRITE = pygame.image.load("C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/images/potion.png")
DIAMOND_SPRITE = pygame.image.load("C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/images/diamante.png")
O2_TANK = pygame.image.load("C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/images/O2Tank.png")

BOMB_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - 8- bit explosion sound effect ['
    'SFX] (128 kbps).mp3')

POTION_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - Undertale Sound Effect - Heal ('
    '128 kbps).mp3')

WALK_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - Single Footstep In Grass (128 '
    'kbps).mp3')

ITEM_COLLECT_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/tomp3.cc - Item collect  Sound Effect.mp3')

WIN_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - Win sound effect no copyright ('
    '128 kbps).mp3')

HIT_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - Punch Sound Effect - Gaming SFX (128 kbps).mp3')

GAME_SOUND = pygame.mixer.Sound(
    'C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/sounds/Y2meta.app - Mega Man 2 Medley 8-Bit (NES) (128 kbps).mp3')
