#Do NOT Change any part of the code provided to you

def sum_of_numbers(input_list):
    output_num = None #Initialize this with proper value
    for i in input_list:
        if(i==5):
            m=input_list.index(i)
        elif(i==8):
            n=input_list.index(i)
        else:
            continue
    list2=input_list[:m]+input_list[n+1:] 
    output_num=sum(list2)
    return output_num

#Modify and use the below code to test your functionality      
input_list=[1,2,2,5,1,3,8,4]
output_num=sum_of_numbers(input_list)
print(output_num)

