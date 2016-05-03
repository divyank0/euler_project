import sys;
import time;
a=2
b=5

u=[a,b];
i=u[-1];

while(i<10000):
   n=[u[-1]+2];
   for j in u[-6:]:
      n.append(j+12)

   n.sort();
   for nn in n:
      if n.count(nn)==1:
         print(nn);
         u.append(nn);
         break;

   i=i+1;

for uu in u:
   if uu%2==0:
      print(uu,u.index(uu))

