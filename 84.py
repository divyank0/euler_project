from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,a));

#with open("54.txt") as file:
#    for line in file:
#        data.append(line.split(' '));


sq_prct=[2.5]*40;
sq=['a1','cc1','a2','t1','r1','b1','ch1','b2','b3','jail',
        'c1','u1','c2','c3','r2','d1','cc2','d2','d3','fp',
        'e1','ch2','e2','e3','r3','f1','f2','u2','f3','g2j',
        'g1','g2','cc3','g3','r4','ch3','h1','t2','h2','go'];

sq_prct_new=[-1/(16*16*16)]*40;
sq_prct_new[sq.index('ch1')]+=-10/16;
sq_prct_new[sq.index('ch2')]+=-10/16;
sq_prct_new[sq.index('ch3')]+=-10/16;
sq_prct_new[sq.index('cc1')]+=-2/16;
sq_prct_new[sq.index('cc2')]+=-2/16;
sq_prct_new[sq.index('cc3')]+=-2/16 +1/16;
sq_prct_new[sq.index('g2j')]=-1;
sq_prct_new[sq.index('jail')]+= +1+3/16+3/16 + 39/(16**3);
sq_prct_new[sq.index('go')]+=3/16+3/16;
sq_prct_new[sq.index('c1')]+=3/16;
sq_prct_new[sq.index('e3')]+=3/16;
sq_prct_new[sq.index('h2')]+=3/16;
sq_prct_new[sq.index('r1')]+=3/16+2/16;
sq_prct_new[sq.index('r2')]+=2/16;
sq_prct_new[sq.index('r3')]+=2/16;
sq_prct_new[sq.index('u1')]+=2/16;
sq_prct_new[sq.index('u2')]+=1/16;
sq_prct_new[sq.index('t1')]+=1/16;
sq_prct_new[sq.index('d3')]+=1/16;

sq_prct_rules=sq_prct_new # change fraction everytime
#print(sum(sq_prct_new,"test"));

for ii in range(0,40):
    sq_prct_new[ii]=sq_prct_new[ii]*2.5;


for k in range(0,10):
    sq_prct_change=[0]*40;
    for i in range(0,40):
        sq_prct[i]+= sq_prct_new[i];
        for j in range(2,9): # effect due to dice
            sq_prct_change[(i+j)%40]+=sq_prct_new[i]*(4-abs(5-j))/16;

    #now changes in according to rules
    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('g2j')];
    sq_prct_change[sq.index('g2j')]=0;

    sq_prct_change[sq.index('cc1')]=sq_prct_change[sq.index('cc2')]*14/16;
    sq_prct_change[sq.index('cc2')]=sq_prct_change[sq.index('cc2')]*14/16;
    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('cc2')]/16;
    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('cc1')]/16;
    sq_prct_change[sq.index('go')] +=sq_prct_change[sq.index('cc1')]/16;
    sq_prct_change[sq.index('go')] +=sq_prct_change[sq.index('cc2')]/16;

    sq_prct_change[sq.index('ch1')]=sq_prct_change[sq.index('ch1')]*6/16;
    sq_prct_change[sq.index('ch2')]=sq_prct_change[sq.index('ch2')]*6/16;
    sq_prct_change[sq.index('ch3')]=sq_prct_change[sq.index('ch3')]*6/16;

    sq_prct_change[sq.index('go')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('go')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('go')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('jail')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('c1')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('c1')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('c1')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('e3')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('e3')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('e3')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('h2')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('h2')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('h2')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('r1')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('r1')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('r1')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('r2')] +=sq_prct_change[sq.index('ch1')]*2/16;
    sq_prct_change[sq.index('r3')] +=sq_prct_change[sq.index('ch2')]*2/16;
    sq_prct_change[sq.index('r1')] +=sq_prct_change[sq.index('ch3')]*2/16;

    sq_prct_change[sq.index('u1')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('u2')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('u1')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_change[sq.index('t1')] +=sq_prct_change[sq.index('ch1')]/16;
    sq_prct_change[sq.index('d3')] +=sq_prct_change[sq.index('ch2')]/16;
    sq_prct_change[sq.index('cc3')] +=sq_prct_change[sq.index('ch3')]/16;

    sq_prct_new=sq_prct_change;


for z in range(0,40):
    print(sq_prct[z],z);

#5, 10, 14, 15 , 16
#091423



