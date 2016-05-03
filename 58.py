from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));

#with open("54.txt") as file:
#    for line in file:
#        data.append(line.split(' '));

diag1=[]; #TR
diag2=[];   #TL
diag3=[];   #BL
diag4=[];   #BR
count=0;
tot=1;
primetot=0;
#not including 1, will be used in calculations only.
for i in range(3,100000,2):
    count=count+2;
    tot=tot+4;
    
    n=(i-2)**2 + count;
    diag1.append(n);
    if (is_prime(int(n))):
        primetot+=1;

    n=((((i-2)**2) +i*i)/2);
    diag2.append((((i-2)**2) +i*i)/2);
    if (is_prime(int(n))):
        primetot+=1;

    

    n=(i*i-count);
    diag3.append(i*i-count);
    if (is_prime(n)):
        primetot+=1;

    diag4.append(i*i);
    

    print(primetot/tot);
    if primetot/tot <0.1 :
        print(i);
        sys.exit();
        
        

    

#print(diag1,diag2,diag3,diag4);
    


