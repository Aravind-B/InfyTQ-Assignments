from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    
    @abstractmethod
    def work(self):
        print('Employee works')


class Traimee(Employee):
    def work(self):
        print('Trainee works')

class Educator(Employee):
    @abstractmethod()
    def work1(self):
        print('Educator works')
        
        
obj1=Traimee()
obj2=Educator()
