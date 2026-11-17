from abilities.ability_imports import *
from abilities.missile import Missile
from timer import EventTimer

class RapidFire:
	COST = None
	KEYS = None
	HANDLER = None

	TIMER = Timer(500)
	
	def __init__(self):
		RapidFire.HANDLER.PA.append(self)
		RapidFire.TIMER.active = True
		Missile.TIMER = Timer(20)
		
	def update(self):
		if not RapidFire.TIMER.active:
			Missile.TIMER = Timer(Missile.COOLDOWN)
			RapidFire.HANDLER.PA.remove(self)

	@EventBus.on("rapid_fire")
	def rapid_fire():
		RapidFire()


