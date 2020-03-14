class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elelment=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        else:
            return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue Full")
        else:
            self.__rear+=1
            self.__elelment[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!")
        else:
            data=self.__elelment[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for i in range(self.__front,self.__rear+1):
            print(self.__elelment[i])

queue1=Queue(5)

queue1.enqueue(1)
queue1.enqueue(2)
queue1.display()