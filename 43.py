summ=0;
for i in range(1000000000,9876543210,1000):

        j=str(i);
        
        if int(j[5])%5>0:
                        continue;

        if (int(j[4:7]))%7>0 or int(j[3])%2>0 or (int(j[2:5]))%3>0:
                        continue;
                
        for ii in range(0,1000,17):
                iii=i+ii;
                n=[];
                j=str(iii);
                if int(j[6:9])%13>0 or int(j[5:8])%11>0:
                        continue;

                if (int(j[5:8]))%11>0:
                        continue;
                s=0;
                for k in j:
                        s=s+int(k);
                        n.append(int(k));
                
                if s!= 45 :
                        continue;

                n.sort();
                if n==[0,1,2,3,4,5,6,7,8,9]:
                        summ=summ+iii;
                        print(iii);
                
                      
