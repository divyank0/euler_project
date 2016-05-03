# total digits=10+9;
# total digits in integer to find. = 9
# 1_2_3_4_5_6_7_8_9_0
#0    #3,7
import math;
n=math.sqrt(2*10**18)
m=math.sqrt(10**18)
for i in range(int(m)+10,int(n),20):

   j=i*i
   if(j//10**18>=1):
      
      
      
      if((j//10**16)%10==2):
         if((j//10**14)%10==3):
            if((j//10**12)%10==4):
               if((j//10**10)%10==5):
                  
                  if((j//10**8)%10==6):
                     #print(j)
                     if((j//10**6)%10==7):
                        if((j//10**4)%10==8):
                           #print(j)
                           if((j//10**2)%10==9):
                              print(j);
