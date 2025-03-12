class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data


root=Node(('Operand',1))
a=root


root=Node(('Operator','+'))
root.left=a
del a
root.right=Node(('Operand',2))
a=root

root=Node(('Operator','*'))
root.left=a
del a
root.right=Node(('Operand',3))
a=root


root=Node(('Operator','+'))
root.left=a
del a
root.right=Node(('Operand',3))
a=root

root=Node(('Operator','^'))
root.left=a
del a
root.right=Node(('Operand',2))


a=root
