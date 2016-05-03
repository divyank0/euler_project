from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(aa):
        return all(aa%i for i in range(2,aa));

s=0;
p=[];

for i in range(1000,10000):
        if is_prime(i)==True:
                p.append(i);


c=0;
cc=0;
for j in p:
        c=c+1;
        cc=0;
        k=sorted(str(j));
        
        for jj in p[c:]:
                cc=cc+1
                if sorted(str(jj))==sorted(str(j)) and jj!=j:
                        for jjj in p[cc+1:]:
                                if sorted(str(jjj))==k and jjj!=jj and jjj!=j and jjj-jj==jj-j:
                                        print(j,jj,jjj);
                                    
                


print(s);
