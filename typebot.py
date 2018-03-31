num=int(input())
import re

def largest_substring(string):

 length = 0
 x=0
 y=0

 for y in range(len(string)):
    for x in range(len(string)2):
        substring = string[y:x]
        if len(list(re.finditer(re.escape(substring),string))) > 1  and len(substring) > length:
            match = substring
            length = len(substring)
 return len(match)

for x in range(0,num):
 t=input()
 max=0
 l=0
 l1=0
 for w in t:
    l += 1
 max=l
 q=largest_substring(t)
 l2=l-q+1
 print(l-l2)
