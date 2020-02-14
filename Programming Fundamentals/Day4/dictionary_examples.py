'''
Created on Jan 23, 2020

@author: aravind.b02
'''
dict1={1:'a',2:'b',3:'c'}

print(dict1[2]) #prints value of key 2
dict1[4]='d' #add new key-value pair
print(dict1)

#iterating through dictionary
#1)gives keys
for i in dict1:
    print(i)
    #or
for i in dict1.keys():
    print(i)
    
#2)
for i in dict1.values():
    print(i)
    
#3)
for i in dict1.items():
    print(i)
    
for i,j in dict1.items():
    print(i,j)
    
a=dict1.get(2) #fetch value of key 2
c=dict1.pop(4) #deletes 4th key value pair
print(dict1)

var1=dict1.popitem() #pops out first key value pair and make it a tuple
dict1.update({"SUM":"h"})
dict1.update(SUM1="j")
