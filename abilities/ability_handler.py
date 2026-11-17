from abilities.missile import Missile
from abilities.rapid_fire import RapidFire

from pygame.sprite import Group


class AbilityHandler:
	KEYS = None
	SCREEN = None

	ALL_ABIL_NAMES = [Missile,RapidFire]
	ACTIVE_ABIL_NAMES = [Missile]
	PASSIVE_ABILS_NAMES = [RapidFire]

	AA = Group() # all current Active Abilities
	PA = Group() # all current Passive Abilities
		
	def check_inputs():
		keys = AbilityHandler.KEYS
		

	

	def setup_abilities(keys):
		AbilityHandler.KEYS = keys
		for ABIL in AbilityHandler.ALL_ABIL_NAMES: 
			ABIL.KEYS = AbilityHandler.KEYS
			ABIL.HANDLER = AbilityHandler

	def set_all_diff_modifiers(diff):
		Missile.set_diff_modifiers(diff)

	def set_all_costs(modifier):
		Missile.COST = 0 * modifier
		RapidFire.COST = 100 * modifier