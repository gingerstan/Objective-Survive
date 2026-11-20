import random
import logging
import pygame as py
import math as m
import time
from functools import lru_cache
from python_event_bus import EventBus
from input_handler import InputHandler as IH
from timer import Timer
from timer import EventTimer
from animation import Animation
from game_states import GameStates
from animation import load_image_sequence
from animation import load_number_sequence
from round_variables import RoundVariables
from game_configs.difficulty_configs import *
from gui import Button
from menu_elements import main_menu
from menu_elements import in_game_menu
from abilities.ability_handler import AbilityHandler as AH
from threats.threat_handler import ThreatHandler as TH
from abilities.missile import Missile
from abilities.rapid_fire import RapidFire
from threats.asteroid import Normal
from threats.comet import Comet

from load_assets import screen
from load_assets import cursor_img
from load_assets import bg_img
from load_assets import bar_img
from load_assets import speed_upgrade_img
from load_assets import radius_upgrade_img
from load_assets import normal_img
from load_assets import rubble_img
from load_assets import metal_img
from load_assets import comet_img
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

cursor_img = py.transform.scale(cursor_img,(60,60))
cursor = py.cursors.Cursor((30,30),cursor_img)
py.mouse.set_cursor(cursor)


class Game:
	g = None
	state = GameStates.START_MENU

	def __new__(cls):
		if cls.g is None:
			cls.g = super().__new__(cls)
		return cls.g

	def __init__(self):
		# pygame and screen initialized in load_assets
		self.clock = py.time.Clock()
		self.screen = screen
		self.framerate = 120
		self.blitQueue = []
		
		self.inputs = IH()
		self.inputs.state = Game.state

		AH.setup_abilities(self.inputs)
		self.vars = RoundVariables(1)

		Button.KEYS = self.inputs

		self.fps = [] # for performance testing

	def main_loop(self):
		while True:
			self.main_menu()  # menu before game, choose duration
			self.game_loop()  # playing the game
			self.end_screen() # reset game object, show score

	def game_loop(self):
		self.inputs.update()
		self.vars.reset(self.inputs.diff)

		AH.STATE = GameStates.IN_GAME
		AH.set_diff_modifiers(self.vars.diff,1)

		spawn_timer = EventTimer(180,"spawn_asteroid")
		spawn_update_rate_timer = EventTimer(120,"update_spawn_rate",spawn_timer)

		g.state = GameStates.IN_GAME

		prev_time = time.time()
		debug_count = 0
		in_game = True
		while in_game:
			self.screen.fill((0,0,0))
			self.screen.blit(bg_img,(0,0))
			self.inputs.keys()
			in_game_menu.update(self.inputs,self.blitQueue)

			now = time.time()
			self.vars.dt = now - prev_time
			prev_time = now
			self.vars.dt *= self.framerate

			if not self.inputs.shift:
				Animation.show()
				# if debug_count < 120:
				# 	debug_count += 1
				# else:
				# 	debug_count = 0
					
				self.check_collisions(self.vars)

				Timer.update_timers()
				AH.update_all()
				TH.GROUP.update()
				self.vars.frames += 1

				in_game = self.check_if_dead()
			else:
				Animation.hide()

			self.all_the_updates()
			
	### END GAME LOOP ###################################


	def all_the_updates(self):
		self.display_score(self.vars.score,False)
		Animation.play_all(self.blitQueue)
		
		AH.AA.draw(self.screen)
		TH.GROUP.draw(self.screen)
		self.screen.blits(self.blitQueue)

		self.inputs.update()
		py.display.update()
		self.blitQueue.clear()
		self.clock.tick(self.framerate)

		self.fps.append(self.clock.get_fps())

	def check_if_dead(self):
		if self.vars.planet_health < 1:
			avg_fps = 0
			for frame in self.fps:
				avg_fps += frame
			avg_fps = avg_fps / len(self.fps)

			logger.info(f"Scored: {self.vars.score}, Difficulty: {Difficulty(self.vars.diff).name}") # add length / abilities used in game to stats
			logger.debug(f"Average FPS: {avg_fps}")

			return False
		return True

	def draw_game_gui(self,vars):
		py.draw.rect(self.screen,(255,0,0),(850,900,self.vars.planet_health * self.vars.hp_gui_factor,60))
		py.draw.rect(self.screen,(0,255,0),(850,820, (Missile.COOLDOWN - Missile.TIMER.time) * (100/Missile.COOLDOWN),60))

		if self.inputs.mouse_pos[1] < 800:
			py.draw.line(self.screen, (255,0,0), (500,700), self.inputs.mouse_pos, 3)

	def check_collisions(self, vars):
		for threat in TH.GROUP:
			if threat.pos[1] > 750:
				threat.hit_planet(self.vars)
				pass

		# for abil in AH.AA:
		# 	py.draw.rect(self.screen,(255,255,255),abil.rect)
			
		hits = py.sprite.groupcollide(AH.AA, TH.GROUP, False, False)
		if hits:
			for abil,threat_array in hits.items():
				for threat in threat_array:
					abil.on_hit(threat)
					if threat.hp < 1:
						if hasattr(threat,"anim"):
							Animation.remove_anim(threat.anim)
						self.vars.score += threat.maxHP
						threat.kill()
						break


	def main_menu(self):
		AH.STATE = GameStates.START_MENU
		g.state = GameStates.START_MENU
		nums = load_number_sequence()

		while g.state == GameStates.START_MENU:
			self.screen.fill((0,0,0))
			self.screen.blit(icon_img,(0,0))
			self.inputs.keys()

			main_menu.update(self.inputs,self.blitQueue)

			self.screen.blits(self.blitQueue)
			self.blitQueue.clear()
			self.inputs.update()
			py.display.update()
			self.clock.tick(self.framerate)


	def end_screen(self):
		AH.AA.empty()
		AH.PA.clear()
		TH.GROUP.empty()
		Timer.ALL_TIMERS.clear()
		Animation.ALL_ANIMATIONS.clear()

		in_end = True
		frames = 0
		while in_end:
			self.screen.fill((0,0,0))
			self.screen.blit(loser_img,(0,0))

			self.display_score(self.vars.score,True)

			if frames > 500:
				in_end = False

			frames += 1
			py.display.update()
			self.clock.tick(self.framerate)

		g.state = GameStates.START_MENU


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

	@EventBus.on("enter_game")
	def enter_game():
		g.state = GameStates.IN_GAME

	@EventBus.on("update_difficulty")
	def update_difficulty(data):
		if g.inputs.diff < 5:
			g.inputs.diff += 1
		elif g.inputs.diff == 5:
			g.inputs.diff = 1
		data[0].image = data[1][g.inputs.diff]

	@EventBus.on("update_spawn_rate")
	def update_spawn_rate(args):
		args[0].period = (g.vars.ast_spawn_slope*g.vars.frames) + g.vars.ast_spawn_mod

	@EventBus.on("spawn_asteroid")
	def spawn_asteroids():
		# add new functions later to have different / random spawn configurations
		a = [
			# {"type":"asteroid","pos" : [500,-50],"hp" : 0,"dx" : 0,"dy" : 0,"img" : rubble_img }
			{"type":"asteroid","pos" : [500,-50],"hp" : 5,"dx" : 0.5,"dy" : 1.2,"img" : normal_img },
			{"type":"asteroid","pos" : [100,-50],"hp" : 12,"dx" : 0.3,"dy" : 0.7,"img" : metal_img },
			{"type":"asteroid","pos" : [900,-50],"hp" : 3,"dx" : -0.5,"dy" : 1.1,"img" : rubble_img },
			{"type":"asteroid","pos" : [300,-50],"hp" : 6,"dx" : 0.1,"dy" : 1.6,"img" : normal_img },
			{"type":"asteroid","pos" : [700,-50],"hp" : 3,"dx" : -0.3,"dy" : 0.9,"img" : rubble_img },
			{"type":"asteroid","pos" : [500,-50],"hp" : 2,"dx" : 0.3,"dy" : 1.8,"img" : rubble_img },
			{"type":"asteroid","pos" : [400,-50],"hp" : 11,"dx" : -0.15,"dy" : 0.5,"img" : metal_img },
			{"type":"asteroid","pos" : [200,-50],"hp" : 15,"dx" : -0.1,"dy" : 0.6,"img" : metal_img },
			{"type":"asteroid","pos" : [800,-50],"hp" : 7,"dx" : 0.1,"dy" : 1,"img" : normal_img },
			{"type":"asteroid","pos" : [250,-50],"hp" : 9,"dx" : 0.15,"dy" : 1.2,"img" : normal_img },
			{"type":"comet","pos":[60,-199],"path_pos":[150,200],"dx":0.22,"dy":0.8,"angle":105,"hp":25,"img" : comet_img },
			{"type":"comet","pos":[500,-199],"path_pos":[500,150],"dx":0.05,"dy":1.2,"angle":90,"hp":20,"img" : comet_img }
		]

		r = random.choice(a)
		if r["type"] == "asteroid":
			threat = Normal(r["pos"],r["hp"],r["dx"],r["dy"],r["img"])
		elif r["type"] == "comet":
			threat = Comet(r["pos"],r["path_pos"],r["dx"],r["dy"],r["angle"],r["hp"],r["img"])
		
		TH.GROUP.add(threat)

	



if __name__ == "__main__":
	g = Game()
	g.main_loop()


