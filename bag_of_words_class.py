import math
class bag_of_words(object):
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def file(self,f1):
        self.f1=f1
        #bag_of_words.__init__(self,f1,f2)   #importing data attributes of class 'bag_of_words'
        """Importing and reading the files"""
        a=open(f1,'r')
        a1=a.read().replace("\n"," ")
        print("file1 matter=",a1)
        return a1
    def word_freq(self,s1,c1):
        self.s1=s1
        self.c1=c1
        """Calculating the frquency of words in the files 'file1' and 'file2'"""
        l=[]
        l1=[]
        d1={}
        for i in c1:
            c=0
            if i not in l:
                l.append(i)
                for j in s1:
                    if i==j:
                        c=c+1
                l1.append(c)
        d1=dict(zip(l,l1))
        print(d1)
        k1=list(d1.values())
        print(k1)
        return k1
    def dot_product(self,d,e):
        self.d=d
        self.e=e
        """Dot product of frquencies"""
        dot=0
        i=0
        while i<len(d):
            dot=dot+(int(d[i])*int(e[i]))
            i=i+1
        print("dot=",dot)
        return dot
    def mod(self,d):
        self.d=d
        """modulus of frequencies"""
        sum1=0
        for i in range(len(d)):
            sq1=int(d[i])**2
            sum1=sum1+sq1
            mod1=math.sqrt(sum1)
        print(mod1)
        return mod1
    def plag_perc(self,g,h,f):
        self.g=g
        self.h=h
        self.f=f
        """dot/mod"""
        mod=g*h
        res=f/mod
        res1=res*100
        print("plagariasm percentage=",res1,"%")
        
        

f1=input('enter file name=')
f2=input('enter file name=')
w=bag_of_words(f1,f2)   #Calling 'bag_of_words' class with attributes f1,f2
a=w.file(f1)         #calling the method 'file' individually for f1 and f2
b=w.file(f2)
s1=a.lower().split(" ") #converting string into list
s2=b.lower().split(" ")
c1=s1+s1               #concatenating the strings
print(c1)
d=w.word_freq(s1,c1)    #calling method 'word_freq' individually for a and b  
e=w.word_freq(s2,c1)
f=w.dot_product(d,e)    #calling 'dot_product' method
g=w.mod(d)              #calling 'mod' method
h=w.mod(e)
r=w.plag_perc(g,h,f)    #calling 'plag_perc' method

            

