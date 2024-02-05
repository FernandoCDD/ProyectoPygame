import pygame
from config import *

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('C:/Users/ferna/OneDrive/Escritorio/2ºDAM/SGE/ProyectoPygame/fonts/8-bit-hud.ttf',
                                     fontsize)
        self.content = content

        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.text_rect = self.image.get_rect(center=(self.width / 2 + 25, self.height / 2))

        self.update_text()

    def update_text(self):
        self.text = self.font.render(self.content, True, self.fg)
        self.image.fill(self.bg)
        self.image.blit(self.text, self.text_rect)

    def isPressed(self, pos, pressed):
        return self.rect.collidepoint(pos) and pressed[0]
