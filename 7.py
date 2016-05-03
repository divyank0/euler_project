a=[2,3];

for i in  range(4,1300):
    for j in a:
        if i%j==0:
            break;

    if j==a[len(a)-1]:
        a = a + [i];

print len(a) ;
