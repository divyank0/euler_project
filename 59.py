from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


with open("59.txt") as file:
    data=eval('['+file.readlines()[0]+']');
    
#print(data);

#ord(the) = 116, 104 , 101, 

for i in range(97,123):
    print(i);
    for j in range(97,123):
        for k in range(97,123):
            key=[i,j,k];
            result=[];
            c=0;
            summ=0;
            for l in data:
                c=c+1;
                
                result.append(l^key[c%3]);
                summ=summ+(l^key[c%3]);
            for m in range(1, len(result)-3):
               if result[m-1]==ord('t'):
                if result[m]==ord("h"):
                   # print("yo");
                    if result[m+1]==ord('e'):
                        if result[m+2]==ord(' '):
                            print(i,j,k);
                            print(summ);

                
                
                
            



  
