n=int(input('Please enter odd number >1:'))
l=[]
for r in range(1,n*n+1):
    l.append(r)
print(l)
total=0
for i in range(0,len(l),1):
    total=total+i
print(total)
    
