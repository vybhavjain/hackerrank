k1,k2=input().split(" ")
k1=int(k1) #number of people
k2=int(k2)
a=[]
for x in range(1,k1+1):
 a.append(x)
 a.append(0)
k3=2*k1-2

for t in range(1,k1):
    y=k3
    z=y
    if a[y]!=0:
     while a[z]!=0:
           z=z-1
     a[z]=a[y]
     #a[y]=0
     a.pop(y)

     k3=k3-1
#print(a)
#for t in range(k1):
a.pop()
#print(a)
for l in range(k2):
 num=int(input())
 print(a[num-1])
