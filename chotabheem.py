'''Bheem,Kalia,Dholu,Bholu and Chutki'''
num=int(input())



for x in range(num):
 variable=[1,2,3,4,5]
 t=int(input())
 for y in range(1,t):
  te=len(variable)
  temp=variable[0]
  for z in range(te-1):
        variable[z]=variable[z+1]
  variable[z+1]=temp
  variable.append(temp)
 if variable[0]==1:
   print("Bheem")
 elif variable[0]==2:
   print("Kalia")
 elif variable[0]==3:
   print("Dholu")
 elif variable[0]==4:
   print("Bholu")
 else:
   print("Chutki")

