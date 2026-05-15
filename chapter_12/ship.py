import pygame

class Ship():
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
