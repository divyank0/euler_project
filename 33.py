

product=[]
for a in range(1,1000):
    for b in range(2,9876):
        c=a*b;
        d=str(a)+str(b)+str(c);
        d=''.join(sorted(d));
        if int(d)==123456789 and len(d)==9:
            print(d,a,b,c);
            product.append(c);

product=set(product);

print(sum(product));
    
