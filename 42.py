from math import sqrt as sqrt;
from math import floor as floor;
with open("42.txt") as f:
        x=eval('[' +f.readlines()[0] +']');

count=0;                
for i in range(0, len(x)):
        a=0;
        for j in x[i]:
                a=a+ord(j)-64;

        for k in range(1,floor(sqrt(a*2)+2)):
                if k*(k+1)/2==a:
                        print(a);
                        count=count+1;

                        
print(count,"final count");

        
