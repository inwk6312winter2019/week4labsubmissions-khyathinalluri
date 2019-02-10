class kangaroo():

	def __init__(self):
		self.pouch_contents=[]


	def __str__(self):
		return str(self.pouch_contents)

	def put_in_pouch(self,val):
			self.pouch_contents.append(val)


kanga=kangaroo()
roo=kangaroo()
roo.put_in_pouch("this is a kangaroo program")
kanga.put_in_pouch(roo)

for i in kanga.pouch_contents:
	print(i)
