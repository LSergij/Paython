import pygame, sys
from settings import Settings
from player1 import Player1
from player2 import Player2
import game_function as g_f
# from background import Background


def init_game():
    pygame.init()

    game_settings = Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
  #  background = Background(screen)
    player1 = Player1(screen)
    player2 = Player2(screen)




    while True:
       pygame.time.delay(30)
       g_f.check_events(game_settings, player1, player2, screen)
       g_f.update_screen(screen, game_settings,player1, player2)
       player1.update()
       player2.update()



init_game()
