#lexicographic permutation, millionth of 0123456789

#10!=3628800

from math import factorial as f;
from itertools import permutations as p;
t=1000000;

cnt=0;

for d in p([0,1,2,3,4,5,6,7,8,9],10):
    cnt+=1;
    if cnt==t:
        print(d,cnt);
