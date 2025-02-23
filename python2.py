a=3
b=5
n=10//3
total=0
for r in range(2,n):
    print(r)
    if r*a<10:
        total+=r*b
    elif r*b<10:
        total+=r*b
    else:
        continue
print(total)
        
