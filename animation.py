import pygame as py
white = (255,255,255)

class Animation:
	ALL_ANIMATIONS = []
	SCREEN = None
	HIDDEN = False

	def __init__(self, seq_prefix, pos, colorkey=(255,255,255), scale=1, angle=0, loop=False):
		Animation.ALL_ANIMATIONS.append(self)
		seq = Animation.SEQUENCES[seq_prefix]

		self.num_of_frames = seq["num_of_frames"]
		self.frame_time = seq["frame_time"] # how many game frames one frame of the animation lasts for
		self.frames = seq["frames"].copy()
		self.angle = angle
		self.loop = loop

		if scale != 1:
			for i in range(self.num_of_frames):
				self.frames[i] = py.transform.scale_by(self.frames[i],scale)

		if angle != 0:
			for i in range(self.num_of_frames):
				self.frames[i] = py.transform.rotate(self.frames[i],self.angle)

		self.frame_num = 0
		self.sub_frame_num = 0

		rect_width = int(self.frames[0].get_width()) / 2
		rect_height = int(self.frames[1].get_height()) / 2

		j = pos[0] - rect_width
		k = pos[1] - rect_height

		self.pos = (j,k)


	def play(self, blitQueue):
		if self.frame_num < self.num_of_frames:
			if not Animation.HIDDEN:
				blitQueue.append((self.frames[self.frame_num],self.pos))
			if self.sub_frame_num < self.frame_time:
				self.sub_frame_num += 1
			else:
				self.sub_frame_num = 0
				self.frame_num += 1
		else:
			if self.loop:
				self.frame_num = 0
				self.sub_frame_num = 0
			else:
				Animation.ALL_ANIMATIONS.remove(self)


	def play_all(blitQueue):
		for anim in Animation.ALL_ANIMATIONS:
			anim.play(blitQueue)

	def remove_anim(anim):
		Animation.ALL_ANIMATIONS.remove(anim)

	def hide():
		Animation.HIDDEN = True

	def show():
		Animation.HIDDEN = False


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
		frame.convert()
		frame_array.append(frame)

	return frame_array

def load_all_sequences(sequences):
	for name,array in sequences.items():
		sequences[name]["frames"] = load_image_sequence(name,sequences[name]["num_of_frames"])

	return sequences

# TODO: load sequences in from another file instead of here
sequences = {
	"death" : {
		"frames" : [],
		"num_of_frames" : 11,
		"frame_time" : 7
	},
	"cometPath" : {
		"frames" : [],
		"num_of_frames" : 7,
		"frame_time" : 9
	},

}
Animation.SEQUENCES = load_all_sequences(sequences)