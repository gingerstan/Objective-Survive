from dataclasses import dataclass
from pygame import image


# the Menu class is a container for the whole menu system,
# it does not have any graphics of its own.

# the first Menu loaded into the system is the starting menu,
# after which order does not matter.


class MenuSystem:
	def __init__(self,screen,inputs,menu_list):
		self.screen = screen # pygame screen object
		self.inputs = inputs # button input handler
		self.menus = menu_list



class Menu:
	def __init__(self,element_list):
		self.elements = []
		for element in self.elements:
			element.set_parent = self
		

class MenuElement:
	def __init__(self,pos,img,parent):
		self.pos = pos
		self.img = img
		self.parent = parent

	def set_parent(self,parent):
		self.parent = parent


class Button(MenuElement):
	def __init__(self,pos,img,parent=None):
		super().__init__(pos,img,parent)
		self.pos = pos.copy()
		self.img = img
		self.parent = parent

	def update(self):
		pass

	
class Statics(MenuElement):
	def __init__(self,pos,img,parent=None):
		super().__init__(pos,img,parent)
		self.pos = pos.copy()
		self.img = img
		self.parent = parent

	def update(self):
		pass


# use to open the main menu of a menu system
def open_menu(menu: Menu):



