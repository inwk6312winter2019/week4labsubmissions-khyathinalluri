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



myfilew=open("words.txt")
k=[]
for line in myfilew:
    line=line.strip()
    k.append(line)
#print(k)

myfile=open("58771-0.txt")
t=list(opening_file(myfile).keys())
#print(t)

n=set(t)-set(k)
print(n)
print("no of words in words.txt:" ,len(n))
print("no of  obscure words are:",len(t)-len(n))
