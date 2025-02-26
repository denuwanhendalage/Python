def getNum():   
    file_input=input()  
    File=open(file_input,'r')  
    get_number=File.read()  
    return get_number
    
    
n_value=int(getNum())   
if 0<=n_value<=20:  
    n=n_value
else:          
    print('Invalid input!')  
    exit()
def show():   
    Fibonacci_N1=0  
    Fibonacci_N2=1   
    if n==0:
        Fibonacci_value=0  
    elif n==1: 
        Fibonacci_value=1  
    else:  
        for number in range(2,n+1):  
            Fibonacci_N3=Fibonacci_N1+Fibonacci_N2  
            Fibonacci_N1=Fibonacci_N2  
            Fibonacci_N2=Fibonacci_N3  
        Fibonacci_value=Fibonacci_N2  
    return Fibonacci_value   


def saveFile():
    Output='Fibonacci'+'('+str(n)+')'+' ='+' '+str(show())    
    print(Output)   
    Text_file_name=str(n)+'.'+'txt' 
    file_output=open('Text_file_name','w')  
    file_output.write(str(Output))  
    file_output.close()  
    return
saveFile()  
