from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(aa):
        return all(aa%ii for ii in range(2,floor(sqrt(aa))+1));

s=0;
p=[];

for i in range(2,1000000):
        if is_prime(i)==True:
                p.append(i);

print("ffff");

c=0;
s=0;
cc=0;
count=0;
for j in p:
        cc=0;
        s=j;
        c=c+1;
        for jj in p[c:]:
                cc=cc+1;
                s=s+jj;
                if s>1000000:
                        break;
                if is_prime(s) :
                        if cc>count:
                                count=cc
                                print(cc,s);
                        
