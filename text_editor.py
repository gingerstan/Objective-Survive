from animation import load_from_spritesheet
from pygame import *
import pygame
from input_handler import InputHandler
from dataclasses import dataclass


char_dict = {}
chars = load_from_spritesheet()
for i in range(len(chars)):
	chars[i] = pygame.transform.scale_by(chars[i],0.50)

def fill_chars_dict():
	for i in range(26):
		char_dict[chr(i+97)] = chars[i] 
	char_dict[chr(32)] = chars[27]

fill_chars_dict()

# Assumes all rows are left aligned at the same x value.
# Saves the text box after rendering the first time.
class SimpleTextBox:
	CHAR_DICT = None
	def __init__(self,text,pos,x_spacing=25,y_spacing=25,scale=1):
		self.make_surface(text,pos,x_spacing,y_spacing,scale)

	def make_surface(self,text,pos,x_spacing=25,y_spacing=25,scale=1):
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
		lowered = text.lower()
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

		self.surf = pygame.transform.scale_by(new_surf,1)

	# returns pre-computed text box
	def update(self,blitQueue):
		blitQueue.append((self.surf,self.pos))

SimpleTextBox.CHAR_DICT = char_dict

test = """holy fucking SHIT
	this is a MASSIVE STRING\nNO WAY THIS works\nhuuuuuge
	       space"""	

simple = SimpleTextBox(test,(0,0))	       	
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

		if debug < 100:
			debug += 1
		else:
			if count == 35:
				count=0
			else:
				count+=1
			debug = 0
			print(clock.get_fps())


		simple.update(blitQueue)

		screen.blits(blitQueue)
		IH.update()
		blitQueue.clear()
		pygame.display.update()
		clock.tick(165)


testing()