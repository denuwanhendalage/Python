def getNum():   #This function use for get the 'n' value through file readind
    file_input=input()  #use for input that file to this program
    File=open(file_input,'r')  #after we open that file for read
    get_number=File.read()  #read that file and get the number,that number assign to variable 'get_number'
    return get_number
    
    
n_value=int(getNum())    #'n_value' variable use for detect to existence of errors or incompatible values 
if 0<=n_value<=20:  #use for run program for 0<=n<=20 values
    n=n_value
else:          
    print('Invalid input!')  #output 'Invalid input!' and then go to next function
    exit()
def show():   #that function use for get particular value of fibonacci series
    Fibonacci_N1=0  #Fibonacci first value F(0)=0
    Fibonacci_N2=1   #Fibonacci second value F(1)=1
    if n==0:
        Fibonacci_value=0  #because F(0)=0
    elif n==1: 
        Fibonacci_value=1  #because F(1)=1
    else:  #If n value is higher than 1,then run below program
        for number in range(2,n+1):  #use for repeat below program
            Fibonacci_N3=Fibonacci_N1+Fibonacci_N2  #create next fibonacci number using before fibonacci number
                                                    #F(n)=F(n-2)+F(n-1)
            Fibonacci_N1=Fibonacci_N2  #F(n-2) number is assign to F(n-1)
            Fibonacci_N2=Fibonacci_N3  #new F(n) number is assign to F(n-2)
        Fibonacci_value=Fibonacci_N2  #real fibonacci value is F(n)='Fibonacci_N2'
    return Fibonacci_value   #return the fibonacci value

#this function use for output fibonacci number
def saveFile():
    Output='Fibonacci'+'('+str(n)+')'+' ='+' '+str(show())    #to create string alike 'Fibonacci(2)=2'
    print(Output)   #output that string
    Text_file_name=str(n)+'.'+'txt' #create numbered text files name
    file_output=open('Text_file_name','w')  #create output text file 'file_output'
    file_output.write(str(Output))  #'Output' string write on 'file_output' file
    file_output.close()  #end the writing process
    return
saveFile()  #use for call the 'saveFile' function
