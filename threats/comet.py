from animation import Animation
from pygame.sprite import Sprite
import math as m

class Comet(Sprite):
	def __init__(self,pos,path_pos,dx,dy,angle,hp,img):
		super().__init__()

		self.pos = pos.copy()
		self.dx = dx
		self.dy = dy
		self.hp = hp
		self.maxHP = hp
		self.image = img

		# calculate cometpath angle and start pos from comet dx dy and pos

		rect_width = int(img.get_width()) / 2
		rect_height = int(img.get_height()) / 2

		j = pos[0] - rect_width
		k = pos[1] - rect_height
		self.blit_pos = [j,k]

		self.rect = img.get_rect()
		self.rect.center = self.pos

		self.score = (dx + dy)*10 + hp

		self.anim = Animation("cometPath",path_pos,scale=0.75,angle=angle,loop=True)

	def update(self):
		if self.pos[0] > 1100 or self.pos[0] < -100 or self.pos[1] > 800 or self.pos[1] < -200:
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
		Animation.remove_anim(self.anim)
		self.kill()

