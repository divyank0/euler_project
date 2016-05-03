abundant=[];
n=[[1,1]];
qq=28123
for i in range(2,qq+1):
    n.append([i,1]);
    summ=0;
    for j in range(1,i):
        if i%j==0:
            summ=summ+j;

    if summ>i:
        abundant.append(i);


for x in range(0,len(abundant)-1):
    for y in range (0,len(abundant)-1):
        z=abundant[x]+abundant[y];
        if z<qq:
            n[z-1][1]=0;


s=0;        
for j in range(0,qq-1):
    s=s+(n[j][0])*(n[j][1]);
            
            
print(s);
