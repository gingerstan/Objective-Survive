from pygame.sprite import Group
from threats.asteroid import Normal
from threats.comet import Comet

class ThreatHandler:
	ALL_THREATS = [Normal,Comet]
	GROUP = Group()

	def __init__(self):
		pass
