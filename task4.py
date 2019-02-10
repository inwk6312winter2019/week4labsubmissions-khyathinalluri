class Time():
	"""this class is used to make modifications in time"""


def print_time(self):
	return (self.hours,self.min,self.seconds)

def is_after(t1,t2):
	return (print_time(t1)>print_time(t2))



t1=Time()
t2=Time()
t1.hours=12
t1.min=54
t1.seconds=56
t2.hours=11
t2.min=32
t2.seconds=14

#print(print_time(t1))
#print(print_time(t2))
print(is_after(t1,t2))

