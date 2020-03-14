#OOPR-Assgn-30
#Start writing your code here

class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity

        
    def validate_quantity(self):
        if(1<=self.__quantity<=5):
            return True
        else:
            return False
    
class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None

    def get_service_id(self):
        return self.__service_id


    def get_customer(self):
        return self.__customer


    def get_pizza_type(self):
        return self.__pizza_type


    def get_additional_topping(self):
        return self.__additional_topping

        
    def validate_pizza_type(self):
        if(self.__pizza_type.lower() in ['small','medium']):
            return True
        else:
            return False
               
    
    def calculate_pizza_cost(self):
        a=self.validate_pizza_type()
        b=self.__customer.validate_quantity()
        if(a and b):
            Pizzaservice.counter+=1
            if(self.__pizza_type.lower()=='small'):
                if(self.__additional_topping):
                    self.pizza_cost=(150+35)*self.get_customer().get_quantity()
                else:
                    self.pizza_cost=150*self.get_customer().get_quantity()
                self.__service_id='S'+str(Pizzaservice.counter)
            else:
                if(self.__additional_topping):
                    self.pizza_cost=(200+50)*self.get_customer().get_quantity()
                else:
                    self.pizza_cost=200*self.get_customer().get_quantity()
                self.__service_id='M'+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__delivery_charge=None
        self.__distance_in_kms=distance_in_kms

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms

        
    def validate_distance_in_kms(self):
        if(1<=self.__distance_in_kms<=10):
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        a=self.validate_distance_in_kms()
        if(a):
            super().calculate_pizza_cost()
            if(self.pizza_cost!=-1):
                if(self.__distance_in_kms<=5):
                    self.__delivery_charge=self.__distance_in_kms*5
                else:
                    self.__delivery_charge=25+(self.__distance_in_kms-5)*7
                self.pizza_cost+=self.__delivery_charge
        else:
            self.pizza_cost=-1
  
     