import pygame
from pygame.sprite import Sprite

class Vidas(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/vidas.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom