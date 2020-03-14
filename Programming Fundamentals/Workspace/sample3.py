class Parent:
    def __init__(self,num):
        self.num=num
    
class Child(Parent):
    def m1(self):
        self.num=150
        super().__init__(100)

parent=Parent(200)
child=Child(300)
print(child.num)
child.m1()
print(child.num)