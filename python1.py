i=1
list1=[]
while i<4:
    list=input().split()
    list2=[]
    for r in range(len(list)):
        element=list[r]
        list2.append(int(element))
    list1.append(list2)
    i=i+1
print(list1)
l=list1
total=0
total2=0
for t in range(len(l)):
    total=total+l[t][t]
print(total)
for i in range(len(l)):
    if i==(len(l)-1-t):
        continue
    else:
        total=total+l[t][len(l)-1-t]
print(total)
    
        
    

    
    
