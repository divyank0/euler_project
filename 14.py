longest = 1;

for j in range(13,1000000):
    i=j;
    count=0;
    while (i>1):
       # print(i);
        count=count+1;
        if (i%2==0):
            i=i/2;
        else:
            i=3*i+1;

    if count>longest:
        longest=count;
        print(count,j);

        
        
print(longest)
