import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(screen, ai_setting)
    bullets = Group()
    last_fire_time = 0

    while True:
        gf.check_events(ship)
        ship.update()
        bullets.update()
        last_fire_time = gf.fire_bullet(
            ai_setting, screen, ship, bullets, last_fire_time)
        gf.update_screen(ai_setting, screen, ship, bullets)

run_game()
