'''
Created on Jan 22, 2020

@author: aravind.b02
'''
list1=[1,2,4,3,4,5]
print(list1)
print(list1.append(6)) #add an element to list
print(list1.extend("fg")) #add string elements separately at the end
print(list1.extend(["fg","g"])) #add string list
print(list1.insert(0,1)) #add element 1 at position 0
print(list1.pop()) #Removes last element
print(list1.pop(0)) #Removes element at position 0
print(list1.count(2))  #count of a particular value
print(list1.index(4)) #gives first occurance position of element 4
print(list1.index(4,3)) #give index position of element 4 after 3rd index
print(list1.remove(4)) #removes element 4 from list
print(list1.reverse()) #reverses the list
print(max(list1))
print(min(list1))
print(sum(list1))
list2=list1.copy()
print(list2)
print(list1.clear())