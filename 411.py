def is_prime(a):
    return all(a%ii for ii in range(2,a));

def stations(b):
    stat=[];
    for i in range(0,2*b+1):
        x=(2**i)%b;
        y=(3**i)%b;
        if not {x,y} in stat:
            stat.append({x,y});
    return StationMax(stat);

def StationMax(Coordinates):



summ=0;
for j in range(1,31):
    summ=summ+StationMax(j**5);
    
    
