#OOPR-Assgn-19
#Start writing your code here
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name.casefold()
        self.__ticket_id=None
        self.__source=source.casefold()
        self.__destination=destination.casefold()
        

    def validate_source_destination(self):
        if(self.__source=="delhi"):
            if(self.__destination=='mumbai' or self.__destination=='chennai' 
            or self.__destination== 'pune' or  self.__destination== 'kolkata'):
                return True
            else:
                return False
        else:
            return False
        
    
    def generate_ticket(self):
        a=self.validate_source_destination()
        if(a):
            sou=self.__source[:1]
            des=self.__destination[:1]
            Ticket.counter+=1
            if(Ticket.counter<10):
                self.__ticket_id=sou+des+str(0)+str(Ticket.counter)
            else:
                self.__ticket_id=sou+des+str(Ticket.counter)
            Ticket.counter+=1
        else:
            self.__ticket_id=None
    
    def get_ticket_id(self):
        return self.__ticket_id
        
    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination    


obj1=Ticket('Ajay','Delhi','Pune')
obj1.generate_ticket()

if(obj1.get_ticket_id):
    print("Ticket Id: ",obj1.get_ticket_id())
    print("Passenger Name: ",obj1.get_passenger_name())
    print("Source: ",obj1.get_source())
    print("Destination: ",obj1.get_destination())
else:
    print("Invalid Source or Destination")