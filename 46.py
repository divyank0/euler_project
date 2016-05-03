from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(a):
        return all(a%i for i in range(2,a));

p=[2];
for j in range(3,10000,2):
        if is_prime(j)==True:
                p.append(j);
                continue;

        a=all(sqrt((j-k)/2)%1 for k in p);

        if a==True:
                print(j);
                sys.exit();
