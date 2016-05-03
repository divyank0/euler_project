from math import sqrt as sqrt;
from math import floor as floor;
import sys;

def is_prime(a):
        return all(a%i for i in range(2,a));

p=[2];

for jj in range(3,100000):
        if is_prime(jj)==True:
                p.append(jj);

print("HELLO");
for j in range(100000,200000,1):
        a=0;
        b=0;
        c=0;
        d=0;
        if j in p:
                continue;
        
        for k in p:
                if j%k==0:
                        a=a+1;
        if a!=4:
                continue;
        
        for kkk in p:
                if (j+1)%kkk==0:
                        b=b+1;         
        if b!=4:
                continue;
        
        if a==4and b==4:
                print(j);

                
        for kk in p:
                if (j+2)%kk==0:
                        c=c+1;
                if (j+3)%kk==0:
                        d=d+1;
        if a==4 and b==4 and c==4 and d==4:
                print(j,a,b,c,d)
                sys.exit();
