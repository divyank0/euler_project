with open("13.txt") as f:
    lines=f.readlines();
    
summ=0;

for i in range (0,100):
    summ= int(lines[i]) +summ;

print(summ);

print
