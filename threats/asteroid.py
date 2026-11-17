# import pygame as py, sys
from pygame.sprite import Sprite


class Normal(Sprite):
	def __init__(self, pos, hp, dx, dy, img):
		super().__init__()

		self.pos = pos.copy()
		self.blit_pos = pos.copy()
		self.hp = hp
		self.maxHP = hp
		self.dx = dx 
		self.dy = dy
		self.image = img

		self.rect = img.get_rect()
		self.rect.center = self.pos

		self.score = (dx + dy)*10 + hp


	def update(self):
		if self.pos[0] > 1100 or self.pos[0] < -100:
			self.kill()
		if self.pos[1] > 800 or self.pos[1] < -100:
			self.kill()

		self.pos[0] += self.dx
		self.pos[1] += self.dy

		rect_width = int(self.image.get_width()) / 2
		rect_height = int(self.image.get_height()) / 2

		j = self.pos[0] - rect_width
		k = self.pos[1] - rect_height

		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.blit_pos = [j,k]


	def hit_planet(self,vars):
		vars.planet_health -= self.hp
		self.kill()




ALL_THREATS = [Normal]


