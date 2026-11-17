from python_event_bus import EventBus

class Timer:
	ALL_TIMERS = []

	def __init__(self, end_time: int):
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

	def kill(self):
		Timers.ALL_TIMERS.remove(self)


class EventTimer:
	def __init__(self, period: int, eventName: str, *args):
		Timer.ALL_TIMERS.append(self)
		self.period = period
		self.time = 0
		self.eventName = eventName
		self.args = args
		self.active = True

	def update(self):
		if self.active:
			if self.time < self.period:
				self.time += 1
			else:
				self.time = 0
				if len(self.args) != 0:
					EventBus.call(self.eventName, self.args)
				else:
					EventBus.call(self.eventName)

	def toggle(self):
		self.active = not self.active

	def kill(self):
		Timers.ALL_TIMERS.remove(self)

	def set_period(self, new_period):
		self.period = new_period


# class LoopTimer:
# 	def __init__(self, end_time: int):
# 		Timer.ALL_TIMERS.append(self)
# 		self.loop_period = loop_period
# 		self.time = 0
# 		self.active = True

# 	def update(self):
# 		if self.active:
# 			if self.time < self.loop_period:
# 				self.time += 1
# 			else:
# 				self.time = 0

# 	def toggle(self):
# 		self.active = not self.active

# 	def update_timers():
# 		for timer in Timer.ALL_TIMERS:
# 			timer.update()

# 	def kill(self):
# 		Timers.ALL_TIMERS.remove(self)