import string
import matplotlib.pyplot as pyplot
def de_punctuation(line):
    for e in string.punctuation:
             if e in line:
                  line=line.replace(e," ")
    return line
def repeating_words(l):
    d={}
    for word in l:
        if word in d:
           d[word]+=1
        else:
           d[word]=1
    return d

def opening_file(myfile):
   c=0
   l1=[]
   for line in myfile:
       line=line.strip(string.whitespace+string.punctuation)
       line=de_punctuation(line)
       for word in line.split():
           l1.append(word.lower())
           c=c+1
   #print(l1)
   print(c)
   return repeating_words(l1)


final={}
myfile=open("58771-0.txt")
t=opening_file(myfile)
d=sorted((value,key)for(key,value) in t.items())
result=dict((y,x) for (x,y) in d)
#print(result)
key=list(result.values())
#print(key)
c=len(key)
for i in range(0,len(key)):
	final[key[i]]=c
	c=c-1
print(final)
pyplot.clf()
#pyplot.xscale(scale)
#pyplot.Yscale(scale)
pyplot.title("frequency vs rank")
pyplot.xlabel("frequncy")
pyplot.ylabel("rank")
x=list(final.keys())
y=list(final.values())
pyplot.plot(x,y)
pyplot.show()

