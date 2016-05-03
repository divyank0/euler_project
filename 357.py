import math;

def is_prime(a):
    return all(a%ii for ii in range(2,a));

def condi(a):
    for i in range(1,math.floor(math.sqrt(a)) +1):
        if(a%i==0):
            if (i+a//i) not in data:
                return False;

    return True;

data=[];
tt=100000000;
t=tt;
for z in range(2,t):
    if is_prime(z):
        data.append(z);
      #  print(z)


summ=816238422;
# 1316700
for j in range(1316700,t,2):
    
    if j%4 !=0 and (condi(j)):
        summ=summ+j
        print(j);

print(summ)
                
