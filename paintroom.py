num=int(input())

for x in range(0,num):
 t=input()
 max1=0
 max=0
 a=0
 b=0
 l=0
 c=0
 for y in t:
    l += 1
 a=t.count('R')
 b=t.count('B')
 c=t.count('G')
 if (a>=b) and (a>=c):
      max=a
 elif (b>=a) and (b>=c):
    max=b
 else:
    max=c
 max1=l-max
 print(max1)
