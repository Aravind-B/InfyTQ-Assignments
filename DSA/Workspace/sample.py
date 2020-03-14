l1=[1,2,3]

l2=[4,5,6]

l3=zip(l1,l2)
l4=[]
for i,j in l3:
    if(i<j):
        l4.append(j)

print([i for i,j in l3 if i<j])

str1="1.2"
print(str1.isdigit())

str2="r1001rPP"

print(str2.capitalize())