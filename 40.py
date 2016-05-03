a=1;
i=1;

while len(str(a)) < 1000005:
        i+=1;
        a=str(a)+str(i);

print(int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999]));
        
