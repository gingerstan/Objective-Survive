from treelib import Tree, Node
from load_assets import *
import pygame as py
from input_handler import InputHandler
from python_event_bus import EventBus

class MenuSystem:
	def __init__(self):
		self.active_menu = None
		self.menus = []
		self.data = {} # used to contain references to need data

		self.menu_elements = []

	def add_menu(self,menu):
		self.menus.append(menu)
		if not self.active_menu:
			self.active_menu = menu

	def update(self,inputs,blitQueue):
		elements = self.active_menu.elements
		left_click = inputs.left_click()
		mouse_pos = inputs.mouse_pos

		blitQueue.append((self.active_menu.image,self.active_menu.pos))
		
		# if len(self.menu_elements):
		# 	blitQueue.append(self.menu_elements[-1])
		# 	blitQueue.extend((x.image,x.pos) for x in self.menu_elements[-1] if hasattr(x,"image"))
		blitQueue.extend(self.menu_elements)

		for element in elements:
			if left_click and element.rect.collidepoint(mouse_pos):
				match element:
					case MenuButton():
						if element.keep_prev_menu:
							self.menu_elements.append((self.active_menu.image.copy(),self.active_menu.pos.copy()))
							self.menu_elements.extend((x.image,x.pos) for x in self.active_menu.elements if hasattr(x,"image"))
						else:
							self.menu_elements.clear()
							
						self.active_menu = element.target
						if hasattr(element.target,"image"):
							blitQueue.append((element.target.image,element.target.pos))
			
					case FuncButton():
						element.update()
					case _:
						continue

			blitQueue.append((element.image,element.pos))



# menu with a Static background image
class StaticMenu:
	def __init__(self,menu_name,image=None,pos=[0,0],data=None):
		self.elements = []
		self.menu_name = menu_name
		self.pos = pos
		self.data = data # contains information the menu needs, like object references
		self.image = image

	# return image to add to blitQueue
	def update(self):
		pass

	def add_elements(self,element_list):
		for element in element_list:
			self.elements.append(element)
			element.parent = self

# menu with an animated background
# class AnimatedMenu:
# 	def __init__(self,menu_name,menu_id,anim,pos=(0,0)):
# 		self.img = anim

# 	# return current anim frame to add to blitQueue
# 	def update(self):
# 		pass




# button for changing menus
class MenuButton:
	def __init__(self,pos,target,img,keep_prev_menu=True):
		self.pos = pos
		self.target = target
		self.image = img
		self.keep_prev_menu= keep_prev_menu

		self.rect = img.get_rect()
		self.rect.topleft = pos

	def update(self,mouse_pos):
		return self.rect.collidepoint(mouse_pos)


# button for performaing a preset function
class FuncButton:
	def __init__(self,pos,func,img,args=None):
		self.pos = pos
		self.func = func
		self.args = args # tuple [] of args for func, emepty if no args
		self.image = img

		self.rect = img.get_rect()
		self.rect.topleft = pos

	def update(self):
		EventBus.call(self.func)



# py.init()
# py.display.set_caption("menu testing")
# screen = py.display.set_mode((1000,1000), 0, 32)
# clock = py.time.Clock()
# inputs = InputHandler()
# blitQueue = []


# debug = 0
# run = True
# while run:
# 	screen.fill((0,0,0))
# 	inputs.keys()

# 	if debug < 120:
# 		debug += 1
# 	else:
# 		debug = 0

# 	main_menu.update(inputs,blitQueue)

# 	screen.blits(blitQueue)

# 	blitQueue.clear()
# 	inputs.update()
# 	py.display.update()
# 	clock.tick(100)

# m1 = StaticMenu("Start",image=icon_img)
# m2 = StaticMenu("Options",image=options_img)
# m2a = StaticMenu("Graphics",image=empty_img)
# m2b = StaticMenu("Keybinds",image=bar_img,pos=(0,800))
# m3 = StaticMenu("Difficulty",image=loser_img)

# m1_elements = [
# 	MenuButton((500,500),m2,metal_img),
# 	MenuButton((800,800),m3,death_img),
# 	FuncButton((100,100),print,rubble_img,"fuck")
# ]
# m1.add_elements(m1_elements)

# m2_elements = [
# 	MenuButton((500,500),m2a,rubble_img),
# 	MenuButton((700,500),m2b,normal_img),
# 	MenuButton((100,100),m1,back_img)
# ]
# m2.add_elements(m2_elements)

# m2a_elements = [
# 	MenuButton((700,700),m2,speed_upgrade_img)
# ]
# m2a.add_elements(m2a_elements)

# m2b_elements = [
# 	MenuButton((700,700),m2,radius_upgrade_img)
# ]
# m2b.add_elements(m2b_elements)

# m3_elements = [
# 	MenuButton((500,500),m1,back_img)
# ]
# m3.add_elements(m3_elements)

# m = MenuSystem()
# m.add_menu(m1)
# m.add_menu(m2)
# m.add_menu(m2a)
# m.add_menu(m2b)
# m.add_menu(m3)










# print(f"{m1.tag}, {m1.identifier}")
# print(f"{m2.tag}, {m2.identifier}")
