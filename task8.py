import os
import hashlib

def walk(songs,f2):
	for name in os.listdir(songs):
		path=os.path.join(songs,name)
		if os.path.isfile(path):
			if path.endswith(".mp3"):
				#print(path)
				check_func(path,f2)
		else:
			walk(path,f2)


def md5checksum(filepath):
	checksum=hashlib.md5(open(filepath,'rb').read()).hexdigest()
	print(checksum)
	return checksum

def check_func(f1,f2):
	if md5checksum(f1)==md5checksum(f2):
			print(True)
	else:
			print(False)

walk("/home","1.mp3")


