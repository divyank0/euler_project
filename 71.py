from fractions import Fraction as f
import math
f1=f(2,5)
f2=f(3,7)

#d<10**6 n ?   3..7>2..5
#def numinc(f(a,b)):
#    return(f(a+1,b))
#def duminc(f(a,b)):
#    return(f(a,b+1);

a=5
b=2
l=10**6;

for i in range(200,l+1):
    for j in range(math.floor(a*i/b),math.floor(3*i/7)+1):
        if j/i>b/a:
            a=i;
            b=j;
            print(i,j);
            
                   
