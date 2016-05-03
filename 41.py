from math import sqrt as sqrt;
from math import floor as floor;

def is_prime(x):
        return all(x % j for j in range(2, floor(sqrt(x))));

for i in range(7654321,1234566,-2):
        summ=0;
        product=1;
        for a in str(i):
                summ=summ+int(a);
                product=product*int(a);

        if summ==28 and product==5040:
                if is_prime(i):
                        print(i);
                
