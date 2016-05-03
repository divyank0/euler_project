tri=[];

with open("18.txt") as f:
    for line in f:
        tri.append(line.strip().split(' '));
        
a=len(tri);

for i in range(a-2,-1,-1):
    b=len(tri[i]);
    for j in range(0,b):
        
        (tri[i][j])=str(int(tri[i][j])+int(max((tri[i+1][j]),(tri[i+1][j+1]))));




print(tri[0][0]);
