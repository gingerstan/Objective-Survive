from pygame.sprite import Group

class ThreatHandler:
	KEYS = None
	SCREEN = None

	def __init__(self,keys):
		ThreatHandler.KEYS = keys
		self.group = Group()
