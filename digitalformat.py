
f=open('digitalformatinput2.txt','r')
g=f.read().split('\n')
list2=[]
def printing(numbers):
    
    for item in numbers:
        global int_list
        q=list(item)
        int_list=[]
        for element in q:
            number=int(element)
            int_list.append(number)
        list2.append(int_list)
        
file=open('digitalformatoutput2.txt','w')

printing(g)
for item in list2:
    www=item
    def digital_formatting(number):
        for r in range(6):
            print_item=''
            if r==0:
                for item in number:
                    if item in [1,4]:
                        print_item=print_item+'    '
                    elif item in [0,2,3,5,6,7,8,9]:
                        print_item=print_item+'+-+ '
            elif r==1:
                for item in number:
                    if item in [0,4,8,9]:
                        print_item+='| | '
                    elif item in [5,6]:
                        print_item+='|   '
                    elif item in [1,2,3,7]:
                        print_item+='  | '

            elif r==2:
                for item in number:
                    if item in [2,3,4,5,6,8,9]:
                        print_item+='+-+ '
                    elif item in [0,1,7]:
                        print_item+='    '
            elif r==3:
                for item in number:
                    if item in [0,6,8]:
                        print_item+='| | '
                    elif item in [1,3,4,5,7,9]:
                        print_item+='  | '
                    elif item in [2]:
                        print_item+='|   '
            elif r==4:
                for item in number:
                    if item in [0,2,3,5,6,8]:
                        print_item+='+-+ '
                    elif item in [1,4,7,9]:
                        print_item+='    '
            print(print_item)
            woo=print_item+'\n'
            file.write(woo)
    digital_formatting(www)
file.close()






