import pygame as py, sys
from pygame.locals import QUIT
from python_event_bus import EventBus

class InputHandler:
	def __init__(self):
		self.left_mouse = False
		self.left_mouse_prev = False

		self.right_mouse = False
		self.right_mouse_prev = False

		self.mouse_pos = (0,0)

	def keys(self):
		for event in py.event.get():
			if event.type == QUIT:
				py.quit()
				sys.exit()

			if event.type == py.MOUSEBUTTONDOWN:
				if py.mouse.get_pressed()[0]:
					self.left_mouse = True
				if py.mouse.get_pressed()[2]:
					self.right_mouse = True

			if event.type == py.MOUSEBUTTONUP:
				if not py.mouse.get_pressed()[0]:
					self.left_mouse = False
					EventBus.call("left_click")
				if not py.mouse.get_pressed()[2]:
					self.right_mouse = False

		self.mouse_pos = py.mouse.get_pos()

	def left_click(self):
		return not self.left_mouse and self.left_mouse_prev 

	def right_click(self):
		return not self.right_mouse and self.right_mouse_prev

	def update(self):
		self.left_mouse_prev = self.left_mouse
		self.right_mouse_prev = self.right_mouse