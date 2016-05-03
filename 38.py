for i in range(9182,9876):
        a=i*1;
        b=i*2;
        e=1;
        if len(str(a))+len(str(b))==9:
                c=str(a)+str(b);
                for d in c:
                        e=e*int(d);

                        
                if e==362880:
                        print(int(c))
                
                
                
        
