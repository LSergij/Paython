import pygame
from pygame.sprite import Sprite


class Bullet (Sprite):
    def __init__(self,game_settings,screen,player1,player2):
        super().__init__()

        self.rect = pygame.Rect(0,0, game_settings.bullets_width, game_settings.bullets_height)
        self.rect.top = player1.rect.top
        self.rect.top = player2.rect.top

        self.rect.centerx = player1.rect.centerx
        self.rect.centerx = player2.rect.centerx

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
