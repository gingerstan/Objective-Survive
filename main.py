import random
import logging
import pygame as py
import math as m
from functools import lru_cache
from input_handler import InputHandler
from input_handler import GameStates
from ability_handler import *
from asteroid import *
from timer import *
from animation import Animation
from animation import load_image_sequence
from animation import load_number_sequence
from round_variables import RoundVariables
from game_configs.difficulty_configs import *
from gui import Button

from load_assets import bg_img
from load_assets import bar_img
from load_assets import speed_upgrade_img
from load_assets import radius_upgrade_img
from load_assets import aster_img
from load_assets import rubble_img
from load_assets import metal_img
from load_assets import icon_img
from load_assets import loser_img

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
    filename="scores.log",  # Omit to print to the console instead
    encoding="utf-8",
)
logger = logging.getLogger(__name__)


class Game:
	def __init__(self):
		self.clock = py.time.Clock()
		py.init()
		py.display.set_caption("Objective: Survive")
		self.screen = py.display.set_mode((1000,1000), 0, 32)
		self.inputs = InputHandler()
		self.blitQueue = []
		self.framerate = 120

		self.fps = [] # for performance testing

		Button.KEYS = self.inputs

		bg_img.convert()
		icon_img.convert()
		bar_img.convert()
		speed_upgrade_img.convert()
		radius_upgrade_img.convert()

	def main_loop(self):
		while True:
			self.main_menu()  # menu before game, choose duration
			score = self.game_loop()  # playing the game
			self.end_screen(score) # reset game object, show score


	def game_loop(self):
		vars = RoundVariables(self.inputs.difficulty)

		Missile.set_diff_modifiers(self.inputs.difficulty)
		
		spawn_timer = EventTimer(180,"spawn_asteroid")
		spawn_update_rate_timer = EventTimer(120,"update_spawn_rate",spawn_timer,vars)
		

		for ABIL in ALL_ABILS: # ALL_ABILS defined in ability_handler.py
			ABIL.KEYS = self.inputs
			ABIL.HANDLER = vars.abil_handler

		for THREAT in ALL_THREATS: # ALL_THREATS defined in asteroid.py
			THREAT.HANDLER = vars.threat_handler

		self.inputs.state = GameStates.IN_GAME

		debug_count = 0
		in_game = True
		while in_game:
			self.screen.fill((0,0,0))
			self.screen.blit(bg_img,(0,0))
			self.inputs.keys()
		
			# pauses entities so player can use upgrade menu ##########################
			if not self.inputs.shift:
				# if debug_count < 120:
				# 	debug_count += 1
				# else:
				# 	debug_count = 0
					
				self.check_collisions(vars)

				Timer.update_timers()
				vars.abil_handler.update()
				vars.threat_handler.update()
				vars.frames += 1

				if vars.planet_health < 1:
					avg_fps = 0
					for frame in self.fps:
						avg_fps += frame
					avg_fps = avg_fps / len(self.fps)

					in_game = False
					logger.info(f"Scored: {vars.score}, Difficulty: {Difficulty(self.inputs.difficulty).name}") # add length / abilities used in game to stats
					logger.debug(f"Average FPS: {avg_fps}")
			else:
				# check buttons now handled on BusEvent "left_click"
				pass


			# end menu pause ##########################################################

			self.draw_game_gui(vars)
			Animation.play_all(self.blitQueue)
			vars.abil_handler.draw(self.blitQueue)
			vars.threat_handler.draw(self.blitQueue)
			self.screen.blits(self.blitQueue)

			self.inputs.update()
			py.display.update()
			self.blitQueue.clear()
			self.clock.tick(self.framerate)

			self.fps.append(self.clock.get_fps())

		return vars.score


	def draw_game_gui(self,vars):
		self.screen.blit(bar_img,(0,800))
		self.screen.blit(speed_upgrade_img,(50,830))
		self.screen.blit(radius_upgrade_img,(50,900))
		py.draw.rect(self.screen,(255,0,0),(850,900,vars.planet_health * vars.hp_gui_factor,75))

		if self.inputs.mouse_pos[1] < 800:
			py.draw.line(self.screen, (255,0,0), (500,700), self.inputs.mouse_pos, 3)

		self.display_score(vars.score,False)


	@EventBus.on("update_spawn_rate")
	def update_spawn_rate(args):
		args[0].period = (args[1].ast_spawn_slope*args[1].frames) + args[1].ast_spawn_mod


	def check_collisions(self, vars):
		for threat in vars.threat_handler.threats:
			if threat.pos[1] > 750:
				vars.planet_health -= threat.hp
				vars.threat_handler.threats.remove(threat)
				
				break

			for missile in vars.abil_handler.active_abils:
				missile.rect.scale_by_ip(Missile.RADIUS) # some trig function to scale rect correctly
				# py.draw.rect(self.screen,(255,255,255),missile.rect)
				if missile.rect.colliderect(threat.rect):
					vars.score += int(threat.score)
					vars.threat_handler.threats.remove(threat)
					vars.abil_handler.active_abils.remove(missile)
					Animation("death",self.screen,missile.pos,scale=Missile.RADIUS)

					break


	@EventBus.on("left_click")
	def check_game_buttons(inputs):
		if inputs.shift:
			speed_rect = py.Rect(50,830,150,50)
			radius_rect = py.Rect(50,900,150,50)

			if speed_rect.collidepoint(inputs.mouse_pos):
				EventBus.call("upgrade_speed")
			elif radius_rect.collidepoint(inputs.mouse_pos):
				EventBus.call("upgrade_radius")
		else:
			pass

	def main_menu(self):
		self.inputs.state = GameStates.MENU
		nums = load_number_sequence()

		in_menu = True
		while in_menu:
			self.screen.fill((0,0,0))
			self.screen.blit(icon_img,(0,0))
			self.inputs.keys()

			Button.KEYS = self.inputs
			Button.update()

			Button.ALL_BUTTONS[0].img = nums[self.inputs.difficulty]
			Button.draw(self.screen)

			if self.inputs.space_bar_click():
				in_menu = False

			self.inputs.update()
			py.display.update()
			self.clock.tick(self.framerate)


	def end_screen(self,score):
		in_end = True
		frames = 0
		while in_end:
			self.screen.fill((0,0,0))
			self.screen.blit(loser_img,(0,0))

			self.display_score(score,True)

			if frames > 500:
				in_end = False

			frames += 1
			py.display.update()
			self.clock.tick(self.framerate)


	def display_score(self,score,end):
		nums = load_number_sequence()
		scaled_nums = []

		for num in nums:
			scaled_nums.append(py.transform.scale_by(num, 1.3))

		str_score = str(score)

		if end:
			y = 450
			x = 550
			dist = 100
		else:
			y = 10
			x = 600
			dist = 70

		digit = 0
		for i in str_score:
			pos = [(x + (digit*dist)), y]
			if end:
				img = scaled_nums[int(i)]
			else:
				img = nums[int(i)]
			self.screen.blit(img,pos)
			digit += 1


	@EventBus.on("update_difficulty")
	def update_difficulty(inputs):
		if inputs.difficulty < 5:
			inputs.difficulty += 1
		elif inputs.difficulty == 5:
			inputs.difficulty = 1


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
			{"pos" : [400,50],"hp" : 11,"dx" : -0.15,"dy" : 0.5,"img" : metal_img },
			{"pos" : [200,50],"hp" : 15,"dx" : -0.1,"dy" : 0.6,"img" : metal_img },
			{"pos" : [800,50],"hp" : 7,"dx" : 0.1,"dy" : 1,"img" : aster_img }
		]

		r = random.choice(a)
		ast = Normal(r["pos"],r["hp"],r["dx"],r["dy"],r["img"])
		Normal.HANDLER.add(ast)

	




if __name__ == "__main__":
	g = Game()
	g.main_loop()


