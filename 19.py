# 1st day of month is which day of year
#day 1 of 1901 is tueday
#day day 6 is sunday
nod=[31,28,31,30,31,30,31,31,30,31,30,31]; # number of days in month
nodleap=[31,29,31,30,31,30,31,31,30,31,30,31]; # no. of days in leap month year
i=1;
day=[1];
dayleap=[1];

for year in range(1,101):
    months=nod;
    if year%4==0:
        months=nodleap;
        
    for d in months:
        i=int(d)+i;
        day.append(i);


a=len(day);
count=0;

for i in range(0,a-2):  # as one extra month is counted
    day[i]=str(int(day[i]-6));
    if int(day[i])%7==0:
        count+=1;


print(count);        
