import sys;
def tria(a):
        return(a*(a+1)/2);
def pent(b):
        return(b*(3*b-1)/2);
def hexa(c):
        return(c*(2*c-1));
h=[];
p=[];

for k in range(1,50000):
        h.append(hexa(k));


for j in range(1,60000):
        p.append(pent(j));
for i in range(1,100000):
                t=tria(i);
                if t in p and t in h:
                         print(t);
                         
