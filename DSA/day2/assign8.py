#DSA-Assgn-8

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    #Implement other methods here
    def allocate_table(self):
        temp=self.__occupied_table_list.get_head()
        prev=None
        i=1
        if(temp is None or temp.get_data()!=1):
            self.__occupied_table_list.insert(1,None)
            return
        while(temp is not None):
            if(temp.get_data()!=i):
                self.__occupied_table_list.insert(i,prev.get_data())
                return
            else:
                prev=temp
                temp=temp.get_next()
            i+=1
        self.__occupied_table_list.insert(i,prev.get_data())
                
            
    def deallocate_table(self,table_number):
        self.get_occupied_table_list().delete(table_number)


bakehouse=BakeHouse()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.deallocate_table(3)
bakehouse.get_occupied_table_list.__str__()
#Invoke the methods of BakeHouse class and test the program
