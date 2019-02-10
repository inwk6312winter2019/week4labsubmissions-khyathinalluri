import math
class point():
	"""this is a class used to find distance between two points"""

def print_point(self):
		print("(%g,%g)"%(self.x,self.y))



class rectangle():
	"""this is a class for recatngle"""

def move_rectangle(self,dx,dy):
	p = point()
	p.x=self.center.x+dx
	p.y=self.center.y+dy
	return p


ds=rectangle()
ds.center=point()
ds.center.x=0.0
ds.center.y=0.0
center=move_rectangle(ds,5,5)
print_point(center)

