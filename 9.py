
for a in range(1,900):
    for b in range(1,a):
        c=1000-a-b;
        
        if (a*a+b*b)==c*c:
            print(a*b*c);
            exit()
