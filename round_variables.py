from game_configs.difficulty_configs import diff_configs
from pygame.sprite import Group


class RoundVariables:
	def __init__(self,diff):
		self.reset(diff)

	def load_game_config(self):
		pass

	def reset(self,diff):
		self.score = 0
		self.frames = 0
		self.points = 0
		self.diff = diff
		
		self.planet_health = diff_configs[diff]["planet"]["planet_health"]
		self.hp_gui_factor = 100 / self.planet_health

		self.ast_spawn_slope = diff_configs[diff]["threats"]["asteroid_spawn_rate_slope"]
		self.ast_spawn_mod = diff_configs[diff]["threats"]["asteroid_spawn_rate_mod"]
