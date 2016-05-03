###a=[1,x];   #// fucking devide is a mtarix
###b=[1,y];
##
##def addinverse(x,y):
##   return (x*y/(x+y));
##
c=0;
c1=0;
import math;
from decimal import *;
getcontext().prec= 50;

def combinations(iterable, r):
    return math.factorial(iterable)/math.factorial(iterable-r)/math.factorial(r);

for d in range(3,17):
    for i in range(1,d-1-1+1): #0
        for j in range(1,d-i-1+1):  #A
            for k in range(1,d-i-j+1):  #1
                count=(combinations((d-1),i)*combinations((d-i),j)*combinations((d-i-j),k)*(13**(d-i-j-k)));
                c=Decimal(c)+Decimal(count);
            
for d in range(17,17):
    for i in range(1,d-1-1+1): #0
        for j in range(1,d-i-1+1):  #A
            for k in range(1,d-i-j+1):  #1
                (count)=(combinations((d-1),i)*combinations((d-i),j)*combinations((d-i-j),k)*(13**(d-i-j-k)));
                (c1)=Decimal(c1)+Decimal(count);

print(c1);
print(c);
