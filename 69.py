
import time
import math
def fact_primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def phi(n):
    phi = 1
    for i in list(set(fact_primes(n))):
        phi *= (1-1/i)
    return phi


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumenrate(a):
       if isprime:
           for n in range(i*i, limit, i):
               a[n] = False
    return a

limit = 10**6
tic = time.clock()
maxi = 0
for i in range(2, 10**6, 2):
    j = 1.0/phi(i)
    if j > maxi:
        maxi = j
        index = i
print(maxi, index, time.clock()-tic)
