class Settings():
	"""Class to store all settings for Alien Invasion game"""

	def __init__(self):
		"""Initialize game's static settings"""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (240,240,240)

		#Ship settings
		self.ship_limit = 3

		#Bullet Settings
		self.bullet_width = 5 #3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5

		#Alien Settings
		self.fleet_drop_speed = 3
		
		#How quickly the game speeds up
		self.speedup_scale = 1.2
		#How quickly the alien point value increases
		self.score_scale = 1.2

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.ship_speed_factor = 5 #1.5
		self.bullet_speed_factor = 5 #3
		self.alien_speed_factor = 1

		# fleet_direction of 1 represent right, -1 represents left.
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 10


	def increase_speed(self):
		"""Increase speed settings and alien point values"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points  = int(self.alien_points*self.score_scale)