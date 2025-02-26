from datetime import datetime
from cs1033_evaluator import evaluate_lab7

def days_to_birthday(date):
    datetime_object = datetime.strptime(date, "%Y-%m-%d")
    date = datetime_object.date()
    num_days = date.timetuple().tm_yday
    return num_days

personal_details=input() 
file_input=open(personal_details,'r')  
read_file=file_input.read() 
List=read_file.split('\n') 
list1=[]   

for number1 in range(len(List)): 
    element=List[number1].split(' ') 
    list1.append(element)
file_output=open('output.txt','w')


for number1 in range(len(list1)):  
    birthday=list1[number1][1]   
    birth_year=list1[number1][1][0:4]   
    F_or_M=list1[number1][2]   
    day_number=days_to_birthday(str(birthday))   
    if F_or_M=='F':     
        sum_of_days=day_number+500
    else:
        sum_of_days=day_number  
    if number1==0:  
        year_number=1 
    else:
        list2=[]  
        for number2 in range(number1+1): 
            element=list1[number2][1][0:4] 
            list2.append(int(element))  
        year_number=list2.count(int(birth_year))  
    Identity_number=(list1[number1][0]+' '+birth_year+str(sum_of_days).rjust(3,'0')+str(year_number).rjust(3,'0'))
    h=Identity_number+'\n'  
    file_output.write(str(h)) 
file_output.close()  

