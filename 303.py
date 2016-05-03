#semi primes
#remainder=f(n)
#s=8480933482255137 + 
import math;
from primes import a as primes;

numbers=[0,1,2];
n=17;
for ii in range(1,2):
   for i in range(2,n):
      y=[];
      for j in [1,2]:
         x=[];
         for k in numbers:
            z=j*10**(i-1) + k;
            x.append(z);
         y=y+x;
      numbers=numbers+y;

numbers.sort();
numbers=set(numbers[2:])
print("murgi ka")
s=1;

for i in range(2,10000+1):
   #print(i);
   for j in numbers:
      if(j%i==0):
         k=j//i;
         s=s+k;
   if(j%i!=0):
      print("error ");
      print(i,j)
      
      
      
      
      
      
