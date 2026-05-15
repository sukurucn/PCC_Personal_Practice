import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_up_evnts(event,ship)
        elif event.type == pygame.KEYUP:
            check_keydown_events(event,ship)

def update_screen(ai_setting, screen, ship):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    pygame.display.flip()
def check_keydown_events(event,ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
def check_up_evnts(event,ship):
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = False