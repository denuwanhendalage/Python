f=open('inputcreditcard.txt','r')
g=f.read()
list1=g.split('\n')

def number_check(number):
    for item in number:
        k=len(item)
        if k==4:
            return True
        else:
            return False
output=open('outputcreditcard.txt','w')        

def similar(numbers):
    w=list(str(numbers))
    count=1
    for r in range(len(w)-1):
        if w[r]==w[r+1]:
            count=count+1
    if count>=4:
        output.write('Invalid\n')
        print('Invalid')
    else:
        output.write('Valid\n')
        print('Valid')
    return


get_number=int(list1[0])
def validity(List):
    for r in List:
        if len(r)==16:
            card_number=r
            similar(card_number)
        elif len(r)==19:
            e=r.split('-')
            if len(e)==4:
                if number_check(e):
                    card_number=e[0]+e[1]+e[2]+e[3]
                    similar(card_number)
                else:
                    output.write('Invalid\n')
                    print('Invalid')
            else:
                output.write('Invalid\n')
                print('Invalid')
        elif len(r)==1:
            continue
        else:
            output.write('Invalid\n')
            print('Invalid')
    return card_number
    
        
validity(list1)

output.close()

        
    
 
