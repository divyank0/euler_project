from math import floor as ff;

count=5;
for a in range(0,2):
    for b in range(0,4):
        for c in range(0,10):
            for d in range(0,20):
                s=100*a+50*b+20*c+10*d;
                ue=41-ff(s/5);
                for e in range(0,ue):
                    nf=s+5*e
                    uf = 101-ff(nf/2);
                    for f in range(0,uf):
                        for g in range(0,(201-(s+5*e+2*f))):
                            if 100*a+50*b+20*c+10*d+5*e+2*f+1*g==200:
                                count+=1;
                                

print(count);
