import math;
import eulerLibs;


    
fp1=1; # frist
fx1=1;
fp2=1; #last
fp2p2=1;
for i in range(3,1000000):
    f1=fp1+fx1;
    l=len(str(f1))-19;
    if(l>0):
        fx1=fp1/(10**l);    
        fp1=f1/(10**l);
    else:
        fx1=fp1;    
        fp1=f1;
    a1=str(f1)[0:9];
            
    f2=fp2+fp2p2;
    fp2p2=int(str(fp2)[-10:]);
    fp2=int(str(f2)[-10:]);
    a2=str(f2)[-9:];
   # print(i,f);
            
    if(eulerLibs.pad(a1) and eulerLibs.pad(a2)):
       # print("first");
        print(i);
        
