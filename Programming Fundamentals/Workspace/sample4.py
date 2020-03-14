class Parent:
   num=100
   def mtd(self):
       self.__num=200
       self.num=400
       return self.num+10
print(Parent().mtd())