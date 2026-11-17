from abilities.ability_imports import *
from load_assets import nuke_img


class Missile(Sprite):
	TIMER = Timer(120)
	RADIUS = 0.5
	SPEED = 1.8
	DAMAGE = 8

	KEYS = None
	COST = 0
	HANDLER = None

	def __init__(self, mouse_pos, pos=[500,700], img=nuke_img):
		super().__init__()

		self.pos = pos.copy()

		x = mouse_pos[0]
		y = mouse_pos[1]

		dy = self.pos[1] - y
		dx = x - self.pos[0]
		hyp = m.hypot(dx, dy)

		self.dy = dy / hyp
		self.dx = dx / hyp

		self.angle = m.degrees(m.atan2(dy,dx)) - 90 # in degrees
		self.image = py.transform.rotate(img, self.angle)

		rect_width = int(img.get_width()) / 2
		rect_height = int(img.get_height()) / 2

		j = pos[0] - rect_width
		k = pos[1] - rect_height

		self.rect = img.get_rect()
		self.rect.center = pos
		self.blit_pos = [j,k]

	def set_diff_modifiers(diff):
		level = diff_configs[diff]
		Missile.TIMER = Timer(level["missiles"]["cooldown"])
		Missile.RADIUS = level["missiles"]["radius"]
		Missile.SPEED = level["missiles"]["speed"]

	def on_hit(self,threat):
		threat.hp -= Missile.DAMAGE
		Animation("death", Animation.SCREEN, self.pos, scale=Missile.RADIUS)
		self.kill()

	def update(self):
		if self.pos[0] > 1100 or self.pos[0] < -100:
			self.kill()
		if self.pos[1] > 720 or self.pos[1] < -100:
			self.kill()

		self.pos[0] += self.dx * Missile.SPEED
		self.pos[1] -= self.dy * Missile.SPEED

		rect_width = int(self.image.get_width()) / 2
		rect_height = int(self.image.get_height()) / 2

		j = self.pos[0] - rect_width
		k = self.pos[1] - rect_height

		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.blit_pos = [j,k]


	@EventBus.on("left_click")
	def launch_missile():
		if not Missile.KEYS.shift and not Missile.TIMER.active and Missile.KEYS.mouse_pos[1] < 750:
			Missile.TIMER.active = True
			Missile.HANDLER.active_abils.add(Missile(Missile.KEYS.mouse_pos))

	@EventBus.on("upgrade_radius")
	def upgrade_missile_radius():
		Missile.RADIUS += 0.15

	@EventBus.on("upgrade_speed")
	def upgrade_missile_speed():
		Missile.SPEED += 0.3


	
		
		