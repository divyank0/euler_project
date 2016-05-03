from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
from fractions import Fraction as fr;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,int(sqrt(a)+1)));


#with open("59.txt") as file:
 #   data=eval('['+file.readlines()[0]+']');

def Tri(n):
    return(n*(n+1)/2);

def Squ(n):
    m=n*n;
    return(m);
def pen(n):
    m=n*(3*n-1)/2;
    return(m);
def hexa(n):
    m=n*(2*n-1);
    return(m);
def hept(n):
    m=n*(5*n-3)/2;
    return(m);
def octa(n):
    m=n*(3*n-2);
    return(m);

s1=[];
s2=[];
s3=[];
s4=[];
s5=[];
s6=[];

for i in range(10,300):
   if  int(Tri(i))>999  and int(Tri(i))<10000:
    s1.append(int(Tri(i)));
   if  (int(Squ(i)))>999  and (int(Squ(i)))<10000:
    s2.append(int(Squ(i)));
   if  int(pen(i))>999  and int(pen(i))<10000:
    s3.append(int(pen(i)));
   if  int(hexa(i))>999  and int(hexa(i))<10000:
    s4.append(int (hexa(i)));

   if int(hept(i))>999 and int(hept(i))<10000:
    s5.append(int(hept(i)));

   if int(octa(i))<10000 and int(octa(i)) >999:
    s6.append(int(octa(i)));

#s1=(sorted( s1));
#s2=(sorted(s2));
#s3=(sorted( s3));
#s4=(sorted(s4));
#s5=(sorted(s5));
#s6=(sorted(s6));

def funct(a1,a2,a3,a4,a5,a6):
 if a1 in s1:
    if a2 in s2 or a3 in s2 or a4 in s2 or a5 in s2 or a6 in s2:
        if a2 in s3 or a3 in s3 or a4 in s3 or a5 in s3 or a6 in s3:
            if a2 in s4 or a3 in s4 or a4 in s4 or a5 in s4 or a6 in s4:
                if a2 in s5 or a3 in s5 or a4 in s5 or a5 in s5 or a6 in s5:
                    if a2 in s6 or a3 in s6 or a4 in s6 or a5 in s6 or a6 in s6:
                        print(a1+a2+a3+a4+a5+a6);
                        print(a1,a2,a3,a4,a5,a6);
        
    
    

s=s2+s3+s4+s5+s6;
for ss1 in s1:

    for ss2 in s:
        if (str(ss1)[2:4])==(str(ss2)[0:2]):
            
            for ss3 in s:
                if (str(ss2)[2:4])==(str(ss3)[0:2]):

                    
                    for ss4 in s:
                        if (str(ss3)[2:4])==(str(ss4)[0:2]):

                            for ss5 in s:
                                if (str(ss4)[2:4])==(str(ss5)[0:2]):
                                  #  print(ss1,ss2,ss3,ss4,ss5);
                                  
                                    for ss6 in s:
                                        if (str(ss5)[2:4])==(str(ss6)[0:2]) :
                                         if (str(ss6)[2:4])==(str(ss1)[0:2]) :
                                             funct(ss1,ss2,ss3,ss4,ss5,ss6);
                                            
                    
                

    
