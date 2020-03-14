#Do NOT change any part of the code that is provided.
from abc import ABCMeta, abstractmethod 
class Patient(metaclass=ABCMeta):
    def __init__(self,patient_id,patient_name):
        self.__patient_id=patient_id
        self.__patient_name=patient_name
        self.__total_amount=0

    def get_patient_id(self):
        return self.__patient_id

    def get_patient_name(self):
        return self.__patient_name

    def get_total_amount(self):
        return self.__total_amount

    def set_patient_id(self, value):
        self.__patient_id = value

    def set_patient_name(self, value):
        self.__patient_name = value

    def set_total_amount(self, value):
        self.__total_amount = value

    #Method surcharge() calculates and 
    #returns the surcharge amount
    def surcharge(self,amount):     
        if(amount>=0):
            surcharge=amount*0.10
        else:
            surcharge=0
        return surcharge
    
    def base_charge(self):
        return 2000.0
    
    @abstractmethod
    def compute_bill_amount(self,deposit_amount,\
                            injection_id):
        pass
    
class Discount:
    look_up={"Dorm":0,"Standard":30,\
             "Semi-Private":20,"Private":20}
      
    @staticmethod
    def identify_discount(room_type):
        discount=0
        if room_type in Discount.look_up:
            discount=Discount.look_up[room_type]
            return discount
        return discount
    
class Resident(Patient):
    def __init__(self,room_type,days,patient_id,\
                 patient_name,deposit_account):
        super().__init__(patient_id,patient_name)
        self.__room_type=room_type
        self.__days=days
        self.__deposit_account=deposit_account
        self.__treatment_amount=0
        
    def get_room_type(self):
        return self.__room_type
    
    def get_days(self):
        return self.__days
    
    def get_treatment_amount(self):
        return self.__treatment_amount
    
    def get_deposit_account(self):
        return self.__deposit_account
    
    def add_deposit(self, deposit_amount):
        self.__deposit_account.append( \
        self.__deposit_account[-1]+deposit_amount)         

    def treatment_injection(self,injection_id):
        if(injection_id==2):
            price=30.0
        elif(injection_id==45):
            price=45.75
        elif(injection_id==78):
            price=250.0
        elif(injection_id==56):
            price=457.0
        else:
            price=0
            
        no_of_times_per_day=3
        if(price>0):
            if(self.__days>0):
                self.__treatment_amount=price* \
                self.__days*no_of_times_per_day
            else:
                self.__treatment_amount=-1
        else:
            self.__treatment_amount=-1
    def compute_bill_amount(self,deposit_amount,
                            injection_id):
        self.add_deposit(deposit_amount)
        self.treatment_injection(injection_id)
        TA=self.get_treatment_amount()
        
        if(TA==-1):
            super().set_total_amount(-1)
            return
        else:
            BC=super().base_charge()
            S=super().surcharge(TA+BC)
        
            dis1=Discount.identify_discount( 
                            self.__room_type)
            DIS=((TA+BC+S)*dis1)/100
            DEP=self.__deposit_account[-1]
            bill_amount=BC+TA+S-(DIS+DEP)
            super().set_total_amount(bill_amount)
        
    
#You can change the values in the 
#below code to test your functionality 
    
room_type="Semi-Private"            
no_of_days=3                 
patient_id=1001
patient_name="Rohan"
deposit_account=[100,200]
injection_id=78
deposit_amount=800
resident1=Resident(room_type,no_of_days, \
    patient_id,patient_name,deposit_account)
resident1.compute_bill_amount(deposit_amount,
                            injection_id)
print(resident1.get_total_amount())
