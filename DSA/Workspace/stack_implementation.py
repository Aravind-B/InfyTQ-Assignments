

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size


    def get_top(self):
        return self.__top

    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        else:
            return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        else:
            return False
        
    def push(self,data):
        if(self.is_full()):
            print("Stack overflow!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
        
    def display(self):
        print("****************")
        for i in range(self.__top,-1,-1):
            print(self.__elements[i])
        print("****************")
    
    def pop(self):
        if(self.is_empty()):
            print("Stack empty!")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    max_size = property(get_max_size, None, None, None)
    top = property(get_top, None, None, None)

stack1=Stack(5)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(2)
stack1.push(3)

stack1.display()
stack1.pop()
stack1.display()