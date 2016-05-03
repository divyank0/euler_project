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

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

summax=1;
for j in range(1,100):
    print(j)
    for i in range(1,100):
        number=i**j
        summ=sum_digits(number);

        if summ>summax:
            summax=summ;

print(summax);

    
