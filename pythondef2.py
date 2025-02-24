def pass_by_ref( a ):
    a[0]=100
    return
x=[10,20,30]
pass_by_ref(x)
print (x)
