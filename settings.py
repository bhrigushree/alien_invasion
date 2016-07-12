class Settings():
	"""Class to store all settings for Alien Invasion game"""

	def __init__(self):
		"""Initialize game's settings"""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (240,240,240)

		#Ship settings
		self.ship_speed_factor = 5
		self.ship_limit = 0

		#Bullet Settings
		self.bullet_speed_factor = 8
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		#Alien Settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 30
		# fleet_direction of 1 represent right, -1 represents left.
		self.fleet_direction = 1
