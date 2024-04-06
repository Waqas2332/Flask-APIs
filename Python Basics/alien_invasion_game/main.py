import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()  # initializing game screen

    game_settings = Settings()  # Initializing settings for game from settings.py

    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    my_ship = Ship(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(game_settings.bg_color)  # setting background color
        my_ship.blitme()
        pygame.display.flip()  # changes the screen after each update in the game such that changes are visible on
        # the screen


run_game()
