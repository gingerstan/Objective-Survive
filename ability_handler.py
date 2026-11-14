import pygame as py
from abilities.missile import Missile


class AbilityHandler:
	def __init__(self):
		self.active_abils = [] # contains all active ability instances

	def add(self, abil):
		self.active_abils.append(abil)

	def update(self):
		self.active_abils = [a for a in self.active_abils if a.update()]

	def draw(self, screen):
		for abil in self.active_abils:
			#py.draw.rect(screen,(255,255,255), abil.rect)
			screen.blit(abil.img, abil.blit_pos)


# MUST ADD ALL ABILITY CLASSES TO THIS LIST
ALL_ABILS = [Missile]