import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pygame.image.load("images/1.png").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, (800,600)).convert()
        self.rect_img = self.bg_img.get_rect()