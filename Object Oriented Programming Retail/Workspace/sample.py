'''
Created on Feb 4, 2020

@author: aravind.b02
'''

str1="M1-66"
str2="M2-7"

print(str1.split("-"))
print(str2.split("-"))
for i in str1.split("-"):
    if(i.isdigit()):
        print(int(i))
print(int(s) for s in str1.split('-') if s.isdigit())