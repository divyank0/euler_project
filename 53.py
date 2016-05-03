from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,a));

count=0;
for i in range(1,101):
    for j in range(2,i-1):
        if f(i)/(f(j)*f(i-j))>1000000:
            print(i,j);
            count=count+1;
