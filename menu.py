import pygame as py
from input_handler import InputHandler
from load_assets import *


# the Menu class is a container for the whole menu system,
# it does not have any graphics of its own.

# the first Menu loaded into the system is the starting menu,
# after which order does not matter.

# create a list of Menus, create a list of MenuElements for each Menu, 
# use Menu.load_elements to assign MenuElements parent. then add all
# Menus to the MenuSystem


class MenuSystem:
	def __init__(self,screen,inputs,menu_list):
		self.screen = screen # pygame screen object
		self.inputs = inputs # button input handler
		self.menus = menu_list

	def update(self):
		pass



class Menu:
	def __init__(self,parent=None):
		self.parent = parent
		self.elements = []

	def load_elements(self, element_list):
		self.elements = element_list
		for element in self.elements:
			element.set_parent(self)

	def set_parent(self,parent):
		self.parent = parent
		
		
# maybe need to assign a layer to blit to
class MenuElement:
	def __init__(self,pos,img):
		self.pos = pos
		self.img = img
		self.parent = None

	def set_parent(self,parent):
		self.parent = parent


class Button(MenuElement):
	def __init__(self,pos,img):
		super().__init__(pos,img)
		self.pos = pos.copy()
		self.img = img
		self.parent = None

	def update(self):
		pass

	
class Static(MenuElement):
	def __init__(self,pos,img):
		super().__init__(pos,img)
		self.pos = pos.copy()
		self.img = img
		self.parent = None

	def update(self):
		pass




bg = Static([0,800],bar_img)
ability = Button([10,820],speed_upgrade_img)
upgrade_bar = [bg,ability]

bar_menu = Menu()
bar_menu.load_elements(upgrade_bar)

menus = [bar_menu]


py.init()
py.display.set_caption("menu testing")
screen = py.display.set_mode((1000,1000), 0, 32)
clock = py.time.Clock()
inputs = InputHandler()
m = MenuSystem(screen,inputs,menus)
run = True
while run:
	screen.fill((0,0,0))
	inputs.keys()


	inputs.update()
	py.display.update()
	clock.tick(100)


def open_menus(menu_system: MenuSystem):
	pass
	


