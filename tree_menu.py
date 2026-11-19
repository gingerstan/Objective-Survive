from treelib import Tree, Node
from load_assets import *
import pygame as py
from input_handler import InputHandler

# one menu can contain multiple buttons
# each button can only have one function

class MenuSystem:
	def __init__(self):
		self.tree = Tree(node_class=Menu)
		self.active_menu = None

	def add_menu(self,menu,parent_name):
		if self.tree.size():
			self.tree.add_node(menu,parent=parent_name)
		else:
			self.tree.add_node(menu)
			self.active_menu = menu

	def update(self,inputs,blitQueue):
		elements = self.active_menu.elements
		left_click = inputs.left_click()
		mouse_pos = inputs.mouse_pos

		for element in elements:
			if left_click:
				if element.rect.collidepoint(mouse_pos):
					# print(f"Pressed a button!")
					print(f"Button Parent: {element.target}")
					self.active_menu = element.target


			blitQueue.append((element.image,element.pos))



# Menu superclass
class Menu(Node):
	def __init__(self,menu_name,menu_id,parent=None):
		super().__init__(menu_name,menu_id,parent)
		self.elements = []

# menu with a Static background image
class StaticMenu(Menu):
	def __init__(self,menu_name,menu_id,img=None,parent=None,pos=(0,0),data=None):
		super().__init__(menu_name,menu_id,parent)
		self.menu_name = menu_name
		self.menu_id = menu_id
		self.image = img
		self.parent = parent
		self.pos = pos
		self.data = data # contains information the menu needs, like object references

		self.rect = img.get_rect()
		self.rect.center = pos

	# return image to add to blitQueue
	def update(self):
		pass

	def add_elements(self,element_list):
		for element in element_list:
			self.elements.append(element)
			element.parent = self

# menu with an animated background
class AnimatedMenu(Menu):
	def __init__(self,menu_name,menu_id,anim,pos=(0,0)):
		super().__init__(menu_name,menu_id,pos)
		self.img = anim

	# return current anim frame to add to blitQueue
	def update(self):
		pass




# button for changing menus
class MenuButton:
	def __init__(self,pos,target,img):
		self.pos = pos
		self.target = target
		self.image = img

		self.rect = img.get_rect()
		self.rect.topleft = pos

	# can be another menu reference or a function to call
	def set_target(self,target):
		pass

# button for performaing a preset function
class FuncButton:
	pass





m1 = StaticMenu("Start","root",icon_img)
m2 = StaticMenu("Options","option",options_img)
m2a = StaticMenu("Graphics","graphics",empty_img)
m2b = StaticMenu("Keybinds","keybinds",bar_img)
m3 = StaticMenu("Difficulty","difficulty",loser_img)

m1_elements = [
	MenuButton((500,500),m2,metal_img),
	MenuButton((800,800),m3,death_img)
]
m1.add_elements(m1_elements)

m2_elements = [
	MenuButton((500,500),m2a,rubble_img),
	MenuButton((700,500),m2b,normal_img),
	MenuButton((100,100),m1,back_img)
]
m2.add_elements(m2_elements)

m2a_elements = [
	MenuButton((700,700),m2,speed_upgrade_img)
]
m2a.add_elements(m2a_elements)

m2b_elements = [
	MenuButton((700,700),m2,radius_upgrade_img)
]
m2b.add_elements(m2b_elements)

m3_elements = [
	MenuButton((500,500),m1,back_img)
]
m3.add_elements(m3_elements)

m = MenuSystem()
m.add_menu(m1,None)
m.add_menu(m2,m1.identifier)
m.add_menu(m2a,m2.identifier)
m.add_menu(m2b,m2.identifier)
m.add_menu(m3,m1.identifier)

m.tree.show()


py.init()
py.display.set_caption("menu testing")
screen = py.display.set_mode((1000,1000), 0, 32)
clock = py.time.Clock()
inputs = InputHandler()
blitQueue = []


debug = 0
run = True
while run:
	screen.fill((0,0,0))
	inputs.keys()

	if debug < 120:
		debug += 1
	else:
		debug = 0
		# print(m.active_menu.menu_name)

	m.update(inputs,blitQueue)

	screen.blits(blitQueue)

	blitQueue.clear()
	inputs.update()
	py.display.update()
	clock.tick(100)








# print(f"{m1.tag}, {m1.identifier}")
# print(f"{m2.tag}, {m2.identifier}")
