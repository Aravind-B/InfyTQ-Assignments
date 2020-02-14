#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    list1=[]
    if(num1<num2):
        for num3 in range(num1,num2+1):
            temp=str(num3)
            sum1=0
            for i in temp:
                sum1+=int(i)
            if(sum1%3==0 and num3%5==0 and len(temp)==2):
                list1.append(num3)

        if(list1):
            max_num=max(list1)
            return max_num
        else:
            return -1
    else:
        return -1
    
#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,100)
print(max_num)