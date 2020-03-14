
class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))
class Service:
    def __init__(self,car_list):
        self.__car_list=car_list
        for i in self.__car_list:
            self.__car_list.sort(key=lambda i: i.get_year())
    def sort(self):
        for i in self.__car_list:
            self.__car_list=sorted(self.__car_list)
            #self.__car_list.sort(i.get_year())
        
        return self.__car_list
car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
ser1=Service(car_list)
print(ser1.sort())