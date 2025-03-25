f=open('XORinput2.txt','r')
g=f.read().split('\n')
number_variables=int(g[0])
variable_name=g[1].split(' ')
variable_name.append('Y')
print(variable_name)

def print_table(number):
    for r in range(3):
        print_item=''
        if r==0 or r==2:
            print_item+='+'
            for i in range(len(variable_name)):
                if len(variable_name[i])==1:
                    print_item+='-+'
                elif len(variable_name[i])==2:
                    print_item+='--+'
        if r==1:
            print_item+='|'
            for i in range(len(variable_name)):
                print_item+=(variable_name[i]+'|')
        print(print_item)
print_table(number_variables)

def binary_oparetion(value):
    numberofcolumn=2**value
    for r in range(numberofcolumn):
        g=bin(r)
        w=g[2:]
        if len(w)<value:
            w=w.rjust(value,'0')
        list1=list(w)
        list2=list(w)
        for r in range(len(list1)-1):
            for i in range(1) :
                notA=not int(list1[i])
                notB=not int(list1[i+1])
                A=int(list1[i])
                B=int(list1[i+1])
                c=(notA and B) or (A and notB)
            list1=list1[1:]
            list1[0]=int(c)
        list2.append(int(c))
        print_item='|'
        for r in range(len(list2)):
            item=list2[r]        
            if len(variable_name[r])==1:
                print_item+=str(item)+'|'
            elif len(variable_name[r])==2:
                print_item+=' '+str(item)+'|'
        print(print_item)
                
binary_oparetion(number_variables)
