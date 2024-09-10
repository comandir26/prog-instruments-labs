import pygame

from pygame.sprite import Sprite


class Star(Sprite):
	"""A class that implements the star"""

	def __init__(self, screen):
		"""Initializes the attributes of the star"""
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load("images/starsmall.png")
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def blitme(self):
		"""Draws the star in the current position"""
		self.screen.blit(self.image, self.rect)
 