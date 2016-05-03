from math import sqrt as sqrt;
from math import floor as floor;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,a));


for i in range(1,166666):
    m= list(sorted(str(i)));
    if list(sorted(str(2*i)))==m:
        if list(sorted(str(3*i)))==m:
            if list(sorted(str(4*i)))== m:
                print(i);
                if list(sorted(str(5*i)))== m:
                    if list(sorted(str(6*i)))== m:
                        print(i,"the real i");
        
