import pygame as py
from python_event_bus import EventBus
from load_assets import diff_img

# class GUI_Element:
# 	def __init__(self, pos):

class Button:
	ALL_BUTTONS = []
	KEYS = None  # assigned in Game.__init__

	def __init__(self, pos, name, img, width=75,height=75):
		Button.ALL_BUTTONS.append(self)
		self.pos = pos.copy()
		self.name = name
		self.img = img
		self.rect = py.Rect(pos[0],pos[1],width,height)

	def draw(screen):
		for button in Button.ALL_BUTTONS:
			screen.blit(button.img,button.pos)	

	def update():
		for button in Button.ALL_BUTTONS:
			if Button.KEYS.left_click() and button.rect.collidepoint(Button.KEYS.mouse_pos):
				EventBus.call(button.name,Button.KEYS)



#####################
# MAIN MENU BUTTONS

difficulty = Button([800,700],"update_difficulty",diff_img)
