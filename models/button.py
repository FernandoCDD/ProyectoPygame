import pygame
from config import *


class Button:

    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font(
            'C:/Users/claro.defer21_triana/Documents/2ºDAM/SGE/ProyectoPygame/fonts/8-bit-hud.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.imageRect = self.image.get_rect()

        self.imageRect.x = self.x
        self.imageRect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.textRect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.textRect)

    def isPressed(self, mouse_pos, mouse_pressed):
        if self.textRect.collidepoint(mouse_pos):
            if mouse_pressed[0]:
                return True
            return False
        return False
