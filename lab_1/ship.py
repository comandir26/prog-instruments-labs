import pygame 

from pygame.sprite import Sprite


class Ship(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load("images/ship119x96.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.center = float(self.rect.centerx)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.bottom-=1
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.bottom+=1
		self.rect.centerx = self.center

	def center_ship(self):
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom


