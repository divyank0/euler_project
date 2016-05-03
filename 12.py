from math import sqrt;
summ=0;
count=0;
for n in range (9999,19999):
    count=0;
    summ=0;
    for i in range(1,n):
        summ=summ+i;

    for j in range(1,int(sqrt(summ))):
        if summ%j==0:
            count=count+1;

    if count>200:        
        print(count);
            
    if count >250:
        break;
 
print(count)
