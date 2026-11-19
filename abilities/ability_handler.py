from abilities.missile import Missile
from abilities.rapid_fire import RapidFire

from python_event_bus import EventBus
from pygame.sprite import Group
from game_states import GameStates
from functools import wraps


class AbilityHandler:
	STATE = None
	KEYS = None
	SCREEN = None

	ALL_ABIL_NAMES = [Missile,RapidFire]
	ACTIVE_ABIL_NAMES = [Missile]
	PASSIVE_ABILS_NAMES = [RapidFire]

	AA = Group() # all current Active Abilities
	PA = [] # all current Passive Abilities

	def check_state(state):
		def check_state(func):
			def inner():
				if state == AbilityHandler.STATE:
					func()
			return inner
		return check_state


	@EventBus.on("left_click")
	@check_state(GameStates.IN_GAME)
	def left_click():
		keys = AbilityHandler.KEYS
		if not keys.shift and not Missile.TIMER.active and keys.mouse_pos[1] < 750:
			EventBus.call("launch_missile")


	@EventBus.on("right_click")
	@check_state(GameStates.IN_GAME)
	def right_click():
		keys = AbilityHandler.KEYS
		if not keys.shift and not RapidFire.TIMER.active and keys.mouse_pos[1] < 750:
			EventBus.call("rapid_fire")


	def update_all():
		AbilityHandler.AA.update()
		for passive in AbilityHandler.PA:
			passive.update()

	

	def setup_abilities(keys):
		AbilityHandler.KEYS = keys
		for ABIL in AbilityHandler.ALL_ABIL_NAMES: 
			ABIL.KEYS = AbilityHandler.KEYS
			ABIL.HANDLER = AbilityHandler

	def set_diff_modifiers(diff,modifier):
		Missile.set_diff_modifiers(diff)
		Missile.COST = 0 * modifier
		RapidFire.COST = 100 * modifier
