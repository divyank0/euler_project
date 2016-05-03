from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as factorial;
from fractions import Fraction as fr;
from decimal import *
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');


mat=[1]*100
mat[0]=0;
for i in range(1,34):
    mat[3*i-1]=2*i;
#print(mat);


def inter(b,a,n):
    n=n-1;
    if n==1:
        return(fr(a,b));
    
    f=mat[n-1]+fr(a,b);
    #print(f);
    return(inter(f.numerator,f.denominator,n));


nn=100; #nn>=2
result=2+inter(mat[nn-1],1,nn);


s=0;
for aa in str(result.numerator):
    s+=int(aa);

print(s);
    
