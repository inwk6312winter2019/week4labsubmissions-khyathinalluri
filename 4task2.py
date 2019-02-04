import string
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


t={}
myfile=open("58771-0.txt")
res=len(opening_file(myfile))
t[res]="58771-0.txt"
myfile1=open("58785-0.txt")
res1=len(opening_file(myfile1))
t[res1]="58785-0.txt"
myfile2=open("pg58784.txt")
res2=len(opening_file(myfile2))
t[res2]="pg58784.txt"
k=sorted((value,key) for(key,value) in t.items())
print(k[0])

