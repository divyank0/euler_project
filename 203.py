#semi primes
#remainder=f(n)
import math;
from primes import a as primes;

tri=[1];
data=[];
n=51
def nextRow(row):
   l=len(row);
   nRow=[];
   iOld=0;
   for i in row:
      nRow.append(iOld+i);
      iOld=i;
   nRow.append(iOld)
   return nRow


for i in range(1,n+1):
   #print(tri);
   data=data+tri;
   tri=nextRow(tri)
      
kata=data[:];
print(set(kata));
kata=set(kata);
s=0;
for i in kata:
   s=s+int(i);
   for j in range(2,100,1):
      if(i%(j*j)==0):
         s=s-int(i)
         break;
print(s);
         
