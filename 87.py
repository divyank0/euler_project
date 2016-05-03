import math
import eulerLibs
q=50000000;
n=(q)**(1/4);
n=int(n);
count=0;
c1=0
kcount=1
primes=[];
for i in range(1000):
   if(eulerLibs.is_prime(i)):
      primes.append(i);
      

for i in range(2  ,n+1):
   if (i in primes):
      ix=(q-i**4)**(1/3);
      ix=int(ix);
      for j in range(1,ix+1):
         if (j in primes):
            jx=(q-i**4-j**3)**(1/2);
            jx=int(jx);
            c1=0;
            for k in range(1,jx+1):
               if (k in primes):
                  
                  c1=c1+1
            print(i,j,c1)
            count=count+c1;
      
print(count)
