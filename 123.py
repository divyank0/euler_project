#f(n)= 2*n*p(n);
#remainder=f(n)

from primes import a as primes;

exceed=10000;
e=4;

for n in range(1,100000,2):
   p=primes[n];
   f=2*n*p
   f=f%(p*p)
   if(f>exceed):
      e=e+1;
      print(e-1,exceed,f,n,p);
      exceed=exceed*10;
   
   
   
