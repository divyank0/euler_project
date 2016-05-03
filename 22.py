data=[];
with open("22.txt") as f:
    for line in f:
        line.strip('"');
        data.append(line.replace('"','').split(','));

    for d in data:
        xata=d;

xata.sort();
summ=0;

values = {chr(i): i + 1 -ord('A')  for i in range(ord("A"), ord("B") + 26)};
values['\n']=0;

for j in range(0,len(xata)):
    worth=0;
    for k in xata[j]:
        worth=worth+values[k];

    summ=summ+(j+1)*worth;

    
print(summ);        
    
    
