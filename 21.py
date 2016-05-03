def d (n):
    summ=0;
    for i in range(1,n):
        if n%i==0:
            summ=summ+i;

    return(summ)


murgi=0;
for j in range(2,10000):

    dn=d(j);
    if d(dn)==j and dn!=j:
        murgi=murgi+j;
        print(j);

        
print(murgi);    
