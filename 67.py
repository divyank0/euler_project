tri=[];
x=[];
with open("67.txt") as f:
    for line in f:
        tri.append(line.strip().split(' '));
        x.append(line.strip().split(' '));
        
a=len(tri);

for i in range(0,100):
    for j in range(0,i+1):
        st=str(tri[i][j]);
        if int(st[0])==0:
            #print(tri[i][j]);
            tri[i][j]=(st[1]);
            #print(tri[i][j])
print("yoo");

for i in range(a-2,-1,-1):
    b=len(tri[i]);
    for j in range(0,b):
        
        (tri[i][j])=(int(tri[i][j])+int(max((tri[i+1][j]),(tri[i+1][j+1]))));




print(tri[0][0]);
