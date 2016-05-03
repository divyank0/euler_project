from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
from decimal import *
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');

def recur(b1):
    #print((1/b1)%1);
    return((1/b1)%1);
def diff(b1):
    #print(b1);
    return(Decimal((1/b1)//1));
    

def period(ai):
    getcontext().prec = 10000;
    a=Decimal(sqrt(ai));
    a0=a//1;
    rem=Decimal(a-a0);
    n=14;
    a1=[0]*n;
    #print(a1);
    a1[0]=int(a0)
    for i in range(1,n):
        (a1[i])=int(diff((rem)));
        (rem)=recur(rem);
    #print(a1);

    for index in range(1,n//2):
        flag=1;
        for y in range(1,n//2):
            if a1[y]!=a1[y+index]:
                flag=0;
              #  print(ii,a1[y],a1[y+index],index,y);
               # print(a1);
                break;
        if flag==1:
            print(index,ii);
            return(index);
            
                
                
                
                
                      
                

    
                         
        
    
data=[];
for ii in range(200,10001):
    if sqrt(ii)%1==0:
        continue;
    p=period(ii);
    #print(p,ii);
    data.append(p);
    
    
    
