from abc import ABCMeta,abstractmethod
class Test(metaclass=ABCMeta()):
    @abstractmethod
    def sample(self): pass
    @staticmethod
    def sample2(): print("Hello World")

#print(Test.sample2())

class A(Test):
    #print("In class A")
    def sample(self):
        print("In class A")

a=A()
#a.sample()
