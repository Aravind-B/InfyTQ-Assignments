#PF-Assgn-38

def check_double(number):
    num2=number*2
    a=str(number)
    b=str(num2)
    flag=0
    if(len(a)==len(b)):
        for i in a:
            if i in b:
                continue
            else:
                flag=1
    else:
        flag=1
    if(flag):
        return False
    else:
        return True

#Provide different values for number and test your program
print(check_double(142857))