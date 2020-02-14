'''
Created on Jan 24, 2020

@author: aravind.b02
'''
l1=[11,22,33,44,55]
l2=[100,200]

l3=[]
prod=0
for i in l1:
    for j in l2:
        l3.append(i+j)
print(l3)