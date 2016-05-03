import math;

def is_prime(a):
    if(a==1):
        return False;
    else:
        
        return all(a%ii for ii in range(2,a));

#padington number
def pad(x):
    for iii in range(1,10):
        if str(iii) not in str(x):
            return False;
    return True;

