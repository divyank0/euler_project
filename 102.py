import math;
import eulerLibs;

def condi(x1,y1,x2,y2,x3,y3):
    x=0;
    y=0;
    alpha=((y2-y3)*(x-x3) +(x3-x2)*(y-y3))/((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3));
    beta=((y3-y1)*(x-x3) +(x1-x3)*(y-y3))/((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3));
    gamma=1.0-alpha-beta;

    if(alpha>0 and beta>0 and gamma>0):
        return True;
    
    return False;

count=0;
with open("102.txt") as f:
    for line in f:
        coordi=line.strip().split(',');
        p1=int(coordi[0]);
        p2=int(coordi[1]);
        p3=int(coordi[2]);
        p4=int(coordi[3]);
        p5=int(coordi[4]);
        p6=int(coordi[5]);
       # print(p1,p2,p3,p4,p5,p6);
        #x.append(line.strip().split(' '));
        if(condi(p1,p2,p3,p4,p5,p6)):
            count=count+1;
            print(coordi);
