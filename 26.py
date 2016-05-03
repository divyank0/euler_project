output=0;
m=0;
mold=0;
from decimal import *

getcontext().prec=1000;

for d in range(800,1000):
    m=0;
    
    for i in range(1,1000):
        for j in [0,1,2,3,4,5,6,7,]:
            
            if ((Decimal(10**i)-Decimal(10**j))/Decimal(d))%Decimal(1)==Decimal(0):
                m=i-j;
             
                break;
        if m!=0:
            break;
        
    if m>=mold:
        mold=m;
        output=d;
        print(d,1/d,m);

print(output);
            
