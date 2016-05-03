import math;
import eulerLibs;

#repunit
def genRepunit(a):
    s="";
    for ai in range(a):
        s=s+ '1';
    return int(s);

def A(n):
    t=0;
    r=0;
    for i in range(1,100000):
        print(i)
        r=r+10**(i-1)%n;
        if(r%n==0):
            return i;
    print("fuckled"+n);
    return -1;
        
    
maxx=0;
for i in range(0,100000,10):
    k=0;
    j=i+1;
    if(not eulerLibs.is_prime(j)):
        k=A(j);
    if(k>maxx):
        maxx=k;
        print(j,k);
    
    j=i+3;
    if( not eulerLibs.is_prime(j)):
        k=A(j);
    if(k>maxx):
        maxx=k;
        print(j,k);

    j=i+7;
    if(not eulerLibs.is_prime(j)):
        k=A(j);
    if(k>maxx):
        maxx=k;
        print(j,k);

    j=i+9;
    if( not eulerLibs.is_prime(j)):
        k=A(j);
    if(k>maxx):
        maxx=k;
        print(j,k);
    
    
