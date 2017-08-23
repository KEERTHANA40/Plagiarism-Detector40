from collections import Counter
import math
f1=input('enter file name=')
f2=input('enter file name=')
a=open(f1,'r')
b=open(f2,'r')
a1=a.read()
b1=b.read()
print(a1)
print(b1)
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

"""Dot product of frquencies"""
dot=0
i=0

while i<len(k1):
    
    dot=dot+(int(k1[i])*int(k2[i]))
        
    print (dot)
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
"""dot/mod"""
mod=mod1*mod2
res=dot/mod
print(res)
