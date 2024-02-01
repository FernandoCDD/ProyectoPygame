import pygame.image

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

BOMB_SPRITE = pygame.image.load("./images/bomb.png")
POTION_SPRITE = pygame.image.load("./images/potion.png")
DIAMOND_SPRITE = pygame.image.load("./images/diamante.png")
