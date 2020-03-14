#Do not modify the supplied code
def find_code(input_string):
    output_string=""
    list2=[]
    list3=[]
    palindrome_list=[]
    flag=1
    input_string=input_string.replace(":",",")
    list1=input_string.split(",")
    for i in range(len(list1)):
        if(i%2==0):
            list2.append(list1[i])
        else:
            list3.append(list1[i])
    sum1=0
    for i in range(0,len(list3)):
        #print(i)
        rev=list3[i][::-1]
        sum1=int(list3[i])+int(rev)
        while(flag==1):
            if(str(sum1)==str(sum1)[::-1]):
                flag=0
                palindrome_list.append(sum1)
            else:
                rev1=str(sum1)[::-1]
                sum1=int(rev1)+sum1
        flag=1
    #print(palindrome_list)
    #return palindrome_list            
    a=palindrome_list.index(max(palindrome_list))
    output_string=list2[a]
    return output_string

#You may modify the code below for testing
input_string="XYZ:750,ABC:265,QWERTY:195"
print(find_code(input_string))