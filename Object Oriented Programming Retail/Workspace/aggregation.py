class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.__address=addr1

    def view_details(self):
        print(self.name)
        print(self.age)
        print(self.phone_no)
        print(self.__address)
    def update_details(self):
        self.__address.street="NK road"
        
    def get_address(self):
        return self.__address

class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass
    
addr1=Address(32,"MG Road","Hebbal",581202)
cust1=Customer('ABC',25,8899009988)
print(cust1.get_address().street)
cust1.update_details()
print(cust1.get_address().street)

cust1.view_details()