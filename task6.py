class points():
	"""this is a class for points"""

def add(self,c):
	sum=points()
	print(type(c))
	if type(c) ==tuple:
		sum.x=self.x+c[0]
		sum.y=self.y+c[1]
		return sum.x,sum.y
	else:
		sum.x=self.x+c.x
		sum.y=self.y+c.y
		return sum.x,sum.y


t1=points()
t1.x=4
t1.y=3
t2=points()
t2.x=5
t2.y=5
#c=(3,4)
print(add(t1,t2))
#print(add(t1,c))
