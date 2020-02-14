#PF-Exer-26

def factorial(number):
    fact=1
    if(number==0):
        return 1
    else:
        for i in range(1,number+1):
            fact*=i
        return(fact)

def find_strong_numbers(num_list):
    list1=[]

    for k in num_list:
        if(k!=0):
            temp=k
            sum1=0
            while(k>0):
                rem=k%10
                sum1+=factorial(rem)
                k=k//10
            if(temp==sum1):
                list1.append(temp)
    return list1

num_list=[145,375,100,2,10,40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
#print(factorial(4))'''
