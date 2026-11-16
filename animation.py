import pygame as py
white = (255,255,255)

def load_image_sequence(seq_prefix, num_of_frames,colorkey=(255,255,255)):
	frame_array = []
	for i in range(num_of_frames):
		frame = py.image.load(f"assets/{seq_prefix}_{i}.png")
		frame.set_colorkey(colorkey)
		frame_array.append(frame)

	return frame_array

def load_number_sequence():
	frame_array = []
	for i in range(10):
		frame = py.image.load(f"assets/{i}.png")
		frame.set_colorkey(white)
		frame_array.append(frame)

	return frame_array

class Animation:
	ALL_ANIMATIONS = []

	def __init__(self,seq_prefix,num_of_frames,frame_time,screen,pos,colorkey=(255,255,255),scale=1):
		Animation.ALL_ANIMATIONS.append(self)
		self.seq_prefix = seq_prefix
		self.num_of_frames = num_of_frames
		self.frame_time = frame_time # how many game frames one frame of the animation lasts for
		self.screen = screen

		self.frames = load_image_sequence(seq_prefix,num_of_frames,colorkey=colorkey)

		if scale != 1:
			for i in range(num_of_frames):
				self.frames[i] = py.transform.scale_by(self.frames[i],scale)

		self.frame_num = 0
		self.sub_frame_num = 0

		rect_width = int(self.frames[0].get_width()) / 2
		rect_height = int(self.frames[1].get_height()) / 2

		j = pos[0] - rect_width
		k = pos[1] - rect_height

		self.pos = (j,k)


	def play(self):
		if self.frame_num < self.num_of_frames:
			self.screen.blit(self.frames[self.frame_num],self.pos)
			if self.sub_frame_num < self.frame_time:
				self.sub_frame_num += 1
			else:
				self.sub_frame_num = 0
				self.frame_num += 1
			#print(f"frame:{self.frame_num}, sub-frame:{self.sub_frame_num}")
		else:
			Animation.ALL_ANIMATIONS.remove(self)


	def play_all():
		for anim in Animation.ALL_ANIMATIONS:
			anim.play()
		



class LoopingAnimation(Animation):
	def __init__(self,seq_prefix,num_of_frames,frame_time,screen,pos,colorkey=(255,255,255)):
		super().__init__(seq_prefix,num_of_frames,frame_time,screen,pos,colorkey=(255,255,255))
		pass

class PyDrawAnimation:
	def __init__(self):
		pass
