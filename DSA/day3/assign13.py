#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package,
# you can get it from resources page

from day2.DataStructures import Stack

def change_smallest_value(number_stack):
    list1=[]
    while(not number_stack.is_empty()):
        list1.append(number_stack.pop())

    min1=min(list1)
    occurences=list1.count(min1)
    for i in range(occurences):
        number_stack.push(min1)
        list1.remove(min1)
        
    for i in list1[::-1]:
        number_stack.push(i)
        
    return number_stack


#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()