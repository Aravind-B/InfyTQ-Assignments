list1 = [32, 15, 24, 79, 11, 29, 45]
list2 = [11, 32, 24, 15, 45, 79, 29]
print(list1)
list1.sort(key=lambda x:x%10)
print(list1)
def unit_digit(num):
    return num%10
list1.sort(key=unit_digit)
print(list1)



def add(num1,num2):
    return num1+num2

add1=add
print(add)
print(add(3,4))
print(type(add))

print(add1)
print(add1(3,4))

copy_add=lambda x,y:x+y
print(copy_add)
print(copy_add(3,4))