#DSA-Assgn-19

def last_instance(num_list,  start,  end,  key):
    first_index=0
    for i in range(start,end):
        if(key==num_list[i]):
            first_index=i
            break
    a=num_list.count(key)
    return a+first_index-1
    
num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")