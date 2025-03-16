def staircase(n):
    for i in range(1, n+1):
        string = ""
        star = "#"
        space = " "
        string = " "*(n-i)+"#"*i
        print(string)


staircase(6)
