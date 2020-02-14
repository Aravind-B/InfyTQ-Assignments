#OOPR-Exer-13
#Start writing your code here
from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.counter+=1

    def get_consumer_name(self):
        return self.__consumer_name


    def get_consumer_number(self):
        return self.__consumer_number
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass
    

class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name, base_pack_name,subscription_period):
        self.__consumer_name="Sita"
        self.__base_pack_name="Silver"
        self.__subscription_period=13

    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if(self.__base_pack_name in ['Silver','Gold', 'Platinum']):
            return True
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")
    
    def calculate_monthly_rent(self):
        if(1<=self.__subscription_period<=24):
            self.validate_base_pack_name()
            if(self.__base_pack_name=="Silver"):
                monthly_rent=350.0
            elif(self.__base_pack_name=="Gold"):
                monthly_rent=440.0
            else:
                monthly_rent=560.0
            
            if(self.__subscription_period>12):
                discount=monthly_rent
            else:
                discount=0
                
            final_amount=((monthly_rent * self.__subscription_period) - discount)/self.__subscription_period
            return final_amount
        else:
            return -1
                
        