class compleX:
    def __init__(self,Real,Imaginary):
        self.real=Real
        self.img=Imaginary

    def add(self,data):
        return compleX(self.real+data.real, self.img+data.img)

    def multiply(self,data):
        temp=compleX(self.real*data.real-self.img*data.img, self.img*data.real+self.real*data.img)
        return temp
    def show(self):
        if self.img!=-self.img:
            print(str(self.real)+'+'+str(self.img)+'j')
        else:
            print(str(self.real)+str(self.img)+'j')
        
        
