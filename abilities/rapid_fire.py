from abilities.ability_imports import *
from abilities.missile import Missile
from timer import EventTimer

class RapidFire:
	COST = None
	KEYS = None
	HANDLER = None
	
	def __init__(self):
		print("fire!")
		RapidFire.HANDLER.append(self)
		Missile.TIMER = Timer(20)
		self.timer = Timer(500)
		self.timer.active = True


	def update(self):
		if not self.timer.active:
			print("sad")
			Missile.TIMER = Timer(120)
			RapidFire.HANDLER.remove(self)

	@EventBus.on("start_rapid_fire")
	def start_rapid_fire():
		RapidFire()


