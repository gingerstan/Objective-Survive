from game_configs.difficulty_configs import *

class RoundVariables:
	def __init__(self):
		self.reset()

	def load_game_config(self):
		pass

	def reset(self):
		self.abil_handler = None
		self.threat_handler = None
		self.score = 0
		self.frames = 0
		self.planet_health = 5
		self.hp_gui_factor = 100 / self.planet_health
