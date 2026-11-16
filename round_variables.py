from game_configs.difficulty_configs import diff_configs

class RoundVariables:
	def __init__(self,diff):
		self.reset(diff)

	def load_game_config(self):
		pass

	def reset(self,diff):
		self.abil_handler = None
		self.threat_handler = None
		self.score = 0
		self.frames = 0
		self.planet_health = diff_configs[diff]["planet"]["planet_health"]
		self.hp_gui_factor = 100 / self.planet_health
