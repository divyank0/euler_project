import sys
p=[];
for i in range(1,3000):
        p.append(i*(3*i-1)/2);
        

for i in range(2150,2200):
        pi=p[i-1];
        for j in range(1,i):
                pj=p[j-1];

                pplus=pj+pi;
                pminus=abs(pi-pj);

                if pplus in p:
                        print(i,j)
                        if pminus in p:
                                print(pi,pj,pminus,"murgi");
                                sys.exit()
                
                
