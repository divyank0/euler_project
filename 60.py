from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');


p=[2,3];
for i in range(5,10000,2):
    if is_prime(i):
        p.append(i);

#def function
print(len(p));

for j in range(857,len(p)):
    J=str(p[j]);
    print(J);
    
    for k in range(3,j):
     K=str(p[k]);
     if (is_prime(int(J+K))) & (is_prime(int(K+J))):
         
        for l in range(2,k):
         L=str(p[l]);
         if (is_prime(int(J+L))) & (is_prime(int(L+J)))    &   (is_prime(int(K+L))) & (is_prime(int(L+K))):
                                       
         
            for m in range(1,l):
                M=str(p[m]);
                if (is_prime(int(J+M))) & (is_prime(int(M+J))) & (is_prime(int(K+M))) & (is_prime(int(M+K))) & (is_prime(int(L+M))) & (is_prime(int(M+L))):
                    print(J,K,L,M);

                    for n in range(0,m):
                        N=str(p[n]);
                        if (is_prime(int(J+N))) & (is_prime(int(N+J))) & (is_prime(int(K+N))) & (is_prime(int(N+K))) & (is_prime(int(L+N))) & (is_prime(int(N+L))) & (is_prime(int(M+N))) & (is_prime(int(N+M))) :
                            print(J,K,L,M,N);
                            print("murgi");
            
    
                
                
            



  
