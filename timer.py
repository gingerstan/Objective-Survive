

class Timer:
	ALL_TIMERS = []

	def __init__(self, end_time):
		Timer.ALL_TIMERS.append(self)
		self.end_time = end_time
		self.time = 0
		self.active = False

	def update(self):
		if self.active:
			if self.time < self.end_time:
				self.time += 1
			else:
				self.time = 0
				self.active = False

	def toggle(self):
		self.active = not self.active

	def update_timers():
		for timer in Timer.ALL_TIMERS:
			timer.update()
