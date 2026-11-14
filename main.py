import random
import pygame as py
import math as m
from python_event_bus import EventBus
from input_handler import InputHandler
from ability_handler import *
from asteroid import ThreatHandler
from asteroid import Normal
from timer import Timer

from load_assets import bg_img
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


	def main_loop(self):
		while True:
			self.main_menu()  # menu before game, choose duration
			self.game_loop()  # playing the game
			self.end_screen() # reset game object, show score


	def game_loop(self):
		abil_handler = AbilityHandler()
		threat_handler = ThreatHandler()
		
		for ABIL in ALL_ABILS: # ALL_ABILS defined in ability_handler.py
			ABIL.KEYS = self.inputs
			ABIL.HANDLER = abil_handler

		debug_count = 0
		in_game = True
		while in_game:
			self.screen.fill((0,0,0))
			self.screen.blit(bg_img,(0,0))
			
			self.inputs.keys()
			
			py.draw.line(self.screen, (255,0,0), (500,700), self.inputs.mouse_pos, 3)
		

			if debug_count < 240:
				debug_count += 1
			else:
				debug_count = 0
				self.spawn_asteroids(threat_handler)
				
			# need loop to check each asteroid against every ability.
			# make collision checking a function.
			for threat in threat_handler.threats:
				for missile in abil_handler.active_abils:
					missile.rect.scale_by_ip(0.7) # some trig function to scale rect correctly
					# py.draw.rect(self.screen,(255,255,255),missile.rect)
					dist = m.sqrt((threat.blit_pos[0] - missile.rect.center[0])**2 + (threat.blit_pos[1] - missile.rect.center[1])**2)
					if missile.rect.colliderect(threat.rect):
						print("hit!")
						threat_handler.threats.remove(threat)
						abil_handler.active_abils.remove(missile)
						break


			Timer.update_timers()

			abil_handler.update()
			threat_handler.update()

			abil_handler.draw(self.screen)
			threat_handler.draw(self.screen)
			
			self.inputs.update()
			py.display.update()
			self.clock.tick(120)


	def main_menu(self):
		pass


	def end_screen(self):
		pass


	def spawn_asteroids(self, threats):
		# add new functions later to have different spawn configurations
		a = [
			{"pos" : [500,50],"hp" : 5,"dx" : 0.5,"dy" : 1.2,"img" : aster_img },
			{"pos" : [100,50],"hp" : 10,"dx" : 0.3,"dy" : 0.7,"img" : metal_img },
			{"pos" : [900,50],"hp" : 3,"dx" : -0.5,"dy" : 1.1,"img" : rubble_img },
			{"pos" : [300,50],"hp" : 5,"dx" : 0.1,"dy" : 1.6,"img" : aster_img },
			{"pos" : [700,50],"hp" : 3,"dx" : -0.3,"dy" : 0.9,"img" : rubble_img },
			{"pos" : [500,50],"hp" : 3,"dx" : 0.3,"dy" : 1.8,"img" : rubble_img },
			{"pos" : [400,50],"hp" : 3,"dx" : -0.15,"dy" : 0.5,"img" : metal_img }
		]

		r = random.choice(a)
		ast = Normal(r["pos"],r["hp"],r["dx"],r["dy"],r["img"])
		threats.add(ast)




if __name__ == "__main__":
	g = Game()
	g.main_loop()
