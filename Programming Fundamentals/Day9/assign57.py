#PF-Assgn-57

def check_prime(number):
    count=0 #remove pass and write your logic here. if the number is prime return true, else return false
    for i in range(1,(number+1)):
        if((number%i)==0):
            count+=1
    if(count==2):
        return True
    else:
        return False

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    list1=[]
    list1.append(num)
    str1=str(num)
    list2=list(str1)
    while(len(list1)<len(str1)):
        popped=list2.pop(0)
        list2.append(popped)
        str2="".join(list2)
        list1.append(int(str2))
    return list1

def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    c=0
    for i in range(2,limit):
        list2=rotations(i)
        c1=0
        for j in list2:
            if(check_prime(j)):
                c1+=1
        if(c1==len(list2)):
            c+=1
    return c
#Provide different values for limit and test your program
print(get_circular_prime_count(179))
