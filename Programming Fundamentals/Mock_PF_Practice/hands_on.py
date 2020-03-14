from itertools import permutations
l=[1,2,1,4]
l1=permutations(l,3)
l2=[]
for i in set(list(l1)):
    l2.append(list(i))
str1=""
m=max(l2)
for b in m:
    str1+=str(b)
str2=str1+str(len(l2))
print(int(str2))
   
   
'''
dict1={}
for i in l:
    dict1[i]=l.count(i)

count=0
for j in dict1:
    count+=1    

perm_len=len(l)
perm=perm_len*(perm_len-1)*(perm_len-2)
    #perm_len-=1
if(count<len(l)):
    pass
for i in range(perm):
    pop1=l.pop(0)
    l.append(pop1)

for j in l2:
    str1=""
    for k in j:
        str1+=str(k)
    l3.append(int(str1))
''' 

        
