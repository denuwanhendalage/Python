f=open('text.txt','r')
r=f.read()
l=r.split('\n')
list1=[]
for r in range(len(l)):
    list2=[]
    t=l[r].split(' ')
    list1.append(t)
print(list1)

from datetime import datetime

def days_to_birthday(date):
    datetime_object = datetime.strptime(date, "%Y-%m-%d")
    date = datetime_object.date()
    num_days = date.timetuple().tm_yday
    return num_days

for r in range(len(list1)):
    e=list1[r]
    o=list1[r][1]
    y=e[2]
    w=days_to_birthday(str(o))
    if y=='F':
        k=w+500
    else:
        k=w
    
    if len(str(k))==3:
        p=k
    else:
        p='0'+str(k)
    q=list1[r][1][0:4]
    if r==0:
        i=1
    else:
        for y in range(r):
            if q==list1[y][1][0:4]:
                i=i+1
            else:
                i=1
                
        
        
    
    print(e[0]+' '+o[0:4]+str(p)+str(i))
    


    


