import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class to represent aliens onjects"""

	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set it's starting position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#Load the alienr image and set its rect property
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Start each alien near to top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the alien's exact position
		self.x = float(self.rect.x)


	def blitme(self):
		"""Draw the alien at current location"""
		self.screen.blit(self.image, self.rect)


	def update(self):
		"""Move the aliens right or left"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x


	def check_edges(self):
		"""Return True of alien is at edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True