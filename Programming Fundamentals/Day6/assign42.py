#PF-Assgn-42

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True 
    #if the number is prime else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    listoffact=[]
    for i in list_of_factors:
        if(is_prime(i, i//2)):
            listoffact.append(i)
            
    return max(listoffact)
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    factors=find_factors(num)
    f=find_largest_prime_factor(factors)
    return f
    #Accepts the number and returns the largest prime factor of the number

def find_g(num):
    g=0
    for i in range(num,num+9):
        g+=find_f(i)
    return g
 
print(find_g(10))