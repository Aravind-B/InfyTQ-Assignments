#OOP-Assgn-202
#Do Not Change any part of the code provided to you
from abc import ABCMeta, abstractmethod

class CustomerDetails:
    customer_points_details = {'R1001':892, 'R1002':956, 'R1003':1352}
    mem_card_types = ['Silver','Gold','Platinum']
    card_type_points = [2,4,5]

    #To Trainee
    @staticmethod
    def get_card_points(card_type):
        if(card_type.capitalize() in CustomerDetails.mem_card_types):
            i=CustomerDetails.mem_card_types.index(card_type.capitalize())
            return CustomerDetails.card_type_points[i]
        else:
            return -1

    #To Trainee
    @staticmethod
    def add_point(cust_id,points):
        if(cust_id.capitalize() in CustomerDetails.customer_points_details):
          CustomerDetails.customer_points_details[cust_id.capitalize()]+=points
        else:
          CustomerDetails.customer_points_details[cust_id.capitalize()]=points

    #To Trainee
    @staticmethod
    def redeem_points(cust_id):
        cust_id=cust_id.capitalize()
        if(cust_id in CustomerDetails.customer_points_details):
            if(CustomerDetails.customer_points_details[cust_id]<=1500):
                redeem_value=0
            else:
                redeem_value=(CustomerDetails.customer_points_details[cust_id]
                              -1500)*0.75
                CustomerDetails.customer_points_details.update({cust_id:1500})
        else:
            return 0
        
        return redeem_value
        
        
        
class Customer(metaclass = ABCMeta):
    def __init__(self,cust_id,cust_name):
        self.__cust_id = cust_id
        self.__cust_name = cust_name

    def get_cust_id(self):
        return self.__cust_id

    def get_cust_name(self):
        return self.__cust_name

    @abstractmethod
    def validate_cust_details(self):
        pass


class RegisteredCustomer(Customer):
    def __init__(self,cust_id,cust_name,mem_card_type):
        super().__init__(cust_id, cust_name)
        self.__mem_card_type = mem_card_type

    def get_mem_card_type(self):
        return self.__mem_card_type

    #To Trainee
    def validate_cust_details(self):
        if(super().get_cust_id() is not None and super().get_cust_name() \
           is not None and self.__mem_card_type is not None):
            return True
        else:
            return False

class Bill:
    __counter = 5001
    def __init__(self,customer,redeemption_required):
        self.__customer = customer
        self.__redeemption_required = redeemption_required
        self.__bill_num = None

    def get_customer(self):
        return self.__customer

    def get_redeemption_required(self):
        return self.__redeemption_required

    def get_bill_num(self):
        return self.__bill_num

    #To Trainee
    def generate_bill_num(self):
        self.__bill_num=Bill.__counter
        Bill.__counter+=1

    #To Trainee
    def calculate_points(self,bill_amount):
        card_type=self.__customer.get_mem_card_type()
        card_points=CustomerDetails.get_card_points(card_type)
        if(card_points==-1):
            return -1
        else:
            points=(bill_amount*card_points)//100
            return points

    #To Trainee
    def calculate_final_bill_amount(self,bill_amount):
        if(bill_amount > 100 and self.__customer.validate_cust_details()):
            points=self.calculate_points(bill_amount)
            if(points==-1):
                final_bill_amount=-1
                self.__bill_num=-1
            else:
                cust_id=self.__customer.get_cust_id()
                CustomerDetails.add_point(cust_id, points)
                self.generate_bill_num()
                if(self.__redeemption_required):
                    rd_value=CustomerDetails.redeem_points(cust_id)
                    final_bill_amount=bill_amount-rd_value
                else:
                    final_bill_amount=bill_amount
        return final_bill_amount
                    

cust_obj = RegisteredCustomer('r1003', 'John', 'GolD')
bill_obj = Bill(cust_obj, True)
final_bill_amount = bill_obj.calculate_final_bill_amount(10000)
print('Bill Num :',bill_obj.get_bill_num())
print('Final Bill Amount :',final_bill_amount)
print(CustomerDetails.customer_points_details)