#PF-Assgn-102
def list_rotate(uniquecode_list):
    rotated_list=[]
    #Write your code here
    #str1=uniquecode_list[0].split("-")
    #str1.append(uniquecode_list[1].split("-"))
    for i in uniquecode_list:
        str1=i.split("-")
        str2=""
        count1=0
        for j in str1[0]:
            if(j.isalpha()):
                count1+=1
                str2+=j
        if(count1==2):
            list1=list(str1[1])
            a=list1.pop(0)
            b=list1.pop(0)
            list1.append(a)
            list1.append(b)
            
        elif(count1==1):
            list1=list(str1[1])
            a=list1.pop(0)
            list1.append(a)
            
        rotated_list.append(str2+"".join(list1))
    return rotated_list

#You may modify the below code for testing
uniquecode_list=["AZ01-1234","R137-8714"]
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)