

def is_prime(a):
    if a>1:
        return all(a % i for i in range(2, a));
    else:
        return False;

primes=[2,3];
for i in range(4,1000):
    if is_prime(i):
        primes.append(i);

nmax=0;
amax=-1000;
bmax=0;
             

for p in primes:
    for b in range(2-p-1,1000):
        for n in range(0,1000):
            if not is_prime((n*n+b*n+p)):
                break;
        if n-1>nmax:
            nmax=n-1;
            amax=b;
            bmax=p;
            print(nmax,amax,bmax);
             
        
print(nmax,amax,bmax,amax*bmax);
