#custom exceptions
class InvalidName(Exception):
    pass
    #print("Invalid Name")
#custom exception
class Invalidlength(Exception):
    pass
    #print("Invalid length")

class Customer:
    def __init__(self,name):
        self.name=name
    
    def check_name(self):
        if(type(self.name)!=str):
            raise InvalidName
        elif(len(self.name)!=6):
            raise Invalidlength
        else:
            print(self.name)
try:
    pass
except InvalidName:
    print("Invalid name!")
except Invalidlength:
    print("Invalid length")
cust1=Customer(1)
cust1.check_name()