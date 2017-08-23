import math
def file(f1,f2):
    """Importing and reading the files"""
    a=open(f1,'r')
    b=open(f2,'r')
    a1=a.read().replace("\n"," ")
    b1=b.read().replace("\n"," ")
    print("file1 matter=",a1)
    print("file2 matter=",b1)
    word_freq(a1,b1)    #calling 'word_freq' function
def word_freq(a1,b1):
    """Calculating the frquency of words in the files 'file1' and 'file2'"""
    s1=a1.lower().split(" ")
    s2=b1.lower().split(" ")
    print(s1,s2)
    s=s1+s2
    print(s)
    l=[]
    l1=[]
    d={}
    d1={}
    l2=[]
    l3=[]
    for i in s:
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
    for i in s:
        y=0
        if i not in l2:
            l2.append(i)
            for j in s2:
                if i==j:
                    y=y+1
            l3.append(y)
    d2=dict(zip(l2,l3))
    print(d2)
    k2=list(d2.values())
    print(k2)
    dot_product(k1,k2)  #calling 'dot_product' function
def dot_product(k1,k2):
    """Dot product of frquencies"""
    dot=0
    i=0
    while i<len(k1):
        dot=dot+(int(k1[i])*int(k2[i]))
        i=i+1
    print("dot=",dot)
    """modulus of frequencies"""
    sum1=0
    for i in range(len(k1)):
        sq1=int(k1[i])**2
        sum1=sum1+sq1
        mod1=math.sqrt(sum1)
    print(mod1)
    sum2=0
    for i in range(len(k2)):
        sq2=int(k2[i])**2
        sum2=sum2+sq2
        mod2=math.sqrt(sum2)
    print(mod2)
    plag_perc(mod1,mod2,dot)    #calling 'plag_perc' function
def plag_perc(mod1,mod2,dot):
    """dot/mod"""
    mod=mod1*mod2
    res=dot/mod
    res1=res*100
    print("plagariasm percentage=",res1,"%")
def main():
    f1=input('enter file name=')
    f2=input('enter file name=')
    file(f1,f2) #calling the 'file' function
main()
