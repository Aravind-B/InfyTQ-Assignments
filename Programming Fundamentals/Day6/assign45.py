#PF-Tryout
def find_armstrong(number):
    temp=0
    temp1=number
    remainder=0
    while(number!=0):
        remainder=number%10
        temp+=(remainder*remainder*remainder)
        number=number//10
      
    if(temp1==temp):
        return True
    else:
        return False

number=153
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")