#DSA-Assgn-7

#This assignment needs DataStructures.py file in your package,
# you can get it from resources page

from day2.DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    temp=duplicate_list.get_head()
    #temp1=temp.get_next()
    list1=[]
    list2=[]
    
    while(temp is not None):
        duplicate_list.delete(temp.get_data())
        list1.append(temp.get_data())
        '''
            if(temp.get_data()==temp.get_next().get_data()):
                temp1=temp
                duplicate_list.delete(temp.get_next().get_data())
        '''
        temp=temp.get_next()

    for i in list1:
        if i not in list2:
            list2.append(i)

    for i in list2:
        duplicate_list.add(i)

    return duplicate_list

#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(20)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
print(duplicate_list.display())
remove_duplicates(duplicate_list)
#duplicate_list.delete(40)
print(duplicate_list.display())