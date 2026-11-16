import random
import pygame as py
import math as m
from input_handler import InputHandler
from ability_handler import *
from asteroid import *
from timer import *
from animation import Animation

from load_assets import bg_img
from load_assets import bar_img
from load_assets import speed_upgrade_img
from load_assets import radius_upgrade_img
from load_assets import aster_img
from load_assets import rubble_img
from load_assets import metal_img


class Game:
	def __init__(self):
		self.clock = py.time.Clock()
		py.init()
		py.display.set_caption("Objective: Survive")
		self.screen = py.display.set_mode((1000,1000), 0, 32)
		self.inputs = InputHandler()
		self.framerate = 120


	def main_loop(self):
		while True:
			self.main_menu()  # menu before game, choose duration
			self.game_loop()  # playing the game
			self.end_screen() # reset game object, show score


	def game_loop(self):
		vars = self.RoundVariables()
		vars.abil_handler = AbilityHandler()
		vars.threat_handler = ThreatHandler()
		
		spawn_timer = EventTimer(180,"spawn_asteroid")
		spawn_update_rate_timer = EventTimer(120,"update_spawn_rate",spawn_timer,vars)
		

		for ABIL in ALL_ABILS: # ALL_ABILS defined in ability_handler.py
			#ABIL.KEYS = self.inputs
			ABIL.HANDLER = vars.abil_handler

		for THREAT in ALL_THREATS: # ALL_THREATS defined in asteroid.py
			THREAT.HANDLER = vars.threat_handler

		# test_anim = Animation("death",11,10,self.screen,[500,500])

		debug_count = 0
		in_game = True
		while in_game:
			self.screen.fill((0,0,0))
			self.screen.blit(bg_img,(0,0))
			self.screen.blit(bar_img,(0,800))
			self.screen.blit(speed_upgrade_img,(50,830))
			self.screen.blit(radius_upgrade_img,(50,900))
			self.inputs.keys()
			# print(frames)

			if self.inputs.mouse_pos[1] < 800:
				py.draw.line(self.screen, (255,0,0), (500,700), self.inputs.mouse_pos, 3)
		
			# pauses entities so player can use upgrade menu ##########################
			if not self.inputs.shift:

				if debug_count < 120:
					debug_count += 1
				else:
					debug_count = 0
					

				self.check_collisions(vars)

				Timer.update_timers()
				vars.abil_handler.update()
				vars.threat_handler.update()
			else:
				# check buttons now handled on BusEvent "left_click"
				pass


			# end menu pause ##########################################################

			for anim in Animation.ALL_ANIMATIONS:
				anim.play()

			vars.abil_handler.draw(self.screen)
			vars.threat_handler.draw(self.screen)
				
			self.inputs.update()
			py.display.update()
			vars.frames += 1
			self.clock.tick(self.framerate)

	@EventBus.on("update_spawn_rate")
	def update_spawn_rate(args):
		 args[0].period = (-0.002*args[1].frames) + 200


	def check_collisions(self, vars):
		for threat in vars.threat_handler.threats:
			if threat.pos[1] > 750:
				vars.planet_health -= threat.hp
				vars.threat_handler.threats.remove(threat)
				print(vars.planet_health)
				break

			for missile in vars.abil_handler.active_abils:
				missile.rect.scale_by_ip(Missile.RADIUS) # some trig function to scale rect correctly
				# py.draw.rect(self.screen,(255,255,255),missile.rect)
				dist = m.sqrt((threat.blit_pos[0] - missile.rect.center[0])**2 + (threat.blit_pos[1] - missile.rect.center[1])**2)
				if missile.rect.colliderect(threat.rect):
					vars.score += threat.score
					vars.threat_handler.threats.remove(threat)
					vars.abil_handler.active_abils.remove(missile)
					Animation("death",11,7,self.screen,missile.pos, scale=Missile.RADIUS)

					break


	@EventBus.on("left_click")
	def check_buttons(inputs):
		if inputs.shift:
			speed_rect = py.Rect(50,830,150,50)
			radius_rect = py.Rect(50,900,150,50)

			if speed_rect.collidepoint(inputs.mouse_pos):
				EventBus.call("upgrade_speed")
			elif radius_rect.collidepoint(inputs.mouse_pos):
				EventBus.call("upgrade_radius")


	def main_menu(self):
		pass


	def end_screen(self):
		pass

	@EventBus.on("spawn_asteroid")
	def spawn_asteroids():
		# add new functions later to have different spawn configurations
		a = [
			{"pos" : [500,50],"hp" : 5,"dx" : 0.5,"dy" : 1.2,"img" : aster_img },
			{"pos" : [100,50],"hp" : 12,"dx" : 0.3,"dy" : 0.7,"img" : metal_img },
			{"pos" : [900,50],"hp" : 3,"dx" : -0.5,"dy" : 1.1,"img" : rubble_img },
			{"pos" : [300,50],"hp" : 6,"dx" : 0.1,"dy" : 1.6,"img" : aster_img },
			{"pos" : [700,50],"hp" : 3,"dx" : -0.3,"dy" : 0.9,"img" : rubble_img },
			{"pos" : [500,50],"hp" : 2,"dx" : 0.3,"dy" : 1.8,"img" : rubble_img },
			{"pos" : [400,50],"hp" : 11,"dx" : -0.15,"dy" : 0.5,"img" : metal_img }
		]

		r = random.choice(a)
		ast = Normal(r["pos"],r["hp"],r["dx"],r["dy"],r["img"])
		Normal.HANDLER.add(ast)

	class RoundVariables:
		def __init__(self):
			self.abil_handler = None
			self.threat_handler = None
			self.score = 0
			self.frames = 0
			self.planet_health = 100



if __name__ == "__main__":
	g = Game()
	g.main_loop()



# def check_buttons(self):
# 	speed_rect = py.Rect(50,830,150,50)
# 	radius_rect = py.Rect(50,900,150,50)

# 	if speed_rect.collidepoint(self.inputs.mouse_pos) and self.inputs.left_click():
# 		EventBus.call("upgrade_speed")
# 	elif radius_rect.collidepoint(self.inputs.mouse_pos) and self.inputs.left_click():
# 		EventBus.call("upgrade_radius")