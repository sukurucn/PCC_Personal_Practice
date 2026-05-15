import sys
import pygame
from bullet import Bullet

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_up_events(event, ship)

def fire_bullet(ai_setting, screen, ship, bullets, last_fire_time):
    if ship.firing:
        now = pygame.time.get_ticks()
        if now - last_fire_time >= ai_setting.bullet_cooldown:
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)
            last_fire_time = now
    return last_fire_time

def update_screen(ai_setting, screen, ship, bullets):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        ship.firing = True

def check_up_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        ship.firing = False
