# 2 3 5 7
# 1 3 7 9
# 3 7
# number = a1 + a2**(n) +a3

from math import floor as floor;
from math import sqrt as sqrt
set1 = [2,3,5,7];
set2= [ 1,3,7,9];
set3 = [ 3, 7];

n=0;
total=4*2*(4**n);
setans=[0]*total;
for i in range(0,total):
        ii=[floor(i/total*4),floor((total/4)-1)/total*8];
        setans[i]=(str(set1[int(ii[0])]) + str(set3[int(ii[1])]));

                                          

print(setans);
setpre=['23', '27', '33', '37', '53', '57', '73', '77'];
setans=setpre;

def is_prime(aa,bb):
    return all(aa % i for i in range(2, floor(sqrt(aa)))) and all(bb % i for i in range(2, floor(sqrt(bb))));

def check(a):
    a1=int(a);
    
    return all(is_prime(int(a[x:]),int(a[:1+x])) for x in range(0,len(a)-1));

# 37 is tructable prime
prime=[23,37,53,73];
newprime=prime;
count=0;

        
while len(set(prime)) <11:
        
        setpre=setans;
                
        n=n+1;
        total=4*len(setans);
        setans=[0]*total;
        print(total);
        for i in range(0,total):
                ii=floor(i/4);
                iii=floor(i%4);
                setans[i]= str(setpre[ii])[:n]+ str(set2[iii]) +str(setpre[ii])[n:];

                if is_prime(int(setans[i][:n]),7)==False:
                        count+=1;
                        print(i,count,setans[i]);
                        setans[i]=str(317);
                        continue;
                if check((setans[i])):
                        if not(int(setans[i]) in newprime) :

                            newprime.append(int((setans[i])));
                            print(newprime);
                            

                
        setans=list(set(setans))
        prime=list(set(newprime));
        print(setans,len(prime),prime);
    #____37 317 
    
