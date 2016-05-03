from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');

data9=[];
data=[];
datasort=[];
datasortcount=[];
for i in range(4641,10000):
    j=i**3;
    jsort=sorted(str(j));
    if jsort in datasort:
        datasortcount[(datasort.index(jsort))] +=1;
    else :
        datasort.append(jsort);
        datasortcount.append(1);
        data.append(j);
    
    if len(str(j))==9:
        data9.append(j);
        

if 5 in datasortcount:
    
    print("yes");
