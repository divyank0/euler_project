from decimal import *
import math
getcontext().prec=105

s=0;
for i in range(2,100):
   if not(math.sqrt(i)%1==0):
      t=Decimal(i).sqrt();
      t=str(t).replace('.','')[:100]
      print(i,len(t))
      for j in t:
         s=s+int(j);
      
      
print(s);
