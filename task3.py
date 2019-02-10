class Time():
	"""this class is used to make modifications in time"""


def print_time(self):
	print("current-time-{}:{}:{}".format(self.hours,self.min,self.seconds))






t=Time()
t.hours=8
t.min=54
t.seconds=56
print_time(t)

