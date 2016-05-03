from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(aa):
        return all(aa%ii for ii in range(2,floor(sqrt(aa))+1));

s=0;
p=[];

#no would have 3 ***

for i in range(10000,100000):
        if is_prime(i):
                p.append(i);

pp=[];
count=0;
for j in p:
        jstr=str(j);
        count=0;
        for ji in range(0,5):
                for jj in range(ji,5):
                        if jstr[ji]==jstr[jj]:
                                count=count+1;

        if count==3:
                pp.append(j);
                print(j);
        
