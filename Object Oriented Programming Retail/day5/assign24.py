#OOPR-Assgn-24
#Start writing your code here
class Apparel:
    counter=100
    def __init__(self,price,item_type):
        Apparel.counter+=1
        self.__price=price
        self.__item_type=item_type
        self.__item_id=item_type[0]+str(Apparel.counter)

    def set_price(self, price):
        self.__price = price


    def get_price(self):
        return self.__price


    def get_item_type(self):
        return self.__item_type


    def get_item_id(self):
        return self.__item_id

        
    def calculate_price(self):
        p=1.05*self.__price
        self.set_price(p)

class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price,"Cotton")
        self.__discount=discount

    def get_discount(self):
        return self.__discount

    def calculate_price(self):
        super().calculate_price()
        dis=(self.get_price()*self.__discount)/100
        self.set_price(self.get_price()-dis)        
        self.set_price(1.05*self.get_price())
        
class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price,"Silk")
        self.__points=None

    def get_points(self):
        return self.__points

    def calculate_price(self):
        super().calculate_price()
        if(self.get_price()>10000):
            self.__points=10
        else:
            self.__points=3
        self.set_price(1.1*self.get_price())
