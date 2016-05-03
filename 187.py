#semi primes
#remainder=f(n)
import math;
from primes import a as primes;

c=0;

for i in range(1,100000):
   for j in range(1,10000):
      n=primes[i]*primes[j]
      if(n<10**8):
         c=c+1;
      else:
         break;

print(c);
d=math.sqrt(c);
e=d*d+d
e=e/2;
print(c,d,e)
