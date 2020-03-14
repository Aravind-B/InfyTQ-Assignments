l1 = [24, 55, 66, 77, 88, 33, 11, 99]
num= 77


l1.sort()

while len(l1)!=0:
    mid=len(l1)//2
    if(num == l1[mid]):
        print("Yes")
    elif(num<l1[mid]):
        l1=l1[:mid]
    else:
        l1=l1[mid+1:]