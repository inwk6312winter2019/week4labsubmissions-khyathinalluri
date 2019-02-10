class point():

	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y


	def __str__(self):
		return "%2d,%2d"%(self.x,self.y)


def add(p1,p2):
	sum=point()
	sum.x=p1.x+p2.x
	sum.y=p1.y+p2.y
	return sum

p1=point(4,5)
p2=point(8,3)
print(add(p1,p2))
