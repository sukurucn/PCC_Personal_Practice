import pygame
import game_functions as gf
from setting import Setting
from ship import Ship

def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(screen, ai_setting)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)

run_game()
