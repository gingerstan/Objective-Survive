from abilities.missile import Missile

class Player:
	def __init__(self,cash):
		self.cash = cash
		self.abilities = [Missile]