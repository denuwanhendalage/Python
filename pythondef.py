def number(N):
    for r in range(2,N):
        if N%r==0:
            print(N,'is a not prime number')
            break
        else:
            pass
    else:
        print(N,'is a prime number')
    return
