from math import sqrt
summ=5;

for i in  range(4,2000000):
    summ=summ+i;
    for j in range(2,int(sqrt(i))+2):
        if i%j==0:
            summ=summ-i;
            break;

print(summ);
