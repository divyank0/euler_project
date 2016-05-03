#first element of new layer is always (n-1)^2 +1
f=[2,10];
tr=[9];
tl=[7];
bl=[5];
br=[3];
summ=25;

for i in range(5,1002,2):
    f.append(i*i+1);
    tr.append(i*i);
    tl.append(i*i-i+1);
    bl.append((i*i+(i-2)*(i-2))/2);
    br.append((i-2)*(i-2) +i-1);
    summ=summ+i*i+(i*i-i+1) +((i*i+(i-2)*(i-2))/2) +((i-2)*(i-2) +i-1);

print(summ);    
    
    
