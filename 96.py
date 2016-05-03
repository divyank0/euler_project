#semi primes
#remainder=f(n)
#s=8480933482255137 + 
import math;
from primes import a as primes;







sudoku=[[0,0,3,0,2,0,6,0,0],
         [9,0,0,3,0,5,0,0,1],
         [0,0,1,8,0,6,4,0,0],
         [0,0,8,1,0,2,9,0,0],
         [7,0,0,0,0,0,0,0,8],
         [0,0,6,7,0,8,2,0,0],
         [0,0,2,6,0,9,5,0,0],
         [8,0,0,2,0,3,0,0,9],
         [0,0,5,0,1,0,3,0,0]]
s=[];
for i in range(9):
   s.append(sudoku[i][:]);
   

#stochastic

## ## following code is via backtracking
   

def condition(ss,si,sj,sn):
   a=si//3
   b=sj//3
   a=3*a
   b=3*b
   for x in range(9):
      if(ss[si][x]==sn):
         return False;
      elif(sn<1) or sn>9:
         return False;
      elif(ss[x][sj]==sn):
         return False;
      elif( sn in [ss[a][b],ss[a+1][b],ss[a+2][b],ss[a][b+1],ss[a+1][b+1],ss[a+2][b+1],ss[a][b+2],ss[a+1][b+2],ss[a+2][b+2]]):
         return False;
   
   return True;   

#backtracking
flag=False;
i=-1;
while i<8:
   i=i+1
   j=-1;
   while j<8:
      j=j+1
      flag=False
      #print(i,j)
				
      if(sudoku[i][j]==0):
         n=s[i][j]+1;
         if(s[i][j]==0):
            n=1;
         while not (condition(s,i,j,n)):
            if(n>9):
               s[i][j]=0;
               jj=j-1
               for ri in range(i,-1,-1):
                  for rj in range(jj,-1,-1):
                     if (sudoku[ri][rj]==0):
                        flag=True;
                        i=ri
                        j=rj-1;
                        break;
                  if(flag):
                     break;
                  jj=8;
            if(flag):
               break;
            n=n+1;
         if not (flag):
            s[i][j]=n;
print(s);
