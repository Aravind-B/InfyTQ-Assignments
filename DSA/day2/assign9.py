#DSA-Assgn-9

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

def reverse_linkedlist(reverse_list):
    prev = None
    current = reverse_list.get_head() 
    while(current is not None): 
        next = current.get_next()
        current.get_next() = prev 
        prev = current
        current = next
    reverse_list.set_head(prev) 
    return reverse_list

#Add different values to the linked list and test your program
reverse_list=LinkedList()
reverse_list.add(10)
reverse_list.add(15)
reverse_list.add(14)
reverse_list.add(28)
reverse_list.add(30)
reversed_linkedlist=reverse_linkedlist(reverse_list)
reversed_linkedlist.display()