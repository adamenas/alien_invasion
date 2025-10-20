import pygame.font
from pygame.sprite import Group
from vidas import Vidas
from pathlib import Path

class Pontuacao:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30, 30,30)
        self.font = pygame.font.SysFont(None, 24)
        self.prep_score()
        self.prep_high_score()
        self.prep_nivel()
        self.prep_vidas()
    

    def prep_vidas(self):
        self.vidas = Group()
        for numero_vidas in range(self.stats.ships_left):
            vida = Vidas(self.ai_game)
            vida.rect.x = 10 + numero_vidas * vida.rect.width
            vida.rect.y = 10
            self.vidas.add(vida)
    

    def prep_score(self):
        arredondado = round(self.stats.score, -1)
        score_str = f'pontos: {arredondado:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        high_score = round(int(self.stats.high_score), -1)
        high_score_str = f'recorde: {high_score:,}'
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_nivel(self):
        nivel_str = f'Nível: {self.stats.nivel}'
        self.nivel_image = self.font.render(nivel_str, True, self.text_color, self.settings.bg_color)
        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.right = self.score_rect.right
        self.nivel_rect.top = self.score_rect.bottom + 10

    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.nivel_image, self.nivel_rect)
        self.vidas.draw(self.screen)
        self.screen.blit(self.high_score_image, self.high_score_rect)
    

    def check_high_score(self):
        recorde = Path('recorde.txt')
        if int(self.stats.score) > int(self.stats.high_score):
            self.stats.high_score = self.stats.score
            recorde.write_text(str(self.stats.high_score))
            self.prep_high_score()