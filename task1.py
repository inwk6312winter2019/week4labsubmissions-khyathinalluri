import math
class point(object):
	"""this is a class used to find distance between two points"""


def distance_between_points(self):
	result=math.sqrt(self.x**2+self.y**2)
	print(result)

ds=point()
ds.x=60
ds.y=80
distance_between_points(ds)

