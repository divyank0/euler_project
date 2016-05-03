from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,a));

#with open("54.txt") as file:
#    for line in file:
#        data.append(line.split(' '));

# def is_palindrome
tot=9999;
flag=0;
for j in range(1,10000):
    i=j;
    flag=0;
    count=0;
    while count<50:
        count=count+1;
        ireverse= int(str(i)[::-1]);
        isum=i+ireverse;
        if isum==int(str(isum)[::-1]):
            tot=tot-1;
            flag=1;
            count=50;
        i=isum;
        
    if flag==0:
        print(j,"repsect be");
            

print(tot);

    
