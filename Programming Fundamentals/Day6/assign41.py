#PF-Assgn-41
def find_ten_substring(num_str):
    m=[]
    n=[]
    for i in range(len(num_str)):
        for j in range(len(num_str)):
            m.append(num_str[i:j+1])        
            
    for k in set(m):
        sum1=0
        for j in k:
            #print(k.index(j)+1)
            sum1+=int(j)
            if(sum1==10 and (k.index(j))==len(k)-1):
                n.append(k)
    return(n)
    
num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)