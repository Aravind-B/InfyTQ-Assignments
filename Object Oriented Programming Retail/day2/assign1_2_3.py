#OOPR-Assgn-3

class Customer:
    def __init__(self):
        self.customer_name=None
        self.bill_amount=0
        self.emp_name=None
        self.designation=None
        self.item_id=None
        self.price_per_unit=None
        self.description=None

    def pays_bill(self,amount):
        print(self.customer_name, "pays bill amount of Rs. ",amount)
        
    def purchases(self):
        self.bill_amount=self.bill_amount-(0.05*self.bill_amount)
        self.pays_bill(self.bill_amount)
    

def invoke_purchases():
    customer1=Customer()
    customer1.customer_name="A"
    customer1.bill_amount=300
    customer1.purchases()

    customer2=Customer()
    customer2.customer_name="B"
    customer1.bill_amount=400
    customer2.purchases()
    
    customer3=Customer()
    customer3.customer_name="C"
    customer1.bill_amount=500
    customer3.purchases()

    customer4=Customer()
    customer4.customer_name="D"
    customer1.bill_amount=600
    customer4.purchases()
