import pygame,sys


def check_events(game_settings, player1 , player2 ,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1.moving_right = True
            if event.key == pygame.K_LEFT:
                player1.moving_left = True
            if event.key == pygame.K_UP:
                player1.jump = True
            if event.key == pygame.K_DOWN:
                player1.sit_down = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player1.moving_right = False
            if event.key == pygame.K_LEFT:
                player1.moving_left = False
            if event.key == pygame.K_DOWN:
                player1.sit_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player2.moving_r = True
            if event.key == pygame.K_a:
                player2.moving_l = True
            if event.key == pygame.K_w:
                player2.jump = True
            if event.key == pygame.K_s:
                player2.sit_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player2.moving_r = False
            if event.key == pygame.K_a:
                player2.moving_l = False
            if event.key == pygame.K_s:
                player2.sit_down = False










def update_screen(screen, game_settings, player1, player2,):
    pygame.display.flip()
    screen.fill(game_settings.bg_color)
    player1.blitme()
    player2.blitme()


