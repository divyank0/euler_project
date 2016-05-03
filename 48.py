from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(aa):
        return all(aa%i for i in range(2,aa));

s=10405071317
for i in range(11,1001):
        a= 10405071317;
        b=(i**i)%(10**10);
        s=s+b;
        

print(s);
sys.exit();
