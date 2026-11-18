from pygame.sprite import Group
from threats.asteroid import Normal
from threats.asteroid import Comet

class ThreatHandler:
	ALL_THREATS = [Normal,Comet]
	GROUP = Group()

	def __init__(self):
		pass
