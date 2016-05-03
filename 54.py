from math import sqrt as sqrt;
from math import floor as floor;
from math import factorial as f;
import sys;


def is_prime(a):
    return all(a%i for i in range(2,a));

data=[];
with open("54.txt") as file:
    for line in file:
        data.append(line.split(' '));

# diamond, clubs, heart, spades, suit

def ranked(b):
    b1=b[0:5];
    b2=b[5:10];

    b1original=(b1[iii][0] for iii in range(0,5));
    b2original=(b2[iii][0] for iii in range(0,5));

    for i in range(0,5):
        if b1original[i]=="T":
            b1original[i]=10;
        if b1original[i]=="J":
            b1original[i]=11;
        if b1original[i]=="Q":
            b1original[i]=12;
        if b1original[i]=="K":
            b1original[i]=13;
        if b1original[i]=="A":
            b1original[i]=14;
        if b2original[i]=="T":
            b2original[i]=10;
        if b2original[i]=="J":
            b2original[i]=11;
        if b2original[i]=="Q":
            b2original[i]=12;
        if b2original[i]=="K":
            b2original[i]=13;
        if b2original[i]=="A":
            b2original[i]=14;
            
    b1original=list(map(int,b1value));
    b2original=list(map(int,b1value));
    
    b1value=(sorted(set(b1[ii][0] for ii in range(0,5))));
    for i in range(0,5):
        if b1value[i]=="T":
            b1value[i]=10;
        if b1value[i]=="J":
            b1value[i]=11;
        if b1value[i]=="Q":
            b1value[i]=12;
        if b1value[i]=="K":
            b1value[i]=13;
        if b1value[i]=="A":
            b1value[i]=14;
    b1value=sorted(list(map(int,b1value)));
    b1suit=(sorted(set(b1[ii][1] for ii in range(0,5))));
    
    b2value=(sorted(set(b2[ii][0] for ii in range(0,5))));
    for i in range(0,5):
        if b2value[i]=="T":
            b2value[i]=10;
        if b2value[i]=="J":
            b2value[i]=11;
        if b2value[i]=="Q":
            b2value[i]=12;
        if b2value[i]=="K":
            b2value[i]=13;
        if b2value[i]=="A":
            b2value[i]=14;
    b2value=sorted(list(map(int,b2value)));
    b2suit=(sorted(set(b2[ii][1] for ii in range(0,5))));


    #_____________________________________________
    xata=[1,1];
    countb1=1;
    check=0;
    for q in b1value:
        countbb=0;
        for q2 in b1original:
            if q2==q:
                countbb=countbb+1;
        countb1=countb1*countbb;

        if countbb==3:
            xata[0]==q;

    countb2=1
    for g in b2value:
        countbb2=0;
        for g2 in b1original:
            if g2==g:
                countbb2=countbb2+1;
        countb2=countb2*countbb2;

        if countbb2==3 :
            xata[1]==g;
        
        









    #suit variations
    if len(b1suit)==1 and len(b2value)>2 and len(b2suit)>1:
        return(1);
    if len(b1suit)==1 and len(b2suit)>1 and len(b2value)==2:
        if b1value[4]-b1value[0]==4:
            return(1);
        else:
            return(2);
        
    if len(b1suit)==1 and len(b2suit)==1:
        if b1value[4]-b1value[0]==4 and b2value[4]-b2value[0]==4
            if b1suit[4] > b2suit[4]:
                return(1);
            if b2suit[4]>b1suit[4]:
                return(2);
        if b1value[4]-b1value[0]==4 and (b2value[4]-b2value[0])!=4
            return(1);
        if (b1value[4]-b1value[0])!=4 and (b2value[4]-b2value[0])==4
            return(2);
    
    if len(b2suit)==1 and len(b1value)>2 and len(b1suit)>1:
        return(2);
    if len(b2suit)==1 and len(b1suit)>1 and len(b1value)==2:
        if b2value[4]-b2value[0]==4:
            return(2);
        else:
            return(1);


    #value comparison,
    if len(b1suit)>1 and len(b2suit)>1:

        if len(b1value)==2 and len(b2value)==2:
             ### solve 4 of a kind vs full house
            
        if len(b1value)==2 and len(b2value)!=2:
            return(1);
        if len(b1value)!=2 and len(b2value)==2:
            return(2);

    if len(b1suit)>1 and len(b2suit)>1 and len(b1value)>2 and len(b2value)>2:
        if b1value[4]-b1value[0]==4 and (b2value[4]-b2value[0])!=4 and len(b1value)==5:
            return(1);
        if (b1value[4]-b1value[0])!=4 and (b2value[4]-b2value[0])==4 and len(b2value)==5:
            return(2);
        if b1value[4]-b1value[0]==4 and b2value[4]-b2value[0]==4 and len(b2value)==5 and len(b1value)==5:
            if b1suit[4] > b2suit[4]:
                return(1);
            if b2suit[4]>b1suit[4]:
                return(2);
        if len(b2value)==5 and len(b1value)==5 and b1value[4]-b1value[0]!=4 and b2value[4]-b2value[0]!=4:
            #then this is high card case
            if b1suit[4] > b2suit[4]:
                return(1);
            if b2suit[4]>b1suit[4]:
                return(2);
            


        if (b1value[4]-b1value[0])!=4 and (b2value[4]-b2value[0])!=4:
            if len(b1value)>len(b2value):
                return(2);
            if len(b2value)>len(b1value):
                return(1);
            if len(b2value)==len(b1value):
                if len(b2value)==3:

                    # compare two pair and three of a kind
                    
                    

                if len(b2value)==4:
                    if b2value[4]>b1value[4]:
                        return(2);
                    if b2value[4]<b1value[4]:
                        return(1);

                    

    print(b1value,b2value,b1suit,b2suit): 
    sys.exit("error");        


    #switch(len(b1value,b1suit))


    #if len(b1suit)==4:
    #if len(b1suit)==3;    



count=0;
for i in range(0,len(data)):
    
    count=count+ ranked(data[i]);



