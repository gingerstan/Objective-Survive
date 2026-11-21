from animation import load_from_spritesheet
from pygame import *
import pygame
from input_handler import InputHandler
from dataclasses import dataclass


char_dict = {}
chars = load_from_spritesheet()
for i in range(len(chars)):
	chars[i] = pygame.transform.scale_by(chars[i],1)

def fill_chars_dict():
	for i in range(26):
		char_dict[chr(i+65)] = chars[i] 
	char_dict[chr(32)] = chars[27]

fill_chars_dict()

# Assumes all rows are left aligned at the same x value.
# Saves the text box after rendering the first time.
class SimpleTextBox:
	CHAR_DICT = None
	def __init__(self,text,pos,x_spacing=50,y_spacing=50,scale=1):
		self.make_surface(text,pos,x_spacing,y_spacing,scale)

	def make_surface(self,text,pos,x_spacing=50,y_spacing=50,scale=1):
		self.text = text
		self.pos = pos
		self.x_spacing = x_spacing
		self.y_spacing = y_spacing
		self.scale = scale

		y_max = y_spacing # offset cause the loop misses last line break
		chars_in_row = []
		chars = 0
		for char in text:
			match char:
				case "\n":
					y_max += y_spacing
					chars_in_row.append(chars)
					chars = 0
				case "\t":
					chars += 4
				case _:
					chars += 1

		chars_in_row.append(chars)	

		max = 0
		for row_length in chars_in_row:
			if row_length > max:
				max = row_length

		x_max = max * x_spacing
		new_surf = pygame.surface.Surface((x_max,y_max))

		x = pos[0]
		y = pos[1]
		lowered = text.upper()
		for char in lowered:
			match char:
				case "\n":
					x = pos[0]
					y += y_spacing
				case "\t":
					x += 4 * x_spacing	
				case _:
					new_surf.blit(SimpleTextBox.CHAR_DICT[char],(x-pos[0],y-pos[1]))
					x += x_spacing

		self.image = pygame.transform.scale_by(new_surf,self.scale)

	# returns pre-computed text box
	def update(self,blitQueue):
		blitQueue.append((self.image,self.pos))


test = """holy fucking SHIT
	this is a MASSIVE STRING\nNO WAY THIS works\nhuuuuuge
	       space"""	

test2 = """OHHHH MY GODDDDD
WTF AHHHHHH"""

test3 = "therea	rean\ntelope"

# adds text wrapping at a certain width
class BoundedTextBox:
	CHAR_DICT = None
	def __init__(self,text,pos,width,x_spacing=50,y_spacing=50,scale=1):
		self.make_surface(text,pos,width,x_spacing,y_spacing,scale)

	def make_surface(self,text,pos,width,x_spacing=50,y_spacing=50,scale=1):
		self.text = text
		self.pos = pos
		self.width = width
		self.x_spacing = x_spacing
		self.y_spacing = y_spacing
		self.scale = scale

		y_max = self.y_spacing # offset cause the loop misses last line break
		x_max = 0
		for char in text:
			match char:
				case "\n":
					y_max += self.y_spacing
					x_max = 0
				case "\t":
					x_max += 4 * x_spacing
				case _:
					x_max += x_spacing

			if x_max + x_spacing > width:
				y_max += self.y_spacing
				x_max = 0

		print(f"{width}, {y_max}")
		new_surf = pygame.surface.Surface((width,y_max))

		x = 0
		y = 0
		self.y_spacing = y_spacing
		lowered = text.upper()
		for char in lowered:
			match char:
				case "\n":
					x = 0
					y += self.y_spacing
				case "\t":
					x += 4 * x_spacing	
				case _:
					new_surf.blit(BoundedTextBox.CHAR_DICT[char],(x,y))
					x += x_spacing

			if x + x_spacing > width:
				y += self.y_spacing
				x = 0

		self.surf = pygame.transform.scale_by(new_surf,self.scale)

	# returns pre-computed text box
	def update(self,blitQueue):
		blitQueue.append((self.surf,self.pos))

SimpleTextBox.CHAR_DICT = char_dict
BoundedTextBox.CHAR_DICT = char_dict

bound = BoundedTextBox(test3,(300,700),300)
#simple = SimpleTextBox(test,(0,0),scale=1)	       	
def testing():
	pygame.init()
	pygame.display.set_caption("menu testing")
	screen = pygame.display.set_mode((1000,1000), 0, 32)
	clock = pygame.time.Clock()
	IH = InputHandler()
	blitQueue = []

	debug = 0
	count = 0
	run = True
	while run:
		screen.fill((0,0,0))
		IH.keys()

		if debug < 120:
			debug += 1
		else:
			debug = 0
			#simple.make_surface(test2,(0,0))
			print(clock.get_fps())


		#simple.update(blitQueue)
		bound.update(blitQueue)

		screen.blits(blitQueue)
		IH.update()
		blitQueue.clear()
		pygame.display.update()
		clock.tick(165)


testing()

