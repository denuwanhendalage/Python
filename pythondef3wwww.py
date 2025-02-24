if len(list1)==int(m[1]):
                try:
                    list3=[eval(i) for i in list1]
                    list4=list3
                except:
                    print('Error')
                    break
        else:
            print('Invalid matrix')
            break
