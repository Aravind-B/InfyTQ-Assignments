list1=[12,5,36,48,3,6,8,7,9,45,50]

m=list1.index(5)
n=list1.index(45)

for i in range(m,n+1):
    for j in range(i+1,n+1):
        if(list1[i]>list1[j]):
            list1[i],list1[j]=list1[j],list1[i]
sum1=0
m=list1.index(5)
n=list1.index(45)
list3=[]
for i in range(m,n):
    if(list1[i]>5 and list1[i]<45):
        sum1+=list1[i]
list3.append(sum1)      
list2=list1[:m]+list1[n+1:]
sum2=sum(list2)
list3.append(sum2)
list3.append(5)
list3.append(45)