#PF-Assgn-43

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(1,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors


def find_smallest_number(num):
    i=1
    list1=[]
    while(1):
        list1=find_factors(i)
        if(len(list1)==num):
            break
        else:
            i+=1
    return i

num=4
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)