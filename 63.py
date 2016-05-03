from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');

count=0;
for power in range(1,10000):
    for i in range(1,10):
        if len(str(i**power))==power:
            print(i,power);
            count+=1;
print(count)
