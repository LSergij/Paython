import pygame
from settings import Settings

class Player2():
    def __init__(self, screen):
        self.screen=screen

        self.image = pygame.image.load("images/player2.png")
        self.image=pygame.transform.scale(self.image, (100,150))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.left=self.screen_rect.left
        self.rect.bottom=self.screen_rect.bottom

        self.jump = False
        self.jump_cound= 10

        self.moving_r = False
        self.moving_l =  False
        self.moving_d = False
        self.moving_u = False
        self.sit_down = False



    def update(self):
        if self.moving_r and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 6
        if self.moving_l and self.rect.left > 0:
            self.rect.centerx -= 6
        if not(self.jump):
            if self.moving_d and self.rect.bottom < self.screen_rect.bottom:
                self.rect.bottom += 3

            if self.moving_u and self.rect.top > 0:
                self.rect.bottom -= 3

            if self.sit_down == True:
                self.image = pygame.transform.scale(self.image, (100, 100))
                self.rect.centery = self.screen_rect.bottom - 25
            else:
                self.image = pygame.transform.scale(self.image, (100, 150))
                self.rect.bottom = self.screen_rect.bottom

        else:
            if self.jump_cound >= -10:
                if self.jump_cound < 0:
                    self.rect.bottom += (self.jump_cound ** 2) /2
                else:
                    self.rect.bottom -= (self.jump_cound ** 2) / 2
                self.jump_cound -= 1
            else:
               self.jump = False
               self.jump_cound = 10

        if self.rect.bottom > 0:
            self.moving_d += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)