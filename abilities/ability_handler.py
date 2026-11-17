from abilities.ability_imports import *
from abilities.missile import Missile
from abilities.rapid_fire import RapidFire

from pygame.sprite import Group


class AbilityHandler:
	ALL_ABIL_NAMES = [Missile,RapidFire]
	ACTIVE_ABIL_NAMES = [Missile]
	PASSIVE_ABILS_NAMES = [RapidFire]

	KEYS = None
	SCREEN = None

	def __init__(self,keys):
		AbilityHandler.KEYS = keys
		for ABIL in AbilityHandler.ALL_ABIL_NAMES: # ALL_ABILS defined in ability_handler.py
			ABIL.KEYS = AbilityHandler.KEYS
			ABIL.HANDLER = self

		self.active_abils = Group()


	def check_inputs(self):
		pass

		# this function triggers the activation of abilities if
		# correct conditions are met

	@EventBus.on("right_click")
	def right_click_abils(self,inputs):
		pass

	def set_all_diff_modifiers(diff):
		Missile.set_diff_modifiers(diff)

	def set_all_cost_modifiers():
		Missile.COST = 0
		RapidFire.COST = 100