class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)
     
    def insert(self, data, bracketed):
        a=self
        tan=Node(data)
        if data[0]=='OPERAND':
            try:
                if a.right.left:
                    a.right.righ=tan
            except:
                a.right=tan
                self=a
        elif data[0]=='OPERATOR':
            if not bracketed:
                tan.left=a
                self=tan
            else:
                w=a.right
                a.right=tan
                tan.left=w
        return self
    def evaluate(self):
        list1=['+','*','^','-']
        if self.data[0]=='OPERATOR':
            simbles=self.data[1]
            if self.right.data[0]=='OPERAND':
                number=self.right.data[1]
                self=self.left
                if list1[0]==simbles:
                    self=number+self.evaluate()
                elif list1[1]==simbles:
                    self=number*self.evaluate()
                elif list1[2]==simbles:
                    self=self.evaluate()**number
                elif list[3]==simbles:
                    self=number-self.evaluate()  
                
                
            elif self.right.data[0]=='OPERATOR':  #self.right.data[0]=='operator':
                number=self.right.right.data[1]
                if list1[0]==simbles:
                    self=0
                    
            
        elif self.data[0]=='OPERAND':
            self=self.data[1]
        return self
root = Node(('OPERAND', 1))
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
root=root.get_output()    
