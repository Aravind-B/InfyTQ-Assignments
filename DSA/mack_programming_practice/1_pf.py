#PF-Assgn-103

def fun(input_list):
    output_list=[]
    for i in input_list:
        str1=i.split(":")
        l1=""
        r1=""
        if(str1[0].isalnum() or str1[1].isalnum()):
            if(str1[0].isdigit()):
                l1="X"
            else:
                for j in range(len(str1[0])):
                    if(str1[0][j].isalpha()):
                        l1+=str(j)
    
            if(str1[1].isalpha()):
                r1="Y"
            else:
                for j in range(len(str1[1])):
                    if(str1[1][j].isdigit()):
                        r1+=str(j)
            output_list.append(l1+":"+r1)
        else:
            output_list.append("X:Y")
            
    return output_list

input_list = ['A12z3:xy9z1','Dz2A:fg12x']
output_list = fun(input_list)
print(output_list)
