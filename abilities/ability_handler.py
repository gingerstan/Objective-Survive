from abilities.missile import Missile
from abilities.rapid_fire import RapidFire

from python_event_bus import EventBus
from pygame.sprite import Group


class AbilityHandler:
	KEYS = None
	SCREEN = None

	ALL_ABIL_NAMES = [Missile,RapidFire]
	ACTIVE_ABIL_NAMES = [Missile]
	PASSIVE_ABILS_NAMES = [RapidFire]

	AA = Group() # all current Active Abilities
	PA = [] # all current Passive Abilities
		
	@EventBus.on("left_click")
	def left_click():
		keys = AbilityHandler.KEYS
		if not keys.shift and not Missile.TIMER.active and keys.mouse_pos[1] < 750:
			EventBus.call("launch_missile")

	@EventBus.on("right_click")
	def right_click():
		keys = AbilityHandler.KEYS
		if not keys.shift and not RapidFire.TIMER.active and keys.mouse_pos[1] < 750:
			EventBus.call("rapid_fire")


	def update_all():
		AbilityHandler.AA.update()
		for passive in AbilityHandler.PA:
			passive.update()

	

	def setup_abilities(keys,diff,modifier):
		AbilityHandler.KEYS = keys
		for ABIL in AbilityHandler.ALL_ABIL_NAMES: 
			ABIL.KEYS = AbilityHandler.KEYS
			ABIL.HANDLER = AbilityHandler

		Missile.set_diff_modifiers(diff)

		Missile.COST = 0 * modifier
		RapidFire.COST = 100 * modifier