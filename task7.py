
import string

def sed(pattern_string,replacement_string,f1name,f2name):
	try:
		f1=open(f1name)
		lines=f1.readlines()
		f2=open(f2name,'w')

		for line in lines:
				new_line=line.replace(pattern_string,replacement_string)
				f2.write(new_line)
		f2.close()
	except:
		print("there is an error")


sed("the","a","58771-0.txt","58785-0.txt")
