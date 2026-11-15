import pygame as py, sys
from abc import ABC, abstractmethod
from pygame import sprite

class ThreatHandler:
	def __init__(self):
		self.threats = []

	def add(self, entity):
		self.threats.append(entity)

	def update(self):
		self.threats = [a for a in self.threats if a.update()]

	def draw(self, screen):
		for threat in self.threats:
			# py.draw.rect(screen,(255,255,255), threat.rect)
			# screen.blit(threat.img, threat.blit_pos)
			screen.blit(threat.img, threat.blit_pos)


class Normal(py.sprite.Sprite):
	def __init__(self, pos, hp, dx, dy, img):
		self.pos = pos.copy()
		self.blit_pos = pos.copy()
		self.hp = hp
		self.dx = dx 
		self.dy = dy
		self.img = img

		self.rect = self.img.get_rect()
		self.rect.center = self.pos

		self.score = (dx + dy)*10 + hp


	def update(self):
		if self.pos[0] > 1100 or self.pos[0] < -100:
			return False
		if self.pos[1] > 800 or self.pos[1] < -100:
			return False

		self.pos[0] += self.dx
		self.pos[1] += self.dy

		rect_width = int(self.img.get_width()) / 2
		rect_height = int(self.img.get_height()) / 2

		j = self.pos[0] - rect_width
		k = self.pos[1] - rect_height

		self.rect = self.img.get_rect()
		self.rect.center = self.pos
		self.blit_pos = [j,k]

		return True



ALL_THREATS = [Normal]