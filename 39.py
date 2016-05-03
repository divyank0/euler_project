for p in range(100,1001):
        count=0;
        for a in range(1,333):
                for b in range(a,500):
                        c=p-a-b;
                        if c>b and c*c==a*a+b*b:
                                count=count+1;

        if count > 3:
                print(count,p);
