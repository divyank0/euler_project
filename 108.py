###a=[1,x];   #// fucking devide is a mtarix
###b=[1,y];
##
##def addinverse(x,y):
##   return (x*y/(x+y));
##
##m=100000;
##resultCount=[0]*10000
##for i in range(1,m):
##   for j in range(1,i):
##      n=addinverse(i,j);
##      if (n%1==0):
##         resultCount[int(n)-1]+=1;
##         if (resultCount[int(n)-1]>100):
##            print("voila " +n)
##         223092870 9898 437.0
##446185740 16698 874.0
##      
##      
##      
##      
## 9350130049860600

#y=n*x/(x-n);
import math as math;


def is_prime(a):
    return all(a%i for i in range(2,a));

topCount=5;
#ninja=510510*10*2*19*3*23*3*29*31*37*7;
ninja=510510*2*3*19*23*29*10*31;
for n in range(ninja,ninja*2000,ninja):
   count=1;
   for i in range(2,100):
      occur=0;
      nn=n;
      while(is_prime(i) and nn%i==0):
         nn=nn/i;
         occur=occur+1;
      count=count*(2*occur+1);
      #if(is_prime(i)):
       #  print(i,2*occur)
   if(count>topCount):
      topCount=count;
      print(n,n/ninja,(count+1)/2);
##   for i in range(n+1,n+1+n):
##       a=n*i/(i-n);
##       if (a%1==0):
##          count+=1;
##         # if((count/100)%1==0 and count>99):
##           # print(a//n,count);
##   if (count>topCount):
##      print(n,count,n/ninja);
##      topCount=count;
##   
##       
####
####for x in range(50,101):
####   numbers =[];
##   for y in range(50,x+1):
##      n=x*y/(y+x);
##      numbers.append(int(n*100));
##   print(numbers,x);
##
##   
