#generate prime for easy reference
import math;
import euler_lib as E

g=open("primes.py","w");
a=[];
g.write("a=");
n=1000000
print("13414")
for i in range(n):
        if(E.is_prime(i)):
                a.append(i);

g.write(str(a));
g.close();

