class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    def __init__(self, type,price, brand, camera):     #Method Overriding
        super().__init__(price, brand, camera)          #super() is invoked in case of method overriding
        self.type=type

class SmartPhone(Phone):
    pass

FeaturePhone(10000,"Apple","13px").buy()
